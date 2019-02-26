#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# string_rabin_karp_pattern_search_implement.py
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
# Created by Chyi Yaqing on 02/26/19 17:08.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Rabin-Karp Algorithm for Pattern Searching
    Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function
    search(char pat[], char txt[]) that prints all occurrences of pat[] in
    txt[]. You may assume that n > m

Rabin Karp algorithm matches the hash value of the pattern with the hash value
of current substring of text, and if the hash values match then only it starts
matching individual characters. So Rabin Karp algorithm needs to calculate hash
values for following strings.

"""
# Following program is the python implementation of Rabin Karp Algorithm given
# d is the number of characters in the input alphabet
d = 256

# pat   -> pattern
# txt   -> text
# q     -> A prime number


def rabin_karp_search(pat, txt, q):
    M, N = len(pat), len(txt)
    p = 0  # hash value for pattern
    t = 0  # hash value for txt

