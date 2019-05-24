#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Process Pools:
    The ProcessPoolExecutor works in the same way as ThreadPoolExecutor, but
    uses processes instead of threads. This allows CPU-intensive operations to
    use a separate CPU and not be blocked by the CPython interpreter's global
    interpreter lock.
"""
from concurrent import futures
import os


def task(n):
    return (n, os.getpid())


if __name__ == '__main__':
    ex = futures.ProcessPoolExecutor(max_workers=2)
    results = ex.map(task, range(5, 0, -1))
    for n, pid in results:
        print("run task {} in process {}".format(n, pid))
