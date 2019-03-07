logitech K480 Bluetooth In Raspberry Pi
=======================================

The latest Reaspberry Pi (Raspberry Pi 3B) now comes with its own built in Wi-Fi and Bluetooth 4.1/Low Energy (LE) support, thanks to the BCM43438 chip.

In order to use them we must ensure that our version of Raspbian(the Linux based operating system the Raspberry Pi 3 uses) is up to date and use a little terminal magic. Ensuring that your Raspberry Pi 3 is connected to the internet via an Ethernet cable, open a new terminal and type the following:

```
$ sudo apt-get update 
$ sudo apt-get dist-upgrade 

# install the Raspberry Pi Bluetooth software 
$ sudo apt-get install pi-bluetooth 
$ sudo apt-get install bluetooth bluez blueman  
```

Set Logitech Keyboard K480 in Paired Mode
------------------------------------------

! [Logitech Bluetooth Multi-Device Keyboard K480 Immersion Guide](/imgs/raspberrypi/Logitech-K480.png?raw=True)
Set K480 Keyboard in Paired Mode; Then in Terminal:
```
$ bluetoothctl 

# And run these commands: 
[bluetooth]# power on 
[bluetooth]# devices
[bluetooth]# devices
Device CB:07:AB:EB:5A:84 mobike
Device 34:88:5D:22:5F:BB Logitech Keyboard K480
[bluetooth]# scan on 
[bluetooth]# agent on 

Finally copy the MAC address to pair up with keyboard. 
[bluetooth]# pair 34:88:5D:22:5F:BB
Attempting to pair with 34:88:5D:22:5F:BB
[CHG] Device 34:88:5D:22:5F:BB Connected: yes
[agent] Passkey: 195005
[Logitech Keyboard K480]# trust 34:88:5D:22:5F:BB
Changing 34:88:5D:22:5F:BB trust succeeded
[Logitech Keyboard K480]# connect 34:88:5D:22:5F:BB
Attempting to connect to 34:88:5D:22:5F:BB

# Wait a few seconds and then test your new keyboard by typing on it. Should work right away. 

# If you just created a new install of raspbian on your raspberry pi then your bluetooth keyboard settings should be kept on next reboot.
```
! [Logitech Bluetooth Terminal Configure](/imgs/raspberrypi/Logitech-K480-terminal.png?raw=true)
