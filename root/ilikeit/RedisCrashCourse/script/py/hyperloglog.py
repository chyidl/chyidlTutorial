#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#                ____
#               / . .\
# Life is short \  ---<
# I use Python   \  /
#      __________/ /
#   -=:___________/
# hyperloglog.py
# py
#
# Created by Chyi Yaqing on 09/20/19 15:44.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the MIT
import redis


REDIS_HOST="192.168.1.243"
REDIS_PORT=6379
REDIS_DB=0
REDIS_PASSWORD="000000"


client = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT,db=REDIS_DB,password=REDIS_PASSWORD)
for i in range(1000):
    client.pfadd("codehole", "user%d" % i)
    total = client.pfcount("codehole")
    if total != i+1:
        print(total, i+1)
        break
"""
$ python3 hyperloglog.py
99 100
"""
