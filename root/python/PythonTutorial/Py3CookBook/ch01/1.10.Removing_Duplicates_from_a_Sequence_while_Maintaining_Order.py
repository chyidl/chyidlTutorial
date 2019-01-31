#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 1.10.Removing_Duplicates_from_a_Sequence_while_Maintaining_Order.py
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
# Created by Chyi Yaqing on 01/25/19 15:30.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT
"""
Problem:
    eliminate the duplicate values in a sequence, but preserve the order
    of the remaining items

Solution:
    If the values in the sequence are hashable, the problem can be
    easily solved using a set and a generator
"""


# items are hashable
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
        seen.add(item)


# items are unhashable
def dedupe_unhashable(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


if __name__ == '__main__':
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print("RAW sequence: {}".format(a))
    print("Removing Duplicates: {}".format(list(dedupe(a))))

    print('-'*20)
    a = [
            {'x': 1, 'y': 2},
            {'x': 1, 'y': 3},
            {'x': 1, 'y': 2},
            {'x': 2, 'y': 4}
    ]
    print("RAW : {}".format(a))
    print("dedupe_unhashable() : ".format(
        list(dedupe_unhashable(a, key=lambda d: (d['x'], d['y'])))))
    print("dedepe_unhashable() : ".format(
        list(dedupe_unhashable(a, key=lambda d: (d['x'])))))
