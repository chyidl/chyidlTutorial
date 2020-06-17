Redis Crash Course
==================

Introduction
------------
> Redis is an in-memory key-value store known for its flexibility, performance, and wide language support.
> Redis是互联网技术领域最为广泛的存储中间件[Remote Dictionary Service] "远程字典服务".Redis以其超高的性能、完美的文档、简洁易懂的源码和丰富的客户端库支持在开源中间件领域广泛好评。

Install the Build and Test Dependecies
--------------------------------------
> In order to get the latest version of Redis, we will be compiling and installing the software from source. Before we download the code, we need to statisfy the build dependencies so that we can compile the software.

> To do this, we can install the **build-essential** meta-package from the repositiories. downloading the **tcl** package, which can use to test our binaries.

```
$ sudo apt-get update 
$ sudo apt-get install build-essential tcl make gcc 
```

Download, Compile, and Install Redis From Source
------------------------------------------------
```
# Docker:
# 拉取redis镜像
$ docker pull redis 
# 运行redis容器
$ docker run --name myredis -d -p6379:6379 redis 
# 执行容器中的redis-cli, 可以直接使用命令行操作redis
$ docker exec -it myredis redis-cli 

# GitHub源代码编译 
# Since we won't need to keep the source code that we'll compile long term, we will build in the **~** directory.
$ cd ~ 
# download the latest stable version of Redis source code
$ wget http://download.redis.io/redis-stable.tar.gz 
# Unpack the tarball by typing:
$ tar -xzvf redis-stable.tar.gz
# Move into the Redis source directory structure that was just extracted
$ cd redis-stable 
# compile the Redis binaries by typing:
$ make 
# After the binaries are compiled, run the test suite to make sure everything was built correctly
$ make test 
# Once complete, install the binaries onto the system by typing:
$ sudo make install

# 直接安装方式
(mac)
$ brew install redis 
(ubuntu/debian)
$ sudo apt-get install redis 
(redhat/centos)
$ sudo yum install redis 

# make below directories, redis will create directories by default but this is my perferred way of installing redis. By creating separate directories will life easier.
$ mkdir -p /mnt/chyi_data/redis/db 
$ mkdir -p /mnt/chyi_data/redis/conf 
$ mkdir -p /mnt/chyi_data/redis/

# Install init Script 
# need init configuration so that redis-server should start itself on boot and no manual commands are needed by the user 
$ cd /path/redis-stable/utils && sudo ./install_server.sh 

# When you run "install_server.sh" scripts you will asked questions to configure redis. please provide below details as necessary.
Port           : 6379
Config file    : /mnt/chyi_data/redis/conf/redis_6379.conf
Log file       : /mnt/chyi_data/redis/log/redis_6379.log
Data dir       : /mnt/chyi_data/redis/db
Executable     : /usr/local/bin/redis-server
Cli Executable : /usr/local/bin/redis-cli

# Configure Redis 
# Now that Redis is installed, we can begin to configure it.

# To start off, we need to create a configuration directory. We will use the conventional **/etc/redis** directory, which can be created by typing:
$ sudo mkdir /etc/redis 

# Now, copy over the sample Redis configuration file included in the Redis source archive:
$ sudo cp ~/redis-stable/redis.conf /etc/redis 

# Open the file to adjust a few items in the configuration:
$ sudo vim /etc/redis/redis.conf 

# Find the **supervised** directive. Currently, this is set to no. Since we are running an operating system that uses systemd init system, we can change this to **systemd**.
supervised systemd 

# Next, find the **dir** directory. This option specifies the directory that Redis will use to dump persistent data. We need to pick a location that Redis will have write permission and that isn't viewable by normal users.
dir /var/lib/redis 

# To unbind 127.0.0.1
#bind 127.0.0.1

# To set the password, edit your /etc/redis/redis.conf file 
# find this line 
requirepass foobared  
# Then uncomment it and change foobared to your password. Make sure you choose something pretty long, 32 characters or so would probably be good, it's easy for an outside user to guess upwards of 150k passwords a second, as the notes in the config file mention, 

# Create a Redis systemd Unit File 
# We can create a systemd unit file so that the init system can manage the Redis process.
$ sudo vim /etc/systemd/system/redis.service 
# Inside, we can begin the [Unit] section by adding a description and defining a requirement that networking be available before string this service:

[Unit]
Description=Redis In-Memory Data Store 
After=network.target 

[Service]
User=redis 
Group=redis 
ExecStart=/usr/local/bin/redis-server /etc/redis/redis.conf 
ExecStop=/usr/local/bin/redis-cli shutdown 
Restart=always

[Install]
WantedBy=multi-user.target 
```

Create the Redis User, Group and Directories 
--------------------------------------------
```
# Begin by creating the **redis** user and group. 
$ sudo adduser --system --group --no-create-home redis 

# create the **/var/lib/redis** directory by typing 
$ sudo mkdir /var/lib/redis 

# give the **redis** user and group ownership over this directory:
$ sudo chown redis:redis /var/lib/redis 

# Adjust the permissions so that regular users cannot access this location:
$ sudo chmod 770 /var/lib/redis 
```

Start and Test Redis
--------------------
```
# Start the Redis Service 
$ sudo systemctl start redis 

# Check that service had no errors by running
$ sudo systemctl status redis 

# Test the Redis Instance Functionality 
# To Test that your service is functioning correctly, connect to the Redis server with the command-line client:
$ redis-cli

# In the prompt that follows, test connectivity by typing:
$ 127.0.0.1:6379> ping 

# You should see:
$ PONG 

# Check that you can set keys by typing:
$ 127.0.0.1:6379> set test "It's working!"

# Output 
$ OK 

# Now, retrieve the value by typing 
$ 127.0.0.1:6379> get test 

# You should be able to retrieve the value we stored:
$ "It's working!"

# Exit the Redis prompt to get back to the shell:
$ 127.0.0.1:6379> exit 

# As a final test, let's restart the Redis instance:
$ sudo systemctl restart redis 

# Enable Redis to Start at Boot
$ sudo systemctl enable redis 


$ sudo systemctl restart redis  

Example:
$ redis-cli 
redis 127.0.0.1:6379> AUTH PASSWORD 
Ok 

# Host, port, password and database 
# By default **redis-cli** connects to the server at 127.0.0.1 port 6379. As you can guess, you can easily change this using command line options. To specify a different host name or an IP address, use -h. In order to sent a different port, user -p 

$ redis-cli -h pi -p 6379 
```

