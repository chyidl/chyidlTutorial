#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Fib microservice
# this is kind of a classic kind of concurrency problem with network
from socket import *
from fib import fib


def fib_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = sock.accept()
        print("Connection", addr)
        fib_handler(client)


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
