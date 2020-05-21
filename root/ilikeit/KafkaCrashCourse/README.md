Kafka Crash Course
==================
> Apache Kafka is a popular distributed message broker designed to efficiently handle large volumes of real-time data. A Kafka cluster is not only highly scalable and fault-tolerant, but it also has a much higher through compared to other message brokers such as ActiveMQ and RabbitMQ.
> Kafka achieves high-throughput, low-latency, durability, and near-limitless scalability by maintaining a distributed system based on commit logs, delegating key responsibility to clients, optimizing for batches and allowing for multiple concurrent consumers per message. 

* Brokers:
  * Kafka is maintained as clusters where each node within a cluster is called a Broker.
  * Each Kafka cluster wil designate one of the brokers as the Controller which is responsible for managing and maintaining the overall health of a cluster, in addition to the basic broker responsibilities.

* Topics:
  * As a publish-subscribe messaging system, Kafka uses uniquely named Topics to deliver feeds of messages from producers to consumers.
  * Topics parallelize data for greater read/write performance by partitioning and distributing the data across multiple brokers.
  * Topics retain messages for a configurable amount of time or until a storage size is exceeded.

* Records:
  * Records are messages that contain a key/value pair along with metadata such as a timestamp and message key. 
  * A message can have a maximum size of 1MB by default, as while this is configurable, Kafka was not designed to process large size records.

* Producers:
  * Kafka producers transmit messages to topics and may either allow Kafka to evently distribute the data to different partitions or choose a specific partition based on a message assignment key's has value or the message can specify a partition when transmitted.
  * round-robin approach -- 循环
  * Generally speaking, a single producer per topic is more network efficient than multiple producers.

* Consumers:
  * Consumers are applications that subscribe to a topic in order to consume their messages. 

* Consumer Groups:
  * Kafka stores the current offset per Consumer Group/Topic/Partition, as it would for a single Consumer. This means that unique messages are only sent to a single consumer in a consumer group, and the load is balanced across consumers as equally as possible. 
  * When the number of consumers exceeds the number of Partitions in a Topic, all new consumers wait in idle mode unitl an existing consumer unsubscribes from that parition. As new consumers join a Consumer Group and there are more consumers than paritions. Kafka initiates a rebalancing 

Install Apache Kafka on Ubuntu
------------------------------

```
Apache Kafka: 社区版Kafka 优势迭代速度快 缺陷仅提供基础核心组件，缺失高级特性 
Confluent Kafka : 集成很多高级特性

Kafka服务端代码完全由Scala语言编写 Scala支持面向对象编程和函数式编程 

Kafka 0.7 提供基础的消息队列功能
Kafka 0.8 引入副本机制 
Kafka 0.9 增加基础安全认证/权限功能 
Kafka 0.11.0.0 版本引入幂等性Producer API 以及事务Transcation API 

I/O模型的使用: 阻塞式I/O 非阻塞式I/O I/O 多路复用 信号驱动I/O 异步I/O 
  Java中的Socket对象的阻塞模式 和非阻塞模式 对应前两种模型
  Linux调用select函数属于I/O多路复用模型 
  epoll调用介于IO多路复用和信号驱动IO 
  
  Kafka客户端底层使用Java selector selector 在Linux上实现机制式epoll 在windows实现机制select 

数据网络传输效率:
  Linux部署Kafka能够享受零拷贝技术带来的快速数据传输特性 
  
社区支持度:
  
Kafka 大量使用磁盘 使用方式多是顺序读写操作;一定程度上规避机械磁盘的 随机读写操作慢 
RAID: 磁盘阵列
  提供荣誉的磁盘存储空间 
  提供负载均衡 

规划磁盘容量:
  1. 新增消息数 
  2. 消息留存时间 
  3. 平均消息大小 
  4. 备份数 
  5. 是否启用压缩
避免大流量下的丢包

Zookeeper: 是一个分布式协调框架，负责协调管理并保存Kafka集群的所有元数据信息
  2181: Zookeeper默认端口 


  2181: Zookeeper默认端口 

Kafka 调整参数：
  1. 文件描述符 
    ulimit -n 1000000
  2. 文件系统类型 
    ext3, ext4, XFS 日志型文件系统
    XFS 文件系统性能强于ext4
  3. Swappiness 
    - Swappiness is the kernel parameter that defines how much (and how often) your Linux kernel will copy RAM contents to swap. This parameter default value is "60" and it can take anything from "0" to "100". The higher the value of the swappiness parameters, the more aggressively your kernel will swap.
    - sudo sysctl vm.swapiness=10
    - cat /proc/sys/vm/swappiness 
  4. 提交时间
    - Kafka 发送数据首先写入操作系统页缓存Page Cache.随后操作系统根据LRU算法定期将页缓存数据落盘 
   
  堆越小留给页面缓存的空间越大，这对Kafka是优势


```

Apache Kafka Security
---------------------
> Apache Kafka is an internal middle layer enabling your back-end systems to share  real-time data feeds with each other through Kafka topics. 

* Problems Security is solving
  - Encryption of data in-flight using SSL/TLS:
```
This allows your data to be encryped between your producers and Kafka and your consumers and Kafka.

Encryption solves the problem of the man in the middle (MITM) attack. 
That's because your packets, while being routed to your Kafka cluster, travel your entwork and hop from machines to machines If your dat is PLAINTEXT (by default in Kafka), any of these routes could read the content of the data your're sending.

This encryption comes at a cost: CPU is now leveraged for both the Kafka Clients and athe Kafka Brokers in order to encrypt and decrept packatets.

Please note the encryption is only in-flight and the data still sits unencrypted on your broker's disk.
```

  - Authentication using SSL or SASL:
```
This allows your producers and your consumers to authenticate to your Kafka cluster. 

SSL Authentication:
  --

SASL Authentication:
  -- SASL stands for Simple Authorization Service Layer and trust me

```

  - Authorization using ACLs:
```
Once your clients are authenticated, your Kafka brokers can run them against access control lists (ACL) to determine whether or not a particular client would be authorised to write or read to some topic.
```
