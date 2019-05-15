High Performance MySQL Third
============================

Chapter 1. MySQL Architecture and History
-----------------------------------------

* MySQL's Logical Architecture 
    - The topmost layer: connection handling, authentication, security 
```
Each client connection gets threads within the server process. The server caches threads, so they don't need to be created and destroyed for each new connection.

Authentication is based on username, host, password, port. Once a client has connected, the server verifies whether the client has privileges for each query.
```
    - The second layer: query parsing, analysis, optimization, caching, built-in function(e.g., dates, times, math, and encryption). Any functionality privided across storage engines lives at this level: stored procedures, triggers, and views
```
MySQL parses queries to create an internal structure (the parse tree), and then applies a variety of optimizations. These can include rewriting the query,determining the order in which it will read tables, choosing which index to use, and so on.

Concurrency Control :
    MySQL has to do this at two levels: the server level and the storage engine level.
    How MySQL deals with concurrent readers and writers

    Read/Write Locks: 
        These locks are usually known as shared locks and exclusive locks, or read locks and write locks.
        In the database world, locking happens all the time.
    
    Lock Granularity: 锁颗粒度
        Every lock operation--getting a lock, checking to see whether a lock is free, releasing a lock, and so on--has overhead.
        If the system speends too much time managing locks instead of storing and retrieving data, performance can suffer. 

        Table locks: 表锁
            The most basic locking strategy available in MySQL, and the one with the lowest overhead, is table locks.
            Write locks have a higher priority than read locks.

        Row locks: 行锁 
            Row-level locking is commonly known available in the InnoDB and XtraDB storage engine.
            Row locks are implemented in the storage engine, not the server
    
    Transactions: 事务 
        A transaction is a group of SQL queries that are treated atomically, 
    
    ACID: stands for Atomicity, Consistency, Isolation, and Durability. 
        Atomicity:原子性
        Consistency: 一致性 
        Isolation: 隔离型 
        Durability: 持久性

    Isolation Levels: 隔离级别 Lower isolation levels typically allow higher concurrency and have lower overhead.
        READ UNCOMMITED: transactions can view the results of uncommited transactions. (Reading uncommited data is also known as a dirty read 脏读)
        READ COMMITED: A transaction will see only those changes made by transactions that were already committed. (nonrepeatable read 不可重复读)
        REPEATABLE READ: It guarantees that any rows a transaction reads will "look the same" in subsequent reads within the same transaction, but in theory it still allows another tricky problem: phantom reads幻读; InnoDB and XtraDB solve the phantom read problem with multiversion concurrency control. REPEATABLE READ is MySQL default transaction isolation level. 
        SERIALIZABLE: The highest level of isolation, SERIALIZABLE places a lock on every row it reads.
    
    Deadlocks: 
        A deadlocks is when two or more transactions are mutually holding and requesting locks on the same resources, creating a cycle of dependencies.
        Deadlocks occur when transactions try to lock resources in a different order. 
        database systems implement various forms of deadlock detection and timeout. such as the InnoDB storage engine, will notice circular dependencies and return an error instantly.

    Transaction Logging: 
        Instead of updating the table on disk each time a change occurs, the storage engine can change its in-memory copy of the data.
        appending log event involves sequential I/O in one small area of the disk instead of random I/O in many places.
        (known as write-ahead logging)
    
    Transactions in MySQL:
        MySQL provides two transactional storage engines: InnoDB and NDB Cluster. 
        MySQL operates in AUTOCOMMIT mode by default.
            
            mysql> SHOW VARIABLES LIKE 'AUTOCOMMIT';
            +---------------+-------+
            | Variable_name | Value |
            +---------------+-------+
            | autocommit    | ON    |
            +---------------+-------+
            1 row in set (0.01 sec)
        Data Definition Language(DDL) commands: such as ALTER TABLE, LOCK TABLES.

            mysql> show variables like 'transaction_isolation';
            +-----------------------+-----------------+
            | Variable_name         | Value           |
            +-----------------------+-----------------+
            | transaction_isolation | REPEATABLE-READ |
            +-----------------------+-----------------+
            1 row in set (0.01 sec)
    
        InnoDB uses a two-phase locking protocol. It can acquire locks at any time during a transaction, but it does not release them until a COMMIT or ROLLBACL. It releases all the locks at the same time.

    Multiversion Concurrency Control: 
        Most of MySQL's transactional storage engines use row-locking mechanism and multiversion concurrency control(MVCC).
        MVCC works by keeping a snapshot of the data as it existed at some point in time.
        InnoDB implements MVCC by storing with each row two additional, hidden values that record when the row was created and when it was expired.
        MVCC works only with the REPEATABLE READ and READ COMMITED isolation levels.
```
    - The third layer: storage engines. They are responsible for storing and retrieving all data stored in MySQL.
