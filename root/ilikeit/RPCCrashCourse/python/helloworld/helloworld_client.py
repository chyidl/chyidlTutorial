# Copyright 2020 gRPC authors.
#
from __future__ import print_function
import logging
import grpc
import os
from pb import helloworld_pb2 as pb2
from pb import helloworld_pb2_grpc as pb2_grpc
from grpc_retry import retrying_stub_methods


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pb2_grpc.GreeterStub(channel)
        # os.setenv('GRPC_RETRY_UNAVAILABLE', 5)
        # os.setenv('GRPC_RETRY_DEADLINE_EXCEEDED', 4)
        retrying_stub_methods(stub)
        response = stub.SayHello(pb2.SayHelloRequest(name='you'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
