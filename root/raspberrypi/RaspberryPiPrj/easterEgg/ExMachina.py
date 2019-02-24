#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:encoding=utf-8
#
# ExMachina.py
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
# Created by Chyi Yaqing on 02/23/19 19:49.
# Copyright © 2019. Chyi Yaqing. All rights reserved.
#
# Distributed under terms of the MIT
# BlueBook code descryption
import sys


def sieve(n):
    x = [1] * n
    x[1] = 0
    for i in range(2, n//2):
        j = 2 * i
        while j < n:
            x[j] = 0
            j += i
    return x


def prime(n, x):
    i, j = 1, 1
    while j <= n:
        if x[i] == 1:
            j += 1
        i += 1
    return i - 1


x = sieve(10000)
code = [1206, 301, 384, 5]
key = [1, 1, 2, 2]


sys.stdout.write("".join(chr(i) for i in [73, 83, 66, 78, 32, 61, 32]))
for i in range(0, 4):
    sys.stdout.write(str(prime(code[i], x)-key[i]))
print()

# Result displays "ISBN = 9780199226559"
# This is the ISBM code of the book:
# Embodiment and the inner life : Cognition and Consciousness in the Space of
# Possible Minds
