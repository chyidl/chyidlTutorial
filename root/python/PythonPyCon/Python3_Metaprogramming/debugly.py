#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# debuggly.py
from functools import wraps, partial


def debug(func):
    # func is function to be wrapped
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__qualname__)
        return func(*args, **kwargs)
    return wrapper


# Decorators with Args
def debugArgs(prefix=''):
    # Outer function defines variables for use in regular decorate
    def decorate(func):
        msg = prefix + func.__qualname__
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(msg)
            return func(*args, **kwargs)
        return wrapper
    return decorate


# A test of your function calling skills
def debugRef(func=None, *, prefix=''):
    if func is None:
        return partial(debug, prefix=prefix)

    msg = prefix + func.__qualname__
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(msg)
        return func(*args, **kwargs)
    return wrapper


def debugmethods(cls):
    # cls is a class
    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, debug(val))
    return cls
