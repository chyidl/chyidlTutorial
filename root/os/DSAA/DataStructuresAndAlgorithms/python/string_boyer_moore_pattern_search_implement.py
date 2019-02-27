#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# string_boyer_moore_pattern_search_implement.py
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
# Created by Chyi Yaqing on 02/26/19 17:43.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
In computer science, the Boyer-Moore string-search algorithm is an efficient
string-searching algorithm that is the standard benchmark for practical
string-search literature.

Boyer Moore is a combination of following two approaches:
    1) Bad Character Heuristic
        The bad-character rule considers the character in T at which the
        comparison process failed (assuming such a failure occurred). The
        next occurrence of that character to the left in P is found, and a
        shift which brings that occurrence in line with the mismatches
        occurrence in T is proposed. If the mismatched character does not occur
        to the left in P, a shift is proposed that moves the entirety of P past
        the point of mismatch.

    2) Good Suffix Heuristic
"""


def alphabet_index(c):
    # Returns the index of the given character in the English alphabet,
    # counting from 0
    return ord(c.lower()) - 97  # 'a' is ASCII character 97


def generateBC(patternStr):
    # 模式串的散列表
    pattern_hash_list = [-1]*26
    for i in range(len(patternStr)):
        ascii = alphabet_index(patternStr[i])
        pattern_hash_list[ascii] = i
    return pattern_hash_list


def generateGS(patternStr):
    suffix = [-1]*len(patternStr)
    prefix = [False]*len(patternStr)
    for i in range(len(patternStr)-1):
        j = i
        k = 0  # 公共后缀字串长度
        while j >= 0 and patternStr[j] == patternStr[len(patternStr)-1-k]:
            j -= 1
            k += 1
            suffix[k] = j+1  # j+1 表示公共后缀子串在patterStr[0, i]中起始下标
        if j == -1:
            prefix[k] = True  # 如果公共后缀子串也是模式串的前缀子串
    return suffix, prefix


def boyer_moore_search(txtStr, patternStr):
    if txtStr == "" or patternStr == "":
        return
    if len(patternStr) > len(txtStr):
        return
    pattern_hash_list = generateBC(patternStr)
    suffix, prefix = generateGS(patternStr)
    for i in range(len(txtStr)-len(patternStr)+1):
        for j in range(len(patternStr)-1, -1, -1):
            if txtStr[i+j] != patternStr[j]:
                break  # bad_character 对应的下标是j
        if j < 0:
            print(i, end=" ")  # 匹配成功，打印主串与模式串第一个匹配的字符串的位置
        i += (j - pattern_hash_list[alphabet_index(txtStr[i+j])])

