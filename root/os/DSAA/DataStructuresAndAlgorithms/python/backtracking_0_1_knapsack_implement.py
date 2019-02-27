#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# backtracking_0_1_knapsack_implement.py
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
# Created by Chyi Yaqing on 02/27/19 16:43.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Knapsack Problem -- Backtracking
Given n positive weights Wi, n positive profits Pi, and a positive number M
which is the knapsack capacity, the 0/1 knapsack problem calls for choosing a
subset of the weight such that
"""
weight = [2, 2, 4, 6, 3]
knapsack = 9
maxW = 0  #


def f(i=0, cw=0):
    global maxW
    # cw == knapsack 表示装满了，i==n表示物品都决策完
    if cw == knapsack or i == len(weight):
        if cw > maxW:
            maxW = cw
        return
    f(i+1, cw)  # 选择不装第i个物品
    if (cw + weight[i] <= knapsack):
        f(i+1, cw+weight[i])  # 选择装第i个物品

    return maxW


print(f())
