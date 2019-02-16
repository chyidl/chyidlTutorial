#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# josephus_problem.py
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
# Created by Chyi Yaqing on 02/16/19 09:28.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
In computer science and mathematics, the Josephus Probelm is a theoretical
problem.

There are n people standing in a circle waiting to be executed. The counting
out be-gins at some point in the circle and processeds around the circle in a
fixed direction. In each step, a certain number of people are skipped and the
next person is executed.The elimination proceeds around the circle, until only
the last person remains, who is given freedom. Given the total number of
persons n and a number k which indicates that k-1 persons are skipped and kth
person is killed in circle.  The task is to choose the place in the initial
circle so that you are the last one remaining and so survive.

1) Following is simple recursive implementation of the Josephus problem.
"""


# recursive implementation of the Josephus problem.
def josephus(n, k):
    """
    josephus(n, k) = (josephus(n-1, k) + k) % n
    josephus(1, k) = 0

    After the first person (kth from beginning) is killed, n-1 persons are left
    So we call josephus(n-1, k) to get the position with n-1 persons. But the
    position returned by josephus(n-1, k) will consider the position starting
    from k%n .
    """
    if (n == 1):
        return 0
    else:
        # The position returned by josephus(n-1, k) is adjusted because the
        # recursive call josephus(n-1, k) considers the original position
        # k%n + 1 as position 1
        return (josephus(n - 1, k) + k) % n


# Driver Program to test above function
n = 14
k = 2

print("The chosen place is at index: {}, start from 0".format(josephus(n, k)))
