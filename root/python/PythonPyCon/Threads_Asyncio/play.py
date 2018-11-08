#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# completely different version of asyncio
from types import coroutine
from collections import deque
# This is the core asyncio, it's the way of watching socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE


@coroutine
def read_wait(sock):
    # generator function
    yield 'read_wait', sock


@coroutine
def write_wait(sock):
    yield 'write_wait', sock


class Loop:
    def __init__(self):
        self.ready = deque()
        self.selector = DefaultSelector()

    async def sock_recv(self, sock, maxbytes):
        # wait for something to happen
        await read_wait(sock)
        return sock.recv(maxbytes)

    async def sock_accept(self, sock):
        # wait for something to happen
        await read_wait(sock)
        return sock.accept()

    async def sock_sendall(self, sock, data):
        while data:
            await write_wait(sock)
            nsent = sock.send(data)
            data = data[nsent:]

    def create_task(self, coro):
        self.ready.append(coro)

    def run_forever(self):
        while True:
            while not self.ready:
                # if there's not nothing to ready to run, go get all IO
                events = self.selector.select()
                for key, _ in events:
                    self.ready.append(key.data)
                    self.selector.unregister(key.fileobj)

            while self.ready:
                self.current_task = self.ready.popleft()
                try:
                    op, *args = self.current_task.send(None) # Run to the yield
                    getattr(self, op)(*args)    # Sneaky method
                except StopIteration:
                    pass

    def read_wait(self, sock):
        # the current task is interested in reading on that socket
        self.selector.register(sock, EVENT_READ, self.current_task)

    def write_wait(self, sock):
        # the current task is intertested in writing on that socket
        self.selector.register(sock, EVENT_WRITE, self.current_task)
