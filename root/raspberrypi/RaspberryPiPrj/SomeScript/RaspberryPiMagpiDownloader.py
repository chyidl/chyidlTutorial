#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# >>Copyright 2018- chyidl (@Chyi Yaqing)
"""

"""
import requests
import bs4 as bs    # web scraping with Beautiful Soup
import time
from functools import wraps
import multiprocessing
from queue import Queue         # Constructor for a FIFO queue.
from threading import Thread


def timed(func):
	"""This decorator prints the execution time for the decorated function"""
	@wraps(func)
	def wrapper(*args, **kwargs):
		start = time.time()
		result = func(*args, **kwargs)
		end = time.time()
		print("[{}] run in {}s".format(func.__name__, round(end-start, 2)))
		return result
	return wrapper

def downloadPdf(file):
	print("Beginning file download with requests, [{}], by [{}]".format(file, multiprocessing.current_process()))
	url = "https://www.raspberrypi.org/magpi-issues/{}".format(file)
	r = requests.get(url)
	with open('MagiPi/{}'.format(file), 'wb') as f:
		f.write(r.content)

	# Retrieve HTTP meta-data
	print(r.url)
	print(r.status_code)
	print(r.headers['content-type'])
	print(r.encoding)

# ------------------------ MultiProcessing -------------------------#

@timed
def useMultiPool():
	with multiprocessing.Pool(10) as p:
		print(p.map(downloadPdf, range(1,72)))


# ------------------------- Thread pool --------------------------#

class Worker(Thread):
	"""Thread executing tasks from a given tasks queue"""
	def __init__(self, tasks):
		Thread.__init__(self)
		self.tasks = tasks
		self.daemon = True
		self.start()

	def run(self):
		while True:
			func, args, kwargs = self.tasks.get()
			try:
				func(*args, **kwargs)
			except Exception as err:
				print(err)
			finally:
				self.tasks.task_done()

class ThreadPool:
	"""Pool of threads consuming tasks from a queue"""
	def __init__(self, num_threads):
		self.tasks = Queue(num_threads)
		for _ in range(num_threads):
			Worker(self.tasks)

	def add_task(self, func, *args, **kwargs):
		"""Add a task to the queue"""
		self.tasks.put((func, args, kwargs))

	def wait_completion(self):
		"""wait for completion of all the tasks in the queue"""
		self.tasks.join()

@timed
def useThreadPool(tasks):
	pool = ThreadPool(multiprocessing.cpu_count()*2)
	for task in tasks:
		pool.add_task(downloadPdf, task)
	pool.wait_completion()


def get_table_from_url(url=""):

	rst = [] # 最终结果集

	# Create a handle, page, to handle the contents of the website
	source = requests.get(url)
	soup = bs.BeautifulSoup(source.content,'lxml')
	table = soup.find('table')

	# find the table rows within the table
	table_rows = table.find_all('tr')

	# iterate through the rows, find the th tags,and then print out each of the table data tags
	for tr in table_rows:
		td = tr.find_all('td')
		row = [i.text for i in td]
		try:
			if row and len(row)==5 and '.pdf' in row[1]:
				rst.append(row[1])
		except:
			continue
	return rst



if __name__ == '__main__':

	#useMultiPool() # MultiProcessing   多进程
	#useThreadPool() # MultiThreading   多线程

	# Download MagPi all history PDF Save to Folder MagPi/
	url="https://www.raspberrypi.org/magpi-issues"
	rst = get_table_from_url(url)
	useThreadPool(rst)

