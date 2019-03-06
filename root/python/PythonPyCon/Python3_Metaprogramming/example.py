#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# exmaple.py
from debugly import debug, debugArgs, debugmethods


@debugArgs('+++')
def add(x, y):
    return x + y


@debug
def sub(x, y):
    return x - y


@debug
def mul(x, y):
    return x * y


@debug
def div(x, y):
    return x / y


@debugmethods
class Spam:
    def a(self):
        pass

    def b(self):
        pass


if __name__ == '__main__':
    add(1, 2)
    sub(2, 3)
    mul(3, 4)
    div(4, 5)
