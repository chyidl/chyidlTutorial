RediSearch Crash Course
=======================
```
Redisearch implements a search engine on top of redis, but unlike other redis search libraries, it does not use internal data structures like sorted sets.
Inverted indexes are stored as a special compressed data type that allows for fast indexing and search speed, and low memory footprint.
This also enables more advanced features, like exact phrase matching and numeric filtering for text queries, that are not possible or efficient with traditional redis search approaches.
```

Quick Start Guide
-----------------
* Building and running from source 
```
RediSearch uses CMake as its built system, RediSearch requires CMake version 3 or greater. 
$ git clone https://github.com/RediSearch/RediSearch.git 
$ cd RediSearch 
$ mkdir build 
$ cd build 
$ cmake .. -DCMAKE_BUILD_TYPE=RelWithDebInfo 
$ make -j4
$ sudo vim /etc/systemd/system/redis.service 
[Unit]
Description=Redis In-Memory Data Store 
After=network.target 

[Service]
User=redis
Group=redis
# add loadmodule 
ExecStart=/usr/local/bin/redis-server /etc/redis/redis.conf  --loadmodule /home/pi/RediSearch/build/redisearch.so
ExecStop=/usr/local/bin/redis-cli shutdown 
Restart=always 

[Install]
WantedBy=multi-user.target
$ sudo systemctl restart redis 
```

```
Note: Input is expected to be valid utf-8 or ASCII. The engine cannot handle wide character unicode at the moment.

# Creating an index with fields and weights (default weight is 1.0)
192.168.1.243:6379> FT.CREATE myIdx SCHEMA title TEXT WEIGHT 5.0 body TEXT url TEXT
OK
# Adding documents to the index
192.168.1.243:6379> FT.ADD myIdx doc1 1.0 FIELDS title "hello world" body "lorem ipsum" url "http://redis.io"
OK
192.168.1.243:6379> FT.SEARCH myIdx "hello world" LIMIT 0 10
1) (integer) 1
2) "doc1"
3) 1) "title"
   2) "hello world"
   3) "body"
   4) "lorem ipsum"
192.168.1.243:6379> 
```