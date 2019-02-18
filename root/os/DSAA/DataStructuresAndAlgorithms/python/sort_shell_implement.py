#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# sort_shell_implement.py
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
# Created by Chyi Yaqing on 02/18/19 16:50.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
ShellSort is mainly a variation of Insertion Sort.
"""


# Python3 program for implementation of Shell Sort
def shellSort(arr):
    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = n//2

    # Do a gapped insertion sort for this gap size. The first gap elements
    # a[0..gap-1] are already in gapped order keep adding one more element
    # until the entire array is gap sorted.
    while gap > 0:
        for i in range(gap, n):
            # add a[i] to the element that have been gap sorted save a[i] in
            # temp and make a hole at position i
            temp = arr[i]

            # shift earlier gap-sorted elements up until the correct location
            # for a[i] is found.
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap

            # put temp (the original a[i]) in its correct location
            arr[j] = temp
        gap //= 2


# Driver code to test above
arr = [12, 34, 54, 2, 3]

print("Array before sorting: {}".format(arr))
shellSort(arr)
print("Array after sorting: {}".format(arr))
