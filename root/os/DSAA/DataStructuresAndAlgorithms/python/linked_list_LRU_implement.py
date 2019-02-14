#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# linked_list_LRU_implement.py
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
# Created by Chyi Yaqing on 02/14/19 17:59.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Two data structures to implement an LRU Cache.
1. Queue which is implemented using a doubly linked list. The maximum size
of the queue will be equal to the total number of frames available
(cache size). The most recently used pages will be near front end and least
recently pages will be near rear end.

2. A Hash with page number as key and address of the corresponding queue node
as value.
"""

