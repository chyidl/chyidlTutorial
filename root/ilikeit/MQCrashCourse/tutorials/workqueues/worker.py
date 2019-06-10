#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
worker.py will receive messages from the queue and needs to fake a second of work for every dot in the message body.
It will pop message from the queue and perform the task
"""
# Pika is a pure-Python implementation of the AMQP 0-9-1 protocol
import pika
import time


# guest user can only connect via localhost
#credentials = pika.PlainCredentials('guest', 'guest')
credentials = pika.PlainCredentials('pi', 'macintosh')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.31.156',
                                                               port=5672,
                                                               virtual_host='/',
                                                               credentials=credentials))
channel = connection.channel()
# it's a good practice to repeat declaring the queue in both programs.
channel.queue_declare(queue='hello')


# Whenever we receive a message, this callback function is called by the Pika library
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")


# tell RabbitMQ that this particular callback function should receive messages from our hello queue.
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

# never-ending loop that waits for data and runs callback whenever necessary
print(' [*] Waiting for message. To exit press CTRL+C')
channel.start_consuming()

"""
By default, RabbitMQ will send each message to the next consumer, in sequence. On average every consumer will get the 
This way of distributing messages is called round-robin [♻️循环调度]
"""