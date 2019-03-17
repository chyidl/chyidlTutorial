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
from redlock import RedLock, ReentrantRedLock, RedLockError
from redlock.lock import CLOCK_DRIFT_FACTOR
import mock
import time
import unittest


def test_default_connection_details_value():
    """
    Test that RedLock instance could be created with
    default value of `connection_details` argument.
    """
    RedLock("test_simple_lock")


def test_simple_lock():
    """
    Test a RedLock can be acquired.
    """
    lock = RedLock("test_simple_lock", [{"host": "localhost"}], ttl=1000)
    locked = lock.acquire()
    lock.release()
    assert locked is True


def test_lock_is_locked():
    lock = RedLock("test_lock_is_locked")
    # Clear possible initial states
    [node.delete(lock.resource) for node in lock.redis_nodes]

    assert lock.locked() is False

    lock.acquire()
    assert lock.locked() is True

    lock.release()
    assert lock.locked() is False


def test_locked_span_lock_instances():
    lock1 = RedLock("test_locked_span_lock_instances")
    lock2 = RedLock("test_locked_span_lock_instances")
    # Clear possible initial states
    [node.delete(lock1.resource) for node in lock1.redis_nodes]

    assert lock1.locked() == lock2.locked() is False
    lock1.acquire()

    assert lock1.locked() == lock2.locked() is True

    lock1.release()
    assert lock1.locked() == lock2.locked() is False


def test_lock_with_validity():
    """
    Test a RedLock can be acquired and the lock validity is also retruned.
    """
    ttl = 1000
    lock = RedLock("test_simple_lock", [{"host": "localhost"}], ttl=ttl)
    locked, validity = lock.acquire_with_validity()
    lock.release()
    assert locked is True
    assert 0 < validity < ttl - ttl * CLOCK_DRIFT_FACTOR - 2


def test_from_url():
    """
    Test a RedLock can be acquired via from_url.
    """
    lock = RedLock("test_from_url", [{"url": "redis://localhost/0"}], ttl=1000)
    locked = lock.acquire()
    lock.release()
    assert locked is True


def test_context_manager():
    """
    Test a RedLock can be released by the context manager automically.
    """
    ttl = 1000
    with RedLock("test_context_manager", [{"host": "localhost"}], ttl=ttl) as validity:
        assert 0 < validity < ttl - ttl * CLOCK_DRIFT_FACTOR - 2
        lock = RedLock("test_context_manager", [{"host": "localhost"}], ttl=ttl)
        locked = lock.acquire()
        assert locked is False

    lock = RedLock("test_context_manager", [{"host": "localhost"}], ttl=ttl)
    locked = lock.acquire()
    assert locked is True

    # try to lock again within a with block
    try:
        with RedLock("test_context_manager", [{"host": "localhost"}]):
            # shouldn't be allowed since someone has the lock already
            assert False
    except RedLockError:
        # we expect this call to error out
        pass

    lock.release()


def test_fail_to_lock_acquired():
    lock1 = RedLock("test_fail_to_lock_acquired", [{"host": "localhost"}], ttl=1000)
    lock2 = RedLock("test_fail_to_lock_acquired", [{"host": "localhost"}], ttl=1000)

    lock1_locked = lock1.acquire()
    lock2_locked = lock2.acquire()
    lock1.release()

    assert lock1_locked is True
    assert lock2_locked is False


def test_lock_expire():
    lock1 = RedLock("test_lock_expire", [{"host": "localhost"}], ttl=500)
    lock1.acquire()
    time.sleep(1)

    # Now lock1 has expired, we can accquire a lock
    lock2 = RedLock("test_lock_expire", [{"host": "localhost"}], ttl=1000)
    locked = lock2.acquire()
    assert locked is True

    lock1.release()
    lock3 = RedLock("test_lock_expire", [{"host": "localhost"}], ttl=1000)
    locked = lock3.acquire()
    assert locked is False


class TestLock(unittest.TestCase):
    def setUp(self):
        super(TestLock, self).setUp()
        self.redlock = mock.patch.object(RedLock, '__init__', return_value=None).start()
        self.redlock_acquire = mock.patch.object(RedLock, 'acquire').start()
        self.redlock_release = mock.patch.object(RedLock, 'release').start()
        self.redlock_acquire.return_value = True

    def tearDown(self):
        mock.patch.stopall()

    def test_passthrough(self):
        test_lock = ReentrantRedLock('')
        test_lock.acquire()
        test_lock.release()

        self.redlock.assert_called_once_with('')
        self.redlock_acquire.assert_called_once_with()
        self.redlock_release.assert_called_once_with()

    def test_reentrant(self):
        test_lock = ReentrantRedLock('')
        test_lock.acquire()
        test_lock.acquire()
        test_lock.release()
        test_lock.release()

        self.redlock.assert_called_once_with('')
        self.redlock_acquire.assert_called_once_with()
        self.redlock_release.assert_called_once_with()

    def test_reentrant_n(self):
        test_lock = ReentrantRedLock('')
        for _ in range(10):
            test_lock.acquire()
        for _ in range(10):
            test_lock.release()

        self.redlock.assert_called_once_with('')
        self.redlock_acquire.assert_called_once_with()
        self.redlock_release.assert_called_once_with()

    def test_no_release(self):
        test_lock = ReentrantRedLock('')
        test_lock.acquire()
        test_lock.acquire()
        test_lock.release()

        self.redlock.assert_called_once_with('')
        self.redlock_acquire.assert_called_once_with()
        self.redlock_release.assert_not_called()


def test_lock_with_multi_backend():
    """
    Test a RedLock can be acquired when at least N/2+1 redis instances are alive.
    Set redis instance with port 6380 down or debug sleep during test.
    """
    lock = RedLock("test_simple_lock", connection_details=[
        {"host": "localhost", "port": 6379, "db": 0, "socket_timeout": 0.2},
        {"host": "localhost", "port": 6379, "db": 1, "socket_timeout": 0.2},
        {"host": "localhost", "port": 6380, "db": 0, "socket_timeout": 0.2}], ttl=1000)
    locked = lock.acquire()
    lock.release()
    assert locked is True