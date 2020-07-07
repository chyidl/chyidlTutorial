# Copyright 2020 gRPC authors.
from concurrent import futures
import logging
import grpc
from pb import helloworld_pb2 as pb2
from pb import helloworld_pb2_grpc as pb2_grpc


class Greeter(pb2_grpc.GreeterServicer):

    def SayHello(self, request, context):
        print(f"{request.name} send request")
        return pb2.SayHelloResponse(message="Hello, %s!" %request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
