gPRC - A high performance, open-source universal RPC framework
==============================================================
> gPRC is a modern open source high performance PRC framework that can run in any environment. It can efficiently connect services in and across data centers with pluggable support for load balancing, tracing, health checking and authentication. It is also applicable in last mile of distributed computing to connect devices, mobile applications and browsers to backend services.

RPC - Remote Procedure Call
---------------------------
> RPC框架目标是让远程服务调用更加简单、透明、RPC框架负责屏蔽底层的传输方式(TCP,UDP)、序列化方式(XML、JSON、二进制)和通信细节，服务调用者可以像调用本地接口一样调用远端的服务器提供者，不用关心底层通信和调用过程.

! [RPC 框架调用原理图](/imgs/raspberrypi/gRPC/RPC_Framework.png?raw=true)

* 主流RPC框架
    - 支持多语言的RPC框架 
        * Google - gRPC 
        * Apache (Facebook) - Thrift
    - 支持特定语言的RPC框架
        * Sina - Motan 
    - 支持服务治理服务化特征的分布式服务框架，底层内核仍然是RPC框架
        * Alibaba - Dubbo 
```
随着微服务的发展，基于语言中立性原则构建微服务，逐渐成为一种主流模式
    对于后端并发处理要求高的微服务 - 比较适合Go语言 
    对于前端的Web界面 - 适合Java和JavaScript 

gPRC特点:
    1. 支持多种语言
    2. 基于IDL文件定义服务，通过proto3工具生成指定语言的数据结构、服务端接口以及客户端Stub
    3. 通信协议基于标准的HTTP/2设计、支持双向流、消息头压缩、单TCP的多路复用、服务端推送，这些特性使得gPRC在移动端更加省电和节省网络流量
    4. 序列化支持PB(Protocol Buffer) 和 JSON, Protocol Buffer 是一种语言无关的高性能序列化框架，基于HTTP/2 + PB保障RPC调用的高性能
```

gRPC - Python 
-------------
* Prerequisites
```
$ python3 -m pip install --upgrade pip 
```

* Install gPRC
```
$ python3 -m pip install grpcio 
```

* Install gPRC tools 
> Python's gPRC tools include the protocol buffer compiler protoc and the special plugin for generating server and client code from .proto service definitions.
```
$ python3 -m pip install grpcio-tools 
```

* Download the example
```
# Clone the repository to get the example code:
$ git clone https://github.com/grpc/grpc.git
# Navigate to the "hello, world" Python example:
$ cd grpc/examples/python/helloworld
```

* Run a gRPC application 
```
1. Run the server 
$ python3 greeter_server.py 

2. In another terminal, Run the client 
$ python3 greeter_client.py 
```

* Update a gRPC service 
```
gRPC service is defined using protocol buffer

# 服务定义 (helloworld.proto)
package helloworld;

// The greeting service definition.
service Greeter {
  // Sends a greeting
  rpc SayHello (HelloRequest) returns (HelloReply) {}
}

// The request message containing the user's name.
message HelloRequest {
  string name = 1;
}

// The response message containing the greetings
message HelloReply {
  string message = 1;
}

# 服务端代码
```