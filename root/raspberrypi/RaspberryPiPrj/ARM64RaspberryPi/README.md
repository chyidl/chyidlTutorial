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

* Onboard Wi-Fi on Raspberry Pi 
```
Step1:
$ sudo apt-get install wireless-tools 

Step2:
$ sudo apt-get install wpasupplicant 

Step3: add to /etc/network/interfaces:
auto wlan0
iface wlan0 inet dhcp
wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf 

Step4: add connect to /etc/wpa_supplicant/wpa_supplicant.conf 
country=CN 

network={
    ssid="Airbnb-HK"
    psk="pp341152"
}
```

* Timezone, locale
```
Check Current Timezone Settings 
$ timedatectl # Use the timedatectl command to show the current timezone and time

Show all Available Timezones 
$ timedatectl list-timezones | grep -i Asia/Hong_Kong
Asia/Hong_Kong

Change Timezone 
$ sudo timedatectl set-timezone Asia/Hong_Kong 
```

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

* Headless VncServer Configuration 
```
configure accessing the pi with osx's Screen
1. $ sudo raspi-config > Interface Options > VNC > Enable.
2. Generate the password you wish to use in screen with vncpasswd -print 
pi@RPi2B:~ $ vncpasswd -print
Password:
Verify:
Password=bf8c3dcbaeaeb962267ad00c568c0850
3. Copy the output of that command(e.g.Password=bf8c3dcbaeaeb962267ad00c568c0850)for the config file.
4. Create and edit the following file here:
$ sudo vim /etc/vnc/config.d/common.custom 
5.Add the following config:
Encryption=PreferOn
Authentication=VncAuth
Password=bf8c3dcbaeaeb962267ad00c568c0850
6. Restart the vnc service:
$ sudo systemctl restart vncserver-x11-serviced 
7. Open Screen with the instructions above, and use the password you provided to vncpasswd.
mac> Finder > Go > Connect to Server... 
8. If you need to monitor the logs for vncserver, you can use journalctl
$ sudo journalctl -u vncserver-x11-serviced.service 
```
