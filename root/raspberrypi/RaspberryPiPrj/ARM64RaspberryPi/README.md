ARM64 Ubuntu Raspberry Pi
=========================
* ARMHF vs ARM64 
> ARMHF stands for "arm hard float", and is the name given to a debian port for arm processors(armv7+) that have hardware floating point support.
> ARM64 supports hardware floating point and NEON by default
```
Raspberry Pi 3B + Raspbian 9 
$ uname -a
Linux RPi3B 4.14.98-v7+ #1200 SMP Tue Feb 12 20:27:48 GMT 2019 armv7l GNU/Linux

Raspberry Pi 3BPlus + Ubuntu ARM64 
$ uname -a
Linux RPi3BPlus 4.15.0-1034-raspi2 #36-Ubuntu SMP PREEMPT Fri Apr 5 06:21:41 UTC 2019 aarch64 aarch64 aarch64 GNU/Linux

'arm64' is the Debian port name for the 64-bit ARMv8 architecture,referred to as 'aarch64' in upstream toolchains (GNU triplet aarch64-linux-gnu), and some other distros.

```

* How to determine python 32bit or 64bit mode
```
ne way is to look at sys.maxsize
$ python3 -c 'import sys;print("%x" % sys.maxsize, sys.maxsize > 2**32)'
('7fffffff', False)

$ python3 -c 'import sys;print("%x" % sys.maxsize, sys.maxsize > 2**32)'
7fffffffffffffff True
```

* First boot (Username/Password)
> The login username is "ubuntu", password is "ubuntu". You will be asked to change the password on first login.

> Create a sudo user "$ sudo adduser new_user", and add "new_user" to "sudo" group, "$ sudo usermod -aG sudo new_user"

* Swap 
```
There is no swap partition/file included. If you want swap, it's recommended you do:
$ sudo apt-get install dphys-swapfile

STOP THE SWAP 
$ sudo dphys-swapfile swapoff 

MODIFY THE SIZE OF THE SWAP 
As root, edit the file /etc/dphys-swapfile and modify the variable CONF_SWAPSIZE:
CONF_SWAPSIZE=1024
To modify the swap file, edit the variable CONF_SWAPFILE, and run dphys-swapfile setup which will create and initialize the file.

START THE SWAP 
$ sudo dphys-swapfile swapon
```
