#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
receive.py will receive messages from the queue and print them on the screen.
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
# it's a good practice to repeat declaring the queue in both programs.
channel.queue_declare(queue='hello')


# Whenever we receive a message, this callback function is called by the Pika library
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


# tell RabbitMQ that this particular callback function should receive messages from our hello queue.
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

# never-ending loop that waits for data and runs callback whenever necessary
print(' [*] Waiting for message. To exit press CTRL+C')
channel.start_consuming()

# receive.py program doesn't exit. It will stay ready to receive further messages, and may be interrupted with Ctrl-C
