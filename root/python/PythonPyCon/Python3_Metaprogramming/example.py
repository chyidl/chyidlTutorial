#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# example.py

from debugly import *


@debugarg(prefix='+++')
def add(x, y):
    return x + y

@debugarg(prefix='---')
def sub(x, y):
    return x - y

@debugarg(prefix='***')
def mul(x, y):
    return x * y

@debugarg(prefix='///')
def div(x, y):
    return x / y

@debugmethods
# Sets the class used for creating the type
# By default, it's set to 'type', but you can change it to something else
class Spam(metaclass=type):
    @classmethod
    def grok(cls):  # Not wrapped
        pass
    @staticmethod
    def bar():  # Not wrapped
        pass
    # Only instance methods get wrapped
    @debugarg(prefix="FOO")
    def foo(self):
        pass

@debugattr
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Defining a New Metaclass
# You typically inherit from type and redefine
class mytype(metaclass=type):
    def __new__(cls, name, bases, clsdict):
        clsobj = super().__new__(cls, name, bases, clsdict)
        return clsobj

if __name__ == '__main__':
    print(add(2,3))
    print(sub(2,3))
    print(mul(2,3))
    print(div(2,3))

    # change function
    print(add)
    # <function debug.<locals>.wrapper at 0x10069fef0
    print(help(add))

    # One decorator application
    # Converts all definitions within the class
    # It even mostly works
    spam = Spam()
    print("\nExample Use Decorate Class\n")
    print(Spam.grok())
    print(spam.bar())
    print(spam.foo())

    p = Point(2, 3)
    print(p.x)
    print(p.y)