INSTALL REDIS 5.0 FROM SOURCE IN CENTOS 7
-----------------------------------------
```
# Create a directory and go inside that directory and download the source.
$ mkdir -p /opt/software/redis 
$ cd !$
$ wget http://download.redis.io/redis-stable.tar.gz

# Extract the source and go inside downloaded redis directory.
$ tar -xvzf redis-stable.tar.gz 
$ cd redis-stable 

# Next run these command to compile and install.
$ make -j4 
$ yum install tcl wget 
$ make test 
$ make install 

# make below directories, redis will create directories by default but this is my preferred way of installing redis. By creating separate directories will life easier. 
$ mkdir -p /mnt/chyi_data/redis/db 
$ mkdir -p /mnt/chyi_data/redis/conf 
$ mkdir -p /mnt/chyi_data/redis/ 

# make the start up script executable and make it start at boot.
$ cd /etc/init.d/
$ chmod 777 redis_6379
$ chkconfig --add redis_6379 

# start redis server.
$ /etc/init.d/redis_6379 start | stop | restart 

# That's it ! you all set!
$ vim /etc/init.d/redis_6379

#!/bin/sh
#Configurations injected by install_server below....

EXEC=/usr/local/bin/redis-server
CLIEXEC="/usr/local/bin/redis-cli -a <password>"
PIDFILE=/var/run/redis_6379.pid
CONF="/mnt/chyi_data/redis/conf/redis_6379.conf"
REDISHOST="118.31.50.10"
REDISPORT="6379"
###############
# SysV Init Information
# chkconfig: - 58 74
# description: redis_6379 is the redis daemon.
### BEGIN INIT INFO
# Provides: redis_6379
# Required-Start: $network $local_fs $remote_fs
# Required-Stop: $network $local_fs $remote_fs
# Default-Start: 2 3 4 5
# Default-Stop: 0 1 6
# Should-Start: $syslog $named
# Should-Stop: $syslog $named
# Short-Description: start and stop redis_6379
# Description: Redis daemon
### END INIT INFO


case "$1" in
    start)
        if [ -f $PIDFILE ]
        then
            echo "$PIDFILE exists, process is already running or crashed"
        else
            echo "Starting Redis server..."
            $EXEC $CONF
        fi
        ;;
    stop)
        if [ ! -f $PIDFILE ]
        then
            echo "$PIDFILE does not exist, process is not running"
        else
            PID=$(cat $PIDFILE)
            echo "Stopping ..."
            $CLIEXEC -h $REDISHOST -p $REDISPORT shutdown
            while [ -x /proc/${PID} ]
            do
                echo "Waiting for Redis to shutdown ..."
                sleep 1
            done
            echo "Redis stopped"
        fi
        ;;
    status)
        PID=$(cat $PIDFILE)
        if [ ! -x /proc/${PID} ]
        then
            echo 'Redis is not running'
        else
            echo "Redis is running ($PID)"
        fi
        ;;
    restart)
        $0 stop
        $0 start
        ;;
    *)
        echo "Please use start, stop, restart or status as first argument"
        ;;
esac
```

How fast is Redis?
------------------

