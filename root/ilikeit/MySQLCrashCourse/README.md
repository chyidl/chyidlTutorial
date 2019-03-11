MySQL Crash Course
==================

The offical way to pronounce "MySQL" is "My Ess Que Ell" is an open source relational database management system (RDBMS).

MySQL 8.0 Install and Manage
-------------
```
# My Machine info 
$ cat /etc/os-release 
NAME="Ubuntu"
VERSION="18.04.2 LTS (Bionic Beaver)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 18.04.2 LTS"
VERSION_ID="18.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=bionic
UBUNTU_CODENAME=bionic

# Adding the MySQL Software Repository 
$ wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb
$ sudo dpkg -i mysql-apt-config* 
# During the installation, you'll be presented with a configuration screen where you can specify which version of MySQL you'd prefer, 
$ sudo apt update # Refresh your apt package cache 
$ rm mysql-apt-config*  # clean up after ourseleves and delete the file we download  
# If you need to update the configuration of these repositories, just run $sudo dpkg-reconfigure mysql-apt-config, select new options, and then sudo apt update to refresh your package cache.

# Install MySQL by the following command:
$ sudo apt-get install mysql-server 

# You can set the root password later using the mysql_secure_installation 
$ sudo mysql_secure_installtion

# How to Create a New User
# Making a new user within the MySQL shell 
mysql> CREATE USER 'newuser'@'%' IDENTIFIED BY 'password';
# provide the user with access to the informantion they will need.
#   ALL_PRIVILEGES - full access to a designated database 
#   CREATE - create new tables or databases 
#   DROP - delete tables or databases
#   DELETE - delete rows from tables 
#   INSERT - insert rows into tables 
#   SELECT - allow select command to read through databses;
#   UPDATE - allow them to update table rows 
#   GRANT OPTION - allow them to grant or remove other user's privileges 
mysql> GRANT ALL PRIVILEGES ON *.* TO 'newuser'@'%'; 

# revoke a permission
mysql> REVOKE type_of_permission ON database_name.table_name FROM 'username'@'localhost';

# review user current permissions 
mysql> SHOW GRANTS ;

# drop user 
mysql> DROP USER 'username'@'%';

# log out 
mysql> quit 

# Don't forget reload all the privileges, 
$ FLUSH PRIVILEGES; 刷新权限

# Support full Unicode in MySQL databases

# Switching from MySQL's utf8 to utf8mb4 
Step 1: Create a backup
Create a backup of all the databases on the server you want to upgrade. Safety first!
$ mysqldump -u vps -p project > projectbackup.sql 
```

    1. Stop the MySQL Service ($ sudo systemctl stop mysql)
    2. Start MySQL without a password ($ sudo mysqld_safe --skip-grant-tables &)
    3. Connect to MySQL ($ mysql -uroot)
    4. Set a new MySQL root password (mysql> use mysql; mysql> GRANT ALL PRIVILEGES ON *.* to 'root'@'localhost' IDENTIFIED BY 'your_password'; mysql> flush privileges; mysql> quit;)
    5. Restart MySQL service ($ sudo systemctl restart mysql)
    6. Create New Databases (mysql> CREATE DATABASE xx;)
    7. Creating MySQL database and user ($ mysql -uroot -p; $ mysql> GRANT ALL PRIVILEGES ON xx.* TO 'username'@'%' IDENTIFIED BY 'your_password';)
    8. (mysql> FLUSH PRIVILEGES; Privileges assigned through GRANT option do not need FLUSH PRIVILEGES to take effect - MySQL server will notice these changes and reload the grant tables immediately) 

If you modify the grant tables directly using statements such as INSERT, UPDATE, or DELETE, your changes have no effect on privilege checking until you either restart the server 
or tell it to reload the tables. If you change the grant tables directly but forget to reload them, your changes have no effect until you restart the server. This many leave you
wondering why your changes seem to make no difference! If you modify the grant tables indirectly using account-management statement such as GRANT, REVOKE, SET PASSWORD, or RENAME USER
the server notices these changes and loads the grant tables into memory again immediately.


MySQL Infrastructure 架构
-------------------------

Client --> Connector --> Query Cache --> Analyzer --> Optimizer --> Executor --> Storage Engine.

