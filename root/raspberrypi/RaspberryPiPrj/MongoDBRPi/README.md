Compile and Install MongoDB on Raspberry PI
===========================================

> A 32 bit version of Raspbian is currently the most common OS that runs on a Raspberry Pi. RPI3 comes equipped with a 64 bit CPU, however at the moment only experimental 64 bit versions of Rasbian may be found.
> The highest MongoDB version that will run on 32 bit is v3.2. As of MongoDB v3.4 only 64 bit versions are supported. MongoDB v3.2 is the latest version that you will be able to run on a 32 bit Raspbian. In addition, you will not be able to run MongoDB with the WiredTiger storage engine since it only works on 64 bit versions. You will have to start the DB with MMAPv1 storage engine. Also MMAPv1 has a limit of 2GB of storage, at least on ARM32. Once your DB hits that limit,
> you're out of luck. 

Building MongoDB on ARM32
-------------------------
```
1. The steps below describe how you can compile MongoDB 3.2 on your Raspberry Pi with 32 bit ARM architecture.
$ uname -a 
Linux RPi3BPlus 4.14.98-v7+ #1200 SMP Tue Feb 12 20:27:48 GMT 2019 armv7l GNU/Linux

2. Update/Upgrade your system 
$ sudo apt-get update && sudo apt-get upgrade 
$ sudo apt-get install wget 

3. Download and unpack mongodb source code. 
$ wget https://github.com/mongodb/mongo/archive/r3.2.22.zip
$ unzip mongo-r3.2.22.zip 
$ cd mongo-r3.2.22

4. Check install steps in docs/building.md and verify prerequistes.
$ cat docs/building.md 
$ gcc --version 
$ python --version
$ scons --version 

5. Install dependencies
$ sudo apt-get install aptitude 
$ sudo aptitude install scons build-essential
$ sudo aptitude install libboost-filesystem-dev libboost-program-options-dev libboost-system-dev libboost-thread-dev 
$ sudo apt-get install python-pymongo

6. Temporarily increase swap space.
$ sudo vim /etc/dphys-swapfile 
Change CONF_SWAPSIZE=100 to CONF_SWAPSIZE=1024 
$ sudo /etc/init.d/dphys-swapfile stop 
$ sudo /etc/init.d/dphys-swapfile start 

7. Generate additional sources 
$ cd src/third_party/mozjs-38/
$ ./get_sources.sh 
$ ./gen-config.sh arm linux 
$ cd -

8. Compile and build 
$ scons core --wiredtiger=off --mmapv1=on 

9. Reduce binaries file size 
$ cd ./build/opt/mongo 
$ ls 
-rwxr-xr-x  1 pi pi 159M Apr 24 01:00 mongo
-rwxr-xr-x  1 pi pi 433M Apr 24 14:44 mongod
-rwxr-xr-x  1 pi pi 221M Apr 24 15:57 mongos

This is because they contain debugging information. You can remove this with the strip command, for instance.
$ strip -s mongo mongod mongos
$ ls
-rwxr-xr-x  1 pi pi  14M Apr 24 16:27 mongo
-rwxr-xr-x  1 pi pi  25M Apr 24 16:27 mongod
-rwxr-xr-x  1 pi pi  13M Apr 24 16:27 mongos

10. Copy binaries
$ cd build/opt/mongo 
$ sudo cp mongo mongod mongos /usr/loca/mongodb3.2.22/bin/

```

Install MongoDB 4.0.9 on Ubuntu 18.04 ARM64 RaspberryPi
-------------------------------------------------------
> The latest release MongoDB community edition is an open source NoSQL database system written in C++ that provides scalability, high performance/availability. NoSQL database systems are often referred to as Document-oriented databases. MongoDB common use case is storage and management of Big Data-sized collections of literal documents like text documents, email message, XML documents and many others.
```
There are two ways of installing MongoDB on Ubuntu systems.

Step1: Import MongoDB public GPG Key:
$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4

Step2: Create a list file for MongoDB
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list

Step3: Install mongodb 
$ sudo apt-get update
$ sudo apt-get install -y openssl libcurl3 mongodb-org 

The service name is, mongod, you can start the application by running
$ sudo systemctl start mongod 

Enable the service to start on boot using 
$ sudo systemctl enabled mongod 

Check status using 
$ sudo systemctl status mongod 

the service should be listening on port 27017 
$ ss -tunelp | grep 27017 
```

* MongoDB main configuration file is /etc/mongod.conf You can tweak the settings to your linking, but remember to restart mongod service whenever you make a change.

