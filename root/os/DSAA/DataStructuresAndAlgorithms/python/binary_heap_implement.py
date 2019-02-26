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
Binary Heap Data Structure
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
    1) The root element will be at Arr[1]
    2) Below table shows indexes of other nodes for the ith node,
        Arr[(i)//2]    Returns the parent node
        Arr[2*i]      Returns the left child node
        Arr[(2*i)+1]  Returns the right child node

Operations on Max/Min Heap:
    1) getMin()/getMax(): it returns the root element of Min/Max Heap, Time
        Complexity of this operation is O(1)
    2) extractMin()/extractMax(): Removes the minimum/Maximum element from
        MinHeap/MaxHeap. Time Complexity of this Operation is O(Logn) as this
        operation needs to maintain the heap property (by calling heapify())
        after removing root
    3) decreaseKey(): Decreases value of key. The time complexity of this
        opeation is O(Logn). If the decreases key value of a node is greater
        than the parent of node, then we don't need to do anything. Otherwise,
        we need to traverse up to fix the violated heap property.
    4) insert(): Inserting a new key takes O(Logn) time. We add a new key at
        the end of the tree. If new key is greater than its parent, then don't
        need to do anything. Otherwise, we need to traverse up to fix the
        violated heap property.
    5) delete(): Deleting a key also takes O(Logn) time. We replace the key to
        be deleted with minum infinite by calling decreaeKey(). After
        decreaseKey(), the minus infinite value must reach root, so we
        extractMin() to remove the key.

A Complete binary tree: A complete binary tree is a tree in which each level
has all of its nodes. The exception to this is the bottom level of the tree,
which we fill in from left to right.
"""


class MinHeap:
    def __init__(self):
        self.heapList = [0]   # this zero is not used
        self.currentSize = 0  # to keep track of the current size of the heap

    def heapifyUp(self, i):
        # keep swapping until get to the top of the tree
        while i // 2 > 0:
            # If the newly added item is less than its parent,
            # swap the item with its parent
            if self.heapList[i] < self.heapList[i // 2]:
                self.heapList[i//2], self.heapList[i] = (
                        self.heapList[i], self.heapList[i//2])
            i //= 2

    def heapifyDown(self, i):
        while (i*2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = (
                        self.heapList[mc], self.heapList[i])
            i = mc

    def minChild(self, i):
        if i*2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[2*i] < self.heapList[2*i+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delete(self):
        retval = self.heapList[1]
        # take the last item in the list and moving it to the root position
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.heapifyDown(1)
        return retval

    def insert(self, data):
        self.currentSize += 1
        self.heapList.append(data)
        # comparting the newly added item with its parent.
        self.heapifyUp(self.currentSize)

    # build an entire heap from a list of keys.
    # 完全二叉树，下标从n/2+1到n的节点都是叶子结点
    def buildHeap(self, alist):
        # 因为叶子节点往下堆化只能自己跟自己比较，所以直接从第一个非叶子节点开始
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.heapifyDown(i)
            i -= 1

    def sort(self, alist):
        self.buildHeap(alist)
        while self.currentSize > 1:
            # take the root position in the list and moving it to the last
            self.heapList[self.currentSize], self.heapList[1] = (
                    self.heapList[1], self.heapList[self.currentSize])
            self.currentSize -= 1
            self.heapifyDown(1)
        return self.heapList[1:]

    def printHeap(self):
        print("\nPrint Min Heap {}".format(self.heapList[1:]))


class MaxHeap:
    def __init__(self):
        self.heapList = [0]   # this zero is not used
        self.currentSize = 0  # to keep track of the current size of the heap

    def heapifyUp(self, i):
        # keep swapping until get to the top of the tree
        while i // 2 > 0:
            # If the newly added item is less than its parent,
            # swap the item with its parent
            if self.heapList[i] > self.heapList[i // 2]:
                self.heapList[i//2], self.heapList[i] = (
                        self.heapList[i], self.heapList[i//2])
            i //= 2

    def heapifyDown(self, i):
        while (i*2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] < self.heapList[mc]:
                self.heapList[i], self.heapList[mc] = (
                        self.heapList[mc], self.heapList[i])
            i = mc

    def minChild(self, i):
        if i*2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[2*i] > self.heapList[2*i+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delete(self):
        retval = self.heapList[1]
        # take the last item in the list and moving it to the root position
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.heapifyDown(1)
        return retval

    def insert(self, data):
        self.currentSize += 1
        self.heapList.append(data)
        # comparting the newly added item with its parent.
        self.heapifyUp(self.currentSize)

    # build an entire heap from a list of keys.
    # 完全二叉树，下标从n/2+1到n的节点都是叶子结点
    def buildHeap(self, alist):
        # 因为叶子节点往下堆化只能自己跟自己比较，所以直接从第一个非叶子节点开始
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.heapifyDown(i)
            i -= 1

    def sort(self, alist):
        self.buildHeap(alist)
        while self.currentSize > 1:
            # take the root position in the list and moving it to the last
            self.heapList[self.currentSize], self.heapList[1] = (
                    self.heapList[1], self.heapList[self.currentSize])
            self.currentSize -= 1
            self.heapifyDown(1)
        return self.heapList[1:]

    def printHeap(self):
        print("\nPrint Max Heap : {}".format(self.heapList[1:]))


if __name__ == '__main__':
    minheap = MinHeap()
    minheap.insert(40)
    minheap.insert(39)
    minheap.insert(30)
    minheap.printHeap()
    minheap.delete()
    minheap.printHeap()

    alist = [9, 7, 8, 5, 6, 3, 4, 1, 2]
    print("\nOriginal List: {}".format(alist))
    print("Sorted List is : {}".format(minheap.sort(alist)))
