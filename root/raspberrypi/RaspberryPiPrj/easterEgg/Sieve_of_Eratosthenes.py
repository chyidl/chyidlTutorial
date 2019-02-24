#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Sieve_of_Eratosthenes.py
# easterEgg
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
# Created by Chyi Yaqing on 02/23/19 17:24.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
A prime number (or a prime) is a nature number greater than 1 that cannot be
formed by multiplying two smaller natural numbers.

埃拉托斯特尼筛法 (Sieve of Eratosthenes),是希腊数学家提出的一种简单鉴定素数的算法

Given a number n, print all primes smaller than or equal to n. It is also given
that n is  a small number.

Algorithm:
    1) Create a list of consecutive integers from 2 to n: (2, 3, 4,...,n)
    2) Initially, let p equal 2, the first prime number
    3) Starting from p^2, count up in crements of p and mark each of these
        numbers greater than or equal to p^2 itself in the list, These numbers
        will be
"""
import sys


# Python program to print all primes smaller than or equal to n using
# Sieve of Eratosthenes
def sieveOfEratosthenes(n):
    # Create a boolen array "prime[0..n]" and initialize all entries it as true
    # A value in prime[i] will finally be false if i is Not a prime, else true
    prime = [True for i in range(n+1)]
    p = 2  # the first prime number
    while (p**2 <= n):
        # If prime[p] is not changed, then it is a prime
        if (prime[p] is True):
            # Update all multiples of p
            for i in range(p**2, n+1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, n+1):
        if prime[p]:
            print(p, end=",")


if __name__ == '__main__':
    n = int(sys.argv[1])
    print("Following are the prime numbers smaller than or equal to ", n)
    sieveOfEratosthenes(n)
