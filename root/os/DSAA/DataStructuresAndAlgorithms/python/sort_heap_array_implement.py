#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# sort_heap_array_implement.py
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
# Created by Chyi Yaqing on 02/23/19 13:33.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
HeapSort is a comparsion based sorting technique based on Binary Heap data
structure.

What is Binary Heap?
    1) A complete binary tree: is a binary tree in which every level, except
    possibly the last, is completely filled, and all nodes are as far left as
    possible.

    A Binary Heap is a Complete Binary Tree where items are stored in a special
    order that value in a parent node is greater(or smaller) than the values in
    its two children nodes. The former is called as max heap and the latter is
    called min heap. The heap can be represented by binary tree or array.

Why array based representating for Binary Heap?
    Since a Binary Heap is a Complete Binary Tree, it can be easily represented
    as array and array based representation is space efficient. If the parent
    node is stored at index i, the left child can be calculated by 2*i+1 and
    right child by a*i+2 (assuming the indexing starts at 0).
"""
# Python program for implementation of heap Sort


# To heapify subtree rooted at index i. n is size of heap
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2*i + 1  # left = 2*i + 1
    right = 2*i + 2  # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if left < n and arr[i] < arr[left]:
        largest = left

    # See if right child of root exists and is greater than root
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root
        heapify(arr, n, largest)


# The main function to sort an array of given size
def heapSort(arr):
    n = len(arr)

    # Build a maxheap
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


# Deiver code to test above
if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    heapSort(arr)
    n = len(arr)
    print("Sorted array is")
    for i in range(n):
        print("%d" % (arr[i]), end=" ")
