#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# 2.1.Splitting_Strings_on_Any_of_Multiple_Delimiters.py
# ch02
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
# Created by Chyi Yaqing on 02/01/19 16:52.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT
"""
Problem:
    split a string into fileds but the delimiters consistent throughout the string.
Solution:
    use the re.split() method
"""
import re


line = 'asdf fjdk; afed, fjek,asdf,     foo'
# re.split() function can specify multiple patterns for the separator
print(re.split(r'[;,\s]\s*', line))
