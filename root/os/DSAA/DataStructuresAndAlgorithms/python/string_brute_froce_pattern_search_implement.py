#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# string_brute_froce_pattern_search_implement.py
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
# Created by Chyi Yaqing on 02/26/19 16:51.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Brute Force: Naive algorithm for Pattern Searching
    Given a text txt[0..n-1] and a pattern pat[0..m-1],write a function
    search(char pat[], char txt[]) that prints all occurrences of pat[] in
    txt[]. assume that n > m

Pattern searching is an important problem in computer science. When we do
search for a string in notepad/word file or browser or database, pattern
searching algorithms are used to show the search results.
"""


# Python3 program for Naive Pattern Searching algorithm
def brute_force_search(pat, txt):
    N, M = len(txt), len(pat)

    if N < M:
        return
    # A loop to slide pat[] one by one
    for i in range(N-M+1):
        # For current index i, check for pattern match
        for j in range(0, M):
            if (txt[i + j] != pat[j]):
                break

        if j == M-1:
            print("Pattern found at index {}".format(i))


# Driver Code
if __name__ == '__main__':
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"
    brute_force_search(pat, txt)
