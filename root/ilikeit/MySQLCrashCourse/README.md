# MySQL 

The offical way to pronounce "MySQL" is "My Ess Que Ell" is an open source relational database management system (RDBMS).

## MySQL Infrastructure

Client --> Connector --> Query Cache --> Analyzer --> Optimizer --> Executor --> Storage Engine.

**Connector**

    * $ mysql -h$host -P$port -u$user -p 
    * After the user successfully establishes the connection, the modification of the user rights will not affect the existing connection, and only the newly established connection will use the new permission setting.
    * mysql> SHOW PROCESSLIST; show which threads are running 
    * mysql> SHOW VARIABLES LIKE '%max_connections%'; 
    * mysql> SET GLOBAL max_connections = 5000; to change max_connections 
    * 数据库中，长连接是指连接成功后，如果客户端持续有请求，则一直使用同一个连接，短连接则是指每次执行完很少的几次查询就断开连接，下次查询再重新建立连接
    * OOM killer : Out Of Memory killer is a process that the linux kernel employs when the system is critically low on memory. the OOM
    killer to review all running processes and kill one or more in order to free up system memory and keep the system running. The 
    principle of which are as follows are as follows: The process and its all of its child processes are using a lot of memory, The
    minimum number of processes are killed(ideally one) in order to free up enough ememory to resolve the situation Root,kernel and 
    important system processes are given much lower scores.
    * $ dmesg | egrep -i "killed process" # find if the OOM killer 
    * The OOM Killer will only get invoked when the system is critically low on memory.
    * mysql> mysql_reset_connection  # Resets the connection to clear the session state

    
**Query Cache** 
    
    * Query caching is one of the prominent features in MySQL and a vital part of query optimization. The MySQL query cache is a global
    one shared among the sessions. It caches the select query along with the result set, which enables the identical selects to execute
    faster as the data fetches from the in memory.
    * The MySQL query cache has its own downsides, "frequently updated table" means you're probably not going to get any sort of good 
    usage from the query cache.
    *  mysql> show variables;
    *  mysql> show global status; 
    *  mysql> show variables like 'query_cache_type'; 查询缓存模式状态，ON/OFF 
    *  mysql> show status like 'Qcache%'; # show the amount of cached query in value column. 
```
$ mysql> SHOW STATUS LIKE 'qcache%'; 
+-------------------------+----------+
| Variable_name           | Value    |
+-------------------------+----------+
| Qcache_free_blocks      | 1        |
| Qcache_free_memory      | 16760152 |
| Qcache_hits             | 0        |
| Qcache_inserts          | 0        |
| Qcache_lowmem_prunes    | 0        |
| Qcache_not_cached       | 321      |
| Qcache_queries_in_cache | 0        |
| Qcache_total_blocks     | 1        |
+-------------------------+----------+
8 rows in set (0.01 sec)

$ mysql> select * from test.hs300 limit 10;

mysql> select * from test.hs300 limit 10;
+----+---------------------+-----------+----------------------+--------+---------------------+
| id | date                | code      | name                 | weight | ts                  |
+----+---------------------+-----------+----------------------+--------+---------------------+
|  1 | 2013-01-04 00:00:00 | 000001.SZ | 平安银行             |   0.79 | 2018-12-26 03:43:52 |
|  2 | 2013-01-04 00:00:00 | 000002.SZ | 万科A                |   1.89 | 2018-12-26 03:43:52 |
|  3 | 2013-01-04 00:00:00 | 000009.SZ | 中国宝安             |   0.18 | 2018-12-26 03:43:52 |
|  4 | 2013-01-04 00:00:00 | 000012.SZ | 南玻A                |    0.2 | 2018-12-26 03:43:52 |
|  5 | 2013-01-04 00:00:00 | 000024.SZ | 招商地产(退市)       |   0.41 | 2018-12-26 03:43:52 |
|  6 | 2013-01-04 00:00:00 | 000039.SZ | 中集集团             |   0.17 | 2018-12-26 03:43:52 |
|  7 | 2013-01-04 00:00:00 | 000046.SZ | 泛海控股             |   0.14 | 2018-12-26 03:43:52 |
|  8 | 2013-01-04 00:00:00 | 000059.SZ | 华锦股份             |   0.07 | 2018-12-26 03:43:52 |
|  9 | 2013-01-04 00:00:00 | 000060.SZ | 中金岭南             |   0.25 | 2018-12-26 03:43:53 |
| 10 | 2013-01-04 00:00:00 | 000061.SZ | 农产品               |   0.12 | 2018-12-26 03:43:53 |
+----+---------------------+-----------+----------------------+--------+---------------------+
10 rows in set (0.02 sec)


```
