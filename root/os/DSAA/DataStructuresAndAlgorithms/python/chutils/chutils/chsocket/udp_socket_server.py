#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# udp_socket_server.py
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
# Created by Chyi Yaqing on 03/06/19 10:23.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT
"""

"""
import socket
import threading


def udplink(sock, data, addr):
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)


# socket.SOCK_DGRAM udp, socket.SOCK_STREAM tcp
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口
s.bind(('127.0.0.1', 9527))
print('Bind UDP on 9527...')
while True:
    # 接收数据
    # recvfrom() 方法返回数据和客户端的地址和端口
    data, addr = s.recvfrom(1024)
    # 创建新线程来处理UDP连接
    t = threading.Thread(target=udplink, args=(s, data, addr))
    t.start()
