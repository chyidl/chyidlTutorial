#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# sort_insert_array_implement.py
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
# Created by Chyi Yaqing on 02/18/19 15:56.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Insertion Sort is a simple sorting algorithm t
Loop from i=1 to n-1, Pick element arr[i] and insert it into sorted sequence
    arr[0, i-1]
"""
import numpy as np
import time


# Python program for implementation of Insertion Sort
# Function to do insertion sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are greater than key, to one
        # position ahead of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


# Driver code to test above
arr = [12, 11, 13, 5, 6]
print("Original array is : {}".format(arr))
insertionSort(arr)
print("Sorted array is : {}".format(arr))

testRandoms = np.random.randint(1, 101, [200, 100])
start = time.time()
for i in range(len(testRandoms)):
    insertionSort(testRandoms[i])
print("Consumes sum: {} ms".format((time.time()-start)*1000))
