#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Downloads Neural Networks for Machine Learning course video
# url: https://www.cs.toronto.edu/~hinton/coursera_lectures.html
from requests_html import HTMLSession
from threading import Thread
import threading
import os, sys
import time
import datetime
import logging
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


def downloadfile(logger, absUrl):
    """
    :param logger
    :param absUrl:  url
    :return:
    """
    video_name = absUrl.split('/')[-1]

    # imported the requests library
    import requests

    logger.info("{}: Downloading file: {}".format(threading.get_ident(), video_name))

    # download the url contents in binary format
    r = requests.get(absUrl)

    # open method to open a file on your system and write the contents
    with open(video_name, 'wb') as f:
        f.write(r.content)
    logger.info("{}: Downloaded file: {}".format(threading.get_ident(), video_name))


if __name__ == '__main__':
    logger = SingletonLogger.__call__().get_logger()
    url = 'https://www.cs.toronto.edu/~hinton/coursera_lectures.html'
    session = HTMLSession()

    r = session.get(url)
    videos_links = r.html.absolute_links

    start = time.time()
    pool = ThreadPool()
    for i, url in enumerate(sorted(videos_links)):
        pool.add_task(downloadfile, logger, url)

    end = pool.wait_completetion()
    logger.info("All consuming {} sec".format(end - start))
