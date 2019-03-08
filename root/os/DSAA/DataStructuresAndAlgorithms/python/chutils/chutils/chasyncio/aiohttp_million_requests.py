#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# aiohttp_million_requests.py
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
# Created by Chyi Yaqing on 03/08/19 11:03.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Making 1 million requests with Python-aiohttp

Limits of aiohttp=3.5.4 and check performance in terms of requests per minute.

Everyone knows that asynchronous code performs better when applied to network
operations, but it's still interesting to check this assumption and understand
how exactly it is better and why it's better.

Async programming is not easy. It's not easy because using callbacks and
thinking in terms of events and event handlers requires more effort than usual
synchronous programming.
"""
