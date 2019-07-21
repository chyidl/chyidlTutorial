ActiveMQ 、RabbitMQ 、ZeroMQ 、RocketMQ or Kafka 
================================================

RabbitMQ
--------
> RabbitMQ is the most widely deployed open source message broker [消息中间件].It supports multiple messaging protocols.
> RabbitMQ can be deplyed in distributed and federated configurations to meet high-scale, high-availability requirements.

RabbitMQ Port Access
--------------------
> RabbitMQ nodes bind to ports (open server TCP sockets) in order to accept client and CLI tool connections.
```
    4369: epmd, a peer discovery service used by RabbitMQ nodes and CLI tools
    5672, 5671: used by AMQP 0-9-1 and 1.0 clients without and with TLS
    25672: used for inter-node and CLI tools communication (Erlang distribution server port) and is allocated from a dynamic range ()
    35672-35682: used by CLI tools (Erlang distribution client ports) for communication with nodes and is allocated from a dynamic range
    15672: HTTP API clients, management UI and rabbitmqadmin (only if the management plugin is enabled)
    61613, 61614: STOMP clients without and with TLS (only if the STOMP plugin is enabled)
    1883, 8883: MQTT clients without and with TLS, if the MQTT plugin is enabled.
    15674: STOMP-over-WebSockets clients (only if the Web STOMP plugin is enabled)
    15675: MQTT-over-WebSockets clients (only if the Web MQTT plugin is enabled)
``` 

Installing Latest RabbitMQ
--------------------------

* Below is shell snippet that performs those steps ON Ubuntu/Debian. They are documented in moroe detail below.
```
#!/bin/sh 

## install RabbitMQ signing key 
curl -fsSL https://github.com/rabbitmq/signing-keys/releases/download/2.0/rabbitmq-release-signing-key.asc | sudo apt-key add -

## Install apt HTTPS transport
sudo apt-get install apt-transport-https

## Add Bintray repositories that provision latest RabbitMQ and Erlang 21.x releases
sudo tee /etc/apt/sources.list.d/bintray.rabbitmq.list <<EOF
deb https://dl.bintray.com/rabbitmq-erlang/debian bionic erlang-21.x
deb https://dl.bintray.com/rabbitmq/debian bionic main
EOF

## Update package indices
sudo apt-get update -y

## Install rabbitmq-server and its dependencies
sudo apt-get install rabbitmq-server -y --fix-missing
```

* Below is shell snippet that performs those steps ON REHL, CenOS, Fedora, openSUSE
```
#!/bin/sh 

# Using packageCloud Yum Repository install rabbitmq-server 
curl -s https://packagecloud.io/install/repositories/rabbitmq/rabbitmq-server/script.rpm.sh | sudo bash

# Using packageCloud Yum repository install Erlang 
curl -s https://packagecloud.io/install/repositories/rabbitmq/erlang/script.rpm.sh | sudo bash

```

* Configuring RabbitMQ
> The server is started as a daemon by default when the RabbitMQ server package is installed.it will run as a non-privileged user rabbitmq. 
```
# install rabbitmq with following command 
$ sudo apt-get install rabbitmq-server 

# RabbitMQ Verify version of rabbitmq 
$ ls /usr/lib/rabbitmq/lib/ 

# Note: The server is set up to run as system user rabbitmq. If you change the location of the node database or the logs, you must ensure the files are owned by this user (and also update the environment variables)

# Start and Stop the local server node as usual 
$ sudo service rabbitmq-server start | status | stop | restart 

# rabbitmq-server.service : /lib/systemd/system/rabbitmq-server.service 
# Log Files : /var/log/rabbitmq 

# rabbitmq-management plugin provides an HTTP-based API for management and monitoring of RabbitMQ nodes and clusters,along with a browser-based UI and a command line tool.
$ sudo rabbitmq-plugins enable rabbitmq_management

# Default user access 
# The broker creates a user guest with password guest. By default, these credentials can only be used when connecting to the broker as localhost.

# Management UI Access using a Web browser http://localhost:15672 
$ sudo rabbitmqctl delete_user guest 
# create a new user with admin grants
$ sudo rabbitmqctl add_user myuser mypassword 
$ sudo rabbitmqctl set_user_tags myuser administrator 
# rabbitmqctl set_permissions -p vhost user conf write read 
$ sudo rabbitmqctl set_permissions -p / myuser ".*" ".*" ".*"

# Now you can access using test test 
```

