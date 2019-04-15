MongoDB 
=======

Install MongoDB Community Edition
---------------------------------
```
Install MongoDB 4.0 Community Edition on LTS Ubuntu Linux systems.

1. Import the public key used by the package management system. 
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4

2. Create a list file for MongoDB 
$ echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list

3. Reload local package database
$ sudo apt-get update

4. Install the MongoDB package
$ sudo apt-get install -y mongodb-org

# Start MongoDB
$ sudo service mongod start 

# Stop MongoDB 
$ sudo service mongod stop 

# Restart MongoDB 
$ sudo service mongod restart 

# Begin using MongoDB
# Start a mongo shell on the same host machine as the mongod. localhost:27017 
$ mongo

Uninstall MongoDB Community Edition 
> To completely remove MongoDB from a system, Must remove the MongoDB applications themselves, the configuration files, and any directories containing data and logs.

1. Stop MongoDB 
$ sudo service mongod stop 

2. Remove Packages
$ sudo apt-get purge mongodb-org* 

3. Remove Data Directories
$ sudo rm -r /var/log/mongodb
$ sudo rm -r /var/lib/mongodb
```
