#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# async_wget.py
# chasyncio
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
# Created by Chyi Yaqing on 03/08/19 08:52.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
asyncio异步网络连接获取sina.com, sohu.com, 163.com网站首页
"""
import asyncio
import time


@asyncio.coroutine
def wget(host):
    print('%s: wget %s...' % (time.time(), host))
    connect = asyncio.open_connection(host, 80)
    # yield from 异步操作
    reader, writer = yield from connect
    header = 'GET / HTTP/1.1\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s: %s header > %s' % (
            time.time(), host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


loop = asyncio.get_event_loop()
# 封装成一组Task完成并发
tasks = [wget(host) for host in [
    'www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
