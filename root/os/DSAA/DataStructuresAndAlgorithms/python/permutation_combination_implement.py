#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# permutation_combination_implement.py
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
# Created by Chyi Yaqing on 02/23/19 10:36.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Permutation and Combination in Python

Python provide direct methods to find permutations and combinations of a
sequence. These methods are present in itertools package.
"""
# itertools package to implement permutations method in Python.
# This method takes a list as an input and return an object list of tuples
# that contain all permutation in a list form.
from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

# Get all permutations of [1,2,3,4,5,6,7,8,9,0]
# It generates n! permutations if length of input sequence is n.
perm = permutations([1, 2, 3, 4, 5])

# Print the obtained permutations
for i in list(perm):
    print(i)


# If want to get permutations of length L then implement it in this way

# Get all permutations of length 2 and length 2
# It generate nCr * r! permutations if length of input sequence is n and input
# parameter is r.
perm = permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 5)

# Print the obtained permutations
for i in list(perm):
    print(i)


# Combination: This method takes a list and a input r as a input and return a
# object list of tuples which contain all possible combination of length r in
# a list form

# Get all combinations of [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] and length 5
comb = combinations([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 5)

# Print the obtained combinations
for i in list(comb):
    print(i)

# If want to make combination of same element to same element then we use
# combinations_with_replacement.
# Get all combinations of [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] and length 5
comb = combinations_with_replacement([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 5)

# Print the obtained combinations
for i in list(comb):
    print(i)
