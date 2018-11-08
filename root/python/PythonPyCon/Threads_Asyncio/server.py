#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Network echo server in asyncio
# Coroutines with async and await syntax
from socket import *
import asyncio


# Returns an event loop object implementing the AbstractEventLoop
loop = asyncio.get_event_loop()


# classic server with sockets
async def echo_server(address):
    # Create socket object
    sock = socket(family=AF_INET, type=SOCK_STREAM)
    # set the value of the given socket option
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # Bind the socket to address
    sock.bind(address)
    # Enable a server to accept connections
    sock.listen(5)
    # Set blocking or non-blocking mode of the socket
    sock.setblocking(False)
    while True:
        # Wait for connection
        client, addr = await loop.sock_accept(sock)
        # see where the connection comes from here
        print('Connection from', addr)
        loop.create_task(echo_handler(client))


# how would you handle multiple clients
async def echo_handler(client):
    with client:
        while True:
            data = await loop.sock_recv(client, 1024)
            if not data:
                break
            await loop.sock_sendall(client, b'Got:'+data)
    print('Connection closed')


# run an echo server
loop.create_task(echo_server(('',25000)))
loop.run_forever()
