#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# DRY -- Don't Repeat Yourself

class Structure:
    _fields = []
    def __init__(self, *args):
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

class Stock(Structure):
    _fields = ['name', 'shares', 'price']
    #def __init__(self, name, shares, price):
    #    self.name = name
    #    self.shares = shares
    #    self.price = price

class Point(Structure):
    _fields = ['x', 'y']
    #def __init__(self, x, y):
    #    self.x = x
    #    self.y = y

class Address(Structure):
    _fields = ['hostname', 'port']
    #def __init__(self, hostname, port):
    #   self.hostname = hostname
    #    self.port = port


if __name__ == '__main__':
    s = Stock('Google', 100, 490.1)
    print('Name: {}, Shares: {}, Price: {}'.format(s.name, s.shares, s.price))
