#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# redisClient.py
# chdb
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
# Created by Chyi Yaqing on 03/15/19 12:54.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the MIT

"""
Using Singleton Design Pattern
"""
import os
import redis


class Singleton(type):
    """An metaclass for singleton purpose. Every singleton class should inherit
    from this class by 'metaclass=Singleton'."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if cls not in cls._instances:
            cls._instances[cls] = {}
        if key not in cls._instances[cls]:
            cls._instances[cls][key] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls][key]


class RedisClient(metaclass=Singleton):
    'RedisClient is a singleton class'
    def __init__(self, _host, _port, _db, _password, **kwargs):
        self.pool = redis.ConnectionPool(
                host=_host, port=_port, db=_db, password=_password, **kwargs)

    @property
    def conn(self):
        if not hasattr(self, '_conn'):
            self.getConnection()
        return self._conn

    def getConnection(self):
        self._conn = redis.StrictRedis(connection_pool=self.pool)


if __name__ == '__main__':
    env_dist = os.environ
    host = env_dist.get('REMOTE_REDIS_HOST')
    port = env_dist.get('REMOTE_REDIS_PORT')
    db = 15
    password = env_dist.get('REMOTE_REDIS_PASSWORD')

    client1 = RedisClient(host, port, db, password)
    client2 = RedisClient(host, port, db, password)
    print(client1 == client2)
    print(client1.conn == client2.conn)
