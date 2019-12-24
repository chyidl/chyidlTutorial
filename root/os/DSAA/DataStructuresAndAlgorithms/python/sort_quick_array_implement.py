#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# sort_quick_array_implement.py
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
# Created by Chyi Yaqing on 02/18/19 18:10.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and
partitions the given array around the picked pivot. There are many different
versions of quickSort that pick pivot in different ways.
    1. Always pick first element as pivot
    2. Always pick last element as pivot (implemented below)
    3. Pick a random element as pivot
    4. Pick median as pivot.

Pseudo Code for recursive QuickSort function:
    /* low --> Starting index, high --> Ending index */
    quickSort(arr[], low, high)
    {
        if (low < high)
        {
            /* pi is partitioning index, arr[pi] is now
            at right place */
            pi = partition(arr, low, high)

            quickSort(arr, low, pi- 1) // Before pi
            quickSort(arr, pi + 1, high)// After pi
        }
    }

Partition Algorithm:
"""
# Function to do Quick sort


def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partiton
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


# Python program for implementation of Quicksort Sort
# This function takes last element as pivot, places the pivot element
# at its correct position in sorted array, and places all smaller (smaller
# than pivot) to left of pivot and all greater elements to right of pivot
def partition(arr, low, high):
    i = low  # index of smaller element
    # 获取分区点
    pivot = arr[high]  # pivot

    # 遍历数据
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
if __name__ == '__main__':
    """
    递推公式: quick_sort(p...r) = quick_sort(p...q-1) quick_sort(q+1...r)
    终止条件 p >= r
    """
    # Driver code to test above
    arr = [10, 7, 5, 8, 9, 1, 5]
    print("Original array is {}".format(arr))
    quickSort(arr, 0, len(arr)-1)
    print("Sorted array is {}".format(arr))
