#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# binary_search_tree_linked_list_implement.py
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
# Created by Chyi Yaqing on 02/22/19 11:38.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Trees: Unlike Arrays, Linked Lists, Stack and queues, which are linear data
structures, trees are hierarchical data structures.

Binary Tree Data Structure:
    A tree whose elements have at most 2 children is called a binary tree.

A Binary Tree node contains following parts:
    1) Data
    2) Poniter to left child
    3) Pointer to right child

The Maximum number of nodes at level 'l' of a binary tree is 2^(l-1)
The Maximum number of nodes in a binary tree of height 'h' is 2^(h+1) - 1
(height of a leaf is considered as 0)
In a Binary Tree with N nodes, minimum possible height or minimum number of
level is Log2(N+1)

Types of Binary Tree:

Full Binary Tree: A Binary Tree is full if every node has 0 or 2 children.
    In a Full Binary, number of leaf nodes is number of internal nodes plus 1
    (L = I + 1) Where L = Number of leaf nodes, I = Number of internal nodes

Complete Binary Tree: A Binary Tree is complete Binary Tree if all levels are
completely filled except possibly the last level and the last level has all
keys as left as possible

Perfect Binary Tree: A Binary tree is Perfect Binary Tree in which all internal
nodes have two children and all leaves are at the same level.

Balanced Binary Tree: A binary tree is balanced if the height of the tree is
O(Log n) where n is the number of nodes.

A degenerate tree: A Tree where every internal node has one child.

Binary Search Tree: is a node-based binary tree data structure which has the
following properties:
    1) The left subtree of a node contains only nodes with keys lesser than the
    node's key
    2) The right subtree of a node contains only nodes with keys greater than
    the node's key
    3) The left and right subtree each must also be a binary search tree. There
    must be no duplicate nodes.

Binary Search Tree Delete:
    1) Node to be deleted is leaf : Simply remove from the tree
    2) Node to be deleted has only one child: Copy the child to the node and
    delete the child
    3) Node to be deleted has two children: Find inorder successor of the node.
    Copy contents of the inorder successor to the node and delete the inorder
    successor.
[inorder successor] is needed only when right child is not empty.

Write a Program to FInd the Maximum Depth or Height of a Tree:
    Recursively calculate height of left and right subtree of a node and assign
    height to the node as max of the heights of two children plus 1.
Below pseudo code:
    maxDepth()
    1. If tree is empty then return 0
    2. Else
        a) Get the max depth of left subtree recursively
            call maxDepth(tree->left-subtree)
        b) Get the max depth of right subtree recursively
            call maxDepth(tree->right-subtree)
        c) Get the max of max depths of left and right subtrees and
        add 1 to it for the current node.
            max_depth = max(max dept of left subtree,
            maxdepth of right subtree + 1)
        d) Return max_depth

"""


# A Python class that represents an individual node in a Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# Binary Search Tree is call Binary Order Tree
class BinarySearchTree:

    def __init__(self):
        self.root = None

    # A utility function to search a given key in BST
    def search(self, key):
        # Base Cases: root is null or key is present at root
        if self.root is None or self.root.val == key:
            return self.root

        # Key is greater than root's key
        if self.root.val < key:
            return self.search(self.root.right, key)

        # Key is smaller than root's key
        return self.search(self.root.left, key)

    # A utility function to insert a new node with the given key
    def insert(self, root, node):
        if self.root is None:
            self.root = node
        else:
            if root.val < node.val:
                if root.right is None:
                    root.right = node
                else:
                    self.insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    self.insert(root.left, node)

    # Given a non-empty binary search tree, return the node with minum key
    # value found in that tree. Note that the entire tree does not need to be
    # searched.
    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while (current.left is not None):
            current = current.left

        return current

    # Given a binary search tree and a key, this function delete the key and
    # returns the new root
    def deleteNode(self, root, key):
        # Base Case
        if root is None:
            return root

        # If the key to be deleted is smaller than the root's key then it lies
        # in left subtree
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        # If the key to be delete is greater than the root's key then it lies
        # in right subtree
        elif (key > root.val):
            root.right = self.deleteNode(root.right, key)
            return root
        # We reach here when root is the node to be deleted
        if root.left is None:
            temp = root.right
            del root
            return temp

        elif root.right is None:
            temp = root.left
            del root
            return temp
        else:
            succParent = root.right
            # Find successor
            succ = root.right
            while succ.left is not None:
                succParent = succ
                succ = succ.left

            # Delete successor. Since successor is always left child of its
            # parent we can safely make successor's right right child as left
            # of its parent
            succParent.left = succ.right

            # Copy Successor Data to root
            root.val = succ.val

            # Delete Successor and return root
            del succ
            return root

    # Compute the "maxDepth" of a tree -- the number of nodes along the
    # longest path from the root node down to the farthest leaf node
    def maxDepth(self, node):
        if node is None:
            return 0
        else:
            # Compute the depth of each subtree
            lDepth = self.maxDepth(node.left)
            rDepth = self.maxDepth(node.right)

            # Use the larger one
            if (lDepth > rDepth):
                return lDepth+1
            else:
                return rDepth+1

    # A utility function to do inorder tree traversal
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val, end=" ")
            self.inorder(node.right)

    # A utility function to do preorder tree traversal
    def preorder(self, node):
        if node:
            print(node.val, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # A utility function to do postorder tree traversal
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val, end=" ")


# Driver program to test the above functions
# Let us create the following BST
#       50
#      /  \
#    30    70
#   /  \  /  \
# 20   4060   80
if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(bst.root, Node(50))
    bst.insert(bst.root, Node(30))
    bst.insert(bst.root, Node(20))
    bst.insert(bst.root, Node(40))
    bst.insert(bst.root, Node(70))
    bst.insert(bst.root, Node(60))
    bst.insert(bst.root, Node(80))

    # Inorder traversal of the given tree
    bst.inorder(bst.root)
    print("\nHeight of tree is {}".format(bst.maxDepth(bst.root)))

    print("\nDelete 20")
    root = bst.deleteNode(bst.root, 20)
    print("Inorder traversal of the modified tree")
    bst.inorder(root)

    print("\nDelete 30")
    root = bst.deleteNode(bst.root, 30)
    print("Inorder traversal of the modeifed tree")
    bst.inorder(root)

    print("\nDelete 50")
    root = bst.deleteNode(bst.root, 50)
    print("Inorder traversal of the modified tree")
    bst.inorder(root)
