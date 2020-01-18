#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# skip_list_implement.py
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
# Created by Chyi Yaqing on 02/20/19 17:49.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Skip list is a probabilistic data structure that allows efficient search,
insertion and removal operations. It was invented by William Pugh [1] 1989

On the other hand, skip lists are much like multiple linked lists with some
randomization.
The time complexity of skip lists can be reduced further by adding more layers.
In fact, the time complexity of search, insert and delete can become O(logn) in
average case with O(n) extra space.

Insert an Elements in Skip List

Deciding nodes level:
    randomLevel()
    lvl := 1
    // random() that returns a random value in [0...1]
    while random() < p and lvl < MaxLevel do
    lvl := lvl + 1
    return lvl

Node Structure
    Each node carries a key and a forward array carring pointers to nodes of a
    different level. A level i node carries i forward pointers indexed through
    0 to i

Insertion in Skip List
    start from highest level in the list and compare key of next node of the
    current node with the ley to be inserted. Basic idea is if -
        1. Key of next node is less than key to be inserted then we keep on
        moving forward on the same level
        2. Key of next node is greater than the key to be inserted then we
        store the pointer to current node i at update[i] and move one level
        down and continue our search

Following is the psuedo code for the insertion algorithm
    Insert(list, searchKey)
    local update[0...MaxLevel+1]
    x := list->header
    for i := list-level downto 0 do

Searching an element in Skip list
    Search(list, searchKey)
        x := list->header
        -- loop invariant: x-key < searchKey
        for i := list->level downto 1 do
            while x->forward[i]->key < searchKey do
                x := x->forward[i]
        -- x->key < searchKey <= x->forward[1]->key
        x := x->forward[1]
        if x->key = searchKey then return x->value
            else return failure

Following is the pseudo code for deletion
    Delete(list, searchKey)
        local update[1..MaxLevel]
        x := list->header
        for i := list->level downto 1 do
            while x->forward[i]->key < searchKey do
                x := x->forward[i]
            update[i] := x
        x := x->forward[1]
        if x->key = searchKey then
            for i := 1 to list->level do
                if update[i]->forward[i] != x then break
                update[i]->forward[i] := x->forward[i]
            free(x)
            while list->level > 1 and
                list->header->forward[list->level] = NIL do
            list->level := list->level - 1

References:
    [1] Skip Lists: A Probabilistic Alternative to Balanced Trees – W. Pugh.
    [2] Introduction to Algorithms MIT – Lecture 12: Skip Lists – Erik Demaine
"""
# implement a simple version of the skip list in python
import random


# Python3 code for inserting element in skip list
class Node:
    """A node from a"""
    # Class to implement node

    def __init__(self, data, level):
        self.data = data

        # list to hold references to node of different level(level from 1)
        self.forward = [None]*(level+1)


class SkipList:
    # Class for Skip list
    def __init__(self, max_lvl, P):
        # Maximum level for this skip list
        # If P = 1/2, MaxLevel = 16 is appropriate for data strutures
        # containing up to 2^16 elements
        self.MAXLVL = max_lvl

        # P is the fraction of the nodes with level i references also
        # having level i+1 references
        self.P = P

        # create header node and initialize key to -1
        self.header = self.createNode(self.MAXLVL, None)

        # current level of skip list
        self.level = 0

    # Create new SkipNode
    def createNode(self, lvl, data):
        return Node(data, lvl)

    # create random level for node
    def randomLevel(self):
        lvl = 0
        while random.random() < self.P and lvl < self.MAXLVL:
            lvl += 1
        return lvl

    # insert given key in skip list
    def insertElement(self, key):
        # create update array and initialize it
        update = [None]*(self.MAXLVL+1)
        current = self.header

        # start from highest level of skip list move the current reference
        # forward while key is greater than key of node next to current
        # Otherwise inserted current in update and move one level down and
        # continue search
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].data < key:
                current = current.forward[i]
            update[i] = current

        # reached level 0 and forward reference to right, which is desired
        # position to insert key.
        current = current.forward[0]

        # If current is NULL that means we have reached to end of the level
        # or current's key is not equal to key to insert that means we have
        # to insert node between update[0] and current node
        if current is None or current.data != key:
            # Generate a random level for node
            rlevel = self.randomLevel()

            # if random level is greater than list's current level (node with
            # highest level inserted in list so far), initialize update value
            # with reference to header for further use
            if rlevel > self.level:
                for i in range(self.level+1, rlevel+1):
                    update[i] = self.header
                self.level = rlevel

            # create new node with random level generated
            n = self.createNode(rlevel, key)

            # insert node by rearranging references
            for i in range(rlevel+1):
                n.forward[i] = update[i].forward[i]
                update[i].forward[i] = n

            print("Successfully inserted key {}".format(key))

    def searchElement(self, key):
        current = self.header

        # start from highest level of skip list move the current reference
        # forward while key is greater than key of node next to current
        # Otherwise inserted current in update and move one level down and
        # continue search
        for i in range(self.level, -1, -1):
            while(current.forward[i] and current.forward[i].data < key):
                current = current.forward[i]

        # reached level 0 and advance reference to right, which is prssibly
        # our desired node
        current = current.forward[0]

        # If current node have key equal to search key, we have found our
        # target node
        if current and current.data == key:
            print("Found key ", key)

    def deleteElement(self, search_key):
        # create update array and initialize it
        update = [Node]*(self.MAXLVL+1)
        current = self.header

        # start from highest level of skip list move the current
        # reference forward while key is greater than key of node next
        # to current Otherwise inserted current in update and move one
        # level down and continue search
        for i in range(self.level, -1, -1):
            while (current.forward[i] and current.forward[i].data < search_key):
                current = current.forward[i]
            update[i] = current

        # reached level 0 and advance reference to right, which is prssibly our
        # desired node
        current = current.forward[0]

        # If current node is traget node
        if current is not None and current.data == search_key:
            # start from lowest level and rearrange references just like we
            # do in singly linked list to remove target node
            for i in range(self.level+1):
                # if at level i, next node is not target node, break the loop,
                # no need to move further level
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            # Remove levels having no elements
            while(self.level > 0 and self.header.forward[self.level] is None):
                self.level -= 1
            print("Successfully deleted {}".format(search_key))

    # Display skip list level wise
    def displayList(self):
        print("\n*****Skip List*****")
        head = self.header
        for lvl in range(self.level+1):
            print("Level {}: ".format(lvl), end=" ")
            node = head.forward[lvl]
            while(node is not None):
                print(node.data, end=" ")
                node = node.forward[lvl]
            print("")


if __name__ == "__main__":
    skipList = SkipList(3, 0.5)
    skipList.insertElement(3)
    skipList.insertElement(6)
    skipList.insertElement(7)
    skipList.insertElement(9)
    skipList.insertElement(12)
    skipList.insertElement(19)
    skipList.insertElement(17)
    skipList.insertElement(26)
    skipList.insertElement(21)
    skipList.insertElement(25)
    skipList.insertElement(2)
    skipList.insertElement(8)
    skipList.insertElement(30)
    skipList.displayList()

    # Search for node 19
    skipList.searchElement(19)

    # Delete node 19
    skipList.deleteElement(19)
    skipList.displayList()
