#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:encoding=utf-8
#
# levenshtein_distance_implement.py
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
# Created by Chyi Yaqing on 02/27/19 22:17.
# Copyright © 2019. Chyi Yaqing. All rights reserved.
#
# Distributed under terms of the MIT
"""
In formation theory and computer science, the Levenshtein distance is a metric
for measuring the amount of difference between two sequences(i.e. an edit
distance). The Levenshtein distance between two strings is defined as the
minimum number of edits needed to transform one string into the other, with the
allowable edit operations being insertion, deletion, or substitution of a
single character.
"""


# Iterative, optimized for memory
def minimumEditDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    distances = range(len(s1)+1)
    for index2, char2 in enumerate(s2):
        newDistances = [index2+1]
        for index1, char1 in enumerate(s1):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((
                    distances[index1], distances[index1+1], newDistances[-1])))
        distances = newDistances
    return distances[-1]


print(minimumEditDistance("kitten", "sitting"))
print(minimumEditDistance("mitcmu", "mtacnu"))
print(minimumEditDistance("rosettacode", "raisethysword"))


str1 = "mitcmu"
str2 = "mtacnu"
m, n = len(str1), len(str2)
minDist = max(m, n)


# 回溯算法
def levenshteinDistance(i=0, j=0, edist=0):
    global minDist
    if i == n or j == m:
        if i < n:
            edist += (n - i)
        if j < m:
            edist += (m - j)
        if edist < minDist:
            minDist = edist
        return

    if str1[i] == str2[j]:  # 两个字符串匹配
        levenshteinDistance(i+1, j+1, edist)
    else:
        levenshteinDistance(i+1, j, edist + 1)  # 删除a[i] 或者b[j] 前添加一个字符
        levenshteinDistance(i, j+1, edist + 1)  # 删除b[j] 或者a[i] 前添加一个字符
        levenshteinDistance(i + 1, j + 1, edist + 1)  # 将a[i]和b[j]替换为相同字符


levenshteinDistance(0, 0, 0)
print(minDist)
