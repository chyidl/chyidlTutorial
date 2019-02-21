#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:encoding=utf-8
#
# hash_implement.py
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
# Created by Chyi Yaqing on 02/21/19 22:51.
# Copyright © 2019. Chyi Yaqing. All rights reserved.
#
# Distributed under terms of the MIT
"""
Hashing is an improvement over Direct Access Table. Use hash function
that convert any other key to a smaller number and uses the small numbers
as index in a table called hash table.

A good hash function should have following properties:
    1) Efficiently computable
    2) Should uniformly distribute the keys

Collision Handling:
    1) Separate Chaining: The idea is to make each cell of hash table point to
    a linked list of records that have smae hash function value.
        Advantages:
            a) Simple to implement
            b) Hash table never fills up
            c) Less sensitive to the hash function or load factors
            d) It is mostly used when it is unknown how many and how frequently
            keys may be inserted or deleted

        Disadvantages:
            a) Cache performance of chaining is not good as keys are stored use
            linked list.  Open addressing provides better cache performance as
            everything is stored in same table
            b) Wastage of Space (Some Parts of hash table are never used)
            c) If the chain becomes long, then search time can be become O(n)
            in worst case.
            d) Uses extra space for links

    2) Open Addressing: In open addressing, all elements are stored in the hash
    table itself.
        a) Linear Probing: In linear probing, linearly probe for next slot.
        b) Quadratic Probing: looking for i^2th slot in i'th iteration
        c) Double Hashing: use another hash function hash2(x) and look for
        i*hash2(x) slot in i'th rotation

Hashing in Distributed Systems:

"""
