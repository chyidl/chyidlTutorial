#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
new_task.py to allow arbitrary messages to be sent from the command line. This program will schedule tasks to our work queue.

The main idea behind Work Queues is to avoid doing a resource-intensive task immediately and having to wait for it to complete.
Instead we schedule the task to be done later. We encapsulate a task as a message and send it to the queue. A worker
processer running in the background will pop the tasks and eventually execute the job. When you run many works the tasks
will be shared between them.

This concept is especially useful in web applications where it's impossible to handle a complex task during a short HTTP request window
"""
# Pika is a pure-Python implementation of the AMQP 0-9-1 protocol
import pika
import sys


# guest user can only connect via localhost
#credentials = pika.PlainCredentials('guest', 'guest')
credentials = pika.PlainCredentials('pi', 'macintosh')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.31.156',
                                                               port=5672,
                                                               virtual_host='/',
                                                               credentials=credentials))
channel = connection.channel()

# make sure that RabbitMQ will never lose our queue.
# RabbitMQ doesn't allow redefine an existing queue with different parameters and will return an error to any program that tries to do that.
channel.queue_declare(queue='task_queue', durable=True)
message = ' '.join(sys.argv[1:]) or "Hello World!"

# make our message as persistent - by supplying a delivery_mode property with a value 2
# default exchange, which we identify by the empty string("")
channel.basic_publish(exchange='',
                      routing_key='task_queue', # the queue name
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2, # make message persistent
                      ))
print("[x] Sent 'Hello World!'")
connection.close()

"""
Please keep in mind that this and other tutorials are, well, tutorials, They demonstrate one new concept at a time and may
intentionally oversimplify some things and leave out others. For example topics such as connection management, error handling,
connection recovery, concurrency and metric collection are largely omitted for the sake of brevity. Such simplified code 
should not be considered production ready.

Note on message persistence
    Making messages as persistent doesn't fully guarantee that a message won't be lost. Although it tells RabbitMQ to save
    the message and hasn't saved it yet. Also, RabbitMQ doesn't do fsync(2) [synchronize a file's in-core state with storage device] 
    for every message it may be just saved to cache and not really written to the disk.
"""