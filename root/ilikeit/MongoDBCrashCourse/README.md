MongoDB
=======
> MongoDB is a database engine that provides access to non-relational, document-oriented databases. It is part of the growing NoSQL movement, along with databases like Redis.
> MongoDB seeks to provide an alternative to traditional relational database management systems (RDBMS). In addition to its schema-free design and scalable architecture, MongoDB provides a JSON output and specialized, language-specific bindings that make it particularly attractive for use in custom application development and rapid prototyping.

Install MongoDB Community Edition
---------------------------------
* Packages
```
mongodb-org :   A metapackage that will automatically install the four component packages listed below.
    mongodb-org-server: Contains the mongod daemon, associated init script, and a configuration file (/etc/mongod.conf) 
    mongodb-org-mongos: Contains the mongos daemon 
    mongodb-org-shell: Contains the mongo shell.
    mongodb-org-tools: Contains the following MongoDB tools: 
        mongoimport bsondump,
        mongodump,
        mongoexport, 
        mongofiles,
        mongorestore,
        mongostat,
        mongotop
```

* Install MongoDB Community Edition 
```
1. Configure the package management system (yum)
    $ sudo vim /etc/yum.repos.d/mongodb-org-4.2.repo 
        [mongodb-org-4.2]
        name=MongoDB Repository
        baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/4.2/x86_64/
        gpgcheck=1
        enabled=1
        gpgkey=https://www.mongodb.org/static/pgp/server-4.2.asc

2. Install the MongoDB packages.
    # Install the latest stable version of MongoDB
    $ sudo yum install -y mongodb-org 
```

Run MongoDB Community Edition
-----------------------------
* UNIX ulimit Settings
> Most UNIX-like operating systems, including Linux and macOS, provide ways to limit and control the usage of system resources such as threads, files, and network connections on a per-process and per-user basis. These "ulimits" prevent single users from using too many system resources. Sometimes, these limits have low default values that can cause a number of issues in the course of normal MongoDB operation.
```
# Resource Utilization
    mongod and mongos each use threads and file descriptors to track connections and manage internal operations. This section outlines the general resource utilization patterns for MongoDB. 

    mongod and mongos:
        track each incoming connection with a file descriptor and a thread. 
        track each internal thread or pthread as a system process.
    mongod uses background threads for a number of internal processes, including TTL collections, replication, and replica set health checks, which may require a small number of additional resources. 

# Review and Set Resource Limits 
$ ulimit -a  # ulimit refers to the per-user limitations for various resources. 
-t: cpu time (seconds)              unlimited
-f: file size (blocks)              unlimited
-d: data seg size (kbytes)          unlimited
-s: stack size (kbytes)             8192
-c: core file size (blocks)         0
-m: resident set size (kbytes)      unlimited
-u: processes                       31202
-n: file descriptors                65535
-l: locked-in-memory size (kbytes)  64
-v: address space (kbytes)          unlimited
-x: file locks                      unlimited
-i: pending signals                 31202
-q: bytes in POSIX msg queues       819200
-e: max nice                        0
-r: max rt priority                 0
-N 15:                              unlimited
```

* Directory Paths 
```
By default, MongoDB runs using the mongod user account and uses the following default directoris:
    /var/lib/mongo  (the data directory)
    /var/log/mongodb (the log directory)

# To Use Non-Default Directories 
    1. Create the new directory or directories 
        $ mkdir -p /mnt/chyi_data/mongodb/mongo (data directory)
        $ mkdir -p /mnt/chyi_data/mongodb (log directory)
    2. Edit the configuration file /etc/mongod.conf and modify the following fields accordingly:
        storage.dbPath : to specify a new data directory path (/mnt/chyi_data/mongodb/mongo) 
        systemLog.path : to specify a new log file path (/mnt/chyi_data/mongodb/mongod.log) 
    3. Ensure that the user running MongoDB has access to the directory or directories.
        # By default, MongoDB runs using the mongod user account. Once created, set the owner and group of these directories to mongod
        $ sudo chown -R mongod:mongod /mnt/chyi_data/mongodb
```

* Procedure 
```
1. Start MongoDB
    $ sudo systemctl status mongod  (status, start, stop, restart)

2. Verify that MongoDB has started successfully
    You can verify that the mongod process has started successfully by checking the contents of the log file at /mnt/chyi_data/mongodb/mongod.log for a line reading 
    $ tail -f /mnt/chyi_data/mongodb/mongod.log 
        2019-10-15T16:55:47.715+0800 I  NETWORK  [initandlisten] waiting for connections on port 27017
        ... 
    # Ensure that MongoDB will start following a system reboot by issuing the following command
    $ sudo chkconfig mongod on
        Note: Forwarding request to 'systemctl enable mongod.service'.

3. Begain using MongoDB.
    $ mongo  (mongo shell default localhost port 27017)
```

* Enable Authentication on MongoDB
> Never run a production server without authentication on.
```
# Connect to the server using the mongo shell 
$ mongo mongodb://<host>:<port>

# Create the user administrator 
> use admin
1. User Administrator 
    With access control enabled, ensure you have a user with userAdmin or userAdminAnyDatabase role in the admin database. This user can administrate user and roles such as:
        create users、grant or revoke roles from users、and create or modify customs roles.

2. Procedure 
   The following procedure first adds a user administrator to a MongoDB instance running without access control and then enables access control. 
    1. Start MongoDB without access control. 
        $ mongod --port 27017 --dbpath /mnt/chyi_data/mongodb 
    2. Connect to the instance.
        $ mongo --host --port 27017 
    3. Create the user administrator 
        > use admin 
        > db.createUser(
            {
                user: "root",
                pwd: passwordPrompt(), // or cleartext password 
                roles: [ { role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase" ]
            }
        )
        The databae admin: is the user's authentication database.

# Enable authentication in mongod configuration file 
$ vim /etc/mongod.conf 
    security:
        authorization: "enabled"

From now on, all clients connecting to this server must authenticate themselves as a valid users, and they will be only able to perform actions as determined by their assigned roles.

    4. Connect and authenticate as the user administrator. 
        4.1: Connect with authentication by passing in user credentials 
            $ mongo --port 27017 --authenticationDatabase "admin" -u "root" -p 
            Enter your password when prompted. 
        4.2: Connect first without authentication, and then issue the db.auth() method to authenticate 
            $ mongo --port 27017 
            > use admin
            > db.auth("root", passwordPrompt()) // or cleartext password
        4.3: connect and authenticate in one single step
            $ mongo mongodb://root:password@<host>:<port>  
            this option isn't advised because it will leave your credentials visible in your terminal history, which any program on your computer can actuall read.
    
    5. Finally, create additional users as needed. 
        The following operation adds a user tester to the test database who has readWrite role in the test database:
            > use test
            > db.createUser({
                user: "test",
                pwd: "text123",
                roles: [{ role: "readWrite", db: "test"}]
            })
```

