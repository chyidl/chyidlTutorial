#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import redis


r = redis.StrictRedis(host='192.168.31.156',
                      port=6379,
                      db=0)
print(r.get('test'))
print(r.get('test').decode())

r.set(name='bookName',
      value='一花一世界',
      ex=20,
      nx=True)
print(r.get('bookName').decode())
