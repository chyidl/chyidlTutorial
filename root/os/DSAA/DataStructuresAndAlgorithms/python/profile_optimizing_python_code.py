#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:encoding=utf-8
#
# profile_optimizing_python_code.py
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
# Created by Chyi Yaqing on 02/16/19 22:12.
# Copyright © 2019. Chyi Yaqing. All rights reserved.
#
# Distributed under terms of the MIT
"""
Profiling and optimizing Python code
When to optimize?
    Do you need optimization?
        if speed is not a problem, then there is no reason to optimize
    If yes: Which parts of your code should be optimized?
        Use a profiler, such as cProfile
        Usually, almost all execution time occurs within a small part of code
        Optimize that code, and leae the rest alone
    If you need even better performance
        Redesign the code completely
        But this takes effort!

cProfile and profile provide deterministic profiling of Python programs.
A profile is a set of statistics that describes how often and for how long
various parts of the program executed. These statistics can be formatted into
reports via the pstats module.

1. cProfile is recommended for most user;
2. profile, a pure Python module whose interface is imitated by cProfile.
"""
# Instant User's Manual
import cProfile
import re


cProfile.run('re.compile("foo|bar")')