**Connector连接器**

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

    
**Query Cache查询缓存(MySQL 8.0删除该功能)** 
    
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

mysql> show STATUS LIKE "qcache%";
+-------------------------+----------+
| Variable_name           | Value    |
+-------------------------+----------+
| Qcache_free_blocks      | 1        |
| Qcache_free_memory      | 16756992 |
| Qcache_hits             | 0        |
| Qcache_inserts          | 2        |
| Qcache_lowmem_prunes    | 0        |
| Qcache_not_cached       | 3        |
| Qcache_queries_in_cache | 2        |
| Qcache_total_blocks     | 6        |
+-------------------------+----------+
8 rows in set (0.02 sec)

From the above we are sure the queries are cached. Let us try an insert and see the status, it will invalidate the query cache and reclaim the memory.

mysql> DELETE FROM test.hs300 WHERE id=1;
Query OK, 1 row affected (0.01 sec)

mysql> show STATUS LIKE "qcache%";
+-------------------------+----------+
| Variable_name           | Value    |
+-------------------------+----------+
| Qcache_free_blocks      | 1        |
| Qcache_free_memory      | 16760152 |
| Qcache_hits             | 0        |
| Qcache_inserts          | 3        |
| Qcache_lowmem_prunes    | 0        |
| Qcache_not_cached       | 3        |
| Qcache_queries_in_cache | 0        |
| Qcache_total_blocks     | 1        |
+-------------------------+----------+
8 rows in set (0.00 sec)

Think about how to decide the query cache size:
    query_cache_size 
    Qcache_queries_in_cache
    Qcache_hits 
    Qcache_lowmem_prunes: is the variable which indicates how many times MySQL had to clear/prune some data from the Qcache to make space for the output of other queries.

query_cache_type: controls the query cache, Setting the query_cache_type to zero will avoid the query cache mutex. 

SET query_cache_type=DEMAND; 默认的SQL语句都不使用查询缓存，而对于需要使用查询缓存的语句，可以用SQL_CACHE显示指定
mysql> SELECT SQL_CACHE * from test.hs300 WHERE ID=10; 
```

**Query Parsing解析器**
    
    Lexical analysis 词法分析and parsing语法分析 are prerequisite for any language. There are many tools available in the industry which can help in achieving this goal. 
    Lexer used in MySQL: MySQL uses a hand-written lexer for lexical analysis.The benefit being most of the code can be optimized keeping SQL syntax in mind.
    Parser used in MySQL: MySQL uses 'bison' tool as it's parser generator.

**Query Optimizer优化器**
    
    * EXPLAIN is one of the most powerful tools at your disposal for understanding and optimizing troublesome MySQL queries.
```
mysql> explain select * from test.hs300 where id=2;
+----+-------------+-------+------------+-------+---------------+---------+---------+-------+------+----------+-------+
| id | select_type | table | partitions | type  | possible_keys | key     | key_len | ref   | rows | filtered | Extra |
+----+-------------+-------+------------+-------+---------------+---------+---------+-------+------+----------+-------+
|  1 | SIMPLE      | hs300 | NULL       | const | PRIMARY       | PRIMARY | 4       | const |    1 |   100.00 | NULL  |
+----+-------------+-------+------------+-------+---------------+---------+---------+-------+------+----------+-------+
1 row in set, 1 warning (0.00 sec)

id: -- a sequential identifier for each SELECT within the query(for when you have nested subqueries)
select_type: -- the type of select query. Possible values are:
    * SIMPLE: -- the query is a simple SELECT query without any subqueries or UNIONs 
    * PRIMARY: -- the select is in the outermost query in a JOIN 
    * DERIVED: -- the select is aprt of a subquery within a FROM clause 
    * SUBQUERY: -- the first select in a subquery 
    * DEPENDENT SUBQUERY: -- a subquery which is not cacheable(there are certain conditions for a query to be cacheabel)
    * UNION: -- the select is the second or later statement of a UNION
    * DEPENDENT UNION: -- the second or later SELECT of a UNION is dependent on an outer query.
    * UNION RESULT: -- the select is a result of a UNION 

table: -- the table referred to by the row
partitions: -- 
type: -- How MySQL joins the tables used. This is one of the most insightful fields in the output because it can indicate missing indexes or how the query is written should be reconsidered. 
    * system: the table has only zero or one row 
    * const: the table has only one matching row which is indexed. 
    * eq_ref: all parts of an index are used by the join and the index is PRIMARY KEY or UNIQUE NOT NULL.
    
