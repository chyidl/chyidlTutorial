#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import logging
import os, sys
import datetime
from threading import Thread
from queue import Queue


class SingletonType(type):
    """type is the usual metaclass in Python"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# Syntax sugar:
_ver = sys.version_info

#: Python 2.x?
is_py2 = (_ver[0] == 2)

#: python3.x?
is_py3 = (_ver[0] == 3)

if is_py3:
    # python 3 style
    class SingletonLogger(object, metaclass=SingletonType):
        # __metaclass__ = SingletonType   # python 2 Style
        _logger = None

        def __init__(self):
            self._logger = logging.getLogger("dobby.logger")
            self._logger.setLevel(logging.DEBUG)
            formatter = logging.Formatter('%(asctime)s \t [%(levelname)s | %(filename)s:%(lineno)s] > %(message)s')
            now = datetime.datetime.now()
            dirname = "./log"
            if not os.path.isdir(dirname):
                os.mkdir(dirname)
            fileHandler = logging.FileHandler(dirname + "/log_" + now.strftime("%Y-%m-%d") + ".log")
            streamHandler = logging.StreamHandler()
            fileHandler.setFormatter(formatter)
            streamHandler.setFormatter(formatter)
            self._logger.addHandler(fileHandler)
            self._logger.addHandler(streamHandler)

            print("Generate new instance")

        def get_logger(self):
            return self._logger

elif is_py2:
    pass

######################################################################
# Multi-threading Test
######################################################################


class ThreadWorker(Thread):
    """Thread executing tasks from a given tasks queue."""
    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        """For each get() used to fetch a task, a subsequent call to task_done() tells
        the queue that the processing on the task in complete.
        """
        while True:
            func, args, kwargs = self.tasks.get()
            try:
                func(*args, **kwargs)
            except Exception as error:
                print(error)
            self.tasks.task_done()


class ThreadPool:
    """Pool of threads consuming tasks from a queue"""
    def __init__(self, num_threads=os.cpu_count()*2):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads):
            ThreadWorker(self.tasks)

    def add_task(self, func, *args, **kwargs):
        """add a task to the queue"""
        self.tasks.put((func, args, kwargs))

    def wait_completetion(self):
        """Wait for completion of all the tasks in the queue"""
        self.tasks.join()
        return time.time()


if __name__ == '__main__':
    # Test
    logger1 = SingletonLogger.__call__().get_logger()
    logger2 = SingletonLogger.__call__().get_logger()
    logger1.info("Logger1, Hello, logger")
    logger2.info("Logger2, Hello, logger")

    # Multi-threading Test
    import time
    import threading
    import random

    start = time.time()

    def wait_delay(delay):
        logger = SingletonLogger.__call__().get_logger()
        print("sleeping for (%d)sec" %delay)
        logger.info("{} : sleeping for {} sec".format(threading.get_ident(), delay))
        time.sleep(delay)

    delays = [random.randrange(1,10) for i in range(30)]

    pool = ThreadPool()
    for i, d in enumerate(delays):
        pool.add_task(wait_delay, d)

    end = pool.wait_completetion()
    logger1.info("All consuming {} sec".format(end-start))
