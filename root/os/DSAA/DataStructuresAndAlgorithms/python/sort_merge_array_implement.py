#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# sort_merge_array_implement.py
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
# Created by Chyi Yaqing on 02/18/19 17:22.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Merge Sort is a Divide and Conquer algorithm. It divides input array in two
halves, calls itself for the two halves and then merges the two sorted halves.

MergeSort(arr, l, r)
    if r > l:
        1. Find the middle point to divide the array into two halves:
            middle m = (l + r)/2
        2. Call mergeSort for first half:
            Call mergeSort(arr, l, m)
        3. Call mergeSort for second half:
            Call mergeSort(arr, m+1, r)
        4. Merge the two halves sorted in step 2 and 3:
            Call merge (arr, l, m ,r)

Time Complexity: Sorting arrays on different machines. Merge Sort is a
recursive algorithm and time complexity can be expressed as following
recurrence relation.
    T(n) = 2T(n/2) + o(n)
Auxiliary Space O(n)
"""
import numpy as np
import time


# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements into 2 halves
        R = arr[mid:]
        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half
        i = j = k = 0

        # Copy data to temp arras L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Driver code to test the above code
if __name__ == '__main__':
    arr = [5, 12, 11, 13, 5, 6, 7]
    print("Original array is {}".format(arr))
    mergeSort(arr)
    print("Sorted array is {}".format(arr))

testRandoms = np.random.randint(1, 101, [200, 100])
start = time.time()
for i in range(len(testRandoms)):
    mergeSort(testRandoms[i])
print("Consumes sum: {} ms".format((time.time()-start)*1000))
