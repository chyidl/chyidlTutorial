#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# search_first_last_position_sorted_array.py
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
# Created by Chyi Yaqing on 02/19/19 13:56.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Find first and last positions of an element in a sorted array

Given a sorted array with possibly duplicate elements, the task is to find
indexes of first and last occurrences of an element x in the given array.

The Naive Approach is to run a for loop and check given element in array
    1) Run a for loop and for i = 0 to n-1
    2) take first  = -1 and last = -1
    3) When we find element first time then we update first  = i
    4) We always update last=i whenever we find the element
    5) We print first and last

Using binary search

1. For first occurrence of a number
    a) If (high >= low)
    b) Calculate mid = low + (high-low)/2
    c) If (mid == 0 || x > arr[mid-1]) && arr[mid] == x
        return mid;
    d) Else if (x > arr[mid])
        reurn first(arr, (mid+1), high, x, n)
    e) Else:
        return first(arr, low, (mid-1), x, n)
    f) Otherwise return -1;

2. For last occurrence of a number
    a) if (high >= low)
    b) calculate mid = low + (high - low)/2
    c) if((mid == n-1 || x < arr[mid+1]) && arr[mid] == x)
        return mid
    d) else if(x < arr[mid])
        return last(arr, low, (mid-1), x, n)
    e) else
        return last(arr, (mid + 1), high, x, n)
    f) otherwise return -1
"""


# Python3 program to find first and last occurrence of an elements in given
# sorted array
# Function for finding first and last occurrence of an elements
def findFirstAndLast(arr, n, x):
    first, last = -1, -1
    for i in range(0, n):
        if (x != arr[i]):
            continue
        if (first == -1):
            first = i
        last = i

    if (first != -1):
        print("First Occurrence = {}\nLast Occurrent = {}".format(first, last))
    else:
        print("Not Found")


# Driver code
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 8
print("Original Array is {}, find {}".format(arr, x))
findFirstAndLast(arr, len(arr), x)


# Python3 program to find first and last occurances of a number in
# a given sorted array

# if x is present in arr[] the returns the index of FIRST occurrence of x in
# arr[0..n-1], otherwise returns - 1
def first(arr, low, high, x, n):
    if (high >= low):
        mid = low + (high - low) // 2
        if ((mid == 0 or x > arr[mid - 1]) and arr[mid] == x):
            return mid
        elif x > arr[mid]:
            return first(arr, (mid + 1), high, x, n)
        else:
            return first(arr, low, (mid - 1), x, n)
    return -1


# if x is present in arr[] then returns the index of LAST occurrence of x in
# arr[0..n-1], otherwise returns -1
def last(arr, low, high, x, n):
    if (high >= low):
        mid = low + (high-low)//2
        if ((mid == n-1 or x < arr[mid + 1]) and arr[mid] == x):
            return mid
        elif (x < arr[mid]):
            return last(arr, low, (mid - 1), x, n)
        else:
            return last(arr, (mid + 1), high, x, n)

    return -1


# Driver program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
n = len(arr)
x = 8
print("Original Array is {}, find {}".format(arr, x))
print("First Occurrence = {}\nLast Occurrence = {}".format(
    first(arr, 0, len(arr)-1, x, n), last(arr, 0, len(arr)-1, x, len(arr))))


# if x is present in arr[] then returns the index of first occurrence of bigger
# than x in arr[0..n-1], otherwise returns -1
def biggerFirst(arr, low, high, x, n):
    if (high >= low):
        mid = low + (high-low)//2
        if ((mid == n-1 or x >= arr[mid - 1]) and arr[mid] > x):
            return mid
        elif (x < arr[mid]):
            return biggerFirst(arr, low, (mid - 1), x, n)
        else:
            return biggerFirst(arr, (mid + 1), high, x, n)

    return -1


# if x is present in arr[] then returns the index of first occurrence of bigger
# than x in arr[0..n-1], otherwise returns -1
def smallerLast(arr, low, high, x, n):
    if (high >= low):
        mid = low + (high-low)//2
        if ((mid == 0 or x <= arr[mid + 1]) and arr[mid] < x):
            return mid
        elif (x < arr[mid]):
            return smallerLast(arr, low, (mid - 1), x, n)
        else:
            return smallerLast(arr, (mid + 1), high, x, n)
    return -1


# Driver program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
n = len(arr)
x = 2
print("Original Array is {}, find {}".format(arr, x))
print("First Bigger than {} Occurrence = {}".format(
    x, biggerFirst(arr, 0, len(arr)-1, x, len(arr))))
print("Last Smaller than {} Occurrence = {}".format(
    x, smallerLast(arr, 0, len(arr)-1, x, len(arr))))
