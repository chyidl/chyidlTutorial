#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 8080))   # 连接服务器
sock.sendall(b"hello rpc")           # 将消息输出到发送缓冲区 send buffer
print(sock.recv(1024))              # 从接受缓冲区 recv buffer 读数据
sock.close()
