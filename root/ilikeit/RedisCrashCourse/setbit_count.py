#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:encoding=utf-8
#
# setbit_count.py
# RedisCrashCourse
#
#   __________
#  / ___  ___ \
# / /  \/  \ \
# \ \___/\___/ /\
#  \____\/____/||
#  /     /\\\\\//
# |  🔥 |\\\\\\
#  \      \\\\\\
#    \______/\\\\
#     _||_||_
#
# Created by Chyi Yaqing on 03/27/19 22:12.
# Copyright © 2019. Chyi Yaqing. All rights reserved.
#
# Distributed under terms of the MIT
"""
使用setbit进行统计计数
"""
import os
import redis
import datetime
from bitarray import bitarray


env_dist = os.environ
redis_host = env_dist.get('REMOTE_REDIS_HOST')
redis_port = env_dist.get('REMOTE_REDIS_PORT')
redis_db = 15
redis_password = env_dist.get('REMOTE_REDIS_PASSWORD')


redis_pool = redis.ConnectionPool(
        host=redis_host, port=redis_port, db=redis_db, password=redis_password)
conn = redis.StrictRedis(connection_pool=redis_pool, charset='utf-8', decode_responses=True)
today = datetime.date.today().strftime('%Y-%m-%d')


def setup():
    conn.delete('user:'+today)
    conn.setbit('user:'+today, 100, 0)


def setuniquser(uid):
    conn.setbit('user:'+today, uid, 1)


def countuniquser():
    a = bitarray()
    a.frombytes(conn.get('user:'+today),)
    print(a)
    print(a.count())


if __name__ == '__main__':
    setup()
    setuniquser(uid=0)
    countuniquser()
