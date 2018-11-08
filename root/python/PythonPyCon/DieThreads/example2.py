#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from concurrent.futures import Future
import threading

def spam(x, y, fut):
    result = x + y
    fut.set_result(result)

fut = Future()
t = threading.Thread(target=spam, args=(1,2,fut))
t.start()
t.join()
print('Result', fut.result())
