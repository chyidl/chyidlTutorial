#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# array_dynamic_append_implement.py
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
# Created by Chyi Yaqing on 02/14/19 16:34.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT
"""
1. Implement an array that supports dynamic expansion
    A synamic array is similar to an array, but with the difference that its
size can be dy-namically modified at runtime. The elements of an array occupy a
contiguous block of memory, and once created, its size cannot be changed. A
dynamic array can, once the array is filled, allo-cate a bigger chunk of memory
copy the contents from the original array to this new space, and continue to
fill the avilable slots.

The key is to provide means to grows an array A that stores the elemnts of a
list. We can't actually grow the array, its capacity is fixed. If an element is
appended to a list at a time, when the underlying array is full, we need to
perform following steaps.

1. Allocate a new array B with larger capacity (A commonly used rule for the
new array is to have twice the capacity of the existing array)

2. Set B[i]=A[i], for i=0 to n-1 where n denotes the current no if items.

3. Set A = B that is, we hence forth use B as the arry of supporting list.

4. Insert new element in the new array.
"""
import ctypes  # A foreign function library for Python


class DynamicArray(object):
    # Dynamic Array class (Similar to Python List)
    def __init__(self):
        self.n = 0  # Count actual elements (Default is 0)
        self.capacity = 1  # Default Capacity
        self.A = self.make_array(self.capacity)

    def __len__(self):
        # Return number of elements sorted in array
        return self.n

    def __getitem__(self, k):
        # Return element at index k
        if k < 0:  # support negative numbers index
            k = self.n + k
        if not 0 <= k < self.n:
            # Check it k index is in bounds of array
            return IndexError('K = {} is out of bounds !'.format(k))

        return self.A[k]  # Retrieve from the array at index k

    def append(self, ele):
        # Add element to end of the array
        if self.n == self.capacity:
            # Double capacity if not enough room
            self._resize(2 * self.capacity)

        self.A[self.n] = ele  # Set self.n index to element
        self.n += 1

    def _resize(self, new_cap):
        # Resize internal array to capacity new_cap
        B = self.make_array(new_cap)  # New bigger array

        for k in range(self.n):  # Reference all existing values
            B[k] = self.A[k]

        self.A = B  # Call A the new bigger array
        self.capacity = new_cap  # Reset the capacity

    def make_array(self, new_cap):
        # Returns a new array with new_cap capacity
        return (new_cap * ctypes.py_object)()


# Awesome, made dynamic array, Play around with it
if __name__ == '__main__':
    arr = DynamicArray()
    print("INDEX\t -> SIZE\t -> ELEMENT\t -> CAPACITY")
    for index, ele in enumerate(range(10)):
        # Append new element
        arr.append(ele)
        print(index, "\t ->", len(arr), "\t ->", arr[-1], "\t ->", arr.capacity)
