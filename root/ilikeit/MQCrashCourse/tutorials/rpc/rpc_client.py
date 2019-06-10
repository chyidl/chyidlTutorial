#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
rpc_client.py
"""
# Pika is a pure-Python implementation of the AMQP 0-9-1 protocol
import pika
import uuid


class FibonacciRpcClient():
    def __init__(self):
        # guest user can only connect via localhost
        #credentials = pika.PlainCredentials('guest', 'guest')
        credentials = pika.PlainCredentials('pi', 'macintosh')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.31.156',
                                                                       port=5672,
                                                                       virtual_host='/',
                                                                       credentials=credentials))
        self.channel = self.connection.channel()
        result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = result.method.queue
        self.channel.basic_consume(self.on_response,
                                   no_ack=True,
                                   queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        """actual RPC request"""
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                       reply_to=self.callback_queue,
                                       correlation_id=self.corr_id,
                                   ),
                                   body=str(n))
        while self.response is None:
            self.connection.process_data_events()
        return int(self.response)


if __name__ == '__main__':
    fibonacci_rpc = FibonacciRpcClient()
    print(' [x] Requesting fib(30)')
    response = fibonacci_rpc.call(30)
    print(" [.] Got %r" % response)
"""
Please keep in mind that this and other tutorials are, well, tutorials, They demonstrate one new concept at a time and may
intentionally oversimplify some things and leave out others. For example topics such as connection management, error handling,
connection recovery, concurrency and metric collection are largely omitted for the sake of brevity. Such simplified code 
should not be considered production ready.

"""