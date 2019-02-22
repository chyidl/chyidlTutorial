#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# red_black_tree_implement.py
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
# Created by Chyi Yaqing on 02/22/19 16:44.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Red-Black Tree: is a self-balancing Binary Search Tree (BST) where every node
follows following rules.
    1) Every node has a color either red or black
    2) Root of tree is a always black
    3) There are no two adjacent red nodes (A red node cannot have a red parent
    or red child)
    4) Every path from a node (including root) to any of its descendant NULL
    node has the same number of black nodes.

Why Red-Black Trees?
    Most of the BST operations (e.g., search, max, min, insert, delete.. etc)
    take O(h) time where h is the height of the BST.The cost of these operation
    may become O(n) for a skewed Binary tree. The height of a Red-Black tree is
    always O(Logn) where n is the number of nodes in the tree

Comparison with AVL Tree
    The AVL trees are more balanced compared to Red-Black Trees, but they may
    cause more rotations during insertion and deletion. So if your application
    involves many frequent insertions and deletions, then Red Black trees shoul
    be preferred. And if the insertions and deletions are less frequent and
    search is more frequent operation, then AVL tree should be preferred over
    Red-Black Tree.

How does a Red-Black Tree ensure balance?
    Black Height of a Red-Black Tree : a node of heigh h has black-height>=h/2
    Every Red Black Tree with n nodes has height <= 2Log2(n+1)

Red-Black Tree: we use two tools to do balancing
    1) Recoloring
    2) Rotation

The algorithms has mainly two cases depending upon the color of uncle. If uncle
is red, we do recoloring. If uncle is black, we do rotations and/or recoloring.

Color of a NULL node is considered as Black.
"""


# The possible Node colors
BLACK = 'BLACK'
RED = 'RED'
NIL = 'NIL'


class Node:
    def __init__(self, value, color, parent, left=None, right=None):
        self.value = value
        self.color = color
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self):
        return '{color} {val} Node'.format(color=self.color, val=self.vale)

    def __iter__(self):
        if self.left.color != NIL:
            yield from self.left.__iter__()
        yield self.value
        if self.right.color != NIL:
            yield from self.right.__iter__()

    def __eq__(self, other):
        if self.color == NIL and self.color == other.color:
            return True

        if self.parent is None or other.parent is None:
            parens_are_same = self.parent is None and other.parent is None
        else:
            parents_are_same = self.parent.value == other.parent.value and self.parent.color == other.parent.color
