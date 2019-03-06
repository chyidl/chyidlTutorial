#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# task_worker.py
# chdist
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
# Created by Chyi Yaqing on 03/06/19 09:15.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
任务进程
"""
import time
import queue
from multiprocessing.managers import BaseManager


# 创建类似的QueueManager:
class QueueManager(BaseManager):
    pass


# 由于QueueManager只能从网络上获取Queue,所以注册时只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 连接到服务器，也就是运行task_master的机器
server_addr = '127.0.0.1'
print('Connect to server %s...' % server_addr)

# 端口和验证码保持与Task_master设置完全一致
m = QueueManager(address=(server_addr, 9527), authkey=b'abc')
# 网络连接
m.connect()
# 获取Queue对象
task = m.get_task_queue()
result = m.get_result_queue()


# 从task队列取任务，并把结果写入result队列
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task queue is empty.')


# 处理结束
print('worker exit.')
