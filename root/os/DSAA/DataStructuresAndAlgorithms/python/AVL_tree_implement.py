#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# AVL_tree_implement.py
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
# Created by Chyi Yaqing on 02/22/19 17:01.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
AVL Tree: is a self-balancing Binary Search Tree (BST) where the difference
between heights of left and right subtrees cannot be more than one for allnodes

Why AVL Trees?
Most of BST operations (e.g., search, max, min, insert, delete..etc) take O(h)
time where h is the height of the BST. The cost of these operations may become
O(n) for a skewed Binary tree.If we make sure that height of the tree remains
O(logn) after every insertion and deletion, then we can guarantee an upper
bound of O(Logn) for all these operations.

Insertion: To make sure that the given tree remains AVL after every insertion,
we must augment the standard BST insert operation to perform some re-balancing.
Left Rotation , Right Rotation
T1, T2 and T3 are subtrees of the tree
rooted with y (on the left side) or x (on
the right side)
     y                               x
    / \     Right Rotation          /  \
   x   T3   - - - - - - - >        T1   y
  / \       < - - - - - - -            / \
 T1  T2     Left Rotation            T2  T3
Keys in both of the above trees follow the
following order
 keys(T1) < key(x) < keys(T2) < key(y) < keys(T3)
So BST property is not violated anywhere.

Steps to follow for insertion:
    Let the newly inserted node be w
    1) Perform standard BST insert for w.
    2) Starting from w, travel up and find the first unbalanced node.
"""


# Python code to insert a node in AVL tree
# Generic tree node class
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


# AVL tree class which supports the insert operation
class AVL_Tree:
    # Recursive function to insert key in subtree rooted with node and returns
    # new root of subtree
    def insert(self, root, key):
        # Step 1 - Perform normal BST
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Step 2 - Update the height of the ancestor node
        root.height = 1 + max(
                self.getHeight(root.left), self.getHeight(root.right))

        # STep 3 - Get the balance  factor
        balance = self.getBalance(root)

        # Step 4 - If the node is unbalanced, the try out the 4 cases
        # T1, T2, T3 and T4 are subtrees.
        # Case 1 - Left Left
        #          z                                      y
        #         / \                                   /   \
        #        y   T4      Right Rotate (z)          x      z
        #       / \          - - - - - - - ->        /  \    /  \
        #      x   T3                               T1  T2  T3  T4
        #     / \
        #   T1   T2
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

        # Case 2 - Right Right Case
        #   z                                y
        #  /  \                            /   \
        # T1   y     Left Rotate(z)       z      x
        #     /  \   - - - - - - - ->    / \    / \
        #    T2   x                     T1  T2 T3  T4
        #        / \
        #      T3  T4
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

        # Case 3 - Left Right
        #      z                             z                         x
        #     / \                          /   \                     /   \
        #    y   T4  Left Rotate (y)      x    T4  Right Rotate(z)  y     z
        #   / \      - - - - - - - ->    /  \      - - - - - - ->  / \    / \
        # T1   x                        y    T3                   T1  T2 T3  T4
        #     / \                      / \
        #   T2   T3                  T1   T2
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Case 4 - Right Left
        #    z                            z                            x
        #   / \                          / \                          /  \
        # T1   y   Right Rotate (y)    T1   x      Left Rotate(z)   z      y
        #     / \  - - - - - - - - ->     /  \   - - - - - - - ->  / \    / \
        #    x   T4                      T2   y                  T1  T2  T3  T4
        #   / \                              /  \
        # T2   T3                           T3   T4
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # Return the new root
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        # Return the new root
        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        print("{0} ".format(root.val), end="")
        self.inOrder(root.right)


# Driver program to test above function
if __name__ == '__main__':
    myTree = AVL_Tree()
    root = None
    root = myTree.insert(root, 10)
    root = myTree.insert(root, 20)
    root = myTree.insert(root, 30)
    root = myTree.insert(root, 40)
    root = myTree.insert(root, 50)
    root = myTree.insert(root, 25)

    """The constructed AVL Tree would be
            30
           /  \
         20   40
        /  \     \
       10  25    50"""

    # Preorder Traversal
    print("Preorder traversal of the constructed AVL tree is")
    myTree.inOrder(root)
    print()
