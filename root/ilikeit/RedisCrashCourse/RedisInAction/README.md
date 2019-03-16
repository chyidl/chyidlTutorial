Redis In Action
===============

>Redis is an in-mempry remote database that offers high performance, replication, and a unique data model to produce a platform for sovling problems.

>Redis is a very fast non-relational database that stores a mapping of keys to many (Binary-safe strings、Lists、Sets、Sorted Sets、Hashes、Bit array、HyperLogLogs、Streams) different types of values. Redis supported in-memory persistent storage on disk, replication to scale read performance, and client-side sharing to scale write performance.

>Redis is a type of database that's commonly referred to as NoSQL or non-relational. 

```
Redis: In-memory non-relational database; Strings, lists, sets, hashes, sorted sets; Commands for each data type for common access paterns, with bulk operationsm and aprtial transaction support; Publish/Subscribes, master/slave replication, disk persistence, scripting (strored procedures)

Memcached: In-memory key-value cache; Mapping of keys to values; Commands for create, read, update, delete, and a few others; Multithreaded server for additional performance.

MySQL: Relational database; Databases of tables of rows, views over tabes, spatial and third-party extensions; SELECT, INSERT, UPDATE, DELETE, functions stored procedures; ACID compliant (with InnoDB), master/slave and master/master replication 

MongoDB: On-disk non-relational document store; Databases of tables of schemeal-less BSON documents; Commands for create, read, update, delete, conditional queries, and more; Supports map-reduce operations, master/slave replication, sharding, spatial indexes.
```

> Redis has two different forms of persistence available for writing in-memory data to disk in a compact format.
    
    - The first method is a point-in-time dump
    - the other method is appended-only file: 

```
STRING: Strings, integers, or floating point values; OPerate on the whole string, parts, increment/decrement the integers and floats

LIST: Linked list of strings; Push or Pop items both ends, trim based on offsets, read individual or multiple items, find or remove items by value.

SET: Unordered collection of unique strings; Add, fetch, or remove indiciudal items, check membership, intersect, union, difference,fetch random items.

HASH: Unordered hash table of keys to value; Add, fetch, or remove individual items, fetch the whole hash 

ZSET(sorted set): Ordered mapping of string members to floating-point scores, ordered by score; Add, fetch, or remove individual values, fetch items based on score ranges or member value.
```

Strings in Redis
----------------
```
GET: Fetches the data stored at the given key 

SET: Sets the value stored at the given key 

DEL: Deletes the value stored at the given key(works for all types)
```

Lists in Redis
---------------
```
RPUSH: Pushes the value onto the right end of the list 
LPUSH: Pushes the value onto the left first of the list

RPOP: Pops the value from the right end of the list and returns it
LPOP: Pops the value from the left first of the list and returns it 

LRANGE: Fetches a range of values from the list 

LINDEX: Fetches an item at a given position in the list
```

Sets in Redis
-------------
> Redis SETs use a hash table to keep all strings unique (thourgh there are no associated values)
```
SADD: Adds the item to the set 

SREM: Removes the item from the set, if it exits 

SMEMBERS: Retruns the entire set of items 

SISMEMBER: Checks if an item is in the set 
```

Hashs in Redis
---------------
> In a lot of ways, we can think of HASHs in Redis as miniature versions of Redis itself.
> Using the Colon Character as a Separator:
```
HSET: Stores the value at the key in the hash 

HGET: Fetches the value at the given hash key 

HGETALL: Fetches the entire hash 

HDEL: Removes a key from the hash, if it exists
```

Sorted Sets in Redis
--------------------
> ZSETs also hold a type of key and value. The keys are unique, and the value are limited to floating-point numbers.
```
ZADD: Adds member with the given score to the ZSET 

ZRANGE: Fetches the items in the ZSET from their positions in sorted order 

ZRANGEBYSCORE: Fetches items in the ZSET based on a range of scores 

ZREM: Removes the item from the ZSET, if it exists.
```

RedLock - Distributed locks with Redis and Python 
-------------------------------------------------
> Distributed locks are a very useful primitive in many environments where different processes must operate with shared resources in a mutually exclusive way. 

> There are a number of libraries and blog posts describing how to implement a DLM (Distributed Lock Manager) with Redis, but every library uses a different approach, and many use a simple approach with lower guarantees compared to what can be achieved with slightly more complex designs.
```
Redlock-py (Python implementation).
Aioredlock (Asyncio Python implementation)

    1. Safety property: Mutual exclusion. At any given moment, only once client can hold a lock.
    2. Liveness property A: Deadlock free. Eventually it is always possible to acquire a lock, even if the client that locked a resource crashes or gets partitioned. 
    3. Liveness property B: Fault tolerance. As long as the majority of Redis nodes are up, clients are able to acquire and release locks. 

The simplest way to use Redis to lock a resource is to create a key in an instance. The key is usually created with a limited time to live, using the Redis expires feature, so that eventually it will get released (property 2 in our list). When the client needs to release the resource, it deletes the key. 

Superficially 外表上 this works well, but there is a problem: this is a single point of failure in our architecture. What happens if the Redis master goes down? Well, let's add a slave! and use it if the master is unabailable. This is unfortunately not viable. By doing so we can't implement our safety property of mutual exclusion, because Redis replication is asynchronous.

There is an obvious race condition with this model:
    1. Client A acquires the lock in the master. 
    2. The master crashes before the write to the key is transmitted to the slave.
    3. The slave gets promoted to master 
    4. Client B acquires the lock to the same resource A already holds a lock for. SAFETY VIOLATION!
```
> Correct implementation with a single instance 
```
# The command will set the key only if it does not already exist (NX option), with an expire of 30000 milliseconds (PX option).
6379> SET resource_name my_random_value NX PX 30000 

A simple solution is to use a combination of unix time with microseconds resolution, concatenating it with a client ID, it is not as safe, but probably up to the task in most environments. 
```

> To resove this problem, the Redlock algorithm assume we have N Redis masters.These nodes are totally independent (no replications). In order to acquire the lock, the client will try to acquire the lock in all N instances sequentially. If and only if the client was able to acquire the lock in the majority((N+1)/2) of the instances, the lock is considered to be acquired.
