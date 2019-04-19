#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Creating a Singleton in Python
"""
    Singleton pattern is actually considered an anti-pattern and overuse of it should be avoided. It is not necessarily bad and could
    have some valid use-cases but should be used with caution because it introduces a global state in your application and change
    to it in one place could affect in the other areas and it could become pretty difficult to debug. The other bad thing about them
    is it makes your code tightly coupled plus mocking the singleton could be difficult.
"""


# Method 1: A decorator : Decorators are additive in a way that is often more intuitive than multiple inheritance.
def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class MyClass1:
    pass


# Object created using MyClass1() would be true singleton objects.
m = MyClass1();  n = MyClass1()
print("{}\n{}".format(m, n))
# MyClass1 itself is a function, not a class, so you cannot call class methods from it.
o = type(n)()
print(o)


# Method 2: A metaclass : is the class of a class, like a class defines how an instance of the class behaves, a meta
# Find the metaclass of an object in Python with type(obj)
class Singleton(type):
    """type is the usual metaclass in Python"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# Python3
class MyClass2(metaclass=Singleton):
    pass


# Object created using MyClass1() would be true singleton objects.
m = MyClass2(); n = MyClass2()
print("{}\n{}".format(m, n))
# MyClass1 itself is a function, not a class, so you cannot call class methods from it.
o = type(n)()
print(o)