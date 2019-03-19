#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:encoding=utf-8
#
# interview_with_google_engineer.py
# interviewing.io
#
#   __________
#  / ___  ___ \
# / /  \/  \ \
# \ \___/\___/ /\
#  \____\/____/||
#  /     /\\\\\//
# |  🔥 |\\\\\\
#  \      \\\\\\
#    \______/\\\\
#     _||_||_
#
# Created by Chyi Yaqing on 03/18/19 22:50.
# Copyright © 2019. Chyi Yaqing. All rights reserved.
#
# Distributed under terms of the MIT
# Enjoy your interview!


def case_insensitive_compare(s1, s2):
    if len(s1) != len(s2):
        return False
    s1_iter = iter(s1)
    s2_iter = iter(s2)
    for _ in range(len(s1)):
        s1_c = s1_iter.next()
        s2_c = s2_iter.next()
        if not s1_c.upper() == s2_c.upper():
            return False
    return True


print(case_insensitive_compare('abc', 'ABC'))
print(case_insensitive_compare('abc', 'dev'))
