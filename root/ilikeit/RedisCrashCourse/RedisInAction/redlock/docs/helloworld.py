#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:encoding=utf-8
#
# helloworld.py
# docs
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
# Created by Chyi Yaqing on 03/16/19 20:12.
# Copyright © 2019. Chyi Yaqing. All rights reserved.
#
# Distributed under terms of the MIT
"""
Basic Usage
"""
import os
import time
from redlock import RedLock


# get the string environment
env_dist = os.environ
redis_password = env_dist.get('REMOTE_REDIS_PASSWORD')
with RedLock("distributed_lock",
             connection_details=[
                 # master 1
                 {'host': '192.168.31.156', 'port': 6379, 'db': 0, 'password': redis_password},
                 # master 2
                 {'host': '192.168.31.39', 'port': 6379, 'db': 0, 'password': redis_password},
             ]):
    time.sleep(10)
    print('Hello World')
