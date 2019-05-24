#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Waiting for Tasks in Any Order

    Invoking the result() method of a Future blocks until the task complete
    (either by returning a value or raising an exception), or is canceled.
    The results of multiple tasks can be accessed in the order the tasks were
    scheduled using map(). If it does not matter what order the results should
    be processed, use as_completed() to process them as each task finishes.
"""
from concurrent import futures
import random
import time


def task(n):
    time.sleep(random.random())
    return (n, n/10)


if __name__ == '__main__':
    ex = futures.ThreadPoolExecutor(max_workers=5)
    print("main: random order")
    wait_for = [ex.submit(task, i) for i in range(10, 0, -1)]
    for f in futures.as_completed(wait_for):
        print("main: result: {}".format(f.result()))

    print("main: order")
    results = ex.map(task, range(10, 0, -1))
    for real_rst in list(results):
        print("main: real_rst: {}".format(real_rst))
