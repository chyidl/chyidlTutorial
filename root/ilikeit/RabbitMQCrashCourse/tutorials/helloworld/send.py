#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pika

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.82.56',
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