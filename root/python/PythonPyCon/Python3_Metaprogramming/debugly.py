#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# debuggly.py
from functools import wraps


def debug(func):
    # func is function to be wrapped
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(func.__qualname__)
        return func(*args, **kwargs)
    return wrapper


# Decorators with Args
def debugArgs(prefix=''):   # Outer function defines variables for use in regular decorate
    def decorate(func):
        msg = prefix + func.__qualname__

        @wraps(func)
        def wrapper(*args, **kwargs):
            print(msg)
            return func(*args, **kwargs)
        return wrapper
    return decorate
