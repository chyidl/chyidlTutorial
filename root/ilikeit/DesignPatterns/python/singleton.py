#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# singleton.py
# python
#
# Created by Chyi Yaqing on 03/21/19 17:34.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the MIT


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    if (id(s1) == id(s2)):
        print("Same")
    else:
        print("Different")
