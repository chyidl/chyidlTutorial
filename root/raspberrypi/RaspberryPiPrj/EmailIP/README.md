# RPi Email IP On Boot Debian

Send Email Containing IP Address On Boot.

## What Does it Do?

This code will extract the ip address of your Pi and then send a email containing the ip to the specified email address. This is inspired by the need to access the Pi via SSH or other network protocols without a monitor and moving from network to network.

## Overview of this Guide

You need to :
  1. Create a Python script and store it in a direcotry
  ```
# create code dir
  $ mkdir ~/code 
# Save in chyiemail.py and EmailIP.py 
# Make it executable
  $ sudo chmod +x EmailIP.py 
# 
  $ sudo vim /etc/rc.local 
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.
# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
  python3 /home/pi/code/startup_mailer.py
fi
exit 0
  ```
  2. Make Python script executable.
  3. Set the program to run at boot time
- [chyiemail.py is util script](/root/raspberrypi/RaspberryPiPrj/EmailIP/chyiemail.py)
- [EmailIP.py is app script](/root/raspberrypi/RaspberryPiPrj/EmailIP/EmailIP.py)
