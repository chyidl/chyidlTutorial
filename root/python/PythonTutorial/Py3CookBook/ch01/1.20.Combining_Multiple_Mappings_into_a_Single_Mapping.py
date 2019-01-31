#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 1.20.Combining_Multiple_Mappings_into_a_Single_Mapping.py
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
# Created by Chyi Yaqing on 01/31/19 15:36.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT
"""
Problem:
    multiple dictionaries combine into a single mapping
Solution:
    Suppose you have two dictionaries
"""
from collections import ChainMap


a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

# lookups  both dictionaries
# ChainMap simply keeps a list of the underlying mappings and redefines common
c = ChainMap(a, b)
print(c['x'])  # Outputs 1 (from a)
print(c['y'])  # Outputs 2 (from b)
# If there are duplicate keys, the valyes from the first mapping get used
print(c['z'])  # Outputs 3 (from a)

# len(c)
print(len(c))
print('list(c.keys()) : {}, list(c.values()) : {}'.format(
    list(c.keys()), list(c.values())))

# Operations that mutate the mapping always affect the first mapping listed.
c['z'] = 10
c['w'] = 40
del c['x']
print(a)
# A ChainMap uses the original dictionaries, so it doesn't have this behavior