> Redis includes the redis-benchmark utility that simulates running commands done by N clients at the same time sending M total queries (It is similar to the Apache's ab utility). Below you'll find the full output of a benchmark executed against a Linux box.

```
Usage: redis-benchmark [-h <host>] [-p <port>] [-c <clients>] [-n <requests]> [-k <boolean>]

 -h <hostname>      Server hostname (default 127.0.0.1)
 -p <port>          Server port (default 6379)
 -s <socket>        Server socket (overrides host and port)
 -a <password>      Password for Redis Auth
 -c <clients>       Number of parallel connections (default 50)
 -n <requests>      Total number of requests (default 100000)
 -d <size>          Data size of SET/GET value in bytes (default 2)
 --dbnum <db>       SELECT the specified db number (default 0)
 -k <boolean>       1=keep alive 0=reconnect (default 1)
 -r <keyspacelen>   Use random keys for SET/GET/INCR, random values for SADD
  Using this option the benchmark will expand the string __rand_int__
  inside an argument with a 12 digits number in the specified range
  from 0 to keyspacelen-1. The substitution changes every time a command
  is executed. Default tests use this to hit random keys in the
  specified range.
 -P <numreq>        Pipeline <numreq> requests. Default 1 (no pipeline).
 -q                 Quiet. Just show query/sec values
 --csv              Output in CSV format
 -l                 Loop. Run the tests forever
 -t <tests>         Only run the comma separated list of tests. The test
                    names are the same as the ones produced as output.
 -I                 Idle mode. Just open N idle connections and wait.

$ redis-benchmark -q -n 100000 -a password 

# Running only a subset of the tests 
$ redis-benchmark -t set,lpush -n 100000 -q
SET: 97847.36 requests per second
LPUSH: 100908.17 requests per second

$ redis-benchmark -n 100000 -q script load "redis.call('set', 'foo', 'bar')"
script load redis.call('set', 'foo', 'bar'): 97465.88 requests per second

# Select the size of the key space
$ redis-cli flushall # Delete all the keys of all the existing databases, not just the currently selected one. This command never fails.
$ redis-benchmark -t set -r 100000 -n 1000000
====== SET ======
  1000000 requests completed in 9.57 seconds
  50 parallel clients
  3 bytes payload
  keep alive: 1

99.97% <= 1 milliseconds
99.99% <= 2 milliseconds
100.00% <= 3 milliseconds
100.00% <= 3 milliseconds
104525.97 requests per second

$ redis-cli dbsize

# Using pipelining
# Redis supports pipelining, so it is possible to send multiple commands at once, a feature often exploited by real world applications. Redis pipelining is able to dramatically improve the number of operations per second a server is able do deliver. 
$ redis-benchmark -n 1000000 -t set,get -P 16 -q 
SET: 887311.44 requests per second
GET: 1162790.62 requests per second

# Pitfalls and misconceptions
# If you plan to compare Redis to something else, then it is important to evaluate the functional and technical differences, and take them in account.
    
    1.Redis is a server: all commands involve network or IPC round trips. 
    2.Redis commands return an acknowledgement
    3.Naively iterating on synchronous Redis commands does not benchmark Redis itself, but rather measure your network (or IPC) latency and the client library intrinsic latency. To really test Redis, you need multiple connections (like redis-benchmark) and/or to use pipelining to aggregate several commands and/or multiple threads or processes.
    4. Redis is an in-memory data store with some optional persistence options. If you plan to compare it to transaction servers (MySQL, PostgreSQL, etc...), then you should consider activating AOF and decide on a suitable fsync policy.
    5. Redis is, mostly, a single-threaded server from the POV of commands execution (actually modern versions of Redis use threads for different things).it is not designed to benifit from multiple CPU cores. People are supposed to launch serveral Redis instance to scale out on several cores if needed.It is not really fair to compare one single Redis instance to a multi-threaded data store.

# The redis-benchmark program is a quick and useful way to get some figures and evaluate the performance of a Redis instance on a given hardware.However, by default, it does not represent the maximum throughput a Redis instance can sustain. Actually, by using pipelining and a fast client (hiredis), it is fairly easy to write a program generating more throughput than redis-benchmark. 

# Factors impacting Redis performance 
    1. Network bandwidth and latency usually have a direct impact on the performance. It is a good practice to use the **ping** program to quickly check the latency between the client and server host is normal before launching the benchmark.In many real word scenarious, Redis throughput is limited by the network well before being limited by the CPU.
    2. CPU is another very important factor. Being single-threaded, Redis favors fast CPUs with large caches and not many cores.
    3. Speed of RAM and memory bandwidth seem less critical for global performance factor with redis-benchmark.
    4. Redis runs slower on a VM compared to running without virtualization using the same hardware.
    5. When the server and client benchmark programs run on the same box, both the TCP/IP loopback and unix domain sockets can be used. Depending on the platform, unix domain sockets can achieve around 50% more throughput than the TCP/IP loopback (on Linux for instance). The default behavior of redis-benchmark is to use the TCP/IP loopback.
    6. Being based on epoll/kqueue, the Redis event loop is quite scalable. Redis has already been benchmarked at more than 60000 connections, and was still able to sustain 50000 q/s in these conditions. 
```

Redis (Remote Dictionary Service)
---------------------------------
> Redis 本质上是一个数据结构服务器(data structures server)以高效的方式实现多种数据结构
```
- String字符串 [maximum length of 512MB]
    * Redis Strings Use Cases
    * Session Cache: which is crucial in that your users do not lose their data in the event they log out or lose connection
    * Queues: Any application that deals with traffic congestion, messaging, data gathering, job management, or packer routing should consider a Redis Queue.
    * Usage & Metered Billing: 
    * 字符串string是Redis最简单的数据结构，Redis所有的数据结构都是以唯一的key字符串作为名称，然后通过这个唯一的key值来获取响应的value数据，不同类型的数据结构的差异就在于value的结构不一样.
    * Redis字符串是动态字符串，内部结构实现类似Java的ArrayList,采用预分配冗余空间的方法来减少内存的频繁分配。内部当前字符串实际分配的空间capacity一般要高于实际字符串长度len,当字符串长度小于1M时，扩容都是加倍现有的空间，如果超过1M，扩容一次只会多扩1M空间,字符串最大长度为512M.
    * 字符串是由多个字节组成，每个字节是由8个bit组成，如此便可以将一个字符串看成很多bit的组合.bitmap[位图]数据结构
    * Strings are the most basic kind of Redis value. Redis Strings are binary safe, this means that a Redis string can contain any kind of data, for instance a JPEG image or a serialized Ruby object.
    * A String value can be max 512 Megabytes in length. 
    * Use Strings as atomic counters using commands in the INCR family: INCR, DECR, INCRBY. 
    * Append to strings with the APPEND command.
    * Use Strings as a random access vectors with GETRANGE and SETRANGE.
    * Encode a lot of data in little space, or create a Redis backed Bloom Filter using GETBIT and SETBIT.
```
健值对
192.168.1.215:6379[1]> set name codehole
OK
192.168.1.215:6379[1]> get name
"codehole"
192.168.1.215:6379[1]> exists name
(integer) 1
192.168.1.215:6379[1]> del name
(integer) 1
192.168.1.215:6379[1]> get name
(nil)
批量健值对
192.168.1.215:6379[1]> set name1 codehole
OK
192.168.1.215:6379[1]> set name2 holycoder
OK
192.168.1.215:6379[1]> mget name1 name2 name3
1) "codehole"
2) "holycoder"
3) (nil)
192.168.1.215:6379[1]> mset name1 boy name2 girl name3 unknown
OK
192.168.1.215:6379[1]> mget name1 name2 name3
1) "boy"
2) "girl"
3) "unknown"
192.168.1.215:6379[1]>
过期和Set命令扩展
192.168.1.215:6379[1]> set name codehole
OK
192.168.1.215:6379[1]> get name
"codehole"
192.168.1.215:6379[1]> expire name 5  # 5s 过期
(integer) 1
192.168.1.215:6379[1]> get name
(nil)
192.168.1.215:6379[1]> setex name 5 codehole  # 5s后过期，等价于set+expire
OK
192.168.1.215:6379[1]> get name
"codehole"
192.168.1.215:6379[1]> get name
(nil)
192.168.1.215:6379[1]> setnx name codehole # 如果name不存在就执行set创建
(integer) 1
192.168.1.215:6379[1]> get name
"codehole"
192.168.1.215:6379[1]> setnx name holycoder
(integer) 0  # 因为name已经不存在，所以set创建不成功
192.168.1.215:6379[1]> get name
"codehole"  # 没有更改
计数--整数进行自增操作,自增范围是signed long的最大最小值，超过这个值，Redis会报错
192.168.1.215:6379[1]> set age 30
OK
192.168.1.215:6379[1]> incr age
(integer) 31
192.168.1.215:6379[1]> incrby age 5
(integer) 36
192.168.1.215:6379[1]> incrby age -5
(integer) 31
192.168.1.215:6379[1]> set codehole 9223372036854775807  # Long.Max = 2̂63 -1 
OK
192.168.1.215:6379[1]> incr codehole
(error) ERR increment or decrement would overflow
```
- List列表: Lists contain strings that are sorted by their insertion order. 
    * LPUSH command: insert an element an the head 
    * RPUSH command: insert at the tail
    Redis List Use Cases:
      - Social Networking Sites: Redis Lists to populates timelines or homepage feeds. 
      - RSS Feeds: 
      - LeaderBoards:  积分榜
    * Redis的列表相当于Java语言中的LinkedList,Redis的list的插入和删除操作非常快，时间复杂度O(1),但是索引定位很慢，时间复杂度为O(n).当列表弹出最后一个元素之后，该数据结构自动被删除，内存被回收
    * Redis列表结构常用来做异步队列使用，将需要延后处理的任务结构序列化字符串塞进Redis的列表，另一个线程从这个列表中轮询数据进行处理
    * lindex: 相当于Java链表的get(int index)方法，需要对链表进行遍历，性能随着参数index增大而变差
    * ltrim: start_index和end_index定义一个区间，区间外的值删除，可以通过ltrim实现一个定长的链表, index可以是负数
    * Redis
      列表底层存储使用的快速链表quicklist的结构，首先在列表元素较少的情况下使用一块连续的内存存储，这个结构是ziplist，压缩列表，将所有元素紧挨着一起存储，分配的是一块连续的内存，当数量比较大的时候才会改成quicklist，因为普通链表需要附加指针空间太大，比较浪费空间，而且会加重内存的碎片化。所以Redis将链表和ziplist结合起来组成quicklist，将多个ziplist使用双向指针串联使用，既满足快速的插入删除性能，又不会出现太大的空间冗余.
```
队列: 右边进左边出
192.168.1.215:6379[1]> rpush books python java golang
(integer) 3
192.168.1.215:6379[1]> llen books
(integer) 3
192.168.1.215:6379[1]> lpop books
"python"
192.168.1.215:6379[1]> lpop books
"java"
192.168.1.215:6379[1]> lpop books
"golang"
192.168.1.215:6379[1]> lpop books
(nil)
栈: 右边进右边出
192.168.1.215:6379[1]> rpush books python java golang
(integer) 3
192.168.1.215:6379[1]> llen books
(integer) 3
192.168.1.215:6379[1]> rpop books
"golang"
192.168.1.215:6379[1]> rpop books
"java"
192.168.1.215:6379[1]> rpop books
"python"
192.168.1.215:6379[1]> rpop books
(nil)
List操作
192.168.1.215:6379[1]> rpush books python java golang
(integer) 3
192.168.1.215:6379[1]> lindex books 1  # O(n) 慎用
"java"
192.168.1.215:6379[1]> lrange books 0 -1  # 获取所有元素 O(n) 慎用
1) "python"
2) "java"
3) "golang"
192.168.1.215:6379[1]> ltrim books 1 -1  # O(n) 慎用
OK
192.168.1.215:6379[1]> lrange books 0 -1
1) "java"
2) "golang"
192.168.1.215:6379[1]> ltrim books 1 0  # 清空整个列表,因为区间范围长度为负
OK
192.168.1.215:6379[1]> llen books
(integer) 0
```
- Hashes: 
    * 2^32-1: (more than 4 billion) 
    * Redis的字典相当于Java语言中的HashMap，属于无序字典，内部实现同Java中HashMap同样的(数组+链表二维)结构，第一维hash的数组位置碰撞时，就会将碰撞的元素使用联表串联起来.
    * Redis的字典值只能是字符串，Java的HashMap的字典很大时，rehash是耗时的操作,需要一次性全部rehash，Redis为了高性能，不能阻塞服务，采用渐进式rehash策略.渐进式rehash会在rehash的同时，保留新旧两个hash结构，查询时同时查询两个hash结构，然后在后续定时任务以及hash操作指令中，循序渐进将旧hash的内容一点点迁移到新的hash结构中，当搬迁完成后，就会使用新的hash结构取而代之.
    * hash移除最后一个元素之后，该数据结构自动被删除，内存被回收
    * hash结构的存储消耗要高于单个字符串
    * Redis Hashes Use Case:
      * User Profiles: 
      * User Posts: 
```
hash 字典
192.168.1.215:6379[1]> hset books java "think in java"  # 命令行的字符串如果包含空格要用引号括起来
(integer) 1
192.168.1.215:6379[1]> hset books golang "concurrency in go"
(integer) 1
192.168.1.215:6379[1]> hset books python "python cookbook"
(integer) 1
192.168.1.215:6379[1]> hgetall books  # entries(), key和value间隔出现
1) "java"
2) "think in java"
3) "golang"
4) "concurrency in go"
5) "python"
6) "python cookbook"
192.168.1.215:6379[1]> hlen books
(integer) 3
192.168.1.215:6379[1]> hget books java
"think in java"
192.168.1.215:6379[1]> hset books golang "learning go programming"
(integer) 0
192.168.1.215:6379[1]> hget books golang
"learning go programming"
192.168.1.215:6379[1]> hmset books java "effective java" python "learning python" golang "modern golang programming"
OK
192.168.1.215:6379[1]> hset user age 26  # hincrby 计数增加
(integer) 1
192.168.1.215:6379[1]> hincrby user age 1
(integer) 27
```
- Sets集合
    * Redis Sets are powerful data types intersections and unions.
    * take the same time to add or remove items in a set.
    * SADD 
    * Redis的集合相当于Java语言中HashSet, 内部实现相当于一个特殊的字典，字典中所有的value都是一个值NULL.
    * 集合中最后一个元素移除之后，数据结构自动删除，内存被回收
    * Redis Sets Use Case:
      * Analyzing Ecommerce Sales: 
      * IP Address Tracking: analyze all of the IP addresses that visited a specific website page 
```
set集合
192.168.1.215:6379[1]> sadd books python
(integer) 1
192.168.1.215:6379[1]> sadd books python  # 重复
(integer) 0
192.168.1.215:6379[1]> sadd books java golang
(integer) 2
192.168.1.215:6379[1]> smembers books   # 注意顺序，和插入的并不一致，因为set是无序的
1) "python"
2) "golang"
3) "java"
192.168.1.215:6379[1]> sismember books java  # 查询某个value是否存在，相当于contains(o)
(integer) 1
192.168.1.215:6379[1]> sismember books rust
(integer) 0
192.168.1.215:6379[1]> scard books  # 获取长度相当于count() 
(integer) 3
192.168.1.215:6379[1]> spop books  # 弹出一个值
"golang"
```
- Sorted Sets有序集合
    * Sorted Sets associate every member with a scores.
    * Redis的zset类似于Java的SortedSet和HashMap的结合体，一方面是一个set,保证内部value的唯一性,另一方面可以给每个value赋于一个score，代表这个value的排序权重，内部实现用的是一种叫做跳跃列表(skiplist)的数据结构
    * zset中的最后一个value被移除后，数据结构自动删除，内存被回收
    * zset 内部的排序功能是通过[跳跃列表]数据结构实现的，因为zset需要支持随机的插入和删除，所以不能使用数组表示。当新元素需要查询，首先要定位到特定位置的插入点，这样才能保证联表的有序，通常会使用二分查找寻找插入点，但是二分查找的对象必须是数组，只有数组才能支持快速位置定位，链表做不到.
    * 跳跃表采用随机策略来决定新元素可以兼职到第几层; L0层肯定是100%,L1层50%,L2层只有25%,L3层只有12.5%
    * Redis Sorted Sets Use Cases
      * Q&A Platforms: ensure the best quality content is listed at the top of the page.
      * Gaming App Scoreboards: Online gaming apps 
      * Task Scheduling Service: Redis Sorted Sets are a great tool for a task scheduling service. 
      * Geo Hashing: 
```
zset集合
192.168.1.215:6379[1]> zadd books 9.0 "think in java"
(integer) 1
192.168.1.215:6379[1]> zadd books 8.9 "java concurrency"
(integer) 1
192.168.1.215:6379[1]> zadd books 8.6 "java cookbook"
(integer) 1
192.168.1.215:6379[1]> zrange books 0 -1  # 按score排序列出，参数区间为排名范围
1) "java cookbook"
2) "java concurrency"
3) "think in java"
192.168.1.215:6379[1]> zrevrange books 0 -1  # 按score逆序列出,参数区间为排名范围
1) "think in java"
2) "java concurrency"
3) "java cookbook"
192.168.1.215:6379[1]> zcard books  # 相当于count() 
(integer) 3
192.168.1.215:6379[1]> zscore books "java concurrency"  # 获取指定value的score 
"8.9000000000000004"  # 内部的score使用double类型进行存储，所以存在小数点精度问题
192.168.1.215:6379[1]> zrank books "java concurrency"  # 排名
(integer) 1
192.168.1.215:6379[1]> zrangebyscore books 0 8.91  # 根据分值区间遍历 zset 
1) "java cookbook"
2) "java concurrency"
192.168.1.215:6379[1]> zrangebyscore books -inf 8.91 withscores  # 根据分值区间(-∞, 8.91] 遍历zset，同时返回score值，inf代表infinite, 无穷大
1) "java cookbook"
2) "8.5999999999999996"
3) "java concurrency"
4) "8.9000000000000004"
192.168.1.215:6379[1]> zrem books "java concurrency"  # 删除value 
(integer) 1
192.168.1.215:6379[1]> zrange books 0 -1
1) "java cookbook"
2) "think in java"
192.168.1.215:6379[1]>
```
- 容器型数据结构
    * list/set/zset/hash 这四种数据结构是容器型数据结构
        - create if not exitst: 如果容器不存在，则创建，再进行操作
        - drop if no elements : 如果容器内没有元素，则立即删除元素，释放内存 
- 过期时间
    * Redis 所有数据结构都可以设置过期时间，Redis会自动删除响应的对象,需要注意，过期是以对象为单位，比如hash过期是整个hash对象的过期，而不是其中某个子key 
    * 如果一个字符串已经设置了过期时间，然后set方法会覆盖掉原有的过期时间设置
```
过期时间
192.168.1.215:6379[1]> set codehole yoyo
OK
192.168.1.215:6379[1]> expire codehole 600
(integer) 1
192.168.1.215:6379[1]> ttl codehole
(integer) 597
192.168.1.215:6379[1]> set codehole yoyo
OK
192.168.1.215:6379[1]> ttl codehole
(integer) -1
```

Redis Data Structure Internal implementation
--------------------------------------------
* Memory efficiency: 存储效率
    - Redis是专用于存储数据，对于计算机资源的主要消耗就在于内存的占用，因此节省内存是非常重要的方面，这意味着Redis一定要非常精细地考虑压缩数据、减少内存碎片等问题
* Fast reponse time: 快速响应时间
    - 与快速响应时间相对的是高吞吐量(high throughout). Redis是用于提供在线访问，对于单个请求的响应时间要求很高，因此，快速响应时间是比高吞吐量更重要。
* Single-threaded:单线程 
    - Redis的性能瓶颈不在于CPU资源、而在于内存访问和网络I/O，采用单线程的设计带来的好处、极大简化数据结构和算法实现，相反Redis通过异步I/O和pipeline机制实现高速并发访问
* dict 
    - dict是一个维护key-value映射关系的数据结构，Redis中
* sds
* ziplist 
* quicklist 
* skiplist 
```

