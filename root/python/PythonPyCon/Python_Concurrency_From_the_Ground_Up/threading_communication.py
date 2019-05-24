#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#                ____
#               / . .\
# Life is short \  ---<
# I use Python   \  /
#      __________/ /
#   -=:___________/
# threading_communication.py
# Python_Concurrency_From_the_Ground_Up
#
# Created by Chyi Yaqing on 05/23/19 18:46.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the MIT
"""
Python threads: communication and stopping
    1. How to stop / kill a thread
    2. How to safely pass data to a thread and back

Here's a sample "worker" thread implementation. It can be given tasks,
where each task is a directory name, and it does useful work. This work is
recursively listing all the files contained in the given directory and
its sub-directories
"""
import os
import time
import threading
from queue import Queue


class WorkerThread(threading.Thread):
    """A worker thread that takes"""
