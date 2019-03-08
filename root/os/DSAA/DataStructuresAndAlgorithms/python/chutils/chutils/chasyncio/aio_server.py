#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# aio_server.py
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
# Created by Chyi Yaqing on 03/08/19 12:43.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Set up simple (async) aiohttp server.
The server is going to read full html text of Thinkdifferent.html. It will add
random delays between responses. Some responses will have zero delay, and some
will have maximum of 3 seconds delay. This should resemble real application,
few apps respond to all requests with same latency, usually latency differs
from response to response.
"""
import asyncio
import random
from datetime import datetime
from aiohttp import web


# Set seed to ensure async and sync client get same distribution of
# delay values and tests are fair
random.seed(1)


async def hello(request):
    request.match_info.get("name", "foo")
    n = datetime.now().isoformat()
    delay = random.randint(0, 3)
    await asyncio.sleep(delay)
    headers = {"content_type": "application/json", "delay": str(delay)}
    # opening file is not async here, so it may block, to improve
    # efficiency of this you can consier using asyncio Executors
    # that will delegate file oeeration to separate thread or process
    # and improve performance.
    # https://docs.python.org/3/library/asyncio-eventloop.html#executor
    # https://pymotw.com/3/asyncio/executors.html
    with open("Thinkdifferent.txt", "r") as r:
        print("{}: {} delay: {}".format(n, request.path, delay))
        json_body = r.read()
        response = web.json_response(
                {'result': json_body}, status=200, headers=headers)
    return response


app = web.Application()
app.router.add_route("GET", "/{name}", hello)
web.run_app(app)