```

分布式锁
--------
> 分布式应用进行逻辑处理时经常会遇到并发问题，比如一个操作要修改用户状态，修改状态需要先读取用户状态，在内存里进行修改，改完再存回去,如果这样的操作同时进行，就会出现并发问题，因为读取和保存状态两个操作不是原子操作(原子操作是指不会被线程调度机制打断的操作，这种操作一旦开始就一直运行到结束，中间不会有任何的context
> switch线程切换)
```
分布式锁就是为了解决并发执行的问题，Redis分布式锁使用很广泛。一般首先setnx (set if not exist)指令，然后del指令删除
192.168.1.215:6379[1]> setnx lock:chyiyaqing true
(integer) 1
192.168.1.215:6379[1]> expire lock:chyiyaqing 5
(integer) 1
... do something critical ... 
192.168.1.215:6379[1]> del lock:chyiyaqing
(integer) 1

如果逻辑执行到中间出现异常，可能回导致del指令没有执行，就会陷入死锁，锁永远得不到释放
所以我们在拿到锁之后，设置过期时间，这样即使中间出现异常也可以保证5秒之后锁自动释放
如果在setnx和expire之间服务器进程突然挂掉，就会导致expire得不到执行，也会造成死锁;问题根源在于setnx和expire两条指令不是原子指令。Redis事务特点是全部执行或全部放弃。
Redis2.8版本中加入set指令的扩展参数，是的setnx和expire指令可以一起执行

