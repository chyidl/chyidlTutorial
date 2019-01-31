#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 1.3.Keeping_the_Last_N_Items.py
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
# Created by Chyi Yaqing on 01/25/19 09:05.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT
"""
Problem:
    Want to keep a limited history of the last few items seen during
    iteration or during some other kind of processing.

Solution:
    Keeping a limited history is a perfect use for a collections.deque.
"""
# collections -- Container datatypes
# deque -- list-like container with fast appends and pops on either end
from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


# Example use on a file
if __name__ == '__main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'Python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)


"""cpython/Modules/_collectionsmodule.c
deque objects  -- doubly-linked list

d.leftblock[leftindex]
d.rightblock[rightindex]

    d.leftindex and d.rightindex are always in the range:
        0 <= index <= BLOCKLEN
    (d.leftindex + d.len -1 ) % BLOCKEN == d.rightindex


"""
