#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# recursive algorithm
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

