#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Scheduling Individual Tasks

Schedule an individual task with an executor using submit(), and use the Future
instance returned to wait for that task's results.
"""
from concurrent import futures
import threading
import time


def task(n):
    print("{}: sleeping {}".format(threading.current_thread().name, n))
    time.sleep(n / 10)
    print("{}: done with {}".format(threading.current_thread().name, n))
    return n / 10


if __name__ == '__main__':
    ex = futures.ThreadPoolExecutor(max_workers=2)
    print("main: starting")
    f = ex.submit(task, 5)
    print("main: future: {}".format(f))
    print("main: waiting for results")
    result = f.result()
    print("main: result: {}".format(result))
    print("main: future after result: {}".format(f))