```
    MySQL Storage Engines:
        MySQL stores each database (also called a schema) as a subdirectory of its data directory in the underlying filesystem.
        MySQL Table definition in a .frm file with the same name as the table.

        mysql> show table status like 'user' \G
        *************************** 1. row ***************************
                   Name: user
                 Engine: MyISAM
                Version: 10
             Row_format: Dynamic
                   Rows: 5   # For MyISAM and most other engines, this number is always accurate. For InnoDB, it is an estimate.
         Avg_row_length: 118 # bytes 
            Data_length: 592 # How much data (in bytes) the entire table contains.
        Max_data_length: 281474976710655 # The maximum amount of data this table can hold. This is engine-specific. 
           Index_length: 4096 # How much disk space the index data consumes 
              Data_free: 0
         Auto_increment: NULL # The next AUTO_INCREMENT value 
            Create_time: 2019-04-28 23:52:31
            Update_time: 2019-04-29 00:00:37
             Check_time: NULL # When the table was last checked using CHECK TABLE or myisamchk.
              Collation: utf8_bin # The default character set and collation for character columns in this table.
               Checksum: NULL
         Create_options:  # Any other optional that were specified when the table was created.
                Comment: Users and global privileges
        1 row in set (0.00 sec)
        
        InnoDB is the default transactional storage engine for MySQL and the most important and broadly useful engine overall.

        InnoDB's history:
            The modern version of InnoDB support new feature such as building indexes by sorting, the ability to drop and add indexes without rebuilding the whole table.

        InnoDB overview:
            InnoDB stores its data in a series of one or more data files that are collectively known as a tablespace.
            InnoDB uses MVCC to achieve high concurrency, and it implementes all four SQL standard isolation levels.
            InnoDB provides very fast primary key lookups. secondary indexes(indexes that aren't the primary key) contain the primary key columns.
            InnoDB has a veriety of internal optimizations. These include predictive read-ahead for prefetching data from disk, an adaptive hash index that automatically builds hash in-dexes in memory for very fast lookups, and an insert buffer to speed inserts.

    Selecting the Right Engine:
        Transactions:
            If application requires transactions, InnoDB (or XtraDB) is the most stable, well-integrated, proven choice. 
            MyISAM is a good choice if a task doesn't require transactions and issues primarily either SELECT or INSERT queries.

        Backups:
            If you need to perform online backups, you basically need InnoDB. 

        Crash recovery:
            MyISAM tables become corrupt more easily and take much longer to recover than InnoDB tables. In fact, this is one of the most important reasons why a lot of people use InnoDB when they don't need transactions.
    
    Table Conversions: 
        There are several ways to convert a tbale from one strage engine to another.
        ALTER TABLE: 
            mysql> ALTER TABLE mytable ENGINE = InnoDB; 
            It can tale a lot of time, MySQL will perform a row-by-row copy of your old table into a new table,
        Dump and Import:
            first dump the table to a text file using the mysqldump utility.
            second edit the dump file to adjust the CREATE TABLE statement.(be sure to change the table name, Because there is not exist same name in the same database; mysqldump default write a DROP TABLE command before the CREATE TABLE)
        CREATE and SELECT:
            mysql> CREATE TABLE innodb_table like myisam_table;
            mysql> ALTER TABLE innodb_table ENGINE=InnoDB;
            mysql> INSERT INTO innodb_table SELECT * FROM myisam_table;
    
    MySQL Development Model:
        MySQL remains GPL-licensed and open source, with the full source code(except for commerically licensed plugins, of course) available to the community.
```

