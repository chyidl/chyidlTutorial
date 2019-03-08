#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# aio_collect_all_response.py
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
# Created by Chyi Yaqing on 03/08/19 11:56.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Want to collect all response in one list and do some postprocessing on them.
Let's return this response, keep it in list, and print all responses at the end
"""
import asyncio
from aiohttp import ClientSession


async def fetch(url, session):
    async with session.get(url) as response:
        # response.read() is async operation.
        # This means that it does not return result immediately
        return await response.read()  # NOT: return response.read()


async def run(urls):
    tasks = []
    # Fetch all responses within one Client session,
    # keep connection alive for all requests.
    async with ClientSession() as session:
        for url in urls:
            task = asyncio.ensure_future(fetch(url, session))
            tasks.append(task)

        # This collects bunch of Future objects in one place and
        # waits for all of them to finish
        responses = await asyncio.gather(*tasks)
        # You now have all response bodies in this variable
        print(responses)


urls = ['http://httpbin.org/headers' for x in range(10)]
loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(urls))
loop.run_until_complete(future)