192.168.1.215:6379[1]> set lock:chyidl true ex 5 nx  # setnx 和expire组合一起原子执行，分布式锁的基础
OK
... do something critical ... 
192.168.1.215:6379[1]> del lock:chyidl
(integer) 0

超时问题:
    Redis分布式锁不能解决超时问题，如果在加锁和释放锁之间的逻辑执行过长，以至于超出锁的超时限制，就会出现问题，因为第一个线程持有锁过期，第一个线程逻辑还没有执行完，第二个线程就提前获取锁，导致代码不能严格的串行执行,为了避免出现上面问题，Redis分布式锁不能用于较长时间的任务。
解决办法：为set指令的value参数设置一个随机数，释放锁时先匹配随机数是否一致，然后再删除key,这是为了确保当前线程占用的锁不会被其他线程释放，除非这个锁被服务器释放，但是匹配value和删除key不是一个原子操作，Redis也没有提供类似于delifequals这样的指令.需要使用Lua
# delifequals 
if redis.call("get", KEYS[1]) == ARGV[1] then 
    return redis.call("del", KEYS[1])
else
    return 0 
end 

可重复锁:
    线程在持有锁的情况下再次请求加锁，如果一个锁支持同一个线程的多次加锁，那么这个锁就是可重入，Java语言中ReentrantLock就是可重入锁，Redis分布式锁如果要支持可重入，需要对客户端set方法进行包装，使用线程Threadlocal变量存储当前持有锁的计数. 
