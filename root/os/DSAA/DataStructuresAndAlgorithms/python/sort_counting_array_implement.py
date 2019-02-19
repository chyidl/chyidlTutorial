#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# sort_counting_array_implement.py
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
# Created by Chyi Yaqing on 02/19/19 11:09.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Counting Sort is a sorting technique based on keys between a specific range.It
works by counting the number of objects having distinct key values. Then doing
some arthmetic to calculate the position of each object in the output.

For simplicity, consider the data in the range 0 to 9.
Input data: 1, 4, 1, 2, 7, 5, 2
    1) Take a count array to store the count of each unique object.
        Index:  0 1 2 3 4 5 6 7 8 9
        Count:  0 2 2 0 1 1 0 1 0 0

    2) Modify the count array such that each element at each index stores the
    sum of previous counts.
        Index:  0 1 2 3 4 5 6 7 8 9
        Count:  0 2 4 4 5 6 6 7 7 7

The modified count array indicates the position of each object in the
the output sequence.
    3) Output each object from the input sequence followed by decreasing its
    count by 1
    Process the input data: 1, 4, 1, 2, 7, 5, 2. Position of 1 is 2. Put data
    1 at index 2 in output. Decrease count by 1 to place next data 1 at an
    index 1 smaller than this index.
"""


# Python program for counting sort
# The main function that sort the given string arr[] in alphabetical order
def countSort(arr):
    # The output character array that will have sorted arr
    output = [0 for i in range(256)]

    # Create a count array to store count of inidividul characters and
    # initialize count array as 0
    count = [0 for i in range(256)]

    # For storing the resulting answer since the string is immutable
    ans = ["" for _ in arr]

    # Store count of each character
    for i in arr:
        count[ord(i)] += 1

    # Change count[i] so that count[i] now contains actual position of this
    # character in output array
    for i in range(256):
        count[i] += count[i-1]

    # Build the output character array
    for i in range(len(arr)):
        output[count[ord(arr[i])]-1] = arr[i]
        count[ord(arr[i])] -= 1

    # Copy the output array to arr, so that arr now contains sorted characters
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans


# Driver program to test above function
arr = "geeksforgeeks"
ans = countSort(arr)
print("Sorted character array is {}".format(ans))
