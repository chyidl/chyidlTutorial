#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# sort_selection_array_implement.py
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
# Created by Chyi Yaqing on 02/18/19 16:16.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Selection Sort:
The selection sort algorithm sorts an array by repeatedly finding the minimum
element(considering ascending order)from unsorted part and putting it at the
beginning. The algorithm maintains two subarrays in a given array.
    1) The Subarray which is already sorted
    2) Remaining subarray which is unsorted

In every iteration of selection sort, the minimum element (considering ascendin
order) from the unsorted subarray is picked and moved to the sorted subarray
"""


# Python program for implementation of Selection Sort
def selectionSort(arr):
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# Driver code to test above
arr = [64, 25, 12, 22, 11]
print("Original array is : {}".format(arr))
selectionSort(arr)
print("Sorted array is : {}".format(arr))
