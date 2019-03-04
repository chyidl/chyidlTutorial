#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# pascal_triangle_implement.py
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
# Created by Chyi Yaqing on 03/04/19 15:19.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
杨辉三角形，又称帕斯卡三角形，是二项式系数的一种写法，形似三角形。
"""


def triangles(max):
    L = [1]
    n = 1
    while n < max:
        yield L
        L = [sum(i) for i in zip([0]+L, L+[0])]
        n += 1


if __name__ == '__main__':
    for i in triangles(10):
        print(i)
