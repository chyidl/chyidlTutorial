#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# utils_test.py
# tests
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
# Created by Chyi Yaqing on 03/05/19 15:03.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
chutils/utils.py 测试模块
"""
# Path hack.
import sys
import os
import unittest
sys.path.insert(0, os.path.abspath('..'))
from chutils import utils


class TestDecorate(unittest.TestCase):

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_chlog_metric(self):
        # Test chlog decorate  and metric
        @utils.metric
        @utils.chlog()
        def foo():
            print(sys.platform)
        # Run Testcase
        foo()


class TestStudent(unittest.TestCase):

    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_80_100(self):
        s1 = utils.Student('Chyi Yaqing', 80)
        s2 = utils.Student('Chyi Dobby', 100)
        self.assertEqual(s1.name, 'Chyi Yaqing')
        self.assertEqual(s2.name, 'Chyi Dobby')
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_invalid(self):
        s1 = utils.Student('Chyi Yaqing', 10)
        s2 = utils.Student('Chyi Dobby', 10)
        with self.assertRaises(ValueError):
            s1.score = -1
        with self.assertRaises(ValueError):
            s2.score = 101


if __name__ == '__main__':
    # 运行单元测试
    unittest.main()
