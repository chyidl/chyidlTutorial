#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# test_lock.py
# tests
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
# Created by Chyi Yaqing on 03/16/19 15:22.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the MIT

"""
"""
import unittest
from redlock import RedLock, ReentrantRedLock, RedLockError
from redlock.lock import CLOCK_DRIFT_FACTOR
import mock
import time


def test_default_connection_details_value():
    """
    Test that RedLock instance could be created with
    default value of `connection_details` argument.
    """
    RedLock("test_simple_lock")


def test_simple_lock():
    'Test a RedLock can be acquired.'
    lock = RedLock("test_simple_lock", [{"host": "localhost"}], ttl=1000)
    locked = lock.acquire()
    lock.release()
    lock.release()
    assert locked is True


