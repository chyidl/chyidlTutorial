#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# binary_search_array_implement.py
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
# Created by Chyi Yaqing on 02/19/19 12:42.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Binary Search: Search a sorted array by repeatedly dividing the search interval
in half. Begin with an iteraval convering the whole array. If the value of the
search key is less than the item in the middle of the interval, narrow the
interval to the lower half. Other-wise narrow it to the upper half. Repeatedly
cheack until the value is found or the interval is empty.
"""


# Python program for recursive binary search.
# Returns index of x in arr if present, else -1
def binarySearch_recursive(arr, l, r, x):
    # Check base case:
    if r >= l:
        mid = l + (r-l)//2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, the it can only be present in
        # left subarray
        elif arr[mid] > x:
            return binarySearch_recursive(arr, l, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binarySearch_recursive(arr, mid + 1, r, x)
    else:
        # Element is not present in the array
        return -1


# Python code to implement iterative Binary Search
# It returns location of x in given array arr if present, else returns -1
def binarySearch_iterative(arr, left, right, x):
    while left <= right:
        mid = left + (right-left)//2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            left = mid + 1

        # If x is smaller, ignore right half
        else:
            right = mid - 1

    # If we reach here, then the element was not present
    return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10
print("Original Array is {}, search {}".format(arr, x))


# Function call
result = binarySearch_recursive(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index {}".format(result))
else:
    print("Element is not present in array")

# Function call
result = binarySearch_iterative(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index {}".format(result))
else:
    print("Element is not present in array")