```
- [reentrantlock.py](root/ilikeit/RedisCrashCourse/script/py/reentrantlock.py)
- [RedisWithReentrantLock.java](root/ilikeit/RedisCrashCourse/script/java/RedisWithReentrantLock.java)
```


```

延时队列
--------
```
消息中间件 RabbitMQ, Kafka增加异步消息传递功能，Redis构建的消息队列不是专业的消息队列，没有非常多的高级特性，没有ACK保证。

Redis list列表数据结构常用来作为异步消息队列使用，使用rpush/lpush 操作入队列，使用lpop和rpop出队列.
如果Redis队列中为空，客户端可能会陷入pop死循环，不停的pop没有数据，这样会浪费生命的轮询，空轮训会拉高客户端的CPU，QPS.

使用blpop/brpop代替lpop/rpop,阻塞读队列.此处注意--空闲连接的问题,如果线程一直阻塞blocking,Redis客户端连接就成为闲置连接，闲置过久，服务器会主动断开连接，减少闲置资源占用，这时候blpop/brpop会抛出异常.此处便携客户端消费者需要捕获异常，而且需要重试连接.

sleep会阻塞当前的消息处理线程,会导致队列的后续消息处理出现延迟.

延迟队列可以通过Redis的zset(有序列表)来实现，将消息序列化成一个字符串作为zset的value,消息到期处理时间作为score.然后使用多线程轮询zset获取到期的任务进行处理，多线程保障可用性，因为使用多线程需要考虑并发争抢任务，避免不能被多次执行.

优化: 可以使用lua scripting 优化将zrangebyscore和zrem在服务端进行原子化操作，这样多个进程之间争抢任务就不会出现浪费.
```
```
192.168.1.243:6379[1]> rpush notify-queue apple banana pear
(integer) 3
192.168.1.243:6379[1]> llen notify-queue
(integer) 3
192.168.1.243:6379[1]> lpop notify-queue
"apple"
192.168.1.243:6379[1]> llen notify-queue
(integer) 2
192.168.1.243:6379[1]> lpop notify-queue
"banana"
192.168.1.243:6379[1]> llen notify-queue
(integer) 1
192.168.1.243:6379[1]> lpop notify-queue
"pear"
192.168.1.243:6379[1]> llen notify-queue
(integer) 0
192.168.1.243:6379[1]> lpop notify-queue
(nil)
```

位图 - 数据结构
---------------
```
Redis提供位图数据结构，其实就是普通的字符串，也就是byte数组.可以使用普通的get/set直接获取和设置整个位图的内容，也可以使用位图操作getbit/setbit等将byte数组看成位数组来处理.

Redis位数组是自动扩展，如果设置某个偏移位置超过现有的内容范围就会自动将位数组进行零扩充.
Redis提供位图统计执行bitcount和位图查找bitpos, bitcount用来统计指定位置范围内1的个数，bitpos用来查找指定范围内出现第一个0或1的位置
    bitcount统计用户一共签到多少天
    bitpos指令查找用户从那一天开始第一次签到,如果指定范围参数[start, end]，就可以统计某一个时间范围内用户签到多少天。
    start和end参数是字节索引，也就是说指定的位参数必须是8的倍数.

bitfield: 三个子指令,分别是get/set/incrby都可以对指定片段进行读写,但是最多只能处理64个连续的位,如果超过64位，就需要使用多个子指令，bitfiled可以一次执行多个子指令.
BITFILED command supports different subcommands:
    SET <type> <offset> <value> -- Set the specified value and return its previous value. 
    SET <type> <offset> - GET the specified value. 
    INCRBY <type> <offset> <increment> -- Increment the specified counter.
    OVERFLOW SAT - Saturation, so that overflowing in one direction or the other, will saturate the integer to its maximum value in the direction of the overflow.
    OVERFLOW WRAP - This is usual wrap around, but the interesting thing is that this also works for signed integers, by wrapping towards the most negative or most positive values.
    OVERFLOW FALT - In this mode the operation is not performed at all if the value would overflow.
