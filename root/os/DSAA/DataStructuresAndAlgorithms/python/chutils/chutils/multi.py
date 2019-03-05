#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# multi.py
# chutils
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
# Created by Chyi Yaqing on 03/05/19 17:25.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
multiprocessing 多进程

"""
import os
import time
import random
from multiprocessing import Process, Pool, Queue
import subprocess
import threading


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end-start)))


print('Parent process %s.' % os.getpid())
p = Process(target=run_proc, args=('test',))
print('Child process will start.')
p.start()
p.join()
print('Child process end.')


print('Processing (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (
        os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (
        os.getpid(), pid))

print('Parent process %s.' % os.getpid())
p = Pool()  # 默认为CPU核心数
for i in range(5):
    p.apply_async(long_time_task, args=(i,))
print('Waiting for all subrocesses done...')
p.close()
p.join()
print('All subprocesses done.')

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)


print('$ nslookup')
p = subprocess.Popen(
        ['nslookup'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)


# 进程间通信, 父进程创建两个子进程，一个写Queue,一个读Queue
def write(q):
    '写数据进程执行代码'
    print('Process (%s) to write:' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s queue...' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    '读数据进程执行的代码'
    print('Process (%s) to read:' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


# 父进程创建Queue, 并传给各个子进程
q = Queue()
pw = Process(target=write, args=(q,))
pr = Process(target=read, args=(q,))
# 启动子进程pw, 写入:
pw.start()
# 启动子进程pr, 读取:
pr.start()
# 等待pw结束
pw.join()
# pr进程内部死循环，无法等待结束，只能强制终止
pr.terminate()


# 新线程执行代码
def loop():
    print('threading %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
    print('thread %s is ended.' % (threading.current_thread().name))


print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)


# 假定银行存款
balance = 0
lock = threading.Lock()


def change_it(n):
    # 先存后取，结果应该是0
    global balance
    balance += n
    balance -= n


def run_thread(n):
    for i in range(10000000):
        # 先获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 释放锁
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start(), t2.start()
t1.join(), t2.join()
print(balance)


'''
# Python 死循环
def loop():
    x = 0
    while True:
        x += 1
        x -= 1


for i in range(os.cpu_count()):
    t = threading.Thread(target=loop)
    t.start()
'''

# 创建全局ThreadLocal对象
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    # 绑定ThreadLocal的student
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice', ), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start(), t2.start()
t2.join(), t2.join()
