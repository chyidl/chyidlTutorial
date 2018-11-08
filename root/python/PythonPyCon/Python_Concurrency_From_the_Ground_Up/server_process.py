#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Fib microservice
# Process instead process what you're doing is launching like an entirely new
# copy of Python and it runs independently and you can handle multiple things
# one potential advantage with processes is that you can take advantage of more
# CPU cores
from socket import *
from fib import fib
from multiprocessing import Process


def fib_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = sock.accept()
        print("Connection", addr)
        # Python use real system threads POSIX threads or managed operating system
        # global interpreter lock
        # You can't use multiple CPU Core
        # GIL global interpreter lock prioritizes things.
        # GIL is that it prioritizes things that want to run on the CPU
        #Thread(target=fib_handler, args=(client,),daemon=True).start()
        Process(target=fib_handler, args=(client,)).start()

# Only handle one client at a time
def fib_handler(client):
    while True:
        req = client.recv(1024)
        if not req:
            break
        n = int(req)
        result = fib(n)
        resp = str(result).encode('ascii') + b'\n'
        client.send(resp)
    print('Closed')

fib_server(('', 25000))