```
```
使用位操作将字符串设置为hello(不是直接使用set指令)首先需要得到hello的ASCII码，用Python命令行可以很方便地得到每个字符的ASCII的二进制值
Python 3.7.4 (default, Sep  7 2019, 18:27:02)
[Clang 10.0.1 (clang-1001.0.46.4)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> bin(ord('h'))
'0b1101000'     #高位 -> 地位
>>> bin(ord('e'))
'0b1100101'
>>> bin(ord('l'))
'0b1101100'
>>> bin(ord('l'))
'0b1101100'
>>> bin(ord('o'))
'0b1101111'
>>>
使用redis-cli设置第一个字符,hello(0110100001100101011011000110110001101111),位数组的顺序和字符位的顺序是相反的。
192.168.1.243:6379[1]> setbit str 1 1
0
192.168.1.243:6379[1]> setbit str 2 1
0
192.168.1.243:6379[1]> setbit str 4 1
0
192.168.1.243:6379[1]> setbit str 9 1
0
192.168.1.243:6379[1]> setbit str 10 1
0
192.168.1.243:6379[1]> setbit str 13 1
0
192.168.1.243:6379[1]> setbit str 15 1
0
192.168.1.243:6379[1]> setbit str 17 1
0
192.168.1.243:6379[1]> setbit str 18 1
0
192.168.1.243:6379[1]> setbit str 20 1
0
192.168.1.243:6379[1]> setbit str 21 1
0
192.168.1.243:6379[1]> setbit str 25 1
0
192.168.1.243:6379[1]> setbit str 26 1
0
192.168.1.243:6379[1]> setbit str 28 1
0
192.168.1.243:6379[1]> setbit str 29 1
0
192.168.1.243:6379[1]> setbit str 33 1
0
192.168.1.243:6379[1]> setbit str 34 1
0
192.168.1.243:6379[1]> setbit str 36 1
0
192.168.1.243:6379[1]> setbit str 37 1
0
192.168.1.243:6379[1]> setbit str 38 1
0
192.168.1.243:6379[1]> setbit str 39 1
0
192.168.1.243:6379[1]> get str
hello
192.168.1.243:6379[1]> getbit str 1    # 获取某个具体位置的值 0/1 
1
192.168.1.243:6379[1]> set str1 hello  # 整存 
OK
192.168.1.243:6379[1]> getbit str1 1   # 获取某个位置的值 0/1 
1
192.168.1.243:6379[1]>
注意，对应位的字节是不可打印字符，redis-cli会显示该字符的16进制形式 

bitcount 指令和bitpos指令
192.168.1.243:6379[1]> bitcount str
21
192.168.1.243:6379[1]> bitcount str 0 0      # 第一个字符中1的位数
3   
192.168.1.243:6379[1]> bitcount str 0 1      # 前两个字符中1的位数 
7
192.168.1.243:6379[1]> bitpos str 0          # 第一个0位
0
192.168.1.243:6379[1]> bitpos str 1          # 第一个1位
1
192.168.1.243:6379[1]> bitpos str 1 1 1      # 从第二个字符算起，第一个1位
9
192.168.1.243:6379[1]> bitpos str 1 2 2      # 从第三个字符算起，第一个1位
17
192.168.1.243:6379[1]>

192.168.1.243:6379[1]> set w hello
OK
192.168.1.243:6379[1]> bitfield w get u4 0      # 从第一位开始取4位，结果是无符号数u 
6
192.168.1.243:6379[1]> bitfield w get u3 2      # 从第三位开始取3位，结果是无符号数u 
5
192.168.1.243:6379[1]> bitfield w get i4 0      # 从第一个位开始取4位，结果是有符号i
6
192.168.1.243:6379[1]> bitfield w get i3 2      # 从第三个位开始取3位，结果是有符号数i 
-3
192.168.1.243:6379[1]>
所谓的有符号数是指获取的位数组中第一个位是符号位，剩下的才是值，如果第一位是1，就是负数，无符号表示非负数，没有符号位，获取的位数组全部都是值。有符号数最多可以获取64位，无符号数只能获取63位（因为Redis协议中integer是由符号数，最大64位，不能传递64位无符号值）如果超过位数限制，Redis就会参数出错.
```

HyperLogLog
-----------
```
UV: Unique visitor: 通过互联网访问、浏览网页的自然人。一天内同一访客多次访问仅计算一个UV
IP: Internet Protocol: 独立IP访问过某站点的IP总数,一天内相同IP地址只被计算一次
PV: Page View: 页面的浏览量或点击量
VV: Visit View 统计所有访客1天内访问网站的次数
HyperLogLog数据结构提供不精确的去除重复计数方案.准确误差0.81% 
HyperLogLog提供两个指令pfadd, pfcount
    pfadd:增加计数
    pfcount:获取计数
```
- [hyperloglog.py](root/ilikeit/RedisCrashCourse/script/py/hyperloglog.py)



<antirez> blog
---------------

* English has been my pain for 15 years
-------------------------------------
```
```

Redis Review Source Code
------------------------
```
```

Lua Programming Language
------------------------
> Lua is a language which has been around since 1993. Its origins in engineering made for a compact language which could be embedded in other applications.
```
```

Redis Best Practices
====================

Indexing Patterns
-----------------
> Conceptually, Redis is based on the key/value database paradigm. Every piece of data is associated with a key, either directly or indirectly. If you want to retrieve data based on anything besides the key, you'll need to implement an index that leverages one of the many data types available in Redis.

* Sorted Sets as indexes
> Sorted Sets (ZSETs) are a native Redis data type that can be thought of a set of unique memebers (repeats are not stored) with each member being attached to a number (termed score) that acts as a natural sorting mechanism.
> While members cannot be repeated, any number of members can share the same score. 
> With relatively low time complexity to add, remove and retrieve ranges (by rank or score), this lends itself naturally to being an index.
```
ZADD key [NX|XX] [CH] [INCR] score member [score member ...]
#   Time complexity: O(log(N)) for each item added, where N is the number of elements in the sorted set.
# Adds all the specified members with the specified scores to the sorted set stored at key.
# The score values be the string representation of a double precision floating point number. +inf and -inf values are valid values as well.
#   XX: Only update elements that already exist. Never add elements 
#   NX: Don't update already existing elements. Always add new elements.
#   CH: Modify the return value from the number of new elements added, to the total number of elements changed(CH is an abbreviation of changed).
#       Note: normally the return value of ZADD only counts the number of new elements added
#   INCR: When this option is specified ZADD acts like ZINCRBY. Only one score-element pair can be specified in this mode. 
# Redis sorted sets use a double 64-bit floating point number to represent the score. IEEE 754 floating point number: (-2^53 ~ 2^53)

```

Communication Patterns 
----------------------
> 

Data Storage Patterns
---------------------

Time Series Patterns
--------------------

Basic Rate Limiting Pattern
---------------------------

Bloom Filter Pattern
--------------------

Counting
--------

Redis 面试问题
-------------
```
1. Redis能用来做什么?
    缓存：是Redis使用最多的领域，相比Memcache更加容易理解、使用和控制
    分布式锁：
    Redis业务应用范围非常广泛：
        点赞数、评论数、点击数 hash
        ID列表(排序) zset
        标题、摘要、作者和封面信息用于列表展示 hash 
        缓存近期热帖，减少数据库压力 hash 
        实际情况下需求可能没有太多，因为请求压力不大的情况下，很多数据都可以直接从数据库中查询，但请求压力大，以前通过数据库直接存取的数据则必须要挪到缓存里

2. Redis有哪些数据结构?
    字符串String, 字典Hash, 列表List, 集合Set, 有序集合SortedSet 
    HyperLogLog, Geo, Pub/Sub,
    Bloom Filter, Redis Search, Redis-ML 

3. Redis分布式锁？
    > setnx争抢锁，抢到之后，expire给锁加上一个过期时间，防止忘记释放锁 
    > 如果在setnx之后，expire之前进程意外Crash或者重启维护，会怎样？
    < 同时把setnx和expire合成一条指令使用 

4. 假如Redis里面有1亿个key,其中有10w个key是以某种固定的前缀开头，如何将他们全部找出来?
    使用keys指令扫描指定模式的key列表,由于Redis是单线程，keys指令会导致线程阻塞一段时间，线上服务会停顿，知道指令执行完毕，服务才回复，这个时候可以使用scan指令，scan指令可以无阻塞的提取出指定模式的可以列表，但是会有一定的重复概率，在客户端做一次去重操作，整体花费会比keys指令时间长

5. 如果使用redis做异步队列？
    一般使用list结构作为队列，rpush生产消息，lpop消费消息，当lpop没有消息的时候，适当sleep重试
    list指令中还有一个blpop,在没有消息可消费的情况下会阻塞直到消息到来
    如何生产一次消费多次？可以使用pub/sub主题订阅模式，可以实现1:N的消息队列
    pub/sub有什么缺点？在消费者下线的情况下，生产的消息会丢失，可以使用专门的消息队列RabbitMQ
    > redis如何实现延迟队列？可以使用sorted set,使用时间戳作为score.消息内容作为key调用zadd来生产消息，消费者使用zrangebyscore指令获取N秒之前的数据轮询进程处理

6. 如果大量的Key需要设置同一时间过期，需要注意什么?
    如果大量的Key过期时间设置的过于集中，到过期时间，redis可能出现短暂的卡顿现象，一般需要在时间上加上一个随机值，使得过期时间分散一些

7. Redis如何做持久化?
    bgsave做镜像全量持久化, aof做增量持久化，因为bgsave会耗费较长时间，在停机时候会导致大量丢失数据，所以需要aof配合使用。在redis实例重启时，优先使用aof来恢复内存的状态，如果没有aof日志，就会使用rdb文件来恢复.
    Redis会定期做aof重写，压缩aof文件日志大小，Redis4.0之后有混合持久化的功能，将bgsave的全量和aof的增量做了融合处理，这样即保证恢复的效率又兼顾数据的安全
    取决于aof日志sync 属性的配置，如果不要求性能，在每次写指令时都sync一下磁盘，就不会丢失数据，但是高性能的要求下每次都sync是不现实的，一般都是定时sync,比如1s1次，这时候最多会丢失1s数据.
    bgsave原理是什么： fork, cow,fork是指redis通过创建子进程来进行bgsave操作, cow指copy on write，子进程创建后，父子进程共享数据段，父进程继续提供读写服务，写脏的页面数据会逐渐和子进程分离开来

8. Pipeline的优势？
    可以将多次I/O往返的时间缩减为一次，前提是pipeline执行的指令之间没有因果相关性，使用redis-benchmark进行压力测试的时候可以发现影响热地说QPS峰值的一个重要因素是pipeline批次指令的数目.

9. Redis同步机制了解么?
    Redis可以使用主从同步，从从同步，第一次同步时，主节点做一次bgsave,并同时将后续修改操作记录到内存buffer,待完成后将rdb文件全量同步复制到节点，复制节点接受完成后将rdb镜像加载到内存，加载完成后，在通知主节点将期间修改的操作记录同步到复制节点进行重放就完成同步过程.

10. 是否使用过Redis集群，集群的原理是什么?
    Redis Sentinal - 高可用，在master宕机时会自动将slave提升为master,继续提供服务
    Redis Cluster  - 扩展性，单个redis内存不足时，使用cluster进行分片存储.

11. 缓存穿透，缓存击穿，缓存雪崩?
    设计缓存系统，需要考虑缓存穿透、缓存击穿、缓存失效雪崩
    
    - 缓存穿透是指查询一个一定不存在的数据，由于缓存是不命中时被动写，并且出于容错考虑，如果从存储层查不到数据则不写入缓存。这将导致这个不存在的数据每次请求都要到存储层去查询，失去了缓存的意义，在流量大时，可能DB就挂掉，要是有人利用不存在的Key频繁攻击应用，这就是漏洞
        > 有很多的方法有效的解决缓存穿透的问题，最常见的则是采用布隆过滤器，将所有的可能存在的数据哈希到一个足够大的bitmap中，一个一定不存在的数据就会被bitmap拦截掉，从而避免对底层存储系统的查询压力.
        > 另一种简单粗暴的方法,如果一个查询返回的数据为空(不管是数据不存在还是系统故障)，仍然把这个空结果进行缓存，但他的过期时间会很短，最长不超过五分钟
    
    - 缓存雪崩:是指我们设置缓存时采用相同的过期时间，倒置缓存在某一个时刻同时失效，请求全部转发到DB，DB瞬时压力过重雪崩.
        > 缓存失效时的雪崩效应对底层系统的冲击非常可怕，大多数系统设计者考虑用加锁或者队列的方式保证缓存单线程(进程)写，从而避免失效时大量的并发请求落到底层存储系统上，
        >在原有的失效时间基础上增加一个随机值，比如1-5分钟随机值，这样每个缓存的过期时间的重复率就会降低，就很难引起集体失效的事件
    
    - 缓存击穿: 对于设置过期时间的key, 如果这些key可能会在某些时间点被超高并发地访问，是一种非常热点的数据，这时候，需要考虑一个问题，缓存被击穿的问题，这个和导致雪崩的区别在于这里针对某一个Key缓存，前者则是很多key。缓存在某个时间点过期的时候，恰好在这个时间点对这个Key有大量的并发请求过来，这些请求发现缓存过期一般都会从后端加载数据并回设到缓存，这个时候大并发的请求可能会瞬间把后端DB压垮.
        > 使用互斥锁(mutex key):业界比较常用的做法是使用mutex,就是在缓存失效的时候(判断拿出的值为空)，不是立即去load db.而是先使用缓存工具的某些带成功操作返回值的操作(Redis的SETNX或者Memcache的ADD)去SET一个mutex key.当操作返回成功时，在进行load db的操作并会设缓存，否则，就重试整个get缓存的方法。
        > SETNX是(SET IF NOT EXISTS)就是只有不存在的时候才设置，可以利用它实现锁的效果，
public String get(key) {
    String value = redis.get(key);
    if (value == null) { // 代表缓存值过期
        // 设置3min的超时时间，防止del操作失败的时候，下次缓存过期一直不能load db 
        if (redis.setnx(key_mutex, 1, 3 * 60) == 1) { // 代表设置成功
            value = db.get(key);
            redis.set(key, value, expire_secs);
            redis.del(key_mutex);
        } else {    // 这时候代表其他线程已经load
            sleep(50);
            get(key);   // 重试
        }
    }
}

对于缓存系统常用的缓存满了，和数据丢失问题，需要根据具体业务分析，通常采用LRU策略处理溢出，Redis的RDB和AOF持久化策略来保证一定情况下的数据安全.
```

A Speed Guide To Redis Lua Scripting
------------------------------------
* What's Lua?
> Lua is a language which has been around since 1993. Its origins in engineering made for a compact language which could be embedded in other applications. Nginx, Redis

* What does Redis let you do with Lua?
```
localhost:6379> EVAL 'local val="Hello Compose" return val' 0
"Hello Compose"
```

<antirez - 安迪雷斯>
-------------------
> 
```
./redis-benchmark --threads 8 -c 150 -t get -n 10000000 
```

Appendix
--------
* IEEE 754 
> The IEEE Standard for Floating-Point Arithmetic is a technical standard for floating-point arithmetic established in 1985 by the Institute of Electrical and Electronics Engineers(IEEE).
```
```
