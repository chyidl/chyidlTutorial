#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 8080))
sock.listen(1)  # 监听客户端连接

while True:
    conn, addr = sock.accept()      # 接受客户端连接
    recv_data = conn.recv(1024)     # 从接受缓冲区读消息 recv buffer
    print(recv_data)
    conn.sendall(recv_data)         # 将响应发送到发送缓冲 send buffer
    conn.close()