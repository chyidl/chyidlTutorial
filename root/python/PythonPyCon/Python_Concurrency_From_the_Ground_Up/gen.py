#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# use yield to blocking idea
# Python actually does (generator function) have a feature that blocks like that
from collections import deque


tasks = deque()


def countdown(n):
    while n > 0:
        # yield statement essentially make the function stop until you call next
        yield n
        n -= 1


# task scheduler
# round-robin scheduler
def run():
    while tasks:
        task = tasks.popleft()
        try:
            x = next(task) # Run to the yield
            print(x)
            tasks.append(task)
        except StopIteration:
            print("Task")


for i in countdown(5):
    print(i)

# put a bunch of generator functions on there
tasks.extend([countdown(10), countdown(5), countdown(20)])

run()
