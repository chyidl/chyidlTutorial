#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# recursion_implement.py
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
# Created by Chyi Yaqing on 02/18/19 13:41.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Recursion : The process in which a function calls itself directly or indirectly
is called recursion and the corresponding function is called as recursive
function. Using recursive algorithm, certain problems can be solved quite

The idea is represent a problem in terms of one of more smaller problems, and
add one or more base conditions that stop recursion.

What is the difference between direct and indirect recursion?

What is tail recursion?
    The tail recursive can be optimized by compiler.
"""


# A NON-tail-recursive function. The function is not tail recursive because the
# valye returned by fact(n-1) is used in fact(n) and call to fact(n-1) is not
# the last thing done by fact(n)
def fact(n):
    if n is 0:
        return 1
    return n * fact(n-1)


# Driver program to test above function
print(fact(5))


# The above function can be written as a tail recursive function.
def factTR(n, a):
    if n is 0:
        return a

    return factTR(n-1, n*a)


# A wrapper over factTR
def fact(n):
    return factTR(n, 1)


# Driver program to test above function
print(fact(5))


# A tail recursive function to calculate n th fibnacci number
def fib(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    return fib(n-1, b, a+b)


# Driver Code
n = 9
print("fib({}) = {}".format(n, fib(n)))
