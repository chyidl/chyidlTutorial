#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# udp_socket_client.py
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
# Created by Chyi Yaqing on 03/06/19 10:30.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
客户端
"""
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Chyi Yaqing', b'Steve jobs', b'Dobby']:
    # 发送数据
    s.sendto(data, ('127.0.0.1', 9527))
    # 接收数据
    print(s.recv(1024).decode('utf-8'))

s.close()
