#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# bplus_tree_implement.py
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
# Created by Chyi Yaqing on 03/04/19 11:35.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT


"""
B+ 树非叶子节点的定义

假设 keywords = [3, 5, 8, 10]
4 个键值将数据分为5个区间: (INF, 3), [3, 5), [5, 8), [8, 10), [10, INF)
5 个区间分别对应: children[0]..children[4]

m值使实现计算得到的，计算的依据是让所有信息的大小正好等于页的大小:
    PAGE_SIZE = (m-1)*4[keywordss 大小]+m*8[children 大小]
"""
class BPlusTreeNode:
    def __init__(self, n=2):
        self._n = n  # 几叉数
        self.children = [None]*self._n  # 保存字节点指针
