#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# logging_decorate.py
# Python3_Metaprogramming
#
# 🎂"Here's to the crazy ones. The misfits. The rebels.
# The troublemakers. The round pegs in the square holes.
# The ones who see things differently. They're not found
# of rules. And they have no respect for the status quo.
# You can quote them, disagree with them, glority or vilify
# them. About the only thing you can't do is ignore them.
# Because they change things. They push the human race forward.
# And while some may see them as the creazy ones, we see genius.
# Because the poeple who are crazy enough to think thay can change
# the world, are the ones who do."
#
# Created by Chyi Yaqing on 03/05/19 21:04.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT
import os
from functools import wraps
import logging


def debug(func):
    # Key idea: Can change decorator independently of code that uses it
    if 'DEBUG' not in os.environ:
        return func
    log = logging.getLogger(func.__module__)
    msg = func.__qualname__
    @wraps(func)
    def wrapper(*args, **kwargs):
        log.debug(msg)
        return func(*args, **kwargs)
    return wrapper


if __name__ == '__main__':
    @debug
    def foo():
        print("Hello")

    foo()
