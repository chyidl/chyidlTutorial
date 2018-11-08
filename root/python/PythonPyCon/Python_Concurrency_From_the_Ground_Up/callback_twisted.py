#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from twisted.internet import reactor, protocol


class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)


def main(port):
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(port, factory)
    reactor.run()
