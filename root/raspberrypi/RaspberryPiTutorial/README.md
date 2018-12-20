# RaspberryPi Tutorial 


## WiringPi Tutorial 

WiringPi is a PIN based GPIO access library written in C for the BCM2835(Raspberry Pi Zero), BCM2836(Raspbe    rry Pi Model 2B) and BCM2837 (Raspberry Pi Model 3B) SoC devices used in all Raspberry Pi.

WiringPi includes a command-line utility gpio which can be used to program and setup the GPIO pins. You can use this to read and write the pins and even use it control them from shell scripts.

### Download and Install

![# gpio -v](/imgs/raspberrypi/RaspberryPi_gpio-v.png?raw=true)
- [$ gpio -v # check that wiringPi is not already installed]()

If you get something, then you have it already installed. 

![# gpio readall](/imgs/raspberrypi/RaspberryPi_gpio-readall.png?raw=true)
- [$ gpio readall]()


### Installing Python 3.6 on a Raspberry Pi 

Python3.6 offers a new method for string generation, the f-string syntax

```
1. Install the required build-tools 
$ sudo apt-get update 
$ sudo apt-get install make libsqlite3-dev build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev
$ sudo apt-get install python3-dev libffi-dev libssl-dev build-essential -y 

2. Download and install Python 3.6. When downloading the source code, select the most recent release of Python 3.6. available on the official site. Adjust the file names accordingly.

$ wget https://www.python.org/ftp/python/3.6.7/Python-3.6.7.tar.xz
$ tar -xvf Python-3.6.7.tar.xz 
$ cd Python-3.6.7
$ ./configure --enable-optimizations --with-ensurepip=install
$ make -j 4
$ sudo make install OR sudo make altinstall 
$ sudo pip3 install --upgrade pip 
```

### Change Raspberry Pi's Swapfile Size on Raspbian 

**Reason Why**

Ever get the dreaded error:

```
Virtual memory exhausted: Cannot allocate memory
```

With the first iterations of Raspberry Pi the Model A comes with 256mb of memory. While the Raspberry Pi B comes with a modeest 512mb of memory. For most applications this amount of memory is actually quiet a bit. As soon as you start compiling your own binaries this amount starts to seem dismal.

**Limitations**

The Raspbian distribution comes with a 100mb swapfile. This is actually a bit on the small side. A general rule of thumb if swapfile size should be acout twice as much as the available RAM on the machine. In the examples below I have a Raspbian Pi 2B. So the amount of swap I use is 1024mb.

**Commands**

We will change the configuration in the file */etc/dphys-swapfile*

```
$ sudo nano /etc/dphys-swapfile 

# The default value is Raspbian is:
CONF_SWAPSIZE=100 

# We will need to change this to:
CONF_SWAPSIZE=1024

# Then you will need to stop and start the service that manages the swapfile own Rasbian:
$ sudo/etc/init.d/dphys-swapfile stop 
$ sudo /etc/init.d/dphys-swapfile start 

# You can then verify the amount of memory + swap by issuing the following command:

$ free -m 

# The output should look like:

$ free -m
              total        used        free      shared  buff/cache   available
Mem:            875          31          38          11         805         769
Swap:          1023           0        1023
```

**Finished!**

That should be enough swap to complete any future compiles I may do n the future.

