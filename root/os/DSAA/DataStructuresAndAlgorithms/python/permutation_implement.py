#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# permutation_implement.py
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
# Created by Chyi Yaqing on 02/23/19 11:02.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
"""


def permutations(arr, k):
    if k == 1:
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()

    for i in range(k):
        arr[i], arr[k-1] = arr[k-1], arr[i]
        permutations(arr, k-1)
        arr[i], arr[k-1] = arr[k-1], arr[i]


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    permutations(arr, 4)
