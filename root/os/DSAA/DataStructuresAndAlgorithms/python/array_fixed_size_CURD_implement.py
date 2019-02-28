#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# array_fixed_size_CURD_implement.py
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
# Created by Chyi Yaqing on 02/28/19 13:50.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Implement an fixed size array, support dynamic add, delete, update, read
"""
import ctypes   # A foreign function library for Python


class FixedSizeArray:
    # Fixed Size Array class
    def __init__(self, capacity):
        self.n = 0  # Count actual element (Default is 0)
        self.capacity = capacity  # Default Capacity
        self.A = self.make_array(self.capacity)

    def __len__(self):
        # Return number of elements stored in array
        return self.n

    def __repr__(self):
        # "official" string representation of an object
        return ",".join(str(self.A[i]) for i in range(self.n))

    def __getitem__(self, index):
        # Return element at index
        index = self.checkindex(index)
        return self.A[index]  # Retrieve from the array at index

    def append(self, ele):
        # Add element to correct position
        if self.n == self.capacity:
            return RuntimeError('fixed size Array {} is full'.format(self.n))
        # finding correct position self.A[i] < ele < self.A[i+1]
        if self.n == 0:
            self.A[0] = ele
        elif self.n == 1:
            if ele < self.A[0]:
                self.A[0], self.A[1] = ele, self.A[0]
            else:
                self.A[1] = ele
        else:
            corrPos = float("-inf")
            for i in range(self.n-1):
                if self.A[i] <= ele <= self.A[i+1]:
                    corrPos = i+1
            if corrPos == float("-inf") and ele < self.A[0]:
                for i in range(self.n-1, -1, -1):
                    self.A[i+1] = self.A[i]
                self.A[0] = ele
            else:
                self.A[self.n] = ele
        self.n += 1

    def delete(self, idx):
        # delete element in idx
        idx = self.checkindex(idx)
        for i in range(idx, self.n-1):
            self.A[i] = self.A[i+1]
        self.n -= 1

    def update(self, idx, ele):
        # update element in idx to ele
        self.delete(idx)
        self.append(ele)
        
    def checkindex(self, idx):
        if idx < 0:  # Support negative numbers index
            idx = self.n + idx
        if not 0 <= idx < self.n:
            return IndexError('idx = {} is out of bounds !'.format(idx))
        return idx

    def make_array(self, cap):
        # Returns a array with capacity
        return (cap * ctypes.py_object)()


if __name__ == '__main__':
    arr = FixedSizeArray(10)
    for ele in range(5, -1, -1):
        arr.append(ele)
    print("Print order array")
    print(arr)
    print("Delete element in index  = {}".format(2))
    arr.delete(2)
    print("Print order array")
    print(arr)
    print("Update element in index = {}, ele = {}".format(0, 1024))
    arr.update(0, 1024)
    print("Print order array")
    print(arr)
