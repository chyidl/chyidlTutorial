#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# prime_Sieve_of_Eratosthenes_implement.py
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
# Created by Chyi Yaqing on 03/04/19 17:50.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
埃拉托色尼筛选法(the Sieve of Eratosthenes)

埃氏筛选步骤:
    1) 先把1删除 （现代数学界1既不是质数也不是合数）
    2）读取队列中当前最小的数2，然后把2的倍数删除
    3）读取队列中当前最小的数3，然后把3的倍数删除
    4）读取队列中当前最小的数5，然后把5的倍数删除
    5）读取队列中当前最小的数7，然后把7的倍数删除
    6）如上所述直到需求的范围内所有的数均删除或读取
"""


# 生成器生成从3开始的无限奇数序列
def _int_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):  # 定义筛选函数
    return lambda x: x % n > 0


def primes():
    yield 2  # 先返回一个2
    it = _int_iter()  # 初始化序列
    while True:
        n = next(it)  # 返沪序列的第一个数
        yield n
        it = filter(_not_divisible(n), it)  # 构造新序列


for n in primes():  # 构造循环条件，使之可以输出任何范围的素数序列
    if n < 1000:
        print(n)
    else:
        break
