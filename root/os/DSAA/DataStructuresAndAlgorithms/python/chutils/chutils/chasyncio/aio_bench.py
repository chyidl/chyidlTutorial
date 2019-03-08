#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# aio_bench.py
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
# Created by Chyi Yaqing on 03/08/19 13:40.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Simple HTTP client

Making GET and fetching HTTP response using aiohttp

Async client does not waste time, when something is delayed it simply does
something else, issues other requests or processes all other responses.

adding some synchronization in your client limiting number of
concurrent requests it can process.
"""
import time
import asyncio
from aiohttp import ClientSession


# Create instance of Semaphore
sema = asyncio.Semaphore(1000)


async def fetch(url):
    async with sema, ClientSession() as session:
        async with session.get(url) as response:
            delay = response.headers.get("DELAY")
            d = response.headers.get("DATE")
            current_url = response.url
            response = await response.text(encoding="utf-8")
            print("{}:{} delay {}".format(d, current_url, delay))


start = time.time()
tasks = []
# That's bad, seems like stumbled across 10k connections problems
r = 10000
url = "http://localhost:8080/{}"
loop = asyncio.get_event_loop()
for i in range(r):
    task = asyncio.ensure_future(fetch(url.format(i)))
    tasks.append(task)
loop.run_until_complete(asyncio.wait(tasks))
print("Total time: %.5f second" % float(time.time() - start))
