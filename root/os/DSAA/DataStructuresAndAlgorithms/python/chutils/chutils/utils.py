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
'''A series of convenience functions to make easier with Python3.
Identify bottlenecks as quickly as possible,
fix them and then confirm you've fixed them.
'''
__author__ = 'Chyi Yaqing'
__verion__ = '0.0.1'
import sys
import time
import functools


def chdebug(func=None, *, prefix=""):
    if func is None:
        # Wasn't passed
        return functools.partial(chdebug, prefix=prefix)

    # func is a function to be wrapped
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
        print('%s start call %s():' % (prefix, func.__qualname__))
        result = func(*args, **kwargs)
        print('%s end call %s():' % (prefix, func.__qualname__))
        return result
    return wrapper


def metric(func):
    'a simple timing decorator flexible ways to measure execution time'
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('%s executed in %.4f s' % (func.__qualname__, end-start))
        return result
    return wrapper


class Student:

    def __init__(self, Name, Score):
        self.name = Name
        self.score = Score

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('name must be an string!')
        self._name = value

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    def get_grade(self):
        if self._score >= 80:
            return 'A'
        if self._score >= 60:
            return 'B'
        return 'C'


class Chain:

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __call__(self, param):
        return Chain('%s/%s' % (self._path, param))

    def __str__(self):
        return self._path

    __repr__ = __str__


if __name__ == '__main__':
    # Test chlog decorate  and metric
    @metric
    @chdebug(prefix='')
    def foo():
        print(sys.platform)
    # Run Testcase
    foo()

    @chdebug
    def bar():
        print('bar')
    bar()

    # Test Student property decorate
    s = Student(Name="Chyi Yaqing", Score=99)
    print(s.score)  # OK
    print(s.score)  # OK, 实际转化为s.get_score()
    try:
        s.score = 101
    except Exception as e:
        print(e)

    # Test Chain
    print(Chain().status.user.timeline.list)
    print(Chain().users('Chyi Yaqing').age(26).single(True).repos)
