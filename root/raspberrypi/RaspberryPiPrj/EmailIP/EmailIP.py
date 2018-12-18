#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import os
import time
import socket
import subprocess
from datetime import datetime
from chyiemail import sendMessage

# Change to your own account information
fromAddr='test@qq.com'
fromPasswd='ilsuveijbqelbabh'
Names = ['Bruce Lee']
Emails = ['test@gmail.com']
Subject = "RPi Email IP On Boot"
message_Template = """Dear ${PERSON_NAME},

IP :

[CHYIYAQING.CHYIDL.COM]

Yours Truly
"""

def get_device_ip_address():
    try:
        if os.name == "nt":
            # On Windows
            result = "Running on Windows"
            hostname = socket.gethostname()
            result += "\nHostname: " + hostname
            host = socket.gethostbyname(hostname)
            result += "\nHost-IP-Address: " + host
            return result
        elif os.name == "posix":
            #gw = os.popen("ip -4 route show default").read().split()
            #s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            #s.connect((gw[2], 0))
            #ipaddr = s.getsockname()[0]
            #gateway = gw[2]
            #host = socket.gethostname()
            lsb_release = os.popen("lsb_release -a").read()
            #result = lsb_release + "\nIP:\t\t" + ipaddr + "\nGateway:\t\t" + gateway + "\nHost:\t\t" + host
            ifconfig = os.popen("ifconfig").read()
            result = lsb_release + ifconfig
            return result
        else:
            result = os.name + " not supported yet."
            return result
    except:
        return "Could not detect ip address"

if __name__ == '__main__':
    result = get_device_ip_address()
    template = message_Template.replace('[CHYIYAQING.CHYIDL.COM]', result)
    sendMessage(fromAddr,fromPasswd,Names,Emails,Subject,template)
    print("Thanks my boss: -)")
