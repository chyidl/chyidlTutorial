#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# performance tests Time of a long running requests
from socket import *
import time


sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 25000))


# infinite loop
while True:
    start = time.time()
    sock.send(b'30')
    resp = sock.recv(1024)
    end = time.time()
    print(end-start,' sec')

