#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:encoding=utf-8
#
# portScanner.py
# easterEgg
#
# 🎂"Here's to the crazy ones. The misfits. The rebels.
# The troublemakers. The round pegs in the square holes.
# The ones who see things differently. They're not found
# of rules. And they have no respect for the status quo.
# You can quote them, disagree with them, glority or vilify
# them. About the only thing you can't do is ignore them.
# Because they change things. They push the human race forward.
# And while some may see them as the creazy ones, we see genius.
# Because the poeple who are crazy enough to think thay can change
# the world, are the ones who do."
#
# Created by Chyi Yaqing on 02/23/19 20:23.
# Copyright © 2019. Chyi Yaqing. All rights reserved.
#
# Distributed under terms of the MIT
"""
Port Tester v0.1
Test which remote ports the server running this script can access to.
"""
import sys
import socket


NAME = "Port Tester"
VERSION = "v0.1"


# Functions goes here
def banner():
    return "\n####################\n# {0} {1} #\n####################".format(
            NAME, VERSION)


def exitProgram(code):
    if code == 1:
        sys.exit("\n[!] Exiting help...\n")
    if code == 2:
        sys.exit("\n[!] Test finished, exiting...\n")
    if code == 3:
        sys.exit("\n[!] Exiting...\n")
    if code == 4:
        sys.exit("\n[-] Exiting, check arguments...\n")


def strToInt(convert, typeParam):
    try:
        value = int(convert)
        return value
    except Exception:
        print("\n[-] Number given in " + typeParam + " is invalid")
        exitProgram(3)


def checkTimeout(timeout):
    if timeout is None or timeout <= 0:
        # Default timeout : 3 seconds
        timeout = 3
    else:
        pass
    return timeout


def connectHost(host, port, timeout):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((host, port))
        # Connection established, we can access that port
        return "[+] We can reach port " + str(port)
    except Exception:
        # If some error happens (refused / filtered), we cannot access
        # that port, print that
        return "[-] We cannot reach port " + str(port)


if len(sys.argv) <= 4:
    print(banner())
    print("\nUsage:\n======\n\npython", sys.argv[0], "-s [START PORT] -e [END PORT] -t [TIMEOUT (Seconds) (Optional, default: 3)]")
    exitProgram(1)


# Set some variables
count = 0
timeout = None
start_port = None
end_port = None


# Read args
for arg in sys.argv:
    if arg == "-s":
        start_port = strToInt(sys.argv[count+1], "-s")
    elif arg == "-e":
        end_port = strToInt(sys.argv[count+1], "-e")
    elif arg == "-t":
        timeout = strToInt(sys.argv[count+1], "-t")
    count += 1


# Do some checks
if start_port is None or end_port is None:
    exitProgram(4)

timeout = checkTimeout(timeout)


# Test started
print(banner())
print("\n[!] Port-test started...")
print("[!] Timeout: " + str(timeout) + " seconds\n")


# In case we has DNS problems on the server, we use the IP instead the domain,
# if you wanna use the domain :
# hostname = socket.gethostbyname("open.zorinaq.com")
hostname = '67.215.250.139'  # open.zorinaq.com , 65k ports open


for port in range(start_port, end_port+1):
    print(connectHost(hostname, port, timeout))

exitProgram(2)
