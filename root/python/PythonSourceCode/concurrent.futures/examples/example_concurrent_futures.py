#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#                ____
#               / . .\
# Life is short \  ---<
# I use Python   \  /
#      __________/ /
#   -=:___________/
# example_concurrent_futures.py
# concurrent.futures
#
# Created by Chyi Yaqing on 05/24/19 14:00.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the MIT
"""
concurrent.futures -- Manage Pools Launching parallel tasks

The concurrent.futures module provides a high-level interface for
asynchronously executing callables.

    ThreadPoolExecutor: thread
    ProcessPoolExecutor: process

Thread, Process Both implement the same interface, which is defined by the
abstract Executor class.

The module provides two types of classes for interacting with the pools:
    Executors: are used for managing pools of workers.
    Futures: are used for managing results computed by the workers.
"""
