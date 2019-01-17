#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Simple socket client thread smaple
"""
1. Doing the I/O in a separate thread
2. Using asynchronous I/O with callbacks integrated into the GUI event loop
"""
import socket
# struct -- Interpret bytes as packed binary data
import struct
import threading
# queue -- A synchronized queue class
# Queue is a great biggest difficulty in writing multi-threaded programs is protecting shared data.
import queue  # FIFO


class ClientCommand():
    """ A command to the client thread.
    Each command type has its associated data:

    CONNECT:    (host, port) tuple
    SEND:       Data string
    RECEIVE:    None
    CLOSE:      None
    """
    CONNECT, SEND, RECEIVE, CLOSE = range(4)

    def __init__(self, type, data=None):
        self.type = type
        self.data = data


class ClientReply():
    """
    A replay from the client thread.
    Each reply type has its associated data:

    ERROR:      The error string
    SUCCESS:    Depends on the command - for RECEIVE it's the received
                data string, for others None.
    """
    ERROR, SUCCESS = range(2)

    def __init__(self, type, data=None):
        self.type = type
        self.data = data


class SocketClientThread(threading.Thread):
    """Implements the threading.Thread interface (start, join, etc.) and
        can be controlled via the cmd_q Queue attribute. Replies are
        placed in the replay_q Queue attribute."""
    def __init__(self, cmd_q=None, reply_q=None):
        super(SocketClientThread, self).__init__()
        self.cmd_q = cmd_q or queue.Queue()
        self.reply_q = reply_q or queue.Queue()
        # This is one of the simplest mechanisms for communication between threads: one thread signals an event and other thread wait for it.
        # set() to True, clear() to False. wait() to block until true.
        # a thread-safe flag
        self.alive = threading.Event()
        self.alive.set()
        self.socket = None

        self.handlers = {
            ClientCommand.CONNECT: self._handle_CONNECT,
            ClientCommand.CLOSE: self._handle_CLOSE,
            ClientCommand.SEND: self._handle_SEND,
            ClientCommand.RECEIVE: self._handle_RECEIVE,
        }

    def run(self):
        while self.alive.isSet():
            try:
                # Queue.get with timeout to allow checking self.alive
                cmd = self.cmd_q.get(block=True, timeout=0.1)
                self.handlers[cmd.type](cmd)
            except queue.Empty as e:
                continue

    def join(self, timeout=None):
        self.alive.clear()
        threading.Thread.join(self, timeout)

    def _handle_CONNECT(self, cmd):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((cmd.data[0], cmd.data[1]))
            self.reply_q.put(self._success_reply())
        except IOError as e:
            self.reply_q.put(self._error_reply(str(e)))

    def _handle_CLOSE(self, cmd):
        self.socket.close()
        reply = ClientReply(ClientReply.SUCCESS)
        self.reply_q.put(reply)

    def _handle_SEND(self, cmd):
        # Using the length prefix technique
        # < : little-endian L: unsigned long integer(4)
        header = struct.pack('<L', len(cmd.data))
        try:
            self.socket.sendall(header + cmd.data.encode())
            self.reply_q.put(self._success_reply())
        except IOError as e:
            self.reply_q.put(self._error_reply(str(e)))

    def _handle_RECEIVE(self, cmd):
        try:
            header_data = self._recv_n_bytes(4)
            if len(header_data) == 4:
                msg_len = struct.unpack('<L', header_data)[0]
                data = self._recv_n_bytes(msg_len)
                if len(data) == msg_len:
                    self.reply_q.put(self._success_reply(data))
                    return
            self.reply_q.put(self._error_reply('Socket closed prematurely'))
        except IOError as e:
            self.reply_q.put(self._error_reply(str(e)))

    def _recv_n_bytes(self, n):
        """Convenience method for receiving exactly n bytes from
            self.socket (assuming it's open and connected)
        """
        data = b''
        while len(data) < n:
            chunk = self.socket.recv(n - len(data))
            if chunk == '':
                break
            data += chunk
        return data

    def _error_reply(self, errstr):
        return ClientReply(ClientReply.ERROR, errstr)

    def _success_reply(self, data=None):
        return ClientReply(ClientReply.SUCCESS, data)


#-------------------------------------------------------------------#
if __name__ == '__main__':
    sct = SocketClientThread()
    sct.start()
    sct.cmd_q.put(ClientCommand(ClientCommand.CONNECT, ('localhost', 50007)))
    reply = sct.reply_q.get(True)
    print(reply.type, reply.data)
    sct.cmd_q.put(ClientCommand(ClientCommand.SEND, "hellothere"))
    reply = sct.reply_q.get(True)
    print(reply.type, reply.data)
    sct.cmd_q.put(ClientCommand(ClientCommand.RECEIVE, "hellothere"))
    reply = sct.reply_q.get(True)
    print(reply.type, reply.data)
    sct.cmd_q.put(ClientCommand(ClientCommand.CLOSE))
    reply = sct.reply_q.get(True)
    print(reply.type, reply.data)