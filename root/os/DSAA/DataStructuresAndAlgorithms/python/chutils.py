#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:encoding=utf-8
#
# chutils.py
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
# Created by Chyi Yaqing on 03/04/19 22:39.
# Copyright © 2019. Chyi Yaqing. All rights reserved.
#
# Distributed under terms of the MIT
"""
A series of convenience functions to make easier with Python3.
"""
import sys
import time
import functools


def chlog(text="INFO:"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """ For top-level functions and classes, the __qualname__ attrubute
            is equal to the __name__ attribute. For nested classes, methods,
            and nested functions, the __qualname__ attribute contains a dotted
            path leading to the object from the medule top-level.

            Example with nexted classes
            >>> class C:
            ...     def f(): pass
            ...     class D:
            ...         def g(): pass
            ...
            >>> C.__qualname__
            'C'
            >> C.__name__
            'C'
            >>> C.f.__qualname__
            'C.f'
            >>> C.f.__name__
            'f'
            >>> C.D.__qualname__
            'C.D'
            >>> C.D.__name__
            'D'
            """
            print('%s start call %s():' % (text, func.__qualname__))
            result = func(*args, **kwargs)
            print('%s end call %s():' % (text, func.__qualname__))
            return result
        return wrapper
    return decorator


def metric(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('%s executed in %.4f s' % (func.__qualname__, end-start))
        return result
    return wrapper


if __name__ == '__main__':
    # Test chlog decorate  and metric
    @metric
    @chlog()
    def foo():
        print(sys.platform)
    # Run Testcase
    foo()
