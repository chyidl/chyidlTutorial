#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# debuggly.py
from functools import wraps, partial
import logging
import os

def debug(func):
    # func is function to be wrapped
    msg = func.__qualname__
    @wraps(func) # what this does is copy metadata from one function to another
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    return wrapper

def debuglogging(func):
    if 'DEBUG' not in os.environ:
        return func
    msg = func.__qualname__
    @wraps(func)
    def wrapper(*args, **kwargs):
        log.debug(msg)
        return func(*args, **kwargs)
    return wrapper

# Outer function defines variables for use in regular decorator
def debugarg(prefix=''):
    def decorate(func):
        msg = prefix + func.__qualname__
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(msg)
            return func(*args, **kwargs)
        return wrapper
    return decorate

# A Reformulation
def debug_func(func=None, *, prefix=''):
    if func is None:
        # Wasn't passed
        return partial(debug, prefix=prefix)
    msg = prefix + func.__qualname__
    # func is function to be wrapped
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    return wrapper

# Class Decorator
def debugmethods(cls):
    # cls is a class
    # Walk through class dictionary
    for key, val in vars(cls).items():
        # Identify callables (e.g/. methods)
        if callable(val):
            # Wrap with a decorator
            setattr(cls, key, debug(val))
    return cls

def debugattr(cls):
    orig_getattribute = cls.__getattribute__

    def __getattribute__(self, name):
        print('Get:', name)
        return orig_getattribute(self, name)
    cls.__getattribute__ = __getattribute__

    return cls

# Solution: A Metaclass
class debugmeta(type):
    def __new__(cls, clsname, bases, clsdict):
        # Class gets created normally
        clsobj = super().__new__(cls, clsname, bases, clsdict)
        # Immediately wrapped by class decorator
        clsobj = debugmethods(clsobj)
        return clsobj

