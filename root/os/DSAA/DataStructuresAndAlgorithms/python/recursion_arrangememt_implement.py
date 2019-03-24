#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:encoding=utf-8
#
# recursion_arrangememt_implement.py
# python
#
#   __________
#  / ___  ___ \
# / /  \/  \ \
# \ \___/\___/ /\
#  \____\/____/||
#  /     /\\\\\//
# |  🔥 |\\\\\\
#  \      \\\\\\
#    \______/\\\\
#     _||_||_
#
# Created by Chyi Yaqing on 03/24/19 21:28.
# Copyright © 2019. Chyi Yaqing. All rights reserved.
#
# Distributed under terms of the MIT
"""
排列：从n个元素中任取m个元素,并按照一定的顺序进行排列，称为排列
全排列: 当n==m时，称为全排列
permutation, also called an "arrangement number" or "order", is a
rearrangement of the elements of an ordered list S into a one-to-one
correspondence with S itself. A string of length n has n! permutation.

Algorithm Paradigm: Backtracking
Time Complexity: O(n*n)
"""
# Python program to print all permutations


def toString(alist):
    return ''.join(alist)


# Function to print permutations of string
def permute(alist, left, right):
    if left == right:
        print(toString(alist))
    else:
        for i in range(left, right+1):
            alist[left], alist[i] = alist[i], alist[left]
            permute(alist, left+1, right)
            # backtrack
            alist[left], alist[i] = alist[i], alist[left]


# Driver program to test the above function
alist = ["A", "B", "C"]
n = len(alist)
permute(alist, 0, n-1)