优化器是在表里面有多个索引的时候，决定使用那个索引；或者在一个语句中有多表关联join的时候，决定各个表的连接顺序，

mysql> select * from t1 join t2 using(ID) where t1.c=10 and t2.d=20;
    既可以先从t1里面取出c=10的记录的ID值，再根据ID值关联到表t2里面d的值是否等于20
    也可以从表t2里面取出d=20的记录的ID值，再根据ID值关联到t1再判断t1里面c的值是否等于10.
```

**Query Actuators执行器**
```
    开始执行要判断对表有没有执行查询的权限,如果没有，就会返回没有权限的错误，有过查询缓存打开，会在查询缓存结果的时候做权限验证，查询也会在优化器之前做precheck验证权限。

    mysql> select * from test.hs300 where id=2;
    如果有权限，就打开表会根据表的引擎定义，使用引擎提供的接口
    
    数据库的慢查询日志rows_examined字段表示这个语句执行过程中扫描多少行,在有些场景下，执行器调用一次，引擎内部扫描多行，因此引擎扫描行数跟rows_examined并不是完全相同。

Oracle会在分析阶段判断语句是否正确，表是否存在列.
```

MySQL Log System 
----------------
```
    mysql> create table T(ID int primary key, c int); 
    mysql> insert into T (ID, c) VALUES(1,1),(2,2),(3,3);
    mysql> update T set c=c+1 where ID=2;
    表中有更新的时候，关于这张表的查询缓存会失效，所以更新语句会把表T上的所有缓存结果都清空，这也是我们一般不建议使用查询缓存的原因之一。

    更新语句和查询语句不一样的是更新流程涉及两个重要的日志模块REDO logging重做日志，binlog归档日志。

    The InnoDB transaction log handles REDO logging, this is the mechanism that provides the A(Atomic) C(Consistent) I() D(Durability) in ACID. The transaction log keeps a complete record of every change that occurs to the pages inside the database.
    Since InnoDB tries to keep the working set in memory(InnoDB Buffer Pool), therefore the changes made by transactions will occur in volatile memory and later be flushed to disk.So in the event of volatile memory failure or during a system restart InnoDB can guarantee to a Consistent record of the state of the data in the database in Durable memory and that each transaction is Atomic.

    MySQL WAL(Write-Ahead Logging) is a family of techniques for providing atomicity and durability(two of the ACID properties)in database systems. The changes are first recorded in the log, which must be written to stable storage, before the changes are written to the database.

mysql> SHOW VARIABLES like '%dir';
+---------------------------+----------------------------+
| Variable_name             | Value                      |
+---------------------------+----------------------------+
| basedir                   | /usr/                      |
| character_sets_dir        | /usr/share/mysql/charsets/ |
| datadir                   | /var/lib/mysql/            |
| innodb_data_home_dir      |                            |
| innodb_log_group_home_dir | ./                         |
| innodb_tmpdir             |                            |
| lc_messages_dir           | /usr/share/mysql/          |
| plugin_dir                | /usr/lib/mysql/plugin/     |
| slave_load_tmpdir         | /tmp                       |
| tmpdir                    | /tmp                       |
+---------------------------+----------------------------+
10 rows in set (0.00 sec)
    
    InnoDB REDO log size: the ib_logfile0 file and ib_logfile1 are the default InnoDB redo log files created inside the data directory. with 48MB each. If you wish to change the size of the redo log files, you can simply change it in the configuration file and restart MySQL.

$ sudo ls -lhtr /var/lib/mysql/ib_logfile* 

writePos当前记录的位置；checkPoint当前擦除的位置;擦除记录前要把记录更新到数据文件。redo log可以保证InnoDB即使数据库发生异常重启，之前提交的记录都不会丢失，成为crash-safe. 

binlog: Server层归档日志；REDO log: InnoDB引擎特有的日志。

1. redo log是InnoDB引擎特有的；binlog是MySQL的Server层实现的，所有引擎都可以使用
2. redo log是物理日志，记录的是“某个数据页上做了什么修改”；binlog是逻辑日志，记录的是这个语句的原始逻辑
3. redolog是循环写，空间固定，binlog是追加写，并不会覆盖以前的日志。

