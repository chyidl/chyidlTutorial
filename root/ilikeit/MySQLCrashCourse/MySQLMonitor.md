MySQL实时性能监控
=================
> MySQL数据库实时性能数据监控可以快速帮助定位系统或MySQL数据库的性能瓶颈，所以收集和展示性能数据非常重要
* OS 
    - CPU 
    - Mem 
    - Net 
    - IO 
    - Swap 
* MySQL
    - Network Usage 
    - Open Files/Table 
    - Temporary 
    - Questions 
    - Connection
    - Com
* InnoDB 
    - written 
    - read 
    - innodb_buffer_pool_pages 
    - dirty 
    - writes
    - flush 
    - innodb_rows 
    - innodb_log 
    - reads 
* Doing  [MySQL 真正在做些什么]
    - Processlist 
    - Engine innodb status 
    - Locks 
    - Threads 
    - Slow Queries 

innotop - A Monitoring tool for MySQL
-------------------------------------
> innotop helps in monitoring user statistics, mysql replication status, query list, InnoDB I/O information etc. Another important things about innotop is it refreshes the data continuously.
```
Staring the Innotop - 
# Provide MySQL server username and password which you are about to monitor
$ innotop -h host -P port -u user -ppassword 
[RO] Dashboard (? for help)                              192.168.1.22, 1h54m, 1.09 QPS, 4/3/1 con/run/cac thds, 5.7.27

Uptime  MaxSQL  ReplLag  QPS   Cxns  Run  Miss  Lock  Tbls  Repl  SQL
 1h54m   1h54m           1.09     4    2  7.55     0   232        LOAD REPLACE history_20180102

 To get various different options and its usage press "?".
 [RO] Dashboard (? for help)                              192.168.1.22, 1h55m, 0.89 QPS, 4/3/1 con/run/cac thds, 5.7.27

Switch to a different mode:
    A  Dashboard         I  InnoDB I/O Info     Q  Query List
    B  InnoDB Buffers    K  InnoDB Lock Waits   R  InnoDB Row Ops
    C  Command Summary   L  Locks               S  Variables & Status
    D  InnoDB Deadlocks  M  Replication Status  T  InnoDB Txns
    F  InnoDB FK Err     O  Open Tables         U  User Statistics

Actions:
    d  Change refresh interval        q  Quit innotop
    k  Kill a query's connection      r  Reverse sort order
    n  Switch to the next connection  s  Choose sort column
    p  Pause innotop                  x  Kill a query

Other:
TAB  Switch to the next server group   /  Quickly filter what you see
  !  Show license and warranty         =  Toggle aggregation
  #  Select/create server groups       @  Select/create server connections
  $  Edit configuration settings       \  Clear quick-filters
Press any key to continue

Q - Query List:
[RO] Query List (? for help)                              192.168.1.22, 2h2m, 0.78 QPS, 4/3/1 con/run/cac thds, 5.7.27

When   Load  Cxns   QPS   Slow  Se/In/Up/De%  QCacheHit  KCacheHit  BpsIn    BpsOut
Now    0.05  4      0.78     0   0/37/ 0/ 0       0.00%    100.00%  404.88k  99.09k
Total  0.00  1.95k  0.42     0   0/61/ 0/ 0       0.00%     50.00%  573.14k  13.88k

Cmd    ID      State      User   Host             DB            Time      Query
Query       3  executing  lplus  WIN-UHA4VHLFV5N  history_2018  02:01:47  LOAD DATA LOCAL INFILE 'E:/2018/S_L_20180102
Query       4  update     lplus  192.168.1.54     history_2019     00:05  INSERT INTO `history_20190816` VALUES (68487

This mode displays the output from SHOW FULL PROCESSLIST.

InnoDB Buffers: InnoDB缓冲池，页面统计，插入缓冲，自适应哈希索引
InnoDB Deadlocks: InnoDB的死锁中设计的事务
InnoDB FK Err: InnoDB外健的错误信息

Q - Query List:
[RO] Query List (? for help)                              192.168.1.22, 2h2m, 0.78 QPS, 4/3/1 con/run/cac thds, 5.7.27

When   Load  Cxns   QPS   Slow  Se/In/Up/De%  QCacheHit  KCacheHit  BpsIn    BpsOut
Now    0.05  4      0.78     0   0/37/ 0/ 0       0.00%    100.00%  404.88k  99.09k
Total  0.00  1.95k  0.42     0   0/61/ 0/ 0       0.00%     50.00%  573.14k  13.88k

Cmd    ID      State      User   Host             DB            Time      Query
Query       3  executing  lplus  WIN-UHA4VHLFV5N  history_2018  02:01:47  LOAD DATA LOCAL INFILE 'E:/2018/S_L_20180102
Query       4  update     lplus  192.168.1.54     history_2019     00:05  INSERT INTO `history_20190816` VALUES (68487

```
