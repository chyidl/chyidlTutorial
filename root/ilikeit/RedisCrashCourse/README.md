Redis Crash Course
==================

Introduction
------------
Redis is an in-memory key-value store known for its flexibility, performance, and wide language support.

Install the Build and Test Dependecies
--------------------------------------
In order to get the latest version of Redis, we will be compiling and installing the software from source. Before we download the code, we need to statisfy the build dependencies so that we can compile the software.

To do this, we can install the **build-essential** meta-package from the repositiories. downloading the **tcl** package, which can use to test our binaries.

```
$ sudo apt-get update 
$ sudo apt-get install build-essential tcl 
```

Download, Compile, and Install Redis 
------------------------------------
```
# Since we won't need to keep the source code that we'll compile long term, we will build in the **~** directory.
$ cd ~ 

# download the latest stable version of Redis.
$ wget http://download.redis.io/redis-stable.tar.gz 

# Unpack the tarball by typing:
$ tar -xzvf redis-stable.tar.gz

# Move into the Redis source directory structure that was just extracted
$ cd redis-stable 

# compile the Redis binaries by typing:
$ make 

# After the binaries are compiled, run the test suite to make sure everything was built correctly
$ make test 

# Once complete, install the binaries onto the system by typing:
$ sudo make install

# Configure Redis 
# Now that Redis is installed, we can begin to configure it.

# To start off, we need to create a configuration directory. We will use the conventional **/etc/redis** directory, which can be created by typing:
$ sudo mkdir /etc/redis 

# Now, copy over the sample Redis configuration file included in the Redis source archive:
$ sudo cp ~/redis-stable/redis.conf /etc/redis 

# Open the file to adjust a few items in the configuration:
$ sudo vim /etc/redis/redis.conf 

# find the **supervised** directive. Currently, this is set to no. Since we are running an operating system that uses systemd init system, we can change this to **systemd**.
supervised systemd 

# Next, find the **dir** directory. This option specifies the directory that Redis will use to dump persistent data. We need to pick a location that Redis will have write permission and that isn't viewable by normal users.
dir /var/lib/redis 

# Create a Redis systemd Unit File 
# We can create a systemd unit file so that the init system can manage the Redis process.
$ sudo vim /etc/systemd/system/redis.service 
# Inside, we can begin the [Unit] section by adding a description and defining a requirement that networking be available before string this service:

[Unit]
Description=Redis In-Memory Data Store 
After=network.target 

[Service]
User=redis 
Group=redis 
ExecStart=/usr/local/bin/redis-server /etc/redis/redis.conf 
ExecStop=/usr/local/bin/redis-cli shutdown 
Restart=always

[Install]
WantedBy=multi-user.target 
```

Create the Redis User, Group and Directories 
--------------------------------------------
```
# Begin by creating the **redis** user and group. 
$ sudo adduser --system --group --no-create-home redis 

# create the **/var/lib/redis** directory by typing 
$ sudo mkdir /var/lib/redis 

# give the **redis** user and group ownership over this directory:
$ sudo chown redis:redis /var/lib/redis 

# Adjust the permissions so that regular users cannot access this location:
$ sudo chmod 770 /var/lib/redis 
```

Start and Test Redis
--------------------
```
# Start the Redis Service 
$ sudo systemctl start redis 

# Check that service had no errors by running
$ sudo systemctl status redis 

# Test the Redis Instance Functionality 
# To Test that your service is functioning correctly, connect to the Redis server with the command-line client:
$ redis-cli

# In the prompt that follows, test connectivity by typing:
$ 127.0.0.1:6379> ping 

# You should see:
$ PONG 

# Check that you can set keys by typing:
$ 127.0.0.1:6379> set test "It's working!"

# Output 
$ OK 

# Now, retrieve the value by typing 
$ 127.0.0.1:6379> get test 

# You should be able to retrieve the value we stored:
$ "It's working!"

# Exit the Redis prompt to get back to the shell:
$ 127.0.0.1:6379> exit 

# As a final test, let's restart the Redis instance:
$ sudo systemctl restart redis 

# Enable Redis to Start at Boot
$ sudo systemctl enable redis 

# To set the password, edit your /etc/redis/redis.conf file 
# find this line 
# requirepass foobared  
# Then uncomment it and change foobared to your password. Make sure you choose something pretty long, 32 characters or so would probably be good, it's easy for an outside user to guess upwards of 150k passwords a second, as the notes in the config file mention, 

$ sudo systemctl restart redis  

Example:
$ redis-cli 
redis 127.0.0.1:6379> AUTH PASSWORD 
Ok 

# Host, port, password and database 
# By default **redis-cli** connects to the server at 127.0.0.1 port 6379. As you can guess, you can easily change this using command line options. To specify a different host name or an IP address, use -h. In order to sent a different port, user -p 

$ redis-cli -h pi -p 6379 
```
