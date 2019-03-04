#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# map_reduce_str2int_str2float_implement.py
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
# Created by Chyi Yaqing on 03/04/19 16:50.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT
from functools import reduce


CHAR_TO_NUMBER = dict(zip(".0123456789", [x for x in range(-1, 10)]))


def str2int(s):
    ints = map(lambda ch: CHAR_TO_NUMBER[ch], s)
    return reduce(lambda x, y: x*10 + y, ints)


def str2float(s):
    floats = map(lambda ch: CHAR_TO_NUMBER[ch], s)
    point = 0

    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f

        if point == 0:
            return f * 10 + n
        else:
            point *= 10
            return f + n / point
    # functools.reduce(function, iterable[], initializer)
    return reduce(to_float, floats, 0.0)


if __name__ == '__main__':
    # string to int
    print(str2int('0'))
    print(str2int('12300'))
    print(str2int('0012345'))

    # string to float
    print(str2float('0'))
    print(str2float('123.456'))
    print(str2float('0.1234'))
    print(str2float('.1234'))
