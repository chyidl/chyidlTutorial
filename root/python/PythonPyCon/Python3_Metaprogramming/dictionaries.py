#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Spam:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def foo(self):
        pass

s = Spam(2, 3)
print(s.__dict__)
print(Spam.__dict__['foo'])
