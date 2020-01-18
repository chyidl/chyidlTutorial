#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# binary_search_tree.py
# Downloads
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
# Created by Chyi Yaqing on 12/25/19 08:52.
# Copyright © 2019. Chyi Yaqing. All rights reserved.
#
# Distributed under terms of the MIT


class Node:
    """节点"""
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class BinarySearchTree:
    """二叉搜索树"""
    def __init__(self):
        self.root = None

    def find(self, val):
        p = self.root
        while p is not None:
            if val < p.val:
                p = p.left
            elif val > p.val:
                p = p.right
            else:
                return p
        return None

    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
            return
        p = self.root
        while p.val is not None:
            if p.val < val:
                if p.right is None:
                    p.right = Node(val)
                    return
                p = p.right
            else:
                if p.left is None:
                    p.left = Node(val)
                    return
                p = p.left

    def delete(self, val):
        """
        根据删除节点的字节点的个数的不同需要分三种情况处理
            1. 删除节点没有子节点，将父节点指向删除节点的指针置为null
            2. 删除节点只有一个字节点(只有左，或者右)，更新父节点指向要删除节点的指针指向要删除节点的子节点
            3. 删除节点有两个字节点，需要找到节点右子树中的最小节点，替换到要删除的节点上，在删除这个最小节点
        :param val:
        :return:
        """
        p = self.root   # p指向要删除的节点, 初始化指向根节点
        pp = None       # pp记录p的父节点
        while (p is not None) and (p.val is not val):
            pp = p
            if p.val < val:
                p = p.right
            else:
                p = p.left
        # 没有找到要删除的节点
        if p is None:
            return

        # 要删除的节点有两个子节点
        if p.left is not None and p.right is not None:
            # 查找右子树中最小的节点
            minP = p.right
            minPP = p       # minPP 表示 minP 的父节点
            while minP.left is not None:
                minPP = minP
                minP = minP.left
            p.val = minP.val    # 将minP的数据替换到p
            p = minP            # 下面变成删除minP
            pp = minPP

        # 删除节点是叶子节点或者仅有一个子节点
        child = None
        if p.left is not None:
            child = p.left
        elif p.right is not None:
            child = p.right
        else:
            child = None

        if pp is None:        # 删除的是根节点
            self.root = child
        elif pp.left == p:
            pp.left = child
        else:
            pp.right = child

    def findMin(self):
        if self.root is None:
            return None
        p = self.root
        while p.left is not Node:
            p = p.left
        return p

    def findMax(self):
        if self.root is None:
            return None
        p = self.root
        while p.right is not Node:
            p  = p.right
        return p

    def preOrder(self, node):
        """前序遍历二叉树"""
        if node:
            print(node.val, end=" -> ")
            self.preOrder(node.left)
            self.preOrder(node.right)

    def inOrder(self, node):
        """中序遍历二叉树"""
        if node:
            self.inOrder(node.left)
            print(node.val, end=" -> ")
            self.inOrder(node.right)

    def postOrder(self, node):
        """后序遍历二叉树"""
        if node:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.val, end=" -> ")


if __name__ == '__main__':
    raw_list = [10,9,8,7,1,2,3,4,5,6]
    print(raw_list)
    btree = BinarySearchTree()
    for val in raw_list:
        btree.insert(val)
    btree.inOrder(btree.root)
    print()
    btree.preOrder(btree.root)
    print()
    btree.postOrder(btree.root)