#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from types import coroutine

def countdown(n):
    while  n > 0:
        yield n
        n -= 1


@coroutine
def spam():
    result = yield 'somevalue'
    print('The result is', result)


async def foo():
    print("Start foo")
    await spam()
    print("End foo")


async def bar():
    print("Start bar")
    await foo()
    print("End bar")


for i in countdown(5):
    print(i)


f = spam()
print(f)
f.send(None)
# f.send(42)

print(foo())
print(foo().send(None))
print(foo().send(42))