* Controlling System Limits on Linux 
> RabbitMQ installations running production workloads may need system limits and kernel parameters tuning in order to handle a decent number of concurrent connections and queues.
```
# The main setting that needs adjustment is the max number of open files, The default value on many operating systems is too low for a messaging broker (1024 on serveral Linux distributions). Recommend allowing for at least 65536 file descriptors for user rabbitmq in production environments.
$ ulimit -n 
1024 

# There are two limits in play: the maximum number of open files the OS kernel allows (fs.file-max) and the per-user limit (ulimit -n). Ther former must be higher than the latter. 

With systemd (Recent Linux Distributions)
$ sudo vim /etc/systemd/system/rabbitmq-server.service.d/limits.conf 
    [Service]
    LimitNOFILE=64000 

Without systemd (Older Linux Distributions)
$ sudo vim /etc/default/rabbitmq-server 

This soft limit cannot go higher than the hard limit (which default to 4096)
$ sudo vim /etc/security/limits.conf 

Changing Limit For Current Session
$ ulimit -n 200000 

Debian & Ubuntu 
$ ulimit -Hn  # Hard limit 
$ ulimit -Sn  # Soft limit 

Enable PAM-Based Limits for Debian & Ubuntu 
You can enable PAM-based user limits so that non-root users, such as the guest user, may specify a higher value for maximum open files.

For example, follow these steps to enable PAM-based limits for all users to allow a maximum of 200000 open files.
1. Edit /etc/pam.d/common-session and add the following line:
    session     required    pam_limits.so 
2. Edit /etc/pam.d/common-session-noninteractive and add the same line as above 
    session     required    pam_limits.so 
3. Edit /etc/security/limits.conf and append the following lines to the file:
    *   soft    nofile  65536
    *   hard    nofile  200000
4. Restart the machine so the limits take effect and verify that the new limits are set with the following command:

Enable PAM-Based Limits for CentOS & Red Hat 
$ ulimit -Hn  # Hard limit 
$ ulimit -Sn  # Soft limit 

enable PAM-based user limits so that non-root users, may specify a higher value for maximum open files.
Follow these steps to enable PAM-based limits for all users to allow a maximum of 200000 open files.

1. Edit /etc/pam.d/login and add the following line:
    session     required pam_limits.so 
2. Edit /etc/security/limits.conf and append the following lines to the file:
    root soft nofile 65535
    root hard nofile 65535
    * soft  nofile 65536
    * hard  nofile 200000 
3. Restart the machine so that the limits to effect and verify that the new limits are set with the following command

# Verifying the Limit 
    1. RabbitMQ management UI displays the number of file descritors available for it 
    2. $ rabbitmqctl status 
```

Command Line Tools
------------------
```
RabbitMQ comes with multiple command line tools:
    rabbitmqctl : for service management and general operator tasks 
        It supports a wide range of operations, mostly administrative (operational) in anture.
            Stopping | Starting |  node
            Access to node status, effective condiguration, health checks 
            Virtual host management
            User and permission management 
            Policy management 
            Listing queues, connections, channels, exchanges, consumers 
            Cluster membership management
    rabbitmq-diagnostics : for diagnostics and health checking 
        # check if the local node is running and CLI tools can successfully authenticate with it 
        $ sudo rabbitmq-diagnostics ping 

        # prints enabled components (applications), TCP listeners, memory usage breakdown, alarms and so on
        $ sudo rabbitmq-diagnostics status 

    rabbitmq-plugins : for plugin management: lists, enables and disables them 
        
    rabbitmqadmin : for operator tasks over HTTP API 

    Node Names: RabbitMq nodes are identified by node names. A node name consists of two parts, a prefix(usually rabbit) and hostname. Node names in a cluster must be unique. 
```

- [1. Hello World](/root/ilikeit/RabbitMQCrashCourse/tutorials/helloworld/receive.py)
    - producer: A Program that sends message is a producer.
    - consumer: A consumer is a program that mostly waits to receive message.
    - queue: A queue is only bound by the host's memory & disk limits.
    - (using the Pika Python client): 
    - RabbitMQ libraries: RabbitMQ speaks AMQP 0.9.1 which is an open, general-purpose protocol for messaging