Chapter 2 Benchmarking MySQL
----------------------------

* Benchmark:
    - benchmarking is not real. real-life workloads are nondeterministic, varying, and too complex to understand readily. 
    - Benchmarks are simpler, more directly comparable to each other, and cheaper and easier to run. And despite their limitations, benchmarks are useful.

* Becnmarking Strategies:
    - full-stack  benchmarking 
    - single component benchmarking 

* What to Measure:
    - Throughput:吞吐量is defined as the number of transactions per unit of time.
    - Response time or latency:响应时间和时延: It's common to use percentile response times instead.
    - Concurrency: 
        * HTTP is stateless and most users are simply reading what's displayed in their browsers, so this doesn't transalte into concurrency on the web server.
        * A more accurate measurement of concurrency on the web server is how many simultaneous requests are running at any given time.

* Capturing System Performance and Status 
    - Try to record status and performance metrics such as CPU usage, disk I/O, network traffic statistics, counters from SHOW GLOBAL STATUS; and so on.    
    - The default MySQL confirguration settings either, because they're turned for tiny applications that consume very little memory.

* Benchmarking Tools:
    - Full-Stack Tools:
        * db: is an Apache HTTP server benchmarking tool. It shows how many requests per second your HTTP server is capable of serving. It's a very simple tool, but its usefulness is limited because it just hamers one URL as fast as it can.
        * http_load: it is also designed to load a web server, but it's more flexible. 
        * JMeter: is a Java application that can load another application and measure its performance.JMeter is much more complex than ab and http_load. 

    - Single-Component Tools:
        * mysqlslap: simulates load on the server and reports timing information.
        * MySQLBenchmark Suite(sql-bench): 
        * Super Smack: 
        * Database Test Suite: 
        * Percona's TPCC-MySQL Tool: 
        * sysbench: 

* MySQL BENCHMARK() FUNCTION
```
mysql> SET @input := 'David Chyi';
Query OK, 0 rows affected (0.00 sec)

mysql> SELECT BENCHMARK(1000000, MD5(@input));
+---------------------------------+
| BENCHMARK(1000000, MD5(@input)) |
+---------------------------------+
|                               0 |
+---------------------------------+
1 row in set (0.94 sec)

mysql> SELECT BENCHMARK(1000000, SHA1(@input));
+----------------------------------+
| BENCHMARK(1000000, SHA1(@input)) |
+----------------------------------+
|                                0 |
+----------------------------------+
1 row in set (1.18 sec)

We don't use BENCHMARK() for real benchmarks.
```

Chapter 3 Profiling Server Performance
--------------------------------------




FAQ
===
![mysql_lock_wait_timeout.png](/imgs/ilikeit/MySQLCrashCourse/mysql_lock_wait_timeout.png?raw=true)
* MySQL Lock wait timeout exceeded; try restarting transaction 
    - SET VARIABLE innodb_lock_wait_timeout=100 for lock time to 100 sec. 
