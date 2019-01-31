#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 1.9.Finding_Commonalities_in_Two_Dictionaries.py
# ch01
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
# Created by Chyi Yaqing on 01/25/19 15:05.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT
"""
Problem:
    find out what Two dictionaties might have in common
"""
a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# Find keys in common
print("a.keys() & b.keys() : ", a.keys() & b.keys())

# Find keys in a that are not in b
print("a.keys() - b.keys() : ", a.keys() - b.keys())

# Find (key, value) pairs in common
print("a.items() & b.items() : ", a.items() & b.items())
