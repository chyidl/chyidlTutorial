#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import socket
import time

myHost = ''
myPort = 50007

sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(2)


while True:
    connection, address = sockobj.accept()
    print('Server connected by', address)

    d = connection.recv(1024)
    print(d)

    time.sleep(1.5)
    connection.send(b'\x04\x00\x00\x00tuxy')
