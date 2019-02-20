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
Skip List: create multiple layers so that we can skip some nodes.

Insert an Elements in Skip List
    start from highest level in the list and compare key of next node of the
    current node with the key to be inserted.
    1) Key of next node is less than key to be inserted then we keep on moving
    forward on the same level
    2) key of next node is greater than the key to be inserted then we store
    the pointer to current node i at update[i] and move one level down and
    continue our search
    At the level 0, we will definitely find a position to insert given key.

Following is the psuedo code for the insertion algorithm
    Insert(list, searchKey)
    local update[0...MaxLevel+1]
    x := list->header
    for i := list-level downto 0 do
"""
import random


# Python3 code for inserting element in skip list
class Node:
    # Constructor to create a new node
    def __init__(self, key, level):
        self.key = key

        # list to hold references to node of different level
        self.forward = [None]*(level+1)


class SkipList:
    # Class for Skip list
    def __init__(self, max_lvl, P):
        # Maximum level for this skip list
        self.MAXLVL = max_lvl

        # P is the fraction of the nodes with level i references also
        # having level i+1 references
        self.P = P

        # create header node and initialize key to -1
        self.header = self.createNode(self.MAXLVL, -1)

        # current level of skip list
        self.level = 0

    def createNode(self, lvl, key):
        return Node(key, lvl)

    # create random level for node
    def randomLevel(self):
        lvl = 0
        while random.random() < self.P
            and lvl < self.MAXLVL: lvl += 1
        return lvl

    # insert given key in skip list


