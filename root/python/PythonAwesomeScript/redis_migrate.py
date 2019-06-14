#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#                ____
#               / . .\
# Life is short \  ---<
# I use Python   \  /
#      __________/ /
#   -=:___________/
# redis_migrate.py
# PythonAwesomeScript
#
# Created by Chyi Yaqing on 06/12/19 15:59.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the MIT
import argparse
import redis
import datetime
import time


def connect_redis(conn_dict):
    conn = redis.StrictRedis(host=conn_dict['host'],
                             port=conn_dict['port'],
                             db=conn_dict['db'],
                             password=conn_dict['password'])
    return conn


def conn_string_type(string):
    format = '<host>:<port>/<db>/<password>'
    try:
        host, portdb = string.split(':')
        port, db, password = portdb.split('/')
        db = int(db)
    except ValueError:
        raise argparse.ArgumentTypeError(
                'incorrect format, should be: %s' % format)
    return {'host': host,
            'port': port,
            'db': db,
            'password': password}


def migrate_redis(source, destination, selectKey="*"):
    src = connect_redis(source)
    dst = connect_redis(destination)
    for key in src.keys(selectKey):
        # ttl(name) Return the number of seconds until the key name will expire
        ttl = src.ttl(key)
        # handle TTL command returning -1 (no expire) or -2 (no key)
        if ttl < 0:
            ttl = 0
        print("Dumping key: %s" % key)
        # dump(name): Return a serialized version of the value stored at the
        # specified key. If key doesn't exist a nill bulk reply is returned.
        value = src.dump(key)
        print("Restoring key: %s" % key)
        try:
            # restore(name, ttl, value, replace=False) Create a key using the
            # provided serialized value, previously obtained using DUMP
            dst.restore(key, ttl, value, replace=True)
        except redis.exceptions.ResponseError:
            print("Failed to restore key: %s" % key)
            pass
    return


def timeit(func):
    """
    A Python decorator for measuring the execution time of methods
    """
    def timed(*args, **kwargs):
        ts = time.time()
        result = func(*args, **kwargs)
        te = time.time()
        print('[ %r ] %r (%r, %r) %2.2f sec' % (
            datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            func.__qualname__, args, kwargs, te-ts))
        return result
    return timed


@timeit
def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('source',
                        type=conn_string_type)
    parser.add_argument('destination',
                        type=conn_string_type)
    options = parser.parse_args()
    migrate_redis(options.source, options.destination)


if __name__ == '__main__':
    run()


"""
Usage:
    python3 redis_migrate.py '192.168.1.209:6379/3/lol' '192.168.1.209:6379/10/lol'
"""
