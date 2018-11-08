#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Thread , we're solving the problem of blocking okay
# put yields into the code because the code might block
# you have concurrency in this with no threads using this weird generator
# try to drive this using a generator function
# Keep in mind about co-routines is that they are not like thread problems, but
# does not avoid the GIL problem, still limited to a CPU core one CPU core
# If you programming with co-rountines, It's basically all in like you have to
# go all co-routines all the way down and the problem
# people who program with co-routines still need to care about the global
# interpreter lock
# asyncio everything is a yield from -- co-routine
from socket import *
from fib import fib
from select import select # pull a whole bunch of sockets ay once
from collections import deque
#from concurrent.futures import ThreadPoolExecutor as Pool
from concurrent.futures import ProcessPoolExecutor as Pool


pool = Pool(4)
tasks = deque()

recv_wait = {} # Mapping sockets -> tasks (generator)
send_wait = {}
future_wait = {}


future_notify, future_event = socketpair()

# callback function
def future_done(future):
    tasks.append(future_wait.pop(future))
    future_notify.send(b'x')

def future_monitor():
    while True:
        yield 'recv', future_event
        future_event.recv(100)

tasks.append(future_monitor())


# task scheduling idea
def run():
    # run as long as there is any task anywhere
    while any([tasks, recv_wait, send_wait]):
        while not tasks:
            # No active tasks to run
            # wait for I/O
            # There's more overhead, I'm doing select
            # select loop that is actually the core of these event-driven
            can_recv, can_send, [] = select(recv_wait, send_wait, [])
            for s in can_recv:
                tasks.append(recv_wait.pop(s))
            for s in can_send:
                tasks.append(send_wait.pop(s))

        task = tasks.popleft()
        try:
            why, what = next(task) # Run to the yield
            # check for sort of the receiving and sending
            if why == 'recv':
                # Must go wait somewhere
                recv_wait[what] = task
            elif why == 'send':
                send_wait[what] = task
            elif why == 'future':
                future_wait[what] = task
                what.add_done_callback(future_done)
            else:
                raise RuntimeError('ARG!')
        except StopIteration:
            print("task done")


# make a class that essentially wraps around a socket object and
class AsyncSocket():
    def __init__(self, sock):
        self.sock = sock

    def recv(self, maxsize):
        yield 'recv', self.sock
        return self.sock.recv(maxsize)

    def send(self, data):
        yield 'send', self.sock
        return self.sock.send(data)

    def accept(self):
        yield 'recv', self.sock
        client, addr = self.sock.accept()
        return AsyncSocket(client), addr

    def __getattr__(self, name):
        return getattr(self.sock, name)


def fib_server(address):
    sock = AsyncSocket(socket(AF_INET, SOCK_STREAM))
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        # this is the new Python3 using yield from like a sub generator
        client, addr = yield from sock.accept()        # blocking
        print("Connection", addr)
        tasks.append(fib_handler(client))

# Only handle one client at a time
def fib_handler(client):
    while True:
        req = yield from client.recv(1024)             # blocking
        if not req:
            break
        n = int(req)
        future = pool.submit(fib, n)
        yield 'future', future
        result = future.result()            # This operation here blocks
        resp = str(result).encode('ascii') + b'\n'
        yield from client.send(resp)                   # blocking
    print('Closed')


# make the thing run
tasks.append(fib_server(('', 25000)))
run()
