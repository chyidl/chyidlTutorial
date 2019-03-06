#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# tcp_socket_client.py
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
# Created by Chyi Yaqing on 03/06/19 09:56.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
创建TCP连接Socket Sina.com
"""
import socket  # 导入socket库


# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('www.sina.com', 80))

# 建立TCP连接之后，发送请求，获取首页内容
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接受新浪服务器返回的数据
buffer = []
while True:
    # 每次最多接受1K 字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

# 接收的数据包括HTTP头和网页本身，需要将HTTP头和网页分离
data = b''.join(buffer)
s.close()  # 关闭Socket

header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收到的数据写入文件:
with open('sina.html', 'wb') as f:
    f.write(html)
