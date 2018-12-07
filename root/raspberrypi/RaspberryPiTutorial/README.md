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
$ sudo apt-get install libsqlite3-dev build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev
$ sudo apt-get install python3-dev libffi-dev libssl-dev -y 

2. Download and install Python 3.6. When downloading the source code, select the most recent release of Python 3.6. available on the official site. Adjust the file names accordingly.

$ wget https://www.python.org/ftp/python/3.6.7/Python-3.6.7.tar.xz
$ tar -xvf Python-3.6.7.tar.xz 
$ cd Python-3.6.7
$ ./configure 
$ make -j4
$ sudo make install OR sudo make altinstall 
$ sudo pip3 install --upgrade pip 
```
