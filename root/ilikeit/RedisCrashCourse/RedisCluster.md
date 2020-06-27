Redis Cluster 
=============
> Redis Cluster是一个Redis分布式部署的形式，使用数据分片的办法把数据分配到不同的节点,每个节点可以有自己的备份节点
> 集群上Redis Sentinel 分布式组建用于提供丰富的HA能力
> Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache and message broker. It supports data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs, geospatial indexes with radius queries and strems.
```
1. Redis Sentinel: [哨兵]
  Use sentinel when speed isn't your primary concern, which makes it an excellent option for smaller implementation with high availability concerns.

2. Redis Cluster: 
  It provides high availability plus clustering solution. Its an excellent choice to ensure high availability while keeping fast access speed in consideration to access data.
```

* 数据分片
```
Redis Cluster 使用Slot: 作为KV系统，把每个key的值hash成0 ~ 16383 之间的数, 这个hash值用来确定对应的数据存储在那个节点中。
```

* Understanding redis 
```
Every Redis Cluster node requires two TCP connections open. The normal Redis TCP port used to serve clients 6379, plus the port obtained by adding 10000 to the data port, so 16379.

Redis Cluster does not use consistent hashing, there are 16384 hash slots in Redis Cluster.

Every node in a Redis Cluster is responsible for a subset of the hash slots, so for example you may have a cluster with 2 nodes.
  1. Node A contains hash slots from 0 to 5500. 
  2. Node B contains has slots from 5501 to 16383.
  3. Node C contains has slots from 11001 to 16383.
```

* Creating Redis Cluster 
```
A Redis cluster uses master-slave configuration to support distributed environment.
$ scp -r chyi@192.168.1.8:~/Downloads/redis-5.0.8.tar.gz .
$ tar xzf redis-5.0.8.ztr.gz
$ cd redis-5.0.8 
$ make -j4
$ make test 
```

* Redis Cluster 
```
In practical terms, Redis Cluster provides the ability to 
  * Automatically split your dataset amoung multiple nodes.
  * Continue operations when a subset of the nodes are experiencing failures or are unable to communicate with the rest of the cluster.

In order to remain available when a subset of master nodes are failing or are not able to communicate with the amjority of nodes, Redis Cluster uses a master-slave model where every master node has N replicas or slaves nodes. The minimal cluster that works as expected requires to contain at least three nodes. We will start with a six nodes cluster with three masters and three slaves.
```

* Running Redis in Cluster mode
```
# The configuration file in which you should define all cluster configuration paramters
(When you will setup on different machines and connect them remotely, you need to specify the bind address in redis.conf file)
$ sudo vim redis-5.0.8/redis.conf 
  port 6001,6002,6003
  bind 192.168.1.6/192.168.1.2/192.168.1.7
  cluster-enabled yes 
  cluster-config-file nodes-6379.conf
  cluster-node-timeout 5000 
  appendonly yes 

Note that the minimal cluster that works as expected requires to contain at least three master nodes.
Start every instance 
$ ./redis-server ./redis.conf    

Since no nodes.conf file existed, every node assigns itself a new ID.
```
