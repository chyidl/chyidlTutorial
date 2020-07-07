RPC Crash Course 
================
> RPC 可以像调用本地一样发起远程调用
```
分布式系统中的网络通信一般会采用四层TCP协议或者七层HTTP协

RPC: Remote Procedure Call 远程过程调用
  1. 屏蔽远程调用根本地调用的区别
  2. 隐藏底层网络通信的复杂性

RPC 通信流程:
  调用方:
    动态代理--序列化--编码-->网络--解码--反序列化-->动态代理 

  提供方:
    网络--解码-->解码-->反序列化--反射执行-->编码-->网络

利用RPC将应用架构从"单体"演进成"微服务化",解决系统耦合的问题
  MQ - 处理异步流程 
  Redis - 缓存热点数据 
  MySQL - 持久化数据 

RPC调用超时如何处理?
  重试机制、降级处理 
RPC调用是否考虑开启压缩?

接口设计兼容 
qps 

服务治理 

动态规划 

RPC/HTTP 属于应用层协议
  HTTP协议属于无状态协议
  RPC 不直接使用HTTP协议原因是无法实现请求跟相应关联
调用方需要维护消息ID列表，然后和返回结果中的消息ID做匹配

网络中传输都是二进制数据
RPC 负责应用间的通信,性能要求高,HTTP协议属于无状态协议

整个协议拆分成两部分：协议头+协议体
  协议头 + 协议体 
  协议头: 是由一堆固定长度参数组成[协议长度，序列化方式，协议标示，消息ID，消息类型]
  协议体: 请求接口方式，请求业务参数值，扩展属性(协议体里面都是经过序列化出来)

支持可扩展的协议:
  固定部分 + 协议头内容 + 协议体内容 
  Header中扩展字段 + Payload扩展字段 通过扩展字段向后兼容

支持协议体扩展 + 支持协议头扩展

网络传输的数据必须是二进制数据
  序列化: 就是将对象转换成二进制数据的过程 
  反序列化:就是反过来将二进制转换为对象的过程

Python:
  pickle: -- implemebts binary protocols for serilizing and de-serialzing a python object structure
  hmac: -- keyed hashing for message authentication
Java:
  ObjectOutputStream 
  ObjectInputStream 

头部数据用来声明序列化协议，序列化版本，用于高低版本向后兼容
任何一种序列化框架，核心思想就是设计一种序列化协议，将对象的类型、属性类型、属性值 -- 按照固定的格式写到二进制字节流完成序列化，再按照固定的格式独处对象的类型。属性类型，属性值，通过这些信息重新创建出一个新的对象，来完成反序列化.

  JSON: 是典型的Key-Value方式，没有数据类型，是一种文本型序列化框架
    - JSON进行序列化的额外空间开销比较大
    - JSON没有类型,需要通过反射解决
   
  Prootobuf: Google内部混合语言数据标准，是一种轻便、高校的结构化数据存储格式，可以用于结构化数据序列化
    - Protobuf使用需要定义IDL(Interface description language)使用不通过语言的IDL编译器生成序列化工具类
    - 序列化后体积相比JSON，小很多 
    - IDL能清晰描述语义，所以足以帮助并保证应用程序之间的类型不会丢失，无需类似XML解析器
    - 序列化反序列化速度快不需要通过反射获取类型
    - 消息格式升级和兼容性不错
序列化与反序列化过程是RPC调用的一个必须过程,序列化的二进制数据体积大小,序列化协议的通用性和兼容性
  安全性>通用性>兼容性>性能>效率>空间开销

RPC框架使用问题?
  1. 对象构造过于复杂: 对象复杂浪费性能，消耗CPU 
  2. 对象过于庞大: 映像请求耗时
  3. 使用序列化框架不支持的类作为入参类
  4. 对象有复杂的继承关系
RPC框架中使用尽量构建简单的对象作为入参和返回值对象
服务调用的稳定性与可靠性要比服务的性能与响应耗时更家重要
1. 对象尽量简单，没有太多的依赖关系，属性不要太多，尽量高内聚
2. 入参对象与返回值对象体积不要太大，

网络IO模型:
  RPC调用本质是服务消费者与服务提供者间的一次网络信息交换过程 
  1.同步阻塞IO (BIO)
    Blocking IO: 同步阻塞IO是最简单，最常见的IO模型，在Linux下，默认情况下所有的socket都是blocking的
    系统内核处理IO操作分为两个阶段，等待数据和拷贝数据
  2.同步非阻塞 IO (NIO)
  3.IO多路复用 -- Java NIO, Redis, Nginx 底层实现就是此类IO模型  
    Reactor模式: 
    当用户进程发起select调用，进程会被阻塞，当发现select负责的socket准备好的数据时才返回，之后才发起一次read
    IO Multiplexing: 多路复用是IO在高并发场景下使用最为广泛的一种IO模型
    复用器select: 用户可以在一个线程内同时处理多个socket的请求
  4.异步非阻塞IO (AIO) -- 异步IO

Reactor Design Pattern:
  wiki: The Reactor design pattern is an event handling pattern for handling service requests delivered concurrenclty by one or more inputs, The service handler then demultiplexes the incoming requests and dsipatches them synchronously to associated request handlers.

  Hollywood principle: -- Don't call us, we'll call you.

Reactor核心解决多请求问题，Thread-Per-Connection应用场景并发量不是特别大； Reactor通过多路复用的思想大大减少程序资源的使用.

Reactor 结构:
  1. Initiation Dispatcher:
    handle_events()  -- select(handlers) 
    register_handlers()
    remove_handlers()
  2. Even Handler: 定义事件处理的方法 
  3. Handle: 

多线程Reactor模式:
  mainReactor: 主要负责客户端的连接并将其传递给subReactor 

Reactor 优缺点:
  1. 大多数设计模式的共性，解耦、提升复用性、模块化、可移值性、事件驱动、细粒度并发控制 
  2. 显著的对性能的提升，不需要每个client对应一个线程、减少线程的使用 

网络IO应用需要系统内核支持以及编程语言的支持

系统内核处理IO操作分为两个阶段，等待数据和拷贝数据
  等待数据: 系统内核在等待网卡接收到数据
  拷贝数据: 系统内核在获取到数据后，将数据拷贝到用户进程空间

零拷贝(Zero-copy):
  > 取消用户空间与内核空间之间的数据拷贝操作;应用进程每次读写操作可以通过一种方式直接将数据写入内核或内核中读取数据，在通过DMA将内核中的数据拷贝到网卡，或将网卡中数据COPY到内核
  阻塞IO:系统内核处理IO操作分为两个阶段，等待数据和拷贝数据，等待数据就是系统在等待网卡接收到数据后，把数据写到内核中，而拷贝数据就是系统内核在获取到数据后，将数据拷贝到用户进程的空间中
  1. 应用进程的写操作，会将数据写到用户空间的缓冲区，再由CPU将数据拷贝到系统内核的缓冲区中，之后在由DMA将这份数据拷贝到网卡中,最后由网卡发送出去，而用户进程的读操作则是将流程反过来，数据同样会拷贝两次才能让应用程序读取数据
  零拷贝两种解决办法:
    > 通过虚拟内存解决
    1. mmap+write:  
    2. sendfile: 
  Netty:
    Nettey零拷贝为了解决用户空间对数据操作进行优化
    Netty提供CompositeByteBuf类 将多个ByteBuf合并为一个逻辑上的ByteBuf避免各个ByteBuf之间的拷贝
    Netty框架中内部ChannelHandler实现类，通过CompositeByteBuf,slice,wrap操作处理TCP传输中的拆包和粘包问题

动态代理:
  动态代理：统一拦截器 

通过动态代理屏蔽RPC调用细节，从而使用者能够面向接口编程 
RPC 支持跨语言，通信协议基于标准的HTTP/2设计，序列化支持PB(Protocol Buffer) 和 JSON 

Grpc 源码:
  > gRPC 是由Google开发开源的一款高性能、跨语言的RPC框架，通信协议基于标准的HTTP/2设计，序列化支持PB(Protocol Buffer) 和JSON
  
```
