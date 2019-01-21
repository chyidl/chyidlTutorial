RabbitMQ 
========

RabbitMQ is the most widely deployed open source message broker [消息中间件].It supports multiple messaging protocols.
RabbitMQ can be deplyed in distributed and federated configurations to meet high-scale, high-availability requirements.

RabbitMQ Port Access
--------------------
    4369: epmd, a peer discovery service used by RabbitMQ nodes and CLI tools
    5672, 5671: used by AMQP 0-9-1 and 1.0 clients without and with TLS
    25672: used for inter-node and CLI tools communication ()
    15672: HTTP API clients, management UI and rabbitmqadmin (only if the management plugin is enabled)
    

RabbitMQ Tutorials
------------------

These tutorials cover the basics of creating messaging applications using RabbitMQ.

```
# install rabbitmq with following command 
$ sudo apt-get install rabbitmq-server 

# rabbitmq-management plugin provides an HTTP-based API for management and monitoring of RabbitMQ nodes and clusters,along with a browser-based UI and a command line tool.
$ sudo rabbitmq-plugins enable rabbitmq_management

# Management UI Access using a Web browser http://localhost:15672 
# create a new user with admin grants
$ sudo rabbitmqctl add_user myuser mypassword 
$ sudo rabbitmqctl set_user_tags myuser administrator 
$ sudo rabbitmqctl set_permissions -p / myuser ".*" ".*" ".*"

# Now you can access using test test 
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
```

RabbitMQ CTL
------------

* $ sudo rabbitmqctl list_queues # see what queues RabbitMQ has
* $ sudo rabbitmqctl list_queues name messages_ready message_unacknowledged
* $ sudo rabbitmqctl list_exchanges # listing exchanges on the server
* $ sudo rabbitmqctl list_bindings # list existing bindings  


HAProxy
-------



Erlang [Erlang Programming Function Language]((/root/ilikeit/RabbitMQCrashCourse/erlang/README.md)
-------