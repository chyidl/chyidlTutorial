#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
receive_logs.py published log messages are going to be broadcast to all the receives
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
# declare the exchange
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs',
                   queue=queue_name)

print(" [*] Waiting for logs. To exit press CTRL+C")


def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(callback,
                      queue = queue_name,
                      no_ack = True)

channel.start_consuming()
"""
Please keep in mind that this and other tutorials are, well, tutorials, They demonstrate one new concept at a time and may
intentionally oversimplify some things and leave out others. For example topics such as connection management, error handling,
connection recovery, concurrency and metric collection are largely omitted for the sake of brevity. Such simplified code 
should not be considered production ready.

"""