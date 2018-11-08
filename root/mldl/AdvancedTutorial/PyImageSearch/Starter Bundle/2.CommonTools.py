#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# compute the n-th number in the sequence by supplying a value
def fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    print(fibonacci(18))
