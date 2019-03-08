#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# async_hello.py
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
# Created by Chyi Yaqing on 03/08/19 08:40.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
用asyncio实现Hello world代码
"""
import asyncio
import threading
import time


@asyncio.coroutine
def hello():
    print("%s: Hello world! (%s)" % (time.time(), threading.currentThread()))
    # 异步调用asyncio.sleep(1):
    yield from asyncio.sleep(1)
    print("%s: Hello again! (%s)" % (time.time(), threading.currentThread()))


# 获取EventLoop:
loop = asyncio.get_event_loop()
# 封装Tasks任务表
tasks = [hello(), hello()]
# 执行coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
