#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# sort_radix_array_implement.py
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
# Created by Chyi Yaqing on 02/19/19 11:49.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Radix sort: The idea of Radix Sort is to do digit by digit sort starting from
least significant digit to most significant digit.
Counting sort is a linear time sorting algorithm that sort in O(n+k) time when
elements are in range from 1 to k.
"""


# Python program for implementation of Radix Sort
# A function to do counting sort of arr[] according to the digit represented by
# exp.
def countingSort(arr, exp1):
    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = int(arr[i]/exp1)
        count[(index) % 10] += 1

    # Change count[i] so that count[i] now contains actual position of this
    # digit in output array
    for i in range(1, 10):
        count[i] += count[i-1]

    # Build the output array
    i = n-1
    while i >= 0:
        index = int(arr[i]/exp1)
        output[count[(index) % 10]-1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copying the output array to arr[], so that arr now contains sorted number
    for i in range(0, len(arr)):
        arr[i] = output[i]


# Method to do Radix Sort
def radixSort(arr):
    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead of pssing digit
    # number, exp is passed. exp is 10^i where i is current digit number
    exp = 1
    while max1/exp > 0:
        countingSort(arr, exp)
        exp *= 10


# Driver code to test above
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array is {}".format(arr))
radixSort(arr)
print("Sorted array is {}".format(arr))
