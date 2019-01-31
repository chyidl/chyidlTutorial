#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 1.16.Filtering_Sequence_Elements.py
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
# Created by Chyi Yaqing on 01/29/19 22:33.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT
"""
Problem:
    extract values or reduce the sequence using some criteria
Solution:
    filter sequence data is use a list comprehension
"""
import math
from itertools import compress


mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print("old list: {}".format(mylist))
# list comprehension
print("new bigger than zero list: {}".format([n for n in mylist if n > 0]))
print("new lowwer than zero list: {}".format([n for n in mylist if n < 0]))

# use generator expressions to produce the filtered values iteratively.
# generator expression
pos = (n for n in mylist if n > 0)
for x in pos:
    print(x)

# built-in filter() function
values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


# filter() create an iterator,
ivals = list(filter(is_int, values))
print(ivals)

# transform the data at the same time
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([math.sqrt(n) for n in mylist if n > 0])

# filter criterion
clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)

clip_pos = [n if n < 0 else 0 for n in mylist]
print(clip_pos)

# apply the results of filtering one sequence to another related sequence.
addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]


more5 = [n > 5 for n in counts]
print(list(compress(addresses, more5)))
