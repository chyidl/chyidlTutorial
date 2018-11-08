#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# contract.py
# Framework for enforcing assertions


class Container:
    def __getitem__(self, index):
        print("Getting:", index)

    def __setitem__(self, index, value):
        print("Setting:", index, value)

def gcd(a, b):
    '''Compute greatest common divisor'''
    assert isinstance(a, int), 'Expected int'
    assert isinstance(a, int), 'Expected int'
    while b:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    c = Container()
    c[12]
    c[12]= 3
    print(gcd(27, 36))
    #print(gcd(2.7, 3.6))
