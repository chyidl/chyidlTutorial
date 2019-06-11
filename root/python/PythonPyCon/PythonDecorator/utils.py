#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#                ____
#               / . .\
# Life is short \  ---<
# I use Python   \  /
#      __________/ /
#   -=:___________/
# utils.py
# PythonDecorator
#
# Created by Chyi Yaqing on 06/11/19 11:02.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the MIT
import time


# A Python decorator for measuring the execution time of methods
def timeit(func):
    """
    @timeit decorator that allows you to measure the execution times
    of dedicated methods (module-level methods or class methods) by
    just adding the @timeit decorator in front of the method call.
    """
    def timed(*args, **kwargs):
        ts = time.time()
        result = func(*args, **kwargs)
        te = time.time()
        print("%r (%r, %r) %2.2f sec" % (
            func.__qualname__, args, kwargs, te-ts))
        return result

    return timed
