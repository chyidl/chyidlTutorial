RPC Crash Course 
================

```
RPC (Remote Procedure Call)远程过程调用,是分布式系统常见的一种通信协议.除了RPC常见的多系统数据交互方案还有分布式消息队列，HTTP请求调用，数据库和分布式缓存
    RPC 和 HTTP调用没有经过中间件，他们是端到端的直接数据交互，HTTP调用其实也可以看成一种特殊的RPC
    Nginx/Redis/MySQL/Dubbo/Hadoop/Spark/Tensorflow 开源产品都是在RPC技术的基础上构建出来的,

Nginx 与 RPC:
    Nginx 代理服务器，可以为后端分布式系统提供负载均衡，可以将后端多个服务地址聚合为单一地址对外提供服务.
    uwsgi协议作为二进制协议，

    Nginx配置负载均衡:
        1. 转发功能: 按照算法[权重、轮询]将客户端请求转发到不同应用服务器上，减轻单个服务器压力，提高系统并发量 
        2. 故障移除：通过心跳检测方式，判断应用服务器是否可以正常工作，如果服务器宕机，自动将请求发送到其他应用服务器
        3. 恢复添加: 检测到发生故障的应用服务器恢复工作，自动将其添加到处理用户请求队伍中
        Nginx 的upstream 支持分配算法:
            1. 轮询 - 轮流处理请求(默认)
                每个请求按时间顺序分配到不同的应用服务器，如果应用服务器down掉，自动剔除，剩下的继续轮询
            2. 权重 - 
                通过配置权重，执行轮询几率，权重和访问比率成正比，用于应用服务器性能不均的情况
            3. IP 哈希算法:
                每个请求按照访问IP的hash结果分配，这样每个访客固定访问一个应用服务器，可以解决session共享问题 
        upstream tomcatserver{
            server 192.168.1.1:8080 weight=3;
            server 192.168.1.2:8080 down;   -- 当前server暂时不参与负载
            server 192.168.1.3:8080;
            server 192.168.1.4:8080 backup; -- 其他所有非backup机器down或者忙的时候，请求backup机器
        }

        server {
            listen 80;
            server_name 8080.max.com;
            location / {
                proxy_pass http://tomcatserver;
                index index.html index.html;
            }
        }
    keepalive + nginx 实现负载均衡高可用
    
Hadoop 与 RPC:
    分布式意味着节点的物理隔离，隔离意味着需要通信，通信意味着RPC的存在
    Hadoop文件系统hdfs,一般包含一个NameNode和多个DataNode，NameNode和DataNode之间就是通过一种称为Hadoop RPC的二进制协议通信

TensorFlow 与 RPC：
    TensorFlow Cluster的RPC通讯使用Google内部gRPC框架 

HTTP 与 RPC：
    HTTP1.0 协议只能是短链接调用
    HTTP1.1 协议增加KeepAlive特性 保持HTTP连接长时间不断开
    HTTP2.0 Google开源一个建立在HTTP2.0协议之上的通信框架gRPC. 

开源RPC协议中Protobuf 和 Thrift 
```

```
RPC 消息协议:
    1. 消息边界: 长度、前缀法 、特殊符号分割 
        \r\n 
        消息发送端在每条消息的开头增加一个4字节长度的整数值，标记消息体的长度
        HTTP Content-length 头消息用来标记消息体的长度
        HTTP协议是一种基于特殊分割符和长度前缀的混合型协议
            HTTP消息头采用纯文本外加\r\n分割
            HTTP消息体通过content-type 决定长度 
        HTTP超文本传输协议 
    2. 消息表示: 二进制、文本
    3. 消息结构: 有模式、无模式
        json -- 显式结构的消息协议 
    4. 压缩算法
        压缩算法是CPU计算密集型操作、
        Google snappy算法 协议层压缩算法 
        zigzag编码:将负数编码成正奇数，正数编码成偶数，解码时遇到偶数直接除以2，就是原值，遇到奇数就加1除2再取负就是原值
```

* Common Tools 
```
  - evans: more expressive universal gRPC client: https://evans.syfm.me 
    

```
