#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# string_kmp_pattern_search_implement.py
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


# Python program for KMP Algorithm
def KMPSearch(pat, txt):
    M, N = len(pat), len(txt)
    # create lps[] that will hold the longest prefix suffix values for pattern
    lps = [0]*M
    j = 0  # index for pat[]

    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, M, lps)

    i = 0  # index for txt[]
    while i < N:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == M:
            print("Found pattern at index {}".format(i-j))
            j = lps[j-1]
        # mismatch after j matches
        elif i < N and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters, they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

def computeLPSArray(pat, M, lps):
    len = 0  # length of the previous longest prefix suffix
    lps[0]  # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to M-1
    while i < M:
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            # This is tricky. Consider the example. AAACAAAA and i = 7.
            # The idea is similar to search step.
            if len != 0:
                len =
