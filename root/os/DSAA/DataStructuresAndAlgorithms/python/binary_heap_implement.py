#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# binary_heap_implement.py
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
# Created by Chyi Yaqing on 02/23/19 12:31.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Heap Data Structure
    A Heap is a special Tree-based data structure in which the tree is a
    complete binary tree.

Heaps can be of two types:
    1) Max-Heap: In a Max-Heap the key present at the root node must be
    greatest among the keys present at all of it's children. The same property
    must be recursively true for all sub-trees in that Binary Tree.

    2) Min-Heap: In a Min-Heap the key present at the root node must be minimum
    among the keys present at all of it's children. The same property must be
    recursively true for all sub-trees in that Binary Tree.

How is Binary Heap represented?
    A Binary Heap is a Complete Binary Tree. A binary heap is typically
    represented as an array.
    1) The root element will be at Arr[0]
    2) Below table shows indexes of other nodes for the ith node,
        Arr[(i-1)/2]  Returns the parent node
        Arr[(2*i)+1]  Returns the left child node
        Arr[(2*i)+2]  Returns the right child node
"""
import operator


# heappop - pop and return the smallest element from heap
# heappush - push the value item onto the heap, maintaining heap invarient
# heapify - transform list into heap, in place, in linear time
# A class for Min Heap
class Heap:
    """
    Attributes:
        heap: List representation of the heap
        compare(p, c): comparator function, returns true if the relation
            between p and c is parent-chield
    """
    # Constructor to initialize a heap
    def __init__(self, heap=None, compare=operator.lt):
        self.heap = []
        self.compare = compare

    def __repr__(self):
        return 'Heap({!r}, {!r})'.format(self.heap, self.compare)

    def _inv_heapify(self, child_index):


    def parent(self, i):
        return (i-1)//2

    # Inserts a new key 'k' push the last heap
    def insertKey(self, k):
        # Push the value item onto the heap, maintaining the heap invariant
        heappush(self.heap, k)

    # Decrease value of key at index 'i' to new_val It is assumed that new_val
    # is smaller than heap[i]
    def decreaseKey(self, i, new_val):
        self.heap[i] = new_val
        while(i != 0 and self.heap[self.parent(i)] > self.heap[i]):
            # Swap heap[i] with heap[parent(i)]
            self.heap[i], self.heap[self.parent(i)] = (
                    self.heap[self.parent(i)], self.heap[i])

    # Method to remove minium element from min heap
    def extractMin(self):
        return heappop(self.heap)

    # This function deletes key at index i. It first reduces value to minus
    # infinite and then calls extractMin()
    def deleteKey(self, i):
        self.decreaseKey(i, float("-inf"))
        self.extractMin()

    # Get the minimum element from the heap
    def getMin(self):
        return self.heap[0]


# Driver program to test above function
if __name__ == '__main__':
    heapObj = MinHeap()
    heapObj.insertKey(3)
    heapObj.insertKey(2)
    heapObj.insertKey(1)
    heapObj.insertKey(15)
    heapObj.insertKey(5)
    heapObj.insertKey(4)
    heapObj.insertKey(45)

    print(
            heapObj.extractMin(),
            heapObj.getMin(),
            heapObj.decreaseKey(2, 1),
            heapObj.getMin())
