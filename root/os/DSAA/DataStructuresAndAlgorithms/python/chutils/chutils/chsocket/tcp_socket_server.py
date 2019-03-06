#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# tcp_socket_server.py
# chsocket
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
# Created by Chyi Yaqing on 03/06/19 10:07.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
服务端进程首先绑定一个端口，并监听来自其他客户端的连接
服务端需要能够区分一个Socket连接是和那个客户端绑定的
Socket依赖4项信息: 服务器地址、服务器端口、客户端地址、客户端端口

127.0.0.1是一个特殊的IP地址，表示本机地址，如果绑定到这个地址，客户端必须同时在本机运行才能连接，外部的计算机无法连接进来
"""
import socket
import time
import threading


def tcplink(sock, addr):
    print('Accept new conecttion from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9527))
s.listen(5)

print('Waiting for connection...')
while True:
    # 接收一个新连接
    sock, addr = s.accept()
    # 创建新线程处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
