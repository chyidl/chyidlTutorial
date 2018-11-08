#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# requests/sec of fast requests
# This test is essentially just going to hammer the server with lots of requests
from socket import *
from threading import Thread
import time


sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 25000))


n = 0   # Global counter
# monitor that the counter
def monitor():
    global n
    while True:
        time.sleep(1)
        # print out how many requests per second it made
        print(n, 'reqs/sec')
        n = 0  # reset the counter
Thread(target=monitor).start()


while True:
    sock.send(b'1')
    resp = sock.recv(1024)
    n += 1

