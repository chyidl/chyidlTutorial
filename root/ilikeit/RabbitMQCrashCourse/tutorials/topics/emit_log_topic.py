#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
emit_log_topic.py using topic exchange in our logging system. start off with a working assumption that the routing keys of logs will have two words
'<facility>.<severity>'
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
channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 1 else '.anonymous.info'
message = ' '.join(sys.argv[2:]) or "Hello World!"

channel.basic_publish(exchange='topic_logs',
                      routing_key=routing_key,
                      body=message)

print("[x] Sent %r:%r" %(routing_key, message))
connection.close()

"""
Please keep in mind that this and other tutorials are, well, tutorials, They demonstrate one new concept at a time and may
intentionally oversimplify some things and leave out others. For example topics such as connection management, error handling,
connection recovery, concurrency and metric collection are largely omitted for the sake of brevity. Such simplified code 
should not be considered production ready.

"""