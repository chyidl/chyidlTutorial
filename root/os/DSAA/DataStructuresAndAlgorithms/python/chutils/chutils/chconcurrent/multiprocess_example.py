#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# multiprocess_example.py
# chconcurrent
#
# Created by Chyi Yaqing on 03/26/19 15:42.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the MIT
"""
multiprocessing.Pool: When to use apply, apply_async or map

Pool.apply, Pool.map blocks until the complte result is returned

Pool.apply_async Pool of worker processes tp perform many function
calls asynchronously. The order of the results is not guaranteed to be
same as the order of the calls to Pool.apply_async.

Notice also that you could call a number of different functions with
Pool.apply_async (not all calls need to use the same function).

In contrast, Pool.map applies the same function to many arguments. However,
unlike Pool.apply_async, the results are returned in an order corresponding
to the order of the arguments.
"""
import multiprocessing as mp
import time


def foo_pool(x):
    time.sleep(2)
    return x*x


result_list = []


def log_result(result):
    # This is called whenever foo_pool(i) returns a result.
    # result_list is modified only by the main process, not the pool workers.
    result_list.append(result)


def apply_async_with_callback():
    pool = mp.Pool()
    for i in range(10):
        # unlike pool.map, the order of the results may not correspond to the
        # order in which the pool.apply_async calls were made.
        pool.apply_async(foo_pool, args=(i, ), callback=log_result)
    pool.close()
    pool.join()
    print(result_list)


if __name__ == '__main__':
    apply_async_with_callback()
    print("MultiProcess Over")
