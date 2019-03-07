#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# server.py
# chweb
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
# Created by Chyi Yaqing on 03/07/19 16:40.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
负责启动WSGI服务器，加载application()函数
"""
# 导入wsgiref模块
from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数
from hello import application


# 创建一个服务器,IP地址，端口9527,处理函数application
httpd = make_server('127.0.0.1', 9527, application)
print('Serving HTTP on port 9527...')
# 开始监听HTTP请求
httpd.serve_forever()
