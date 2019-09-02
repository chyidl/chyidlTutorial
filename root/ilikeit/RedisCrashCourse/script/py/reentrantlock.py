#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#                ____
#               / . .\
# Life is short \  ---<
# I use Python   \  /
#      __________/ /
#   -=:___________/
# reentrantlock.py
# py
#
# Created by Chyi Yaqing on 09/01/19 13:54.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the MIT
"""
还需要考虑内存锁计数的过期时间，不推荐使用重复锁
"""
import redis
import threading


locks = threading.local()
locks.redis = {}


def key_for(user_id):
    return "account_{}".format(user_id)


def _lock(client, key):
    return bool(client.set(key, True, nx=True, ex=5))


def _unlock(client, key):
    client.delete(key)


def lock(client, user_id):
    key = key_for(user_id)
    if key in locks.redis:
        locks.redis[key] += 1
        return True
    ok = _lock(client, key)
    if not ok:
        return False
    locks.redis[key] = 1
    return True


def unlock(client, user_id):
    key = key_for(user_id)
    if key in locks.redis:
        locks.redis[key] -= 1
        if locks.redis[key] <= 0:
            del locks.redis[key]
            self._unlock(key)
        return True
    return False


client = redis.StrictRedis()
print("lock", lock(client, "codehole"))
print("lock", lock(client, "codehole"))
print("unlock", unlock(client, "codehole"))
print("unlock", unlock(client, "codehole"))
