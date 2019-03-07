#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# hello.py
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
# Created by Chyi Yaqing on 03/07/19 16:39.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
实现Web应用程序的WSGI函数
"""


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1></hr><h1>Request Method: %s</h1>' % ((
        environ['PATH_INFO'][1:] or 'web'), (environ['REQUEST_METHOD']))
    return [body.encode('utf-8')]
