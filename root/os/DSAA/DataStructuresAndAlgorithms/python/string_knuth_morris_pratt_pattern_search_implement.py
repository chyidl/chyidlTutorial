#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# string_knuth_morris_pratt_pattern_search_implement.py
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
# Created by Chyi Yaqing on 02/26/19 18:07.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
KMP Algorithm for Pattern Searching

KMP (knuth Morris Pratt) Pattern Searching, The basic idea behind KMP's
algorithm is: whenever we detect a mismatch (after some matches), we already
know some of the characters in the text of the next window. We take advantage
of this information to avoid matching the characters that we know will anyway
match.
"""
