#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# task_master.py
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
# Created by Chyi Yaqing on 03/06/19 09:05.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
服务进程
"""
import random
import queue
from multiprocessing.managers import BaseManager


# 发送任务的队列
task_queue = queue.Queue()
# 接受结果的队列
result_queue = queue.Queue()


# 从BaseManager 即成QueueManager:
class QueueManager(BaseManager):
    pass


# 把两个Queue都注册到网络上，callable参数关联Queue对象
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口9527,设置验证码'abc':
manager = QueueManager(address=('', 9527), authkey=b'abc')
# 启动Queue
manager.start()

# ⚠️ ，在分布式多进程环境下，添加任务到Queue不可以直接对原始的task_queue进行操作，
# 必须通过manager.get_task_queue()获得Queue接口
# 获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

# 分发任务
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)

# 从result队列读取结果
print('Try get results...')
for i in range(10):
    try:
        r = result.get(timeout=10)
        print('Result: %s' % r)
    except queue.Empty:
        print('result queue is empty.')

# 关闭
manager.shutdown()
print('master exit.')
