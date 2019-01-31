#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 1.14.Sorting_Objects_Without_Native_Comparison_Support.py
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
# Created by Chyi Yaqing on 01/27/19 16:07.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT
"""
Problem:
    sort objects of the same class, but they don't natively support
    comparison operation
Solution:
    The built-in sorted() function takes a key argument that can be passed
"""
from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


users = [User(23), User(3), User(99)]
print(sorted(users, key=lambda u: u.user_id))

# Instead of using lambda, an alternative approach is
# to use operator.attrgetter()
print(sorted(users, key=attrgetter('user_id')))