- [2. Work queues](/root/ilikeit/RabbitMQCrashCourse/tutorials/workqueues/worker_ack_durability.py)
    - In order to make sure a message is never lost, RabbitMQ supports message acknowledgments. An ack(nowledgement) is sent back by te consumer to tell RabbitMQ that a particular message had been received, processed and that RabbitMQ is free to delete it. 
    - If a consumer dies(its channel is closed, connection is closed, or TCP connection is lost) without sending an ack. RabbitMQ will understand that a message wasn't processed fully and will re-queue it.
    - This way you can be sure that no message is lost, even if the worker occasionally die.
    - When RabbitMQ quites or crashes it will forget the queues and messages unless you tell it not to. Two things are required to make sure that messages aren't lost: we need to mark both the queue and messages as durable.

- [3. Publish/Subscribe](/root/ilikeit/RabbitMQCrashCourse/tutorials/publishsubscribe/emit_log.py)
    - "publish/subscribe" : published log messages are going to be broacast to all the receivers.
    - exchange : one side it receives messages from producers and the other side it pushes them to queues.
    - exchange types: direct, topic, headers, fanout
    - fanout exchange is just broadcast all the messages it receives to all the queues it knows.

- [4. Routing](/root/ilikeit/RabbitMQCrashCourse/tutorials/routing/emit_log_direct.py)
    - direct exchange: a message goes to the queue whose binding key exactly matches the routing key of the message.

- [5. Topics](/root/ilikeit/RabbitMQCrashCourse/tutorials/topics/emit_log_topic.py)
    - topic exchange: 
    - (star) can substitute for exactly one word
    - (hash) can substitute for zero or more words. it will receive all the messages, regradless of the routing key - like in fanout exchange

- [6. RPC](/root/ilikeit/RabbitMQCrashCourse/tutorials/rpc/rpc_client.py)
    - RPC: Remote Procedure Call.
    
