#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# aio_hello.py
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
# Created by Chyi Yaqing on 03/08/19 11:27.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Simple HTTP hello world

Making GET and fetching one single HTTP response using aiohttp
"""
import time
import asyncio
from aiohttp import ClientSession


# Make your function asynchronous by using async keyword before function
# definition and using await keyword
async def hello(url):
    # ClientSession allows store cookies between requests and keeps objects
    # that are common for all requests(event loop, connection and other things)
    async with ClientSession() as session:
        # use session make requests
        async with session.get(url) as response:
            response = await response.read()
            print(response.decode('utf-8'))


start = time.time()
urls = ["http://httpbin.org/headers" for x in range(10)]
tasks = []
loop = asyncio.get_event_loop()
# wrap asyncio Future object and pass whole lists of Future objects as tasks
for url in urls:
    task = asyncio.ensure_future(hello(url))
    tasks.append(task)
loop.run_until_complete(asyncio.wait(tasks))
print("Total Time: %.5f second" % float(time.time() - start))
