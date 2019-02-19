#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# sort_bucket_quicksort_array_implement.py
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
# Created by Chyi Yaqing on 02/19/19 10:34.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Bucket Sort is mainly useful when input is uniformly distributed over a range.

bucketSort(arr[], n)
    1) Create n empty buckets (Or lists).
    2) Do following for every array element arr[i].
        Insert arr[]i into bucket[n*array[i]]
    3) Sort indicidual buckets using quick sort
    4) Concatenate all sorted buckets.
"""


# Python3 program to sort an array using bucket sort
# Python program for implementation of Quicksort Sort
# This function takes last element as pivot, places the pivot element
# at its correct position in sorted array, and places all smaller (smaller
# than pivot) to left of pivot and all greater elements to right of pivot
def partition(arr, low, high):
    i = low   # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index
# high --> Ending index


# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partiton
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


def bucketSort(x):
    arr = []
    slot_num = 10  # 10 means 10 slots, each slot's size is 0.1
    for i in range(slot_num):
        arr.append([])

    # Put array elements in different buckets
    for j in x:
        index_b = int(slot_num * j)
        arr[index_b].append(j)

    # Sort individual buckets
    for i in range(slot_num):
        if arr[i]:
            quickSort(arr[i], 0, len(arr[i])-1)

    # concatenate the result
    k = 0
    for i in range(slot_num):
        if arr[i]:
            for j in range(len(arr[i])):
                x[k] = arr[i][j]
                k += 1


# Driver Code
x = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print("Original array is {}".format(x))
bucketSort(x)
print("Sorted array is {}".format(x))
