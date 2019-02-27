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
https://brilliant.org/wiki/rabin-karp-algorithm/

Rabin-Karp Algorithm for Pattern Searching
    Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function
    search(char pat[], char txt[]) that prints all occurrences of pat[] in
    txt[]. You may assume that n > m

The Rabin-Karp algorithm is a string searching algrithm that uses hashing to
find patterns in strings. A string is an abstract data type that consists or
a sequence of characters. Letters, words, sentences, and more can be represente
as strings.

The Rabin-Karp algorithm makes use of hash functions and the rolling hash
technique. A hash function is essentially a function that maps one thing to a
value. In particular, hashing can map data of arbitrary size to value of fixed
size.

A rolling hash allows an algorithm to calculate a hash value without having the
rehash the entire string.

RK 算法包含两部分：计算字串哈希值 + 模式串哈希值与子串哈希值比较
RK 算法时间复杂度：O(n)
RK 算法空间复杂度:
"""


class RollingHash:
    def __init__(self, text, sizeWord):
        self.text = text
        self.hash = 0
        self.sizeWord = sizeWord
        
        for i in range(0, sizeWord):
            # ord maps the character to a number
            # substrct out the ASCII value of "a" to start the indexing at zero
            self.hash += (ord(self.text[i]) - ord("a")+1)*(26**(sizeWord-i-1))

        # start index of current window
        self.window_start = 0
        # end of index window
        self.window_end = sizeWord

    def move_window(self):
        if self.window_end <= len(self.text) - 1:
            # remove left letter from hash value
            self.hash -= (ord(self.text[self.window_start]) - ord("a")+1)*26**(
                    self.sizeWord-1)
            self.hash *= 26
            self.hash += ord(self.text[self.window_end]) - ord("a")+1
            self.window_start += 1
            self.window_end += 1

    def window_text(self):
        return self.text[self.window_start:self.window_end]


def rabin_karp(word, text):
    if word == "" or text == "":
        return
    if len(word) > len(text):
        return

    rolling_hash = RollingHash(text, len(word))
    word_hash = RollingHash(word, len(word))

    for i in range(len(text) - len(word) + 1):
        if rolling_hash.hash == word_hash.hash:
            if rolling_hash.window_text() == word:
                print (i, end=" ")
        rolling_hash.move_window()


if __name__ == "__main__":
    print(rabin_karp("a", "abcdaefagh"))
    print(rabin_karp("cpu", "ballcpuaspcpucpu"))
