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

```
