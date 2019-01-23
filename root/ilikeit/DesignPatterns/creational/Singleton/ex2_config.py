#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# https://www.oodesign.com/singleton-pattern.html
"""
When the class is instantiated the singleton will keep the values in its internal structure. If the values are read from the database
or from the database or from files this avoids the reloading the values each time the configuration parameters are used.
"""


# Method 1: A metaclass : is the class of a class, like a class defines how an instance of the class behaves, a meta
# Find the metaclass of an object in Python with type(obj)
class Singleton(type):
    """type is the usual metaclass in Python"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# Single responsibility principle
# Open/closed principle
# Liskov substitution principle
# Interface segregation principle
# Dependency inversion principle