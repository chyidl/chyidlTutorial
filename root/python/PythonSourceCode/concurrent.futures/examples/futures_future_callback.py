#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Future Callbacks
    To take some action when a task completed, without explicitly waiting for
    the result, use add_done_callback() to specify a new function to call when
    the Future is done. The callback should be a callable taking a single
    argument, the Future instance.
"""
from concurrent import futures
import time


def task(n):
    print("{}: sleeping".format(n))
    time.sleep(0.5)
    print("{}: done".format(n))
    return n / 10


def done(fn):
    if fn.cancelled():
        print("{}: canceled".format(fn.arg))
    elif fn.done():
        error = fn.exception()
        if error:
            print("{}: error returned: {}".format(fn.arg, error))
        else:
            result = fn.result()
            print("{}: value returned: {}".format(fn.arg, result))


if __name__ == '__main__':
    ex = futures.ThreadPoolExecutor(max_workers=2)
    print("main: starting")
    f = ex.submit(task, 5)
    f.arg = 5
    f.add_done_callback(done)
    result = f.result()
