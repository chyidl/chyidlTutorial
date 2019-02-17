#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# linked_list_LRU_implement.py
# python
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
# Created by Chyi Yaqing on 02/14/19 17:59.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Interview Question

Software Engineer Interview

"" Design an LRU cache. It's a data struct with a capacity. Beyond this
capacity the least recently used item is removed. You should be able to insert
an element, access and element given its key,and  delete an element,in contant
time. Note that when you access an element,event if it's just for a read,it
becames the most recently used"

Python includes a profiler called cProfile.It not only gives the total running
time, but also times each function separately, and tells you how many times
each function was called, making it easy to determine where you should make
optimizations.

>>> import cProfile
>>> cProfile.run('foo()')

invoke the cProfile when running a script
$ python3 -m cProfile linked_list_LRU_implement.py
$ python3 -m cProfile -o file.prof script.py  # SAVE

>>> import pstats
>>> p = pstats.Stats('shorten.prof')
>>> p.sort_stats('calls')

RunSnakeRun is a small GUI utility that allows you to view (Python) cProfile or
Profile profiler dumps in a sortable GUI view.
"""
import collections


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()  # store the (key, value)

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value


def naive_lru_cache():
    lru_test = LRUCache(capacity=3)
    lru_test.set(1, 1)
    lru_test.set(2, 2)
    lru_test.get(1)
    lru_test.set(3, 3)
    lru_test.get(2)
    lru_test.set(4, 4)
    lru_test.get(1)
    lru_test.get(3)
    lru_test.get(4)
