# Redis Cluster 

```
1. Redis Sentinel: 
  Use sentinel when speed isn't your primary concern, which makes it an excellent option for smaller implementation with high availability concerns.

2. Redis Cluster: 
  It provides high availability plus clustering solution. Its an excellent choice to ensure high availability while keeping fast access speed in consideration to access data.
```

* Understanding redis 
```
Every Redis Cluster node requires two TCP connections open. The normal Redis TCP port used to serve clients 6379, plus the port obtained by adding 10000 to the data port, so 16379.

Redis Cluster does not use consistent hashing, there are 16384 hash slots in Redis Cluster.

Every node in a Redis Cluster is responsible for a subset of the hash slots, so for example you may have a cluster with 3 nodes.
  1. Node A contains hash slots from 0 to 5500. 
  2. Node B contains has slots from 5501 to 11000.
  3. Node C contains hash slots from 11001 to 16383 
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
redis.conf inside src directory 

```
