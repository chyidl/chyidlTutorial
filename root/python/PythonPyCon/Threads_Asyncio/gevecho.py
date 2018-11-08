#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from gevent.server import StreamServer


# This handler will be run for each incoming connection in a dedicated greenlet
def echo(socket, address):
    print('New connection from %s:%s' %address)
    while True:
        data = socket.recv(1024)
        if not data:
            break
        socket.sendall(b'Got:' + data)
    socket.close()


if __name__ == '__main__':
    server = StreamServer(('0.0.0.0', 25000), echo)
    server.serve_forever()