Best Practices
--------------
    * RabbitMQ
        - Client side problems 
        - Server side configurations 
        
    * Connections and channels
        - Use separate connections for publish/consume
            * Publishes may be TCP back-pressured 
            * Then the server won't receive AMQP Acks either 
        - Keep connection/channel count low 
            * Reuse connections 
            * 1 connection for publishing 
            * 1 connection for consuming 
            * 1 channel per thread (don't share)
        - Every connection uses:
            * TCP buffer space(auto-tuned, but may need to be decreased)
            * CPU for metric collection by RabbitMQ mgmt UI
        - Don't open and close connections or channels repeatedly
            * TLS connection: 5 TCP packages
            * AMQP connections: 7 TCP packages
            * AMQP channel: 2 TCP packages 
            * AMQP publish: 1 TCP package(more for larger message)
            * AMQP close channel: 2 TCP packages
            * Total 14-19 package (+Acks)
            * To Build connection proxy keep connection open, local process can connect to this local proxy. and reuse the connection 
    
    * Queues 
        - Short queues are fast queues, because message can be cached or not hit the disk at all.
        - Use lazy queue-mode if they're long (RabbitMQ >= 3.6) : Lazy Queue attempt to move messages to disk as early as practically possible.This means significantly fewer messages are kept in RAM in the majority of cause under normal operation.This comes at a cost of increaed disk I/O.
        - Limit queue size, with TTL(Time to Live) or max-length 
        - Problems with long queues
            * Small msgs embedded in queue index 
            * Take long time to sync between nodes
            * Time consuming to start a server with many msgs.
        - Queues are single-thread (throughput of about 50000 messages / seconds)
        - Max performance: One queue per core
            * Consistent hash exchange plugin 
            * RabbitMQ sharing 
        - Consume (push), don't poll (pull) for messages
        - Auto-ack or ack every X msgs instead of every msg 
        - RabbitMQ management interface collects and stores stats for all queues 
    
    * Persistent messages 
        - For a message to survive a server restart
            * Durable exchange (most are)
            * Durable queue 
            * Persistent message (delivery_mode=2)
        - For throughput use temporary, or non-durable queues
        
RabbitMQ Cluster[2 nodes]
-------------------------
    * All data/state required for the operation of a RabbitMQ broker is replicated across all nodes.An exception to this are message queues, which by default reside on one node, though they are visible and readchable from all nodes.
    * All nodes in a RabbitMQ cluster are equal peers: there are no special nodes in RabbitMQ core.
    * RabbitMQ nodes and CLI tools(e.g. rabbitmqctl) use a cookie to determine whether they are allowed to communicate with each other. For two nodes to be able to communicate they must have the same shared secret called the Erlang Cookie. The Cookie is just a string of alphanumeric characters up to 255 characters in size. Every cluster node must have the same cookie.
    * Assuming all cluster members are available, a client can connect to any node and perform any operation.
    * rabbitmq-diagnostics and rabbitmqctl provide commands that inspect resources and cluster-wide state.
    * rabbitmqctl list_connections : 
    * In a cluster with multiple nodes that have management plugin enabled, the operator can use any node to access management UI.
    * Every node stores and aggregates its own metrics and stats, and provides an API for other nodes to access it. 
    * RabbitMQ Cluster MetaData replication
        - queue Metadata: queue name and queue Attribute
        - exchange Metadata: exchange name, attribute and type 
        - bing Metadata: Exchange -> binding -> Queue 
        - virtual hosts: 
    * Disk and RAM Nodes: In the vast majority of cases you want all your nodes to be disk nodes; RAM nodes are a special case that can be used to improve the performance clusters with high queue, exchange, or bingding churm.
    * sudo rabbitmqctl join_cluster rabbit@RPi3B --ram (Set RAM node, default is Disk Node)
```
# In order to link up our two nodes in a cluster.
# We tell the node rabbit@RPi2B to join the cluster of the rabbit@RPi3B. Prior to that newly joining members must be reset.


# Edit /etc/hosts [all nodes]
$ sudo vim /etc/hosts 
# FQDN - Fully Qualified Domain
192.168.31.156	RPi3B
192.168.31.39 	RPi2B

# Restart rabbitmq-server [all nodes]
$ sudo service rabbitmq-server restart 

# Verify rabbitmq-server is running [all nodes]
$ rabbitmqctl status

# Result
Status of node rabbit@RPi3B ...
[{pid,19599},
 {running_applications,
     [{rabbitmq_management,"RabbitMQ Management Console","3.6.6"},
      {rabbitmq_management_agent,"RabbitMQ Management Agent","3.6.6"},
      {rabbitmq_web_dispatch,"RabbitMQ Web Dispatcher","3.6.6"},
      {rabbit,"RabbitMQ","3.6.6"},
      {ranch,"Socket acceptor pool for TCP protocols.","1.2.1"},
      {webmachine,"webmachine","1.10.3"},
      {amqp_client,"RabbitMQ AMQP Client","3.6.6"},
      {rabbit_common,[],"3.6.6"},
      {mochiweb,"MochiMedia Web Server","2.13.1"},
      {ssl,"Erlang/OTP SSL application","8.1"},
      {public_key,"Public key infrastructure","1.3"},
      {crypto,"CRYPTO","3.7.2"},
      {os_mon,"CPO  CXC 138 46","2.4.1"},
      {compiler,"ERTS  CXC 138 10","7.0.3"},
      {inets,"INETS  CXC 138 49","6.3.4"},
      {asn1,"The Erlang ASN1 compiler version 4.0.4","4.0.4"},
      {syntax_tools,"Syntax tools","2.1.1"},
      {xmerl,"XML parser","1.3.12"},
      {mnesia,"MNESIA  CXC 138 12","4.14.2"},
      {sasl,"SASL  CXC 138 11","3.0.2"},
      {stdlib,"ERTS  CXC 138 10","3.2"},
      {kernel,"ERTS  CXC 138 10","5.1.1"}]},
 {os,{unix,linux}},
 {erlang_version,
     "Erlang/OTP 19 [erts-8.2.1] [source] [smp:4:4] [async-threads:64] [kernel-poll:true]\n"},
 {memory,
     [{total,33390096},
      {connection_readers,0},
      {connection_writers,0},
      {connection_channels,0},
      {connection_other,1420},
      {queue_procs,1420},
      {queue_slave_procs,0},
      {plugins,666856},
      {other_proc,11166212},
      {mnesia,35984},
      {mgmt_db,492340},
      {msg_index,23584},
      {other_ets,740776},
      {binary,256744},
      {code,13241660},
      {atom,795257},
      {other_system,5967843}]},
 {alarms,[]},
 {listeners,[{clustering,25672,"::"},{amqp,5672,"::"}]},
 {vm_memory_high_watermark,0.4},
 {vm_memory_limit,367273574},
 {disk_free_limit,50000000},
 {disk_free,16280457216},
 {file_descriptors,
     [{total_limit,65436},
      {total_used,2},
      {sockets_limit,58890},
      {sockets_used,0}]},
 {processes,[{limit,1048576},{used,239}]},
 {run_queue,0},
 {uptime,124},
 {kernel,{net_ticktime,60}}]
 
# Create rabbitmq-server cluster 
Step 1 view /var/lib/rabbitmq/.erlang.cookie [Master - RPi3B]
[RPi3B]
$ sudo cat /var/lib/rabbitmq/.erlang.cookie 
> KDRIXCDBRMXKPJUKBTVF

Step 2 set cookie same master node [RPi3B] (Make sure the erlang cookies are the same all node.) [RPi2B]
[RPi2B]
$ sudo service rabbitmq-server stop 
$ echo -n "KDRIXCDBRMXKPJUKBTVF" > /var/lib/rabbitmq/.erlang.cookie
$ sudo service rabbitmq-server start

Step 3 join cluster to node 1[RPi3B]
[RPi2B]
$ sudo rabbitmqctl stop_app 
# node must be reset before it can join an existing cluster. Resetting the node removes all resources and data that were previous present on that node.
$ sudo rabbitmqctl reset
$ sudo rabbitmqctl join_cluster rabbit@RPi3B
$ sudo rabbitmqctl start_app 

[RPi3B]
# We can see that the three nodes are joined in a cluster by running the cluster_status command on any of the nodes.
$ sudo rabbitmqctl cluster_status 
# => Cluster status of node rabbit@RPi2B ...
# => [{nodes,[{disc,[rabbit@RPi2B,rabbit@RPi3B]}]},
# => {running_nodes,[rabbit@RPi3B,rabbit@RPi2B]},
# => {cluster_name,<<"rabbit@RPi3B">>},
# => {partitions,[]},
# => {alarms,[{rabbit@RPi3B,[]},{rabbit@RPi2B,[]}]}]

# A stopping node picks an online cluster member to sync with after restart. Upon restart the node will try to contact that peer 10 times by default.with 30 second response timeouts.

现在搭建的集群时默认的普通集群，普通集群中节点可以共享集群中的exchange, routingKey, queue,但是queue中的消息只保存在首次声明的queue的节点中，任何节点的消费者都可以消费其他节点的消息
比如消费者连接rabbitmq1的节点的消费者(代码中建立Connection时，使用的是rabbitmq1的IP)可以消费节点rabbitmq2的队列myqueue2中的消息，消息传输过程是rabbitmq2把myquwuw2中的消息传输给rabbitmq1，
然后rabbitmq1节点把消息发送给consumer,因为queue中的消息只保存在首次声明的queue节点中，这样就有一个问题，如果某个node节点挂掉,那么只能等待该节点重新连接才能继续处理该节点内的消息（如果没有设置持久化的化
节点挂掉后消息会直接丢失）

针对上面的问题, 如果可以让rabbitmq中的节点像redis集群的节点一样，每个节点都保存所有的消息，比如让rabbitmq1不仅保存自己的队列myqueue的消息，还保存其他节点的队列myqueue2和myqueue3种的消息，rabbitmq2节点也一样，这样就不用担心宕机，
RabbitMQ提供这样的功能，镜像队列，镜像队列由一个master和多个slave组成，使用镜像队列的消息会自动在镜像节点间同步，而不是在consumer取数据时临时拉取.
```

Highly Available (Mirrored) Queues
----------------------------------
```
By default, contents of a queue within a RabbitMQ cluster are located on a single node (the node on which the queue was declared).
This is in contrast to exchanges and bindings, which can always be considered to be on all nodes. Queues can optionally be made mirrored across multiple nodes.

# rabbitmq配置镜像队列十分简单，在任意一个node节点下执行下边的命令就可以完成镜像队列的配置(也可以在Web管理界面上添加policy)
# ha-all: 策略名称
# ^my_queue: 匹配符，只有一个^代表匹配所有,^my_queue匹配名称以my_queue开头的queue或exchange;
# ha-mode: 同步模式，一共3种模式
#   1. all - 所有(所有的节点都同步消费)
#   2. exctly - 指定节点的数据(需配置ha-params参数，此参数为int类型比如2,在集群中随机抽取2个节点同步消费)
#   3. nodes - 指定具体节点 (需配置ha-params参数，此参数为数组类型比如{"rabbit@rabbitmq_test_01", "rabbit@rabbitmq_test_03"}明确指定在这两个节点上同步消息)
$ rabbitmqctl set_policy ha-all "^my_queue" '{"ha-mode":"all","ha-sync-mode":"automatic"}'

使用镜像队列，因为各个节点要同步消息，所以比较消耗资源，一般在可靠行比较高的场景使用镜像队列


```

RabbitMQ CTL
------------

* $ sudo rabbitmqctl list_queues # see what queues RabbitMQ has
* $ sudo rabbitmqctl list_queues name messages_ready message_unacknowledged
* $ sudo rabbitmqctl list_exchanges # listing exchanges on the server
* $ sudo rabbitmqctl list_bindings # list existing bindings  


HAProxy
-------

Erlang [Erlang Programming Function Language](/root/ilikeit/RabbitMQCrashCourse/erlang/README.md)
-------


RocketMQ
========

> 消息队列RocketMQ -- 消息中间件，基于高可用分布式集群技术，提供消息订阅和发布，消息轨迹查询以及定时(延时)消息，资源统计，监控报警等，RocketMQ为分布式应用系统提供异步解耦、削峰填谷的能力，同时具备海量消息堆积、高吞吐消息队列RocketMQ提供TCP和HTTP协议层面的接入方式、支持Java、C++、.NET、Go、Python、

![RocketMQ Features](/imgs/ilikeit/MQCrashCourse/RocketMQ.png?raw=True)

* 多协议支持:
    - 支持HTTP协议: 采用RESTful标准，方便易用，快速接入，跨网络能力强，并支持启动语言客户端
    - 支持TCP协议: 区别于HTTP简单的接入方式，提供更为专业、可靠、稳定的TCP协议的SDK介入。
    - 支持STOMP协议: 类似于HTTP的纯文本的协议机制，常用于脚本语言(Ruby, Python, Perl)和消息队列RocketMQ Broker进行轻量级交互

* 管理工具:
    - Web控制台:支持Topic 管理、生产者管理、消费者管理、消息查询、消息轨迹展示和查询、资源报表以及监控报警管理。
    - openAPI: 提供API便于将消息队列RocketMQ 管理工具集成到自己的控制台
    - mqadmin命令集: 专有云输出提供一套丰富的管理命令集，以命令方式对消息队列RocketMQ服务进行管理

* 功能:
    - 事务消息：实现类似X/Open XA的分布式事务功能，以达到事务最终一致性状态
    - 定时（延时）消息：允许消息生产者指定消息进行定时（延时）投递，最长支持40天
    - 大消息：支持最大4MB消息
    - 消息轨迹：通过消息轨迹、能清晰定位消息从发布者发出，经由消息队列RocketMQ服务端、投递给消息订阅者的完整链路，方便定位排查问题。
    - 广播消费：允许同一个Group ID 所标识的所有Consumer都各自消费某条消息一次。
    - 顺序消息：允许消息消费者按照消息发送的顺序对消息进行消费
    - 重置消费进度：根据时间重置消费进度，允许用户进行消息回溯或者丢弃堆积消息
    - 死信队列: 将无法正常消费的消息存储到特殊的死信队列供后续处理
    - 全球消息路由：用于全球不同地域纸巾啊的消息同步复制，保证地域之间的数据一致性

* 消息Pub/Sub模型
> 消息队列RocketMQ支持“发布/订阅”模型，消息发布者(生产者)可以将一条消息发送服务端的某个主题Topic, 多个消息接收方(消费者)订阅这个主题以接收该消息

![Pub/Sub Model](/imgs/ilikeit/MQCrashCourse/pub-sub_model.png?raw=True)

* 名词解释:
    - 消息主题(Topic): 一级消息类型，通过Topic对消息进行分类
    - 消息(Message): 消息队列中消息传递的载体
    - 消息全局唯一标识(Message ID): 由消息队列RocketMQ系统自动生成，唯一标识某条消息
    - 消息的业务标识(Message Key): 由消息生产者Producer 设置，唯一表示某个业务逻辑
    - 消息标签(Tag): 二级消息类型，用来进一步区分某个Topic下的消息分类
    - 消息生产者(Producer): 消息发布者，负责生产并发送消息 
    - 消息消费者(Consumer): 消息订阅者，负责接收并消费消息
    - 消息生产者实例(Producer实例)：不同的Producer实例可以运行在不同的进程内或者不同的机器上，Producer实例线程安全，可以在同一进程内多线程之间共享
    - 消息消费者实例(Consumer实例): 不同的Consumer实例可以运行在不同进程内或者不同机器上，一个Consumer实例内配置线程池消费消息 
    - 组(Group): 一类Producer或Consumer,这类Producer或Consumer通常生产或消费同一类消息，且消息发布或订阅的逻辑一致
    - 组唯一标识(Group ID): Group 的标识 
    - 集群消费: 一个GroupID所标识的所有Consumer平均分摊消费消息
    - 广播消费: 一个GroupID所标识的所有Consumer都会各自消费某条消息一次
    - 定时消费: Producer将消息发送到消息队列RocketMQ服务端，但并不期望这条消息立马投递，而是推迟到当前时间点之后的某个时间投递到Consumer进行消费
    - 延迟消费: Producer将消费发送到消息队列，但不期望这条消息立马投递，而是延迟一定时间后投递Consumer进行消费，该消息即延时消费
    - 事务消息：消息队列启动类似X/Open XA的分布事务功能，通过消息队列的事务消息能达到分布式事务的最终一致
    - 顺序消息：消息队列提供一种按照顺序进行发布和消费的消息类型，分为全局顺序消息和分区顺序消息
        * 全局顺序消息：对于指定的一个Topic,所有消息按照严格的先入先出FIFO的顺序进行发布和消费
        * 分区顺序消息：对于指定的一个Topic,所有的消息根据Sharding Key进行区块分区。同一个分区内的消息按照严格的FIFO顺序进行发布和消费
    - 消息堆积：Producer已经将消息发布到消息队列的服务端，但由于Consumer消费能力有限，未能在短时间内将所有消息正确消费掉，此时在消费队列的服务端保持着未被消费的消息，改状态即为消息堆积 
    - 消息过滤：Consumer可以根据消息标签(tag)对消息进行过滤，确保Consumer最终只接收被过滤后的消息类型。消息过滤在消息队列的服务端完成
    - 消息轨迹: 一条消息从Producer发出到Consumr消费处理过程中，由各个相关节点的时间、地点等数据汇聚而成的完整链路信息。
    - 重置消费位点: 以时间轴为坐标，在消息持久化存储的时间范围内，重新这只Consumer对已订阅的Topic的消费进度，设置完成后Consumer将接收设置时间点之后由Producer发送到消息队列服务端的消息
    - 死信队列(Dead-Letter Queue): 死信队列用于处理被无法正常消费的消息，档一条信息初次消费失败，消息队列RocketMQ会自动进行消息重试，达到最大重试次数之后，若消费依然失败，则表明Consumer在正常情况下无法消费该消息。此时,消息队列不会立刻将消息丢弃，而是将消息发送到Consumer对应的特殊队列中.
    - 消息路由: 消息路由常用语不同地域之间的消息同步，保证地域之间的数据一致性

* 使用场景
    - 异步解耦
    - 分布式事务的数据一致性
    - 消息的顺序收发
    - 削峰填谷
    - 大规模机器的缓存同步

* 一个场景：用户注册后，需要发送注册邮件和短信通知，已告知用户注册成功
    - 串行方式：
        * 1. 用户在注册页面填写账号和密码并提交注册信息，这些信息首先会被写入注册信息
        * 2. 注册信息写入注册系统成功后，再发送请求至邮件通知系统。邮件通知系统收到请求后向用户发送邮件通知
        * 3. 邮件通知系统接收注册系统请求后再向下游的短信通知系统发送请求，短信通知系统收到请求之后向用户发送短信通知.
        * 以上所有任务全部完成，才返回注册结果到客户端，铜壶才能使用账号登陆
    - 并行方式:
        * 1. 用户在注册页面天蝎账号和密码并提交注册信息，这些注册信息首先被写入注册系统成功。
        * 2. 注册信息写入注册系统成功后，再同时发送请求至邮件和短信通知系统。邮件和短信通知系统收到后分别向用户发送邮件和短信通知 
    - 异步解耦：
        * 对于用户来说，注册功能实际上只需要注册系统存储用户的账户信息后，该用户便可以登陆, 后续的注册短信和邮件不是及时需要关注的步骤。
        * 1. 用户在注册页面填写账号和密码并提交注册信息，这些注册信息会被写入注册注册系统成功
        * 2. 注册信息写入注册系统成功后，再发送信息至消息队列，消息队列会会马上返回响应给注册系统，注册完成，用户可以立即登陆
        * 3. 下游的邮件和短信通知系统订阅消息队列的注册请求消息，即可向用户发送邮件和短信通知，完成所有的注册流程.
        * 异步解耦是消息队列的主要特点，主要目的是减少请求响应时间和解耦，主要的使用场景就是将比较耗时而且不需要及时(同步)返回结果的操作作为消息放入消息队列。
    - 分布式事务和数据一致性:
> 注册系统注册的流程中，用户入口在网页注册系统，通知系统在邮件系统，两个系统之间的数据需要保持最终一致
        * 普通消息处理
            - 注册系统和邮件通知系统之间通过消息队列进行异步处理，注册系统将注册信息写入注册系统之后，发送一条注册成功的消息到消息队列，邮件通知系统订阅消息队列的注册消息，做相应的业务处理，发送注册成功或者失败的邮件.

![Distributed Transaction general](/imgs/ilikeit/MQCrashCourse/Distributed_transaction-general.png?raw=True)

            - 1. 注册系统发起注册
            - 2. 注册系统向消息队列发送注册消息成功与否的消息
            - 3. 邮件通知系统收到消息队列的注册成功消息
            - 4. 邮件通知系统发送注册成功邮件给用户
            - 上述情况虽然实现系统间的解耦，上游系统不需要关心下游系统的业务处理结果，但是数据一致性不好处理，如何保证邮件通知系统状态与注册系统状态的最终一致。
        * 事务消息处理(利用事务消息实现系统间的状态数据一致性)

![Distributed Transaction Message](/imgs/ilikeit/MQCrashCourse/Distributed_transaction-message.png?raw=True)
            - 1. 注册系统向消息队列发送半事务消息
                * 1.1 半事务消息发送成功，进入2 
                * 1.2 半事务消息发送失败，注册系统不进行注册，流程结束(最终注册系统与邮件通知系统数据一致)
            - 2. 注册系统开始注册
                * 2.1 注册成功，进入3.1 
                * 2.2 注册失败，进入3.2 
            - 3. 注册系统向消息队列发送半消息状态
                * 3.1 提交半事务消息，产生注册成功消息，进入4
                * 3.2 回滚半事务消息，未产生注册成功消息，流程结束（最终注册系统与邮件通知系统数据一致）
            - 4. 邮件通知系统接收消息队列的注册成功消息
            - 5. 邮件通知系统发送注册成功邮件 (最终注册系统与邮件通知系统数据一致)
    - 消息的顺序收发
        * 全局顺序: 对于指定一个Topic，所有消息将按照严格的先入先出(FIFO)的顺序，进行顺序发布和顺序消费
        * 分区顺序：对于指定一个Topic,所有消息根据Sharding Key进行区块分区，同一分区内的消息按照严格的FIFO顺序进行顺序发布和顺序消费。可以保证一个消息被一个进程消费。注册场景中，可以使用用户ID作为Sharding Key来进行分区，同一分区下新建、更新或删除注册的消息必须按照FIFO的顺序发布和消费
    - 削峰填谷（一般在秒杀或团队抢购中使用广泛）
> 在秒杀或团队抢购活动中，由于用户请求量较大，导致流量暴增，秒杀的应用在处理如此大量的访问流量后，下游的通知系统无法承载海量的调用量，甚至会导致系统崩溃等问题而发生漏通知的情况，为了解决这些问题，可在应用和下游通知系统之间加入消息队列:

![Peak Clipping](/imgs/ilikeit/MQCrashCourse/Peak_clipping.png?raw=True)
    
        * 1.用户发起海量秒杀请求到秒杀业务处理系统
        * 2.秒杀处理系统按照秒杀处理逻辑将满足秒杀条件的请求发送至消息队列
        * 3.下游的通知系统订阅消息队列的秒杀相关信息，再将秒杀成功的消息发送到相关用户
        * 4.用户收到秒杀成功的通知
    - 大规模机器的缓存同步
        
* 产品架构
> 消息队列在任何一个环境都是可扩展的，发布者有可能是个集群，消息服务器必须是一个集群，订阅者有可能是个集群。集群级别的高可用是消息队列跟其他的消息服务器的主要区别。

![Product Architecture](/imgs/ilikeit/MQCrashCourse/Product_Architecture.png?raw=True)


