#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Using map() with a Basic Thread Pool
    ThreadPoolExecutor manager a set of worker threads, passing tasks to them
    as they become available for more work. This example uses map() to
    concurrently produce a set of results from an input iterable.
    map() always returns the values in order based on the inputs.
"""
from concurrent import futures
import threading
import time


def task(n):
    print("{}: sleeping {}".format(threading.current_thread().name, n))
    time.sleep(n / 10)
    print("{}: doen with {}".format(threading.current_thread().name, n))
    return n / 10


if __name__ == '__main__':
    ex = futures.ThreadPoolExecutor(max_workers=4)
    print("main: starting")
    results = ex.map(task, range(5, 0, -1))
    print("main: unprocessing results {}".format(results))
    print("main: waiting for real results")
    real_results = list(results)
    print("main: results: {}".format(real_results))
