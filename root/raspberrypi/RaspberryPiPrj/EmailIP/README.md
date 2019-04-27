# RPi Email IP On Boot Debian

Send Email Containing IP Address On Boot. 

## What Does it Do?

This code will extract the ip address of your Pi and then send a email containing the ip to the specified email address. This is inspired by the need to access the Pi via SSH or other network protocols without a monitor and moving from network to network. 

## Overview of this Guide 

You need to :
  1. Create a Python script and store it in a direcotry 
  2. Make Python script executable.
  3. Set the program to run at boot time 
- [chyiemail.py is util script](/root/raspberrypi/RaspberryPiPrj/EmailIP/chyiemail.py)
- [EmailIP.py is app script](/root/raspberrypi/RaspberryPiPrj/EmailIP/EmailIP.py)
