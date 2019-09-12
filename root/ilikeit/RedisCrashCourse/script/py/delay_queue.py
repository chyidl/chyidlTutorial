#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#                ____
#               / . .\
# Life is short \  ---<
# I use Python   \  /
#      __________/ /
#   -=:___________/
# delay_queue.py
# py
#
# Created by Chyi Yaqing on 09/11/19 13:39.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the MIT
import uuid
import json
import time
import redis


def delay(msg):
    # uuid.uuid4() - Generate a random UUID
    msg.id = str(uuid.uuid4())  # 保证value值唯一
    value = json.dumps(msg)
    retry_ts = time.time() + 5  # 5秒重试
    redis.zadd("delay-queue", retry_ts, value)


def loop():
    while True:
        # 最多取一条
        values = redis.zrangebyscore("delay-queue", 0, time.time(), start=0, num=1)
        if not values:
            time.sleep(1)  # 延迟队列空的，休息1s
            continue
        value = values[0]  # 获取第一条，也只有一条
        # Redis 的zrem是多线程多进程任务的关键，zrem的返回值决定当前实例有没有抢到任务，因为loop方法可能会被多个线程、多个进程调度，同一个任务可能会被多个进程线程抢到，通过zrem来决定唯一成功的线程.
        success = redis.zrem("delay-queue", value)  # 从消息队列中移除该消息
        if success:  # 因为有多线程并发问题，最终只会有一个进程可以抢到消息
            msg = json.loads(value)
            handle_msg(msg)  # 需要对handle_msg进行异常捕获,避免因为个别任务处理问题导致循环异常退出


