#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 1.6.Mapping_Keys_to_Multiple_Values_in_a_Dictionary.py
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
# Created by Chyi Yaqing on 01/25/19 14:06.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT
"""
Problem:
    make a dictionary that maps keys to more than one value

Solution:
    need to store the multiple values in another container such
    as a list or set.
"""
from collections import defaultdict


d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
d['b'].append(4)
print('defaultdict(list) : {}'.format(d))

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(1)
d['b'].add(1)
print('defaultdict(set) : {}'.format(d))