执行器和InnoDB引擎在执行update query语句的内部流程：
    1. 执行器先找引擎ID=2的行，ID是主键，引擎直接用树搜索找到这一行，如果ID=2这一行所在的数据页本来就在内存中，就直接返回给执行器，否则需要先从磁盘读入内存，然后再返回。
    2. 执行器拿到引擎返回的数据，修改值，得到新的一行数据，再调用引擎接口写入这一行新数据。
    3. 引擎将这一行新数据更新到内存中，同时将这个更新操作记录到redolog里面，此时redo log处于prepare状态，然后告知执行器执行完成，随时可以提交事务。
    4. 执行器生成这个操作的binlog,并把binlong写入磁盘
    5. 执行器调用引擎的提交事务接口，引擎把刚刚写入的redolog改成提交commit状态，更新完成

redo log写入拆成两个步骤，prepare和commit,这就是两阶段提交

数据恢复的过程：数据库备份+备份的binlog. 
redolog 如果不使用“两阶段提交”那么数据库的状态就有可能和用日志恢复出来的库的状态不一致。

数据库扩容：需要全量备份加上应用binlog实现，redolog 和 binlog都可以用于表示事务的提交状态，而两阶段提交就是让这两个状态保持逻辑上的一致性。
MySQL里面重要的两个日志：物理日志redo log 和 逻辑日志binlog. redo log用于保证crash-safe能力， 

mysql> show variables like 'innodb_flush_log%';
+--------------------------------+-------+
| Variable_name                  | Value |
+--------------------------------+-------+
| innodb_flush_log_at_timeout    | 1     |
| innodb_flush_log_at_trx_commit | 1     |
+--------------------------------+-------+
2 rows in set (0.00 sec) 

innodb_flush_log_at_trx_commit = 1表示每次事务的redo log都直接持久化到磁盘，这样可以保证MySQL异常重启之后数据不丢失

mysql> show variables like 'sync_binlog%';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| sync_binlog   | 1     |
+---------------+-------+
1 row in set (0.02 sec)

sync_binlog = 1 表示每次事务的binlog都持久化到磁盘。这样保证mysql异常重启之后binlog不丢失

"两阶段提交"是跨系统维持数据逻辑一致性常用的方案

Redo log记录做了什么改动，binlog有两种模式statement格式是记录SQL语句，row格式会记录行的内容，更新前和更新后。
```

## Transaction isolation [事务隔离]
```
A transaction is a single unit of work. If a transaction is successful, all of the data modifications made during the transaction are committed and become a permanent part of the database. If a transaction encounters errors and must be canceled or rolled back, then all of the data modifications are erased.

Check MySQL Storage Engines:
MariaDB [(none)]> SHOW ENGINES;
+--------------------+---------+--------------------------------------------------------------------------------------------------+--------------+------+------------+
| Engine             | Support | Comment                                                                                          | Transactions | XA   | Savepoints |
+--------------------+---------+--------------------------------------------------------------------------------------------------+--------------+------+------------+
| MRG_MyISAM         | YES     | Collection of identical MyISAM tables                                                            | NO           | NO   | NO         |
| CSV                | YES     | Stores tables as CSV files                                                                       | NO           | NO   | NO         |
| MEMORY             | YES     | Hash based, stored in memory, useful for temporary tables                                        | NO           | NO   | NO         |
| MyISAM             | YES     | Non-transactional engine with good performance and small data footprint                          | NO           | NO   | NO         |
| SEQUENCE           | YES     | Generated tables filled with sequential values                                                   | YES          | NO   | YES        |
| Aria               | YES     | Crash-safe tables with MyISAM heritage                                                           | NO           | NO   | NO         |
| PERFORMANCE_SCHEMA | YES     | Performance Schema                                                                               | NO           | NO   | NO         |
| InnoDB             | DEFAULT | Percona-XtraDB, Supports transactions, row-level locking, foreign keys and encryption for tables | YES          | YES  | YES        |
+--------------------+---------+--------------------------------------------------------------------------------------------------+--------------+------+------------+
8 rows in set (0.00 sec)

ACID: Atomicity[原子性], Consistency[一致性], Isolation[隔离性] and Duration[持久性]
```
