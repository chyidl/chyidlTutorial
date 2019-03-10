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

