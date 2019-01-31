#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 1.4.Finding_the_Largest_or_Smallest_N_Items.py
# ch01
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
# Created by Chyi Yaqing on 01/25/19 10:47.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT
# heapq --  Heap queue algorithm
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print("{} the Largest is {}".format(nums, heapq.nlargest(3, nums)))
print("{} the Smallest is {}".format(nums, heapq.nsmallest(3, nums)))

# nlargest, nsmallest accept a key parameter
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares':75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
print("{} price cheap smallest : {}".format(portfolio, cheap))
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print("{} price cheap largest : {}".format(portfolio, expensive))
