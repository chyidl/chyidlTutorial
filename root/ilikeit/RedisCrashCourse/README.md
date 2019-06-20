Redis Crash Course
==================

Introduction
------------
> Redis is an in-memory key-value store known for its flexibility, performance, and wide language support.

Install the Build and Test Dependecies
--------------------------------------
> In order to get the latest version of Redis, we will be compiling and installing the software from source. Before we download the code, we need to statisfy the build dependencies so that we can compile the software.

> To do this, we can install the **build-essential** meta-package from the repositiories. downloading the **tcl** package, which can use to test our binaries.

```
$ sudo apt-get update 
$ sudo apt-get install build-essential tcl make gcc 
```

Download, Compile, and Install Redis 
------------------------------------
```
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
