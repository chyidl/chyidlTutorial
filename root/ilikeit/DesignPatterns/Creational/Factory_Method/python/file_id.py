#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class A(object):
    pass

if __name__ == '__main__':
    a = A()
    b = A()

    print(id(a) == id(b))
    print(a, b)