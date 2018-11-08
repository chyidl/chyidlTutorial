#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Fib microservice
from socket import *
from fib import fib
from threading import Thread
# we are going program with threads you have to stay away from CPU bound work
# throw the work out to a pool like a process pool
from concurrent.futures import ProcessPoolExecutor as Pool


pool = Pool(4)

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
        # GIL prioritizes things.
        Thread(target=fib_handler, args=(client,),daemon=True).start()


# Only handle one client at a time
def fib_handler(client):
    while True:
        req = client.recv(1024)
        if not req:
            break
        n = int(req)
        # You're like serializing data you're sending it off to a subprocess
        future = pool.submit(fib, n)
        result = future.result()
        resp = str(result).encode('ascii') + b'\n'
        client.send(resp)
    print('Closed')

fib_server(('', 25000))
