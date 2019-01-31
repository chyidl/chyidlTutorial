#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 1.13.Sorting_a_List_of_Dictionaries_by_a_Common_Key.py
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
# Created by Chyi Yaqing on 01/27/19 15:50.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT
"""
Problem:
    sort the entries according to one or more of the dictionary values
Solution:
    Sorting this type of structure is easy using the operator module's
    itemgetter function.
"""
# operator -- Standard operators as functions
# itemgetter -- Return a callable object
from operator import itemgetter


rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))


print('rows_by_fname: {}'.format(rows_by_fname))
print('rows_by_uid: {}'.format(rows_by_uid))
print('rows_by_lfname: {}'.format(rows_by_lfname))
