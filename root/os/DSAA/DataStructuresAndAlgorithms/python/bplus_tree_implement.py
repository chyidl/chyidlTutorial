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
B+树：MySQL数据库索引
    数据库索引的作用是加速查找：查找的方式包括【值查找、区间查找】
    select * from user where id=123456; 值查找
    select * from user where  id between 100 and 200;
性能方面：考察时间和空间两方面，执行效率和存储空间;希望通过索引，查询数据的效率尽可能的高，存储空间方面，希望索引不要消耗太多的内存空间.

    散列表:查询性能是O(1),但是散列表不支持区间查找
    平衡二叉查找树:查询性能是O(logn),而且对树进行中序遍历，可以得到从小到大的有序数据序列。不支持按照区间快速查找数据。
    跳表：是在链表上加上多层索引构成，支持快速的插入、查找、删除数据，数据复杂度是O(logn),并且跳表支持按照区间快速查找数据.只需要定位区间起点值对应在链表中的节点，然后从这个结点开始，顺序遍历链表，知道区间终点为止。

B+树：二叉查找树演化过来的，而非跳表。为了让二叉查找树支持按照区间查找数据，树中的节点并不存储数据本身，而是作为索引，每个叶子节点串在一条链表上，链表中的数据是从小到大有序,因此支持区间查找的功能。如果把树存储在硬盘中，那么每次节点的读取或者访问都对应一次磁盘IO操作，数的高度就等于每次查询数据时磁盘IO操作的次数.尽量降低树的高度。

通常内存的访问速度是纳秒级别，磁盘访问速度是毫秒级别.

操作系统按照页的4KB大小读取，一次读取一页的数据，数据的写入过程会涉及索引的更新，索引导致写入变慢的主要原因.
"""
