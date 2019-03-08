#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# async_Produce_Consumer.py
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
# Created by Chyi Yaqing on 03/07/19 22:36.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
协程 - 生产者消费者模型
"""


# 生产者
def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('[Producer] Producing %s...' % n)
        r = c.send(n)
        print('[Producer] Consumer return: %s' % r)
    c.close()


# 消费者
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[Consumer] Consuming %s...' % n)
        r = '200 OK'


c = consumer()
produce(c)
