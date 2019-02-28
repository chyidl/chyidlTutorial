#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:encoding=utf-8
#
# array_two_merge_sorted_implement.py
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
# Created by Chyi Yaqing on 02/14/19 22:12.
# Copyright © 2019. Chyi Yaqing. All rights reserved.
#
# Distributed under terms of the MIT
"""
Given two sorted arrays, the task is to merge them in a sorted manner.

Method 1: Merge two sorted arrays with O(1) extra space
    merge two array such that the initial numbers (after complete sorting) are
    in the first array and the remaining numbers are in the second array. Extra
    space allowed in O(1).

    This task is simple and O(m+n) if we are allowed to use extra space. But it
    be-comes really complicated when extra space is not allowed and doesn't
    look posible in less the O(m*n) worst case time.

Below is algorithm:
    1) Iterate through every element of ar2[] starting from last element. Do following for every element ar2[i]
    a) Store last element of ar1[j]: last = ar1[j]
    b) Loop for last element of ar1[] while element ar1[j] is smaller than ar2[i].
        ar1[j+1] = ar1[j]  // Move element one position ahead
        j--
    c) If any element of ar1[] was moved or (j != m-1)
        ar1[j+1] = ar2[i]
        ar2[i] = last
"""


# Below is the implementation of above algorithm.
# Python program to merge two sorted arrays with O(1) extra space.
# Merge ar1[] and ar2[] with O(1) extra space
def merge_method1(ar1, ar2, m, n):
    # Iterate through all elements of ar2[] starting from the last element
    for i in range(n-1, -1, -1):
        # Find the smallest element greater then ar2[i]. Move all elements
        # one position ahead till the smallest greater element is not found
        last = ar1[m-1]
        j = m-2
        while (j >= 0 and ar1[j] > ar2[i]):
            ar1[j+1] = ar1[j]
            j -= 1

        # If there was a greater element
        if (j != m-2 or last > ar2[i]):
            ar1[j+1] = ar2[i]
            ar2[i] = last


# Driver program
ar1 = [1, 5, 9, 10, 15, 20]
ar2 = [2, 3, 8, 13]
m, n = len(ar1), len(ar2)

print("Before Merging \n First Array:", end="")
for i in range(m):
    print(ar1[i], " ", end="")

print("\nSecond Array: ", end="")
for i in range(n):
    print(ar2[i], " ", end="")

print()
print('='*20)
merge_method1(ar1, ar2, m, n)

print("After Merging \n First Array:", end="")
for i in range(m):
    print(ar1[i], " ", end="")

print("\nSecond Array: ", end="")
for i in range(n):
    print(ar2[i], " ", end="")


"""
Method 2 (O(n1 + n2) Time and O(n1 + n2) Extra Space)
    The idea is to use Merge function of Merge sort.
    1. Create an array ar3[] of size n1 + n2
    2. Simultaneously traverse ar1[] and ar2[].
        Pick smaller of current elements in ar1[] and ar2[], copy this
        smaller element to next position in ar3[] and move ahead in ar3[]
        and the array whose element is picked.
    3. If these are remaining elements in ar1[] or ar2[], copy them also in
    ar3[]
"""


# Python program to merge two sorted arrays with O(n1 + n2) Extra Space
# Merge arr1[0..m-1] and arr2[0..n-1] into arr3[0..n+m-1]
def merge_method2(ar1, ar2, m, n):
    ar3 = [None] * (m + n)
    i, j, k = 0, 0, 0
    # Traverse both array
    while i < m and j < n:
        # Check if current elemnt of first array is smaller then current
        # element of second array. If yes, store first array element and
        # increment first array index. Otherwise do same with second array
        if ar1[i] < ar2[j]:
            ar3[k] = ar1[i]
            k += 1
            i += 1
        else:
            ar3[k] = ar2[j]
            k += 1
            j += 1

    # Store remaining elements of first array
    while i < m:
        ar3[k] = ar1[i]
        k += 1
        i += 1

    # Store remaining elements of second array
    while j < n:
        ar3[k] = ar2[j]
        k += 1
        j += 1

    return ar3


# Driver program
ar1 = [1, 5, 9, 10, 15, 20]
ar2 = [2, 3, 8, 13]
m, n = len(ar1), len(ar2)

print("\nMethod 2: Before Merging \n First Array:", end="")
for i in range(m):
    print(ar1[i], " ", end="")

print("\nSecond Array: ", end="")
for i in range(n):
    print(ar2[i], " ", end="")

print()
print('='*20)
ar3 = merge_method2(ar1, ar2, m, n)

print("Array after merging\n")
for i in range(m + n):
    print(ar3[i], " ", end="")
