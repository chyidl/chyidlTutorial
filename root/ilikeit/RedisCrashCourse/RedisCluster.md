# Redis Cluster 
> Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache and message broker. It supports data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperloglogs, geospatial indexes with radius queries and strems.
```
1. Redis Sentinel: [哨兵]
  Use sentinel when speed isn't your primary concern, which makes it an excellent option for smaller implementation with high availability concerns.

2. Redis Cluster: 
  It provides high availability plus clustering solution. Its an excellent choice to ensure high availability while keeping fast access speed in consideration to access data.
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

* Running Redis in Cluster mode
```
# The configuration file in which you should define all cluster configuration paramters
$ sudo vim redis-5.0.8/redis.conf 
  port 6379 
  cluster-enabled yes 
  cluster-config-file nodes-6379.conf
  cluster-node-timeout 5000 
  appendonly yes 

Note that the minimal cluster that works as expected requires to contain at least three master nodes.
Start every instance 
$ ./redis-server ./redis.conf    

Since no nodes.conf file existed, every node assigns itself a new ID.
```
