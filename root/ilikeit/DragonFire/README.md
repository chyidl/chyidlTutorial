Architecture Evolution Path 
===========================


Appendix
========
* Question 1: 如果假设系统承载的业务量翻10倍，每天新增200万数据, 系统架构要如何演进? 如果系统承载的业务翻100倍，每天新增2000万数据，系统架构要如何演进?
    - Answer: 架构设计能力是很关键，针对业务增长，架构演进能力非常核心，这是资深工程师必须要有的一个意识和能力。
        * 针对10倍增长的场景, 引入分库分表的技术，保证每个库每个表分散一定的数据量，避免单表库数据量的过大
        * 针对100倍增长的场景, 引入数据异构、冷热分离等数据存储的架构设计“采用MySQL分库分表 + 分布式NoSQL数据库 + Elasticsearch分布式搜索 + Redis缓存的架构”先做冷热分离架构，将最热的数据放入分布式NoSQL数据库，专门承载当日数据的高并发写入，以及高性能的读写。然后每过一段时间，做数据归档，把NoSQL里不再频繁使用的冷数据迁移到MySQL里归档。最后应对海量数据的检索，可以把索引构建在Elasticsearch，而且针对特别热查询的数据，可以依托Redis做缓存。

* Question 2: 如何保证数据迁移的效率？如何保证迁移后的数据准确性？在迁移的过程中如何避免影响数据的性能？
    - 

* Question 3: 简单阐述Kafka, RabbitMQ, RocketMQ几种MQ的对比，还有各自的原理以及如何实现分布式消息队列架构的，底层的机制是什么，对比一下特点以及优缺点? 
    - 

* Question 4: 什么是线程安全?
```
线程安全是一个方法或者一个实例可以在多线程环境中使用而不会出现问题.

产生线程不安全的原因?
    多线程访问相同的资源(同一内存区的变量、数组、对象, 系统，数据库，文件)。当多个线程向同一个资源进行写操作才会出现。
```

* Question 5: 系统如何支持高并发?
```
高并发系统:
    每秒百万并发的中间件系统
    每日百亿请求的网关系统
    瞬时每秒几十万请求的秒杀系统
    支撑几亿用户的大规模高并发电商平台的订单系统、商品系统、库存系统

为了支撑高并发请求，在系统架构的设计时，会结合具体的业务场景和特点，设计出各种复杂的架构，这需要大量的底层技术支撑，需要精妙的架构和机制设计的能力.

一个完整而复杂的高并发系统架构中，一定会包含各种复杂的自研基础架构系统、各种精妙的架构设计(比如热点缓存架构设计、多优先级高吞吐MQ架构设计、系统全链路并发性能优化设计)还有各种复杂系统组合而成的高并发架构整体技术方案，还有NoSQL(Elasticesearch)/负载均衡/Web服务器等相关技术

最后真正身缠落地的时候，高并发场景下系统会出现大量的技术问题？
    比如消息中间件吞吐量上不去需要优化
    磁盘写压力过大性能太差
    内存消耗过大容易
    分库分表中间件不知道为什么丢失数据

系统架构尽可能使用最少的机器扛住最大的请求压力，减轻数据库的负担:
    1.系统业务层集群化，引入负载均衡
    2.数据库层面的分库分表+读写分离
    3.针对读多写少的请求，引入缓存集群
    4.针对高写入的压力,引入消息中间件集群(异步化写入)

ElasticSearch技术：在高并发架构下，可以通过分布式架构的ES家属支撑高并发的搜索

技术面准备:
    并发相关原理问题
    消息中间件的问题
    JVM 
    项目技术细节讨论
写代码:
    并发有关题
    算法题
    设计模式(考虑支持扩展性)
    主要涉及有分布式、缓存、消息队列等内容
    来阿里你不缺挑战，可能你更多需要关注第一年你能否活得下来。

Tomcat Implementation:
    Apache Tomcat software is an open source implementation of the Java Servlet, JavaServer Pages, Java Expression Language and Java WebSocket technologies.
    Web应用打包成WAR包部署到Tomcat中,在我们的Web应用中，我们要指名URL被那个类的哪个方法所处理(无论是原始的Servlet开发,还是现在流行的SpringMVC都必须指明).
    请求先到达Tomcat, Tomcat对于请求进行下面的处理:
        1. 提供Socket服务
            Tomcat启动之后，必然是Socket服务(BIO, NIO, AIO)，支持HTTP协议
        2. 进行请求的分发
            Tomcat可以为多个Web应用提供服务，Tomcat可以把URL下发到不同的Web应用
        3. 需要把请求和相应封装成request/response
            我们在Web应用这层不必封装request/response,都是直接使用，这是因为Tomcat已经做好封装
```
