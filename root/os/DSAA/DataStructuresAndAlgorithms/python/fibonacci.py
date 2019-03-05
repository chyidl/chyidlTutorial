#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# fibonacci.py
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
# Created by Chyi Yaqing on 03/05/19 11:23.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT
"""Fibonacci"""


class Fibonacci:
    '''
    >>> f = Fibonacci()
    >>> for n in f:print(n)
    1
    1
    2
    3
    5
    8
    13
    21
    34
    55
    89
    >>> print(f[10])
    55
    '''
    def __init__(self):
        # 初始化两个计数器a, b
        self._a, self._b = 0, 1

    def __iter__(self):
        return self  # 实例本身就是迭代对象

    def __next__(self):
        self._a, self._b = self._b, self._a+self._b
        if self._a > 100:  # 推出循环条件
            raise StopIteration()
        return self._a  # 返回下一个值

    def __str__(self):
        return '斐波那契数列'
    __repr__ = __str__

    def __getattr__(self, attr):
        '动态返回一个属性'
        if attr == 'author':
            return 'Chyi Yaqing'
        raise AttributeError("Fibonacci object has no attribute %s" % attr)

    def __getitem__(self, n):
        '下标访问数列的任意项'
        if isinstance(n, int):  # n 是索引
            self._a, self._b = 0, 1
            for x in range(n):
                self._a, self._b = self._b, self._a + self._b
            return self._a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            self._a, self._b = 0, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(self._a)
                self._a, self._b = self._b, self._a + self._b
            return L


if __name__ == '__main__':
    f = Fibonacci()
    for n in f:
        print(n)
    print(f[10])
    print(f[:50])
    print(f.author)

    import doctest
    doctest.testmod()
