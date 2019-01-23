#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Reliable file updates with Python
    surprisingly naive way: 幼稚
How to improve I/O reliability in Python code.
What does 'reliability' mean anyway?


naive way:

    with open(filename) as f:
        input = f.read()
    output = do_something(input)
    with open(filename, 'w') as f:
        f.write(output)


"""