```
mysql> SET innodb_lock_wait_timeout=100;
Query OK, 0 rows affected (0.00 sec)

mysql> show variables like 'innodb_lock_wait_timeout';
+--------------------------+-------+
| Variable_name            | Value |
+--------------------------+-------+
| innodb_lock_wait_timeout | 100   |
+--------------------------+-------+
1 row in set (0.01 sec)

The transaction which is timeout, try to lock table which is hold by another process. and your timeout variable set with little number of second. so it show error. You can see more status by the command.

mysql> SHOW ENGINE INNODB STATUS\G
*************************** 1. row ***************************
    Type: InnoDB
    Name:
  Status:
    =====================================
    2019-04-30 13:25:57 0xffff6c53c1c0 INNODB MONITOR OUTPUT
    =====================================
    Per second averages calculated from the last 59 seconds
    -----------------
    BACKGROUND THREAD
    -----------------
    srv_master_thread loops: 68 srv_active, 0 srv_shutdown, 217 srv_idle
    srv_master_thread log flush and writes: 285
    ----------
    SEMAPHORES
    ----------
    OS WAIT ARRAY INFO: reservation count 281
    OS WAIT ARRAY INFO: signal count 258
    RW-shared spins 0, rounds 140, OS waits 68
    RW-excl spins 0, rounds 2795, OS waits 67
    RW-sx spins 17, rounds 510, OS waits 16
    Spin rounds per wait: 140.00 RW-shared, 2795.00 RW-excl, 30.00 RW-sx
    ------------
    TRANSACTIONS
    ------------
    Trx id counter 7094
    Purge done for trx's n:o < 7087 undo n:o < 0 state: running but idle
    History list length 22
    LIST OF TRANSACTIONS FOR EACH SESSION:
    ---TRANSACTION 562947959610280, not started
    0 lock struct(s), heap size 1136, 0 row lock(s)
    ---TRANSACTION 562947959609360, not started
    0 lock struct(s), heap size 1136, 0 row lock(s)
    ---TRANSACTION 562947959608440, not started
    0 lock struct(s), heap size 1136, 0 row lock(s)
    ---TRANSACTION 562947959607520, not started
    0 lock struct(s), heap size 1136, 0 row lock(s)
    ---TRANSACTION 562947959606600, not started
    0 lock struct(s), heap size 1136, 0 row lock(s)
    ---TRANSACTION 562947959605680, not started
    0 lock struct(s), heap size 1136, 0 row lock(s)
    ---TRANSACTION 562947959604760, not started
    mysql tables in use 1, locked 1
    0 lock struct(s), heap size 1136, 0 row lock(s)
    ---TRANSACTION 562947959603840, not started
    mysql tables in use 1, locked 1
    0 lock struct(s), heap size 1136, 0 row lock(s)
    ---TRANSACTION 562947959602920, not started
    0 lock struct(s), heap size 1136, 0 row lock(s)
    ---TRANSACTION 562947959602000, not started
    0 lock struct(s), heap size 1136, 0 row lock(s)
    ---TRANSACTION 562947959601080, not started
    0 lock struct(s), heap size 1136, 0 row lock(s)
    ---TRANSACTION 562947959600160, not started
    0 lock struct(s), heap size 1136, 0 row lock(s)
    ---TRANSACTION 562947959599240, not started
    0 lock struct(s), heap size 1136, 0 row lock(s)
    ---TRANSACTION 562947959598320, not started
    0 lock struct(s), heap size 1136, 0 row lock(s)
    ---TRANSACTION 562947959597400, not started
    0 lock struct(s), heap size 1136, 0 row lock(s)
    ---TRANSACTION 562947959596480, not started
    0 lock struct(s), heap size 1136, 0 row lock(s)
    ---TRANSACTION 562947959595560, not started
    0 lock struct(s), heap size 1136, 0 row lock(s)
    ---TRANSACTION 562947959594640, not started
    0 lock struct(s), heap size 1136, 0 row lock(s)
    ---TRANSACTION 562947959593720, not started
    0 lock struct(s), heap size 1136, 0 row lock(s)
    ---TRANSACTION 562947959592800, not started
    0 lock struct(s), heap size 1136, 0 row lock(s)
    --------
    FILE I/O
    --------
    I/O thread 0 state: waiting for completed aio requests (insert buffer thread)
    I/O thread 1 state: waiting for completed aio requests (log thread)
    I/O thread 2 state: waiting for completed aio requests (read thread)
    I/O thread 3 state: waiting for completed aio requests (read thread)
    I/O thread 4 state: waiting for completed aio requests (read thread)
    I/O thread 5 state: waiting for completed aio requests (read thread)
    I/O thread 6 state: waiting for completed aio requests (write thread)
    I/O thread 7 state: waiting for completed aio requests (write thread)
    I/O thread 8 state: waiting for completed aio requests (write thread)
    I/O thread 9 state: waiting for completed aio requests (write thread)
    Pending normal aio reads: [0, 0, 0, 0] , aio writes: [0, 0, 0, 0] ,
     ibuf aio reads:, log i/o's:, sync i/o's:
     Pending flushes (fsync) log: 0; buffer pool: 0
     282 OS file reads, 7508 OS file writes, 983 OS fsyncs
     0.02 reads/s, 16384 avg bytes/read, 69.51 writes/s, 5.41 fsyncs/s
     -------------------------------------
     INSERT BUFFER AND ADAPTIVE HASH INDEX
     -------------------------------------
     Ibuf: size 1, free list len 0, seg size 2, 0 merges
     merged operations:
      insert 0, delete mark 0, delete 0
      discarded operations:
       insert 0, delete mark 0, delete 0
       Hash table size 34679, node heap has 0 buffer(s)
       Hash table size 34679, node heap has 0 buffer(s)
       Hash table size 34679, node heap has 0 buffer(s)
       Hash table size 34679, node heap has 7 buffer(s)
       Hash table size 34679, node heap has 2 buffer(s)
       Hash table size 34679, node heap has 1 buffer(s)
       Hash table size 34679, node heap has 0 buffer(s)
       Hash table size 34679, node heap has 0 buffer(s)
       3966.92 hash searches/s, 242.61 non-hash searches/s
       ---
       LOG
       ---
       Log sequence number 82964197
       Log flushed up to   82964197
       Pages flushed up to 80863511
       Last checkpoint at  80245814
       0 pending log flushes, 0 pending chkp writes
       378 log i/o's done, 2.44 log i/o's/second
       ----------------------
       BUFFER POOL AND MEMORY
       ----------------------
       Total large memory allocated 137428992
       Dictionary memory allocated 451675
       Buffer pool size   8192
       Free buffers       3502
       Database pages     4680
       Old database pages 1707
       Modified db pages  310
       Pending reads      0
       Pending writes: LRU 0, flush list 0, single page 0
       Pages made young 0, not young 0
       0.00 youngs/s, 0.00 non-youngs/s
       Pages read 253, created 4427, written 6604
       0.02 reads/s, 41.25 creates/s, 64.68 writes/s
       Buffer pool hit rate 1000 / 1000, young-making rate 0 / 1000 not 0 / 1000
       Pages read ahead 0.00/s, evicted without access 0.00/s, Random read ahead 0.00/s
       LRU len: 4680, unzip_LRU len: 0
       I/O sum[0]:cur[0], unzip sum[0]:cur[0]
       --------------
       ROW OPERATIONS
       --------------
       0 queries inside InnoDB, 0 queries in queue
       0 read views open inside InnoDB
       Process ID=6039, Main thread ID=281472544002496, state: sleeping
       Number of rows inserted 138861, updated 0, deleted 0, read 9
       1374.93 inserts/s, 0.00 updates/s, 0.00 deletes/s, 0.00 reads/s
       ----------------------------
       END OF INNODB MONITOR OUTPUT
       ============================
       1 row in set (0.00 sec)
    
Check list of locked tables:
mysql> show open tables where in_use>0;
+-----------+------------------+--------+-------------+
| Database  | Table            | In_use | Name_locked |
+-----------+------------------+--------+-------------+
| chyi_test | history_20190430 |      1 |           0 |
+-----------+------------------+--------+-------------+
1 row in set (0.01 sec)

Check the thread which is using this table
mysql> SHOW FULL PROCESSLIST;
```

* Get locked tables in MySQL Query?
    - List of locked tables:
```
mysql> show open tables WHERE IN_use > 0;
+-----------+------------------+--------+-------------+
| Database  | Table            | In_use | Name_locked |
+-----------+------------------+--------+-------------+
| chyi_test | history_20190430 |     51 |           0 |
+-----------+------------------+--------+-------------+
1 row in set (0.01 sec)

In_use: The number of table locks or lock requests there are for the table.
```
