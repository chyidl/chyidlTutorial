#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# exmaple.py
from debugly import debug


@debug
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
