#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
send.py will send a single messages to the queue.
"""
# Pika is a pure-Python implementation of the AMQP 0-9-1 protocol
import pika


# guest user can only connect via localhost
#credentials = pika.PlainCredentials('guest', 'guest')
credentials = pika.PlainCredentials('pi', 'macintosh')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.31.156',
                                                               port=5672,
                                                               virtual_host='/',
                                                               credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print("[x] Sent 'Hello World!'")
connection.close()

"""
Please keep in mind that this and other tutorials are, well, tutorials, They demonstrate one new concept at a time and may
intentionally oversimplify some things and leave out others. For example topics such as connection management, error handling,
connection recovery, concurrency and metric collection are largely omitted for the sake of brevity. Such simplified code 
should not be considered production ready.
"""