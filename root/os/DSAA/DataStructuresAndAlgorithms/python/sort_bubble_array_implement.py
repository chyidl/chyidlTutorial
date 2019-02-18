#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# sort_bubble_array_implement.py
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
# Created by Chyi Yaqing on 02/18/19 14:19.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Bubble Sort is the simple sorting algorithm that works by repeatedly swapping
the adjacent elements if they are in wrong order.

Optimized Implementation:
    The below function always runs O(n^2) time even if the array is sorted. It
    be optimized by stopping the algorithm if inner loop didn't cause any swap.
"""
import numpy as np
import time


# Python program for implementation of Bubble Sort
# Optimized implementation of Bubble sort
def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1 swap if the element found is
            # greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        # If no two elements were swapped by inner loop, then break
        if swapped is False:
            break


# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

print("Original array is: {}".format(arr))
bubbleSort(arr)
print("Sorted array is: {}".format(arr))

testRandoms = np.random.randint(1, 101, [200, 100])
start = time.time()
for i in range(len(testRandoms)):
    bubbleSort(testRandoms[i])
print("Consumes sum: {} ms".format((time.time()-start)*1000))
