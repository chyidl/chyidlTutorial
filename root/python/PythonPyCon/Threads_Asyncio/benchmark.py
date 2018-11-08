#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# sends a hundred thousand messages to this echo server
from socket import *
import time


def benchmark(addr, nmessages):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(addr)
    start = time.time()
    for n in range(nmessages):
        sock.send(b'x')
        resp = sock.recv(1024)
    end = time.time()
    print(nmessages/(end-start), 'messages/sec')

benchmark(('localhost', 25000), 100000)
