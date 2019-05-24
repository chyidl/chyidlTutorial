#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
If a tasks raises an unhandled exception, it is saved to the Future for the
task and made available through the result() or exception() methods.
"""
from concurrent import futures


def task(n):
    print("{}: starting".format(n))
    raise ValueError("the value {} is no good".format(n))


if __name__ == '__main__':
    ex = futures.ThreadPoolExecutor(max_workers=2)
    print("main: starting")
    f = ex.submit(task, 5)
    error = f.exception()
    print("main: error: {}".format(error))

    try:
        # if result() is called after an unhandled exception is raised within
        # a task function, the same exception is re-raised in the current
        result = f.result()
    except ValueError as e:
        print('main: saw error "{}" when accessing result'.format(e))
