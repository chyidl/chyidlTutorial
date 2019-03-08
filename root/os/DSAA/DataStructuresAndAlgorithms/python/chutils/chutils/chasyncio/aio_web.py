#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# aio_web.py
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
# Created by Chyi Yaqing on 03/08/19 09:14.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
asyncio实现了TCP.UDP.SSL等协议，aiohttp则是基于asyncio实现的HTTP框架

编写一个HTTP服务器,分别处理URL
    / - 首页返回b'<h1>Index</h1>'
    /hello/{name} - 根据URL参数返回文本hello, %s!
"""
import asyncio
from aiohttp import web


async def index(request):
    await asyncio.sleep(0.5)
    return web.json_response({'some': 'data'})


async def hello(request):
    await asyncio.sleep(0.5)
    text = 'hello, %s!' % request.match_info['name']
    #return web.Response(body=text.encode('utf-8'))
    return web.json_response({'result': text})


async def init(loop):
    app = web.Application()
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    # asyncio 创建TCP服务
    srv = await loop.create_server(app._make_handler(), '127.0.0.1', 9527)
    print('Server started at http://127.0.0.1:9527...')
    return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
