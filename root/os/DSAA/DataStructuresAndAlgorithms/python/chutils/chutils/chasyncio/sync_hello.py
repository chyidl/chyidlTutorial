#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# sync_hello.py
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
# Created by Chyi Yaqing on 03/08/19 11:26.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Simple HTTP hello world

Making GET and fetching one single HTTP response
"""
import time
import requests


def hello(urls):
    # Fetch multiple urls
    for index, url in enumerate(urls):
        print(index, requests.get("http://httpbin.org/get").text)
    return None


start = time.time()
urls = ['http://httpbin.org/get' for x in range(10)]
print(hello(urls))
print('Total time: %.5f second' % float(time.time() - start))
