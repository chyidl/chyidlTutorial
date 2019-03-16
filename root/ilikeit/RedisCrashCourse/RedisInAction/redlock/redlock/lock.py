#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# lock.py
# redlock
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
# Created by Chyi Yaqing on 03/16/19 11:32.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the MIT

"""
Distributed locks with Redis
"""
import random
import time
import uuid
import redis
from time import monotonic


DEFAULT_RETRY_TIMES = 3
DEFAULT_RETRY_DELAY = 200
DEFAULT_TTL = 100000
CLOCK_DRIFT_FACTOR = 0.01

# Reference: http://redis.io/topics/distlock
# Section Correct implementation with a single instance
RELEASE_LUA_SCRIPT = """
    if redis.call("get",KEYS[1]) == ARGV[1] then
        return redis.call("del",KEYS[1])
    else
        return 0
    end
"""


class RedLockError(Exception):
    pass


class RedLockFactory:
    'A Factory class that helps reuse multiple Redis connections.'
    def __init__(self, connection_details):
        self.redis_nodes = []
        for conn in connection_details:
            if isinstance(conn, redis.StrictRedis):
                node = conn
            elif 'url' in conn:
                url = conn.pop('url')
                node = redis.StrictRedis.from_url(url, **conn)
            else:
                node = redis.StrictRedis(**conn)
            node._release_script = node.register_script(RELEASE_LUA_SCRIPT)
            self.redis_nodes.append(node)
            self.quorum = len(self.redis_nodes)//2 + 1

        def create_lock(self, resource, **kwargs):
            """
            Create a new RedLock object and reuse stored Redis clients.
            All the kwargs it received would be passed to the RedLock's
            __init__ function.
            """
            lock = RedLock(
                    resource=resource, created_by_factory=True, **kwargs)
            lock.redis_nodes = self.redis_nodes
            lock.quorum = self.quorum
            lock.factory = self
            return lock


class RedLock:
    """
    A distributed lock implementation based on Redis.
    It shares a similar API with the `threading.Lock` class in the
    Python Standard Library.
    """

    def __init__(
            self, resource, connection_details=None,
            retry_times=DEFAULT_RETRY_TIMES, retry_delay=DEFAULT_RETRY_DELAY,
            ttl=DEFAULT_TTL, created_by_factory=False):
        self.resource = resource
        self.retry_times = retry_times
        self.retry_delay = retry_delay
        self.ttl = ttl

        if created_by_factory:
            self.factory = None
            return

        self.redis_nodes = []
        # If the connection_details parameters is not provided,
        # use redis://127.0.0.1:6379/0
        if connection_details is None:
            connection_details = [{
                'host': 'localhost',
                'port': 6379,
                'db': 0,
                }]

        for conn in connection_details:
            if isinstance(conn, redis.StrictRedis):
                node = conn
            elif 'url' in conn:
                url = conn.pop('url')
                node = redis.StrictRedis.from_url(url, **conn)
            else:
                node = redis.StrictRedis(**conn)
            node._release_script = node.register_script(RELEASE_LUA_SCRIPT)
            self.redis_nodes.append(node)
        self.quorum = len(self.redis_nodes)//2 + 1

    def __enter__(self):
        acquired, validity = self.acquire_with_validity()
        if not acquired:
            raise RedLockError('failed to acquire lock')
        return validity

    def __exit__(self, exc_type, exc_value, traceback):
        self.release()

    def locked(self):
        for node in self.redis_nodes:
            if node.get(self.resource):
                return True
        return False

    def acquire_node(self, node):
        'acquire a single redis node'
        try:
            return node.set(self.resource, self.lock_key, nx=True, px=self.ttl)
        except (
                redis.exceptions.ConnectionError,
                redis.exceptions.TimeoutError):
            return False

    def release_node(self, node):
        'release a single redis node'
        # use the lua script to release the lock in a safe way
        try:
            node._release_script(keys=[self.resource], args=[self.lock_key])
        except (
                redis.exceptions.ConnectionError,
                redis.exceptions.TimeoutError):
            pass

    def acquire(self):
        acquired, validity = self._acquire()
        return acquired

    def acquire_with_validity(self):
        return self._acquire()

    def _acquire(self):
        # lock_key should be random and unique
        self.lock_key = uuid.uuid4().hex

        for retry in range(self.retry_times + 1):
            acquired_node_count = 0
            start_time = monotonic()

            # acquire the lock in all the redis instances sequentially
            for node in self.redis_nodes:
                if self.acquire_node(node):
                    acquired_node_count += 1

            end_time = monotonic()
            elapsed_milliseconds = (end_time - start_time) * 10**3

            # Add 2 milliseconds to the drift to account for Redis expires
            # precision, which is 1 milliescond, plus 1 millisecond min drify
            # for small TTLs.
            drift = (self.ttl * CLOCK_DRIFT_FACTOR) + 2

            validity = self.ttl - (elapsed_milliseconds + drift)
            if acquired_node_count >= self.quorum and validity > 0:
                return True, validity
            else:
                for node in self.redis_nodes:
                    self.release_node(node)
                time.sleep(random.randint(0, self.retry_delay) / 1000)
        return False, 0

    def release(self):
        for node in self.redis_nodes:
            self.release_node(node)


class ReentrantRedLock(RedLock):
    def __init__(self, *args, **kwargs):
        super(ReentrantRedLock, self).__init__(*args, **kwargs)
        self._acquired = 0

    def acquire(self):
        if self._acquired == 0:
            result = super(ReentrantRedLock, self).acquire()
            if result:
                self._acquired += 1
            return result
        else:
            self._acquired += 1
            return True

    def release(self):
        if self._acquired > 0:
            self._acquired -= 1
            if self._acquired == 0:
                return super(ReentrantRedLock, self).release()
            return True
        return False
