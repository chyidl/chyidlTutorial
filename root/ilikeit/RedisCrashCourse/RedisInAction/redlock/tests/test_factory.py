#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:encoding=utf-8
#
# test_factory.py
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
# Created by Chyi Yaqing on 03/16/19 20:04.
# Copyright © 2019. Chyi Yaqing. All rights reserved.
#
# Distributed under terms of the MIT
from redlock import RedLockFactory


def test_factory_create():
    factory = RedLockFactory([{"host": "localhost"}])

    lock = factory.create_lock(
        "test_factory_create",
        ttl=500,
        retry_times=5,
        retry_delay=100,
    )

    assert factory.redis_nodes == lock.redis_nodes
    assert factory.quorum == lock.quorum
    assert lock.ttl == 500
    assert lock.retry_times == 5
    assert lock.retry_delay == 100
    assert lock.factory == factory


def test_factory_create_from_url():
    factory = RedLockFactory([{"url": "redis://localhost/0"}])

    lock = factory.create_lock(
        "test_factory_create_from_url", ttl=500, retry_times=5, retry_delay=100
    )

    assert factory.redis_nodes == lock.redis_nodes
    assert factory.quorum == lock.quorum
    assert lock.ttl == 500
    assert lock.retry_times == 5
    assert lock.retry_delay == 100
    assert lock.factory == factory