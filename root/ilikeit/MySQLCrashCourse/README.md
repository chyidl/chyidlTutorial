MySQL Crash Course(Everything before the word "but" is horse shit)
==================
> The offical way to pronounce "MySQL" is "My Ess Que Ell" is an open source relational database management system (RDBMS).
> MySQL is written in C and C++. Its SQL parser is written in yacc, but it uses a home-brewed lexical analyzer.

Install MySQL 5.7 on CentOS
---------------------------

* Step 1 - Enable MySQL Repository 
```
# First of all, You need to enable MySQL 5.7 community release yum repository on your system. The rpm package for yum repository configuration are available on MySQL official website.

-- On CentOS and RHEL 7 -- 
$ sudo yum localinstall https://dev.mysql.com/get/mysql57-community-release-el7-9.noarch.rpm

-- On CentOS and RHEL 6 -- 
$ sudo yum localinstall https://dev.mysql.com/get/mysql57-community-release-el6-9.noarch.rpm
```

* Step 2 - Install MySQL 5.7 Server 
```
As you have successfully enabled MySQL yum repository on your system. Now, Install MySQL 5.7 community server using following commands as per your operating system version.
$ sudo yum install mysql-community-server 

Get Temporary root Password:
$ grep 'A temporary password' /var/log/mysqld.log | tail -1
Sample output:
2019-06-16T07:12:15.556876Z 1 [Note] A temporary password is generated for root@localhost: 3aU0dgHq*3Hsg
```

* Step 3 - Start MySQL Service 
```
After installing rpms use following command to start MySQL Service 
$ sudo service mysqld start|stop|restart
```

* Step 4 - Initial MySQL Configuration 
```
Execute **mysql_secure_installation** script and follow the wizard. It will prompt for root password.
$ sudo mysql_secure_installation 
This wizzard will prompt you for inputs. Input new strong password for MySQL root account. For remaining options read option and provide input as required.
```

* Step 5 - Login to MySQL 
```
Login to MySQL using root access
$ mysql -h localhost -u root -p

After login to MySQL server

/* CREATE NEW DATABASE */
mysql> CREATE DATABASE mydb;

/* CREATE MYSQL USER FOR DATABASE */
mysql> CREATE USER 'db_user'@'%' IDENTIFIED BY 'password';

/* GRANT Permission to User on Database */
mysql> GRANT ALL ON mydb.* TO 'db_user'@'%';

/* RELOAD PRIVILEGES */
mysql> FLUSH PRIVILEGES;
```

* Step 6 - Check MySQL Version 
```
$ mysql -V 
mysql  Ver 14.14 Distrib 5.7.26, for Linux (x86_64) using  EditLine wrapper
```

MySQL 8.0 Install and Manage on Ubuntu
--------------------------------------
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

# A Quick Guide to Using the MySQL APT Repository
# Adding the MySQL APT Repository
$ wget https://dev.mysql.com/get/mysql-apt-config_0.8.13-1_all.deb
$ sudo dpkg -i mysql-apt-config*

# During the installation, you'll be presented with a configuration screen where you can specify which version of MySQL you'd prefer, 
$ sudo apt update # Refresh your apt package cache 

# Install MySQL by the following command:
$ sudo apt-get install mysql-server 

# You can set the root password later using the mysql_secure_installation 
$ sudo mysql_secure_installtion

#Starting and Stopping the MySQL Server

# Check the status of the MySQL server 
$ sudo systemctl status mysql

# Stop the MySQL server with the following command:
$ sudo systemctl stop mysql 

# To restart the MySQL server, use the following command:
$ sudo systemctl start mysql 

# Selectig a Major Release Version 
$ sudo spkg-reconfigure mysql-apt-config 
# update package information from the MySQL APT repository with this command
$ sudo apt-get update 

# To see the names of the packages you have installed from the MySQL APT repository
$ dpkg -l | grep mysql | grep ii 
ii  mysql-apt-config                0.8.13-1                          all          Auto configuration for MySQL APT Repo.
ii  mysql-client                    8.0.16-2ubuntu18.04               amd64        MySQL Client meta package depending on latest version
ii  mysql-common                    8.0.16-2ubuntu18.04               amd64        Common files shared between packages
ii  mysql-community-client          8.0.16-2ubuntu18.04               amd64        MySQL Client
ii  mysql-community-client-core     8.0.16-2ubuntu18.04               amd64        MySQL Client Core Binaries
ii  mysql-community-server          8.0.16-2ubuntu18.04               amd64        MySQL Server
ii  mysql-community-server-core     8.0.16-2ubuntu18.04               amd64        MySQL Server Core Binaires
ii  mysql-server                    8.0.16-2ubuntu18.04               amd64        MySQL Server meta package depending on latest version

# mysql-client: Metapackage for installing the MySQL client 
# mysql-server: Metapackage for installing the MySQL server 
# mysql-common: MySQL database common files 
# mysql-community-client: MySQL client
# mysql-community-server: MySQL server 

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
```

Switching from MySQL's utf8 to utf8mb4
--------------------------------------
```
Step 1: Create a backup 
Create a backup of all the databases on the server you want to upgrade. Safety first!
$ mysqldump -u username -p password > projectbackup.sql 

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

Step 2: Upgrade the MySQL server 
Upgrade the MySQL server to v5.53+, or ask your server administrator to do it for you.

Step 3: Modify databases, tables, and columns 
# For each database:
mysql> ALTER DATABSE database_name CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
# To see the default character set and collation for a given database, use these statements:
mysql> USB db_name;
mysql> SELECT @@character_set_database, @@collation_database;

# For each table:
ALTER TABLE table_name CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_uniocde_ci;

# For each column:
ALTER TABLE table_name CHANGE column_name column_name VARCHAR(191) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

Step 4: Check the maximum length of columns and index keys

Step 5: Modify connection, client, and server character sets 
# In application code, set the connection character set to utf8mb4.

/etc/my.cnf 
[client]
default-character-set = utf8mb4 

[mysql]
default-character-set = utf8mb4

[mysqld]
character-set-client-handshake = FALSE 
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci

# confirm settings 
mysql> SHOW VARIABLES WHERE VARIABLE_NAME LIKE 'character_set_%' OR VARIABLE_NAME LIKE 'collation%';
+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client     | utf8mb4                    |
| character_set_connection | utf8mb4                    |
| character_set_database   | utf8mb4                    |
| character_set_filesystem | binary                     |
| character_set_results    | utf8mb4                    |
| character_set_server     | utf8mb4                    |
| character_set_system     | utf8                       |
| character_sets_dir       | /usr/share/mysql/charsets/ |
| collation_connection     | utf8mb4_unicode_ci         |
| collation_database       | utf8mb4_unicode_ci         |
| collation_server         | utf8mb4_unicode_ci         |
+--------------------------+----------------------------+
11 rows in set (0.03 sec)

Step 6: Repair and optimize all tables 
# After upgraing the MySQL server and making the necessary changes explained above, make sure to repair and optimize all databases and tables. 
# Run the following MySQL queries for each table you want to repair and optimize:
# For each table 
mysql> REPAIR TABLE table_name;
mysql> OPTIMIZE TABLE table_name;

# This can easily be done in one go using the command-line mysqlcheck utility:
$ mysqlcheck -u root -p --auto-repair --optimize --all-databases 
```

MySQL Architecture and Components
----------------------------------
> try to explain things in flow including data processing and SQL execution in MySQL with the help of diagrams.
> MySQL is a very flexible and offers different kinds of storage engines as a plugin for different kinds of needs.
* [InnoDB]: transactional storage engines; it's default and main storage engine for MySQL
* [MyISAM]: non-transactional storage engines 
* MySQL Physical Architecture:
    - MySQL Base Directory:
        * Program log files
            - Libraries 
            - Documents, support files 
            - pid files (Unix)
            - socket files (Unix)
        * Program executable files 
            - mysql 
            - mysqld 
            - mysqladmin 
            - mysqldump 
            - mysql_upgrade 
            - mysqlbinlog 
    - MySQL Data Directory 
        * Data directory
            - Server log files 
            - Status file 
            - Innodb log files 
            - Innodb system tablespace 
            - Innodb log buffer 
            - Innodb General/undo/temp_tablespace.
```
Client --> Connector --> Query Cache --> Analyzer --> Optimizer --> Executor --> Storage Engine.

**Connector连接器**

    * $ mysql -h$host -P$port -u$user -p 
    * After the user successfully establishes the connection, the modification of the user rights will not affect the existing connection, and only the newly established connection will use the new permission setting.
    * mysql> SHOW PROCESSLIST; show which threads are running 
    * mysql> SHOW VARIABLES LIKE '%max_connections%';   # 查看允许最大并发连接数
    * mysql> SET GLOBAL max_connections = 5000; 临时生效 to change max_connections 
    * 数据库中，长连接是指连接成功后，如果客户端持续有请求，则一直使用同一个连接，短连接则是指每次执行完很少的几次查询就断开连接，下次查询再重新建立连接
    * OOM killer : Out Of Memory killer is a process that the linux kernel employs when the system is critically low on memory. the OOM
    killer to review all running processes and kill one or more in order to free up system memory and keep the system running. The 
    principle of which are as follows are as follows: The process and its all of its child processes are using a lot of memory, The
    minimum number of processes are killed(ideally one) in order to free up enough ememory to resolve the situation Root,kernel and 
    important system processes are given much lower scores.
    * $ dmesg | egrep -i "killed process" # find if the OOM killer 
    * The OOM Killer will only get invoked when the system is critically low on memory.
    * mysql> mysql_reset_connection  # Resets the connection to clear the session state
    * SHOW STATUS LIKE 'Threads%'; # 查看线程相关的状态变量
    mysql> show status like 'Threads%';
    +-------------------+-------+
    | Variable_name     | Value |
    +-------------------+-------+
    | Threads_cached    | 0     |   Threads_cached: 缓存中的线程连接数
    | Threads_connected | 51    |   Threads_connected: 当前打开的连接数, 该值和SHOW PROCESSLIST; 输出的记录综述一样
    | Threads_created   | 54    |   Threads_created: 为处理连接而创建的线程数,如果该值很大，可能要增加thread_cache_size. 缓存为命中率 = Threads_created/Connections
    | Threads_running   | 50    |   Threads_running: 非睡眠状态的连接数，通常指并发连接数
    +-------------------+-------+
    4 rows in set (1.44 sec)
```

```
修改最大连接数
[mysqld]
max_connections = 1000 
```

```
线程池: 线程池由许多线程组构成，每个组管理一系列客户端连接，一旦连接被建立，线程池会以轮训调度(Round-robin)方式将连接分配给线程组。每个线程组可拥有的最大线程数量为
```

    
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

Transaction isolation [事务隔离]
--------------------------------
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

事务隔离的实现:回滚操作
事务的启动方式: 
    1.显示启动事务语句, begin或start transaction, commit或rollback 
    2.set autocommit=0,这个命令会将线程的自动提交关掉，如果你只执行一个SELECT语句，这个事物就启动，并不会自动提交，这个事务持续存在直到你主动执行commit或rollback.或者断开连接. 

    begin显示启动事物，执行commit work and chain，则是提交事务并自动启动下一个事务，这样省去再次执行begin语句的开销

SELECT * from information_schema.innodb_trx where TIME_TO_SEC(timediff(now(),trx_started))>60; 查询持续时间超过60s的事务。
```

Index 索引
----------
```
索引:的出现就是为了提高数据查询的效率
    哈希表：Key-Value存储数据结构，哈希索引在做区间查询的速度很慢,哈希表这种数据结构适用于只有等值查询的场景.
    有序数组的二分查找：在等值查询和范围查询场景中的性能都非常优秀O(log(N)).但是，在需要插入数据就必须挪动后面的所有记录，成本太高.有序数组只使用与静态存储引擎，
    二叉搜索树:每个节点的左儿子小于父节点，父节点又小于右儿子.O(log(N)).当然为了维持O(log(N))查询复杂度，需要保持这棵树是平衡二叉树为了做到这个保证，更新的时间复杂度也是O(log(N)).多叉树就是每个节点有多个儿子，儿子之间的大小保证从左到右自增，二叉树是搜索效率最高的，但是实际上大多数的数据库存储并不使用二叉树，原因是，索引不止存在内存中，还要写入磁盘。为了让查询尽量少读磁盘，就必须让查询过程访问尽量少的数据块，那么我们就不应该使用二叉树，而是使用"N"茶树，这里“N叉树”中的"N"取决于数据块的大小。
    N叉树由于在读写上的性能优点，以及适配磁盘的访问模式，已经被广泛应用在数据库引擎中。

    InnoDB索引模型:InnoDB使用B+树索引模型,表都是根据主键顺序以索引的形式存放，这种存储方式的表成为索引组织表。每个索引在InnoDB里面对应一颗B+树。

    根据叶子节点的内容，主键索引和非主键索引，主键索引的叶子节点存放的是整行数据，在InnoDB里，主键索引也被称为聚簇索引(clustered Index). 非主键索引的叶子节点内容是主键的值。在InnoDB里，非主键索引也被称为二级索引secondary index. 

    SELECT * FROM T WHERE ID=500,即主键查询方式，只需要搜索ID这颗B+树
    SELECT * FROM T WHERE k=5;即普通索引查询方式，需要先搜索k索引树，得到ID值，再到ID索引树查询一次，这个过程称为回表.
    基于非主键索引的查询需要多扫描一颗索引树，因此我们在应用中应该尽量使用主键索引。

索引维护:
    B+树为了维护索引有序性，数据页，页分裂。页合并，
    自增主键是指自增列上定义的主键，在建表语句中一般定义为NOT NULL PRIMARY KEY AUTO_INCREMENT. 插入新纪录的时候可以不指定ID值，系统会获取当前ID最大值加1作为下一条记录的ID值，自增主键的插入数据模式，符合递增插入的场景，每次插入一条新纪录，都是追加操作，都不涉及挪动其他记录，也不会触发叶子节点的分裂.而有业务逻辑的字段做主键，往往不同意保证有序插入，这样写数据成本相对较高。
    显然，主键长度越小，普通索引的叶子节点就越小，普通索引占用空间也就越小.所以从性能和存储空间方面的考量，自增主键往往是更合理的选择。

总结：
    InnoDB采用B+树结构，可以很好的配合磁盘的读写特性，减少单次查询磁盘访问次数。由于InnoDB是索引组织表，一般情况下会建议创建一个自增主键，这样非主键占用的空间最小

SQL语句:
    重建索引：因为删除、或者页分裂等原因，导致数据页有空洞，重建索引的过程会创建一个新索引，把数据按顺序插入，这样页面的利用率最高，索引更紧凑，更省空间.
    ALTER TABLE T DROP INDEX k;  # 重建索引k 
    ALTER TABLE T ADD INDEX(k); 
    ALTER TABLE T DROP PRIMARY key;  # 重建主键索引,无论是删除主键还是创建主键，都会将整个表重建
    ALTER TABLE T ADD PRIMARY key(id); 
    -- ALTER TABLE T engine=InnoDB.

$ sudo apt install percona-toolkit 
pt-kill : Kill MySQL queries that match certain criteria  
在业务功能测试阶段输出所有的general_log，分析日志行为提前发现问题

索引优化，避免回表
    覆盖索引: SELECT ID FROM T WHERE k between 3 and 5; ID的值已经在k索引树上，因此可以直接提供查询结果，不需要回表,使用覆盖索引是一个常用的性能优化手段.

联合索引：覆盖索引，不需要回表查整行记录，减少语句的执行时间.

最左前缀原则: B+树这种索引结构，可以利用索引的“最左前缀”来定位记录.只要满足最左前缀，就可以利用索引来加速检索，这个最左前缀可以是联合索引的最左N个字段，也可以是字符串索引的最左M个字符。

建立联合索引的时候，如何安排索引内的字段顺序:
    1.第一原则是，如果通过调整顺序，可以少维护一个索引，那么这个顺序往往就是需要优先考虑采用 
    
mysql> SELECT * FROM tuser WHERE NAME like '张%' and age=10 and ismale=1;
    索引下推优化index condition pushdown: 可以在索引遍历过程中，对索引中包含的字段先做判断，直接过滤掉不满足的记录，减少回表次数.

总结：
    数据库索引：覆盖索引、前缀索引、索引下推
```

Global Lock and Table Lock and Row Lock 全局锁和表锁和行锁
---------------------------------------
```
数据库锁设计的初衷是处理并发问题，作为多用户共享资源，当出现并发访问的时候，数据库需要合理地控制资源的访问规则。

根据加锁的范围，MySQL里面的锁大致可以分为全局锁、表级锁和行锁 
    
    mysql> FLUSH TABLES WITH READ LOCK (FTWRL)对整个库处于只读状态。之后的其他线程语句[数据更新语句(增删改查)，数据定义语句(建表，修改表结构)和更新类事务提交语句]会被阻塞
    全局锁应用场景：做全库逻辑备份，也就是把整个库每个表都SELECT出来存成文本.不加锁，备份系统备份得到的库不是一个逻辑时间点，这个视图不一致.

mysqldump:官方自带的逻辑备份工具使用的参数--single-transaction导入数据之前就会启动一个事务，来确保拿到一致性试图，而由于MVCC(multiversion concurrency control)的支持，这个过程中数据是可以正常更新的。
    single-transaction方法只适用于所有的表使用事务引擎的库，如果该表使用了不支持事务的引擎，那么备份就只能通过FTWRL的方法。

    FTWRL: Flush TABLES WITH READ LOCK. vs SET GLOBAL READONLY=True 
        1. 有些系统中，READONLY的值被用来判断该库是主库还是从库。
        2.执行FTWRL命令后由于客户端发生异常终端，那么MySQL会自动释放这个全局锁，整个库回到正常更新的状态，而将整个库设置为readonly之后，如果客户端发生异常，则数据库就会一直保持readonly状态。这样导致整个库长时间处于不可写状态，风险高。

DML: Data Manipylation Language[SELECT, INSERT, UDPATE, DELETE, MARGE, CALL, EXPANIN PLAN, LOCK TABLE]
DLL: Data Definition Language[CREATE, ALTER, DROP, TRUNCATE, COMMIT, RENAME]

Table Lock表级锁:[表锁， 元数据锁meta lock]
    LOCK TABLES READ/WRITE, UNLOCK TABLES 释放锁
    MDL(metadata lock)保证读写的正确性，当对一个表做增删改查操作的时候，加上MDL读锁，当要对表做结构变更操作的时候，加MDL写锁.
    读锁之间不互斥，因此可以有多个线程同时对一张表增删改查
    读写锁之间、写锁之间是互斥的，用来保障变更表结构操作的安全性。因此如果有两个线程要同时给一个表加字段，其中一个要等另一个执行完才能开始执行.

    长事务，事务不提交，就会一直占用MDL锁，在MySQL的information_schema库的innodb_trx表中，可以查看当前执行中的事务，
    ALTER TABLE tbl_name NOWAIT/WAIT N add column ...

MDL直到事务提交才释放，在做表结构变更的时候，不要锁住线上查询和更新。

InnoDB支持行锁,行锁就是针对数据表中行记录的锁.InnoDB事务中，行锁是在需要的时候才加上，但并不是不需要就立刻释放，而是要等到事务结束时才释放。这就是两阶段协议.

减少锁时间，提升并发度.

死锁和死锁检测：
    当并发系统中不同线程出现循环资源依赖，设计的线程都在等带别的线程释放资源时，就会导致这几个线程进入无限等待状态。成为死锁。 
    1. 一种策略，直接进入等待，直到超时，这个超时时间可以通过参数innodb_lock_wait_timeout 设置
    2. 另一个策略：发起死锁检测, 发现死锁后，主动回滚死锁链条中的某一个事务，让其他事务得以继续执行。参数innodb_deadlock_detect设置为on,表示开启这个逻辑
    
解决由于热点行更新导致的性能问题:
    由于死锁检测要耗费大量的CPU资源.控制并发度，在数据库服务端做并发控制，基本思路就是，对于相同行的更新，在进入引擎之前排队,这样在InnoDB内部就不会有大量的死锁检测工作。或者将一行改为逻辑上的多行减少锁冲突。
    减少死锁的主要方向就是控制访问相同资源的并发事务量。

当备库用--single-transaction做逻辑备份的时候。
1. SET SESSION TRANSACTION ISOLATON LEVEL REPEATABLE READ; 可重复读事务隔离级别
2. START TRANSACTION WITH CONSISTENT SNAPSHOT; 取保得到一致性试图
3. SAVEPOINT sp; 设置保存点 
4. SHOW CREATE TABLE student; 显示表结构，
5. SELECT * FROM student; 正式导入数据
6. ROLLBACK TO SAVEPOINT SP; #回滚到保存点
```

事务到底是隔离还是不隔离
------------------------
```
Begin/start transaction命令并不是一个事务的起点，在执行到他们之后的第一个操作InnoDB表语句，才是事务的真正的起点. 马上执行一个事务start transaction with consistent snapshot; 

MySQL有两种“试图”的概念
    1. view: 他是一个用查询语句定义的虚拟表，在调用的时候执行查询语句并生成结果，创建试图的语法create view...,而他的查询方法与表一样
    2. InnoDB实现的MVCC时用到的一致性读诗图，Consistent read view.用于支持RC（Read commited,读提交）和RR（Repeatable Read可重复读）隔离级别的实现.

    InnoDB里面每一个事务有一个唯一的事务ID，叫做transaction id.是在事务开始的时候向InnoDB事务系统申请的，是按申请顺序严格递增的。而每行数据都有多个版本，每次事务更新数据的时候，都会生成一个新的数据版本。并且把transaction id赋值给这个数据版本的事务ID。row_trx_id.

    InnoDB利用所有数据都有多个版本的这个特性，实现了“秒级创建快照”的能力.一个数据版本，对于一个事务视图来说，除了自己的更新总是可见以外，：还有三种情况：
    1. 版本未提交，不可见
    2. 版本已提交，但是是在诗图创建后提交的，不可见
    3. 版本已提交，而且是在诗图创建前提交的，可见.

更新数据都是先读后写，而这个读，只能读当前的值，称为"当前读current reada"

可重复读的核心就是一执行读(consistent read);而事务更新数据的时候只能用当前读，如果当前的记录的行锁被其他事务占用的话，就需要进入锁等待.

读提交隔离级别下：每个语句执行前都会重新计算出一个新的试图。
start transaction with consistent snapshot; 创建一个持续整个事务的一致性快照.

InnoDB的行数据上有多个版本，每个版本有自己的row trx_id，每个事务或者语句有自己的一致性试图，普通查询语句是一致性读，一致性读会根据row trx_id和一致性试图确定数据版本的可用性. 

    对于事务隔离级别：可重复读，查询支承认在事务启动前就已经提交完成的数据
    对于读提交：查询只承认在语句启动前就已经提交完成的数据
    当前读：总是读取已经提交完成的最新版本
```

普通索引和唯一索引
------------------
```
InnoDB的数据是按照数据页为单位读写，The default page size in InnoDB is 16KB.

Change Buffer:当需要更新一个数据页时，如果数据页在内存中就直接更新，而如果这个数据页还没有在内存中的话，在不影响数据一致性的前提下，InnoDB会将这些更新操作缓存在change buffer中。Change buffer在内存中有拷贝，也会写入磁盘上.将change buffer 中的操作应用到原数据页,得到的最新结果称为merge.除了访问这个数据页会触发merge外，系统有后台线程会定期merge.在数据库正常关闭shutdown的过程中，也会执行merge操作.

唯一索引更新不能使用change buffer.普通索引可以使用change buffer.change buffer的大小可以通过参数innodb_change_buffer_max_size动态设置25表示最多只能占用buffer poll的25%. 

对于写多读少的业务来讲，change buffer的使用效果最好，这种业务模型常见的就是账单类、日志类的系统。

普通索引和唯一索引：这两类在查询能力上没有差别，主要考虑的是对更新性能的影响。

change buffer 和redo log：
    redo log主要节省的是随机写磁盘的IO消耗(转成顺序写)而change buffer主要节省的则是随机读磁盘的IO消耗.
```

MySQL为什么有时候会选错索引
--------------------------
```
创建表,表里面有两个字段a, b, 并分别建立索引
CREATE TABLE `t` (`id` int(11) NOT NULL, `a` int(11) DEFAULT NULL, `b` int(11) DEFAULT NULL, PRIMARY KEY (`id`), KEY `a` (`a`), KEY `b` (`b`)) ENGINE=InnoDB;
表中插入10万行记录,取值按整数递增(1,1,1)
存储过程插入数据
delimiter ;;
create procedure idata() 
begin
    declare i int;
    set i=1;
    while(i<=100000) do
        insert into t values(i, i, i);
        set i = i+1;
    end while;
end;;
delimiter ;
call idata();

mysql> SELECT * FROM t where a between 10000 and 20000; 
mysql> explain 命令: is used to obtain a query execution plan (that is, an explanation of how MySQL would execute a query)

mysql> SET long_query_time=0; 将慢查询日志的阈值设置为0,表示该线程语句都会被记录进入慢查询
mysql> SELECT * FROM t where a between 10000 and 20000; 
mysql> SELECT * FROM t force index(a) where a between 10000 and 20000; 

优化器的逻辑:
    在数据库里面，扫描行数是影响执行代价的因素之一，扫描行数越少，意味着访问磁盘数据的次数越少，消耗的CPU资源越少。

mysql> show index from t; 查看索引的基数

MySQL索引基数的获取： 通过采样统计的方式，采样统计时，InnoDB默认会选择N个数据页，统计这些页面的不同值，得到一个平均值.然后乘以这个索引页面数，就得到这个索引的基数。由于数据表是会持续更新的，索引统计信息也不会固定不变，当变更的数据行数超过1/M的时候，会自动触发重新做一次索引统计。

MySQL中有两种存储索引统计的方式，可以通过设置参数innodb_stats_persistent的值选择:
    innodb_stats_persistent = ON : 表示统计信息会持久化存储，
    innodb_stats_persistent = OFF : 表示统计信息只存储在内存中

mysql> analyze table t; 用来重新统计索引信息 

索引选择异常和处理:
    1. 采用force index强行选择一个索引.
    2. 考虑修改语句，引导MySQL使用我们期望的索引
    3. 在有些场景下，可以新建一个更合适的索引，来提供给优化器做选择，或删掉误用的索引.

索引统计信息不准确导致，可以使用analyze table解决.force index()强行制定索引，
```

字符串字段加索引
---------------
```
支持邮件登陆的系统表:
mysql> create table SUser(ID bigint unsigned primary key, email varchar(64),)engine=innodb; 

mysql> select f1, f2 from SUser where email='xxx'; 如果email字段没有索引，将做全表扫描操作.
mysql> ALTER table SUser add index email(email); 在email字段上创建索引
mysql> ALTER TABLE SUser add index index2(email(6)); 创建索引只取前6个字节

使用前缀索引，定义好长度，就可以做到节省空间，又不用额外增加太多的查询成本.
建立索引时关注的是区分度，区分度越高越好，因为区分度越高，意味着重复的键值越少
mysql> select count(distinct email) as L from SUser; 计算出列上有多少个不同的值;然后依次选取不同的长度的前缀来查看这个值
mysql> select count(distinct left(email, 4)) as L4, from SUser; 

使用前缀索引就用不上覆盖索引对查询性能的优化了，这也是你在选择是否使用前缀索引时需要考虑的一个因素. 
索引选取的越长，占用的磁盘空间就越大，相同的数据页能放下的索引值就越少，搜索的效率也就越低.

使用倒序存储 ：如果你存储的身份证号的时候把它倒过来存，每次查询的时候
mysql> select field_list from t where id_card = reverse('input_id_card_string'); 

使用Hash字段：在表上在创建一个整数字段，来保存身份证的校验码,同时在这个字段上创建索引
mysql> alter table t add id_card_crc int unsigned, add index(id_card_crc); 然后每次插入新纪录的时候，同时使用crc32()函数计算校验码填入新字段中。
mysql> select field_list from t where id_card_crc = crc32('input_id_card_string') and id_card='input_id_card_string'; 

使用倒序存储和hash字段不支持范围查询，只支持等值查询。
```

MySQL的抖动
-----------
```
内存数据页跟磁盘数据页内容不一致的时候，内存页称为“脏页”，内存数据写入磁盘后，内存和磁盘上的数据页的内容就一致，称为“干净页”

1. InnoDB 的redo log 内存满之后 -- 这种情况时InnoDB要尽量避免的，因为出现这种情况的时候，整个系统就不能再接受更新了，所有的更细都必须阻塞
2. InnoDB系统内存不足需要Flush数据页--这种情况其实是常态，InnoDB用缓冲池buffer pool管理内存，缓冲池中的内存页有三种状态:
    a: 还没有使用
    b: 使用了并且是干净页
    c: 使用了并且是脏页
3. MySQL后台不定时刷新
4. MySQL正常关闭之前

InnoDB刷脏页的控制策略： 
    首先：正确告诉InnoDB所在主机的IO能力，这样InnoDB才能知道需要全力刷脏页的时候，可以刷多块 innodb_io_capacity参数，这个值可以设置成磁盘的IOPS,磁盘的IOPS可以通过fio工具测试

$ sudo apt install fio # flexible I/O tester 
fio is a tool that will spawn a number of threds or processes doing a particular type of I/O action as specified by the user. 

InnoDB刷盘速度参考两个因素，一个是脏页比例，一个是redo log写盘速度  
在InnoDB中innodb_flush_neighbors参数用来控制是否将数据页旁边写数据页页一同刷入
```

数据库的空间回收
----------------
```
InnoDB表包含两部分：表结构定义+数据
innodb_file_per_table: 表数据可以存放在共享表空间中，也可以是单独的文件
    OFF: 表示表的数据存放在系统共享表空间中，也就是和数据字典存放在一起
    ON:表示每个InnoDB的表数据存放在一个.ibd为后缀的文件中

建议设置innodb_file_per_table=ON,这样通过drop table命令，系统可以直接删除文件，而如果存放在共享表空间中，即使表删除掉，空间也不会回收. 

数据删除流程:
    数据页复用跟记录复用是不同的。记录的复用只限于符合范围条件的数据，如果我们delete命令整个表的数据删除，结果是所有数据页都会被标记为可复用。但是磁盘上，文件不会变小.

经过大量的增删改查都有可能存在空洞，如果能把这些空洞去掉，就能达到收缩表空间的目的。

mysql> ALTER TABLE A ENGINE=InnoDB; 重建表 
Online DDL: 操作优化
    1. 建立一个临时文件，扫描表A主键的所有数据页
    2. 用数据页中表A的记录生成B+树，存储在临时文件中
    3. 生成临时文件的过程中，将所有对A的操作记录在一个日志文件(row log)中
    4. 临时文件生成后，将日志文件中的操作应用到临时文件，得到一个逻辑数据上与表相同的数据文件对应的
    5.用临时文件替换A的数据文件

GitHub 开源的gh-ost: GitHub's Online Schema Migrations for MySQL 
mysql> ALTER TABLE T engine=innodb,ALGORITHM=inplace; 
mysql> ALTER TABLE T engine=innodb,ALGORITHM-copy; 
mysql> ALTER TABLE T add FULLTEST(filed_name); 给InnoDB表字段加全文索引 

MySQL 8.0全文索引 FULLTEXT index和空间索引SPATIAL index
```

COUNT(*) 实现原理
-----------------
```
MyISAM引擎把一个表的总行数存在了磁盘上，因此执行count(*)的时候会直接返回这个数。效率很高
InnoDB引擎执行count(*)的时候需要把数据一行行的从引擎里面读取出来，然后累积计数.

InnoDB无论在事务支持、并发能力还是数据安全方面，InnoDB都优于MyISAM.
多版本并发控制MVCC:InnoDB事务的隔离级别时可重复度。通过多版本并发控制MVCC实现。每一行记录都要判断自己是否对这个会话可见，因此对于count(*)请求来说，InnoDB只好把数据一行一行的读出来依次判断，可见的行才能够用于计算“基于这个查询”的表的总行树.

在保证逻辑正确的前提下，尽量减少扫描的数据量，是数据库系统设计的通用法则之一.

mysql> SHOW TABLE STATUS FROM DB; TABLE_ROWS 索引统计值是通过采样来估算的

如果需要经常显示交易系统的操作记录总数，我们只能自己计数？
    1. 使用缓存系统保存计数：Redis服务来保存表的总行数。每次插入一行Redis计数加1，删除一行Redis计数就减1.逻辑上不精确。
    2. 数据库保存计数: InnoDB支持崩溃恢复不丢失数据.并且逻辑上一致

COUNT(*)性能问题?
    COUNT()是一个聚合函数，对于返回结果集，一行行的判断，如果COUNT函数的参数不是NULL，累加值+1，否则不加，最后返回累加值.所以COUNT(*)、COUNT(主键id)和COUNT(1) 都表示满足条件的结果集的总行树，而COUNT(字段) 则表示返回满足条件数据行里面，参数“字段”不为NULL的总个数.

COUNT(主键id)：InnoDB 引擎会遍历整张表，把每行的id值都取出来，返回给server层，server层拿到id后，判断是否为空，累加

COUNT(1):InnoDB引擎便利整张表，但不取值，SERVER层对于返回的每一行放一个数字“1”进去，判断是否为空，累加

COUNT(字段)：
COUNT(*)做了专门的优化，不获取值
执行效率排序: COUNT(*)~COUNT(1)>COUNT(id)>COUNT(字段)
```

MySQL Order
-----------
```
创建表结构:

CREATE TABLE `t` (`id` int(11) NOT NULL, `city` varchar(16) NOT NULL, `name` varchar(16) NOT NULL, `age` int(11) NOT NULL, `addr` varchar(128) DEFAULT NULL, PRIMARY KEY (`id`), KEY `city` (`city`))ENGINE=InnoDB;

mysql> explain select city, name, age from t where city = '杭州' order by name limit 1000;
+----+-------------+-------+------------+------+---------------+------+---------+-------+------+----------+----------------+
| id | select_type | table | partitions | type | possible_keys | key  | key_len | ref   | rows | filtered | Extra          |
+----+-------------+-------+------------+------+---------------+------+---------+-------+------+----------+----------------+
|  1 | SIMPLE      | t     | NULL       | ref  | city          | city | 66      | const |    1 |   100.00 | Using filesort |
+----+-------------+-------+------------+------+---------------+------+---------+-------+------+----------+----------------+
1 row in set, 1 warning (0.18 sec)

MySQL会给每一个线程分配一块内存用于排序：sort_buffer. 

SET max_length_for_sort_data = 16; #MYSQL认为单行长度太大采用另外一种算法.

全字段排序 vs rowid排序
    MySQL担心排序内存太小会影响排序效率，才会采用rowid排序算法，这样排序过程中一次可以排序更多行，但是需要再回到原表取数据.

MySQL做排序时成本比较高的操作，
覆盖索引是指，索引上的信息足够满足查询请求，不需要再回到主键索引上取数据.
```

```
SQL语言分为DDL, DML, DCL三大类。
https://blog.csdn.net/chenlycly/article/details/21302073

```

MySQL 查看表结构
```
desc tabl_name;  # 简单描述表结构，字段类型
显示表结构，字段类型，主键，是否为空等属性
mysql> desc asharecalendar;
+-------------------+--------------+------+-----+---------+-------+
| Field             | Type         | Null | Key | Default | Extra |
+-------------------+--------------+------+-----+---------+-------+
| OBJECT_ID         | varchar(100) | NO   | PRI |         |       |
| TRADE_DAYS        | varchar(12)  | YES  | MUL | NULL    |       |
| S_INFO_EXCHMARKET | varchar(60)  | YES  | MUL | NULL    |       |
| OPDATE            | datetime     | YES  |     | NULL    |       |
| OPMODE            | varchar(1)   | YES  |     | NULL    |       |
+-------------------+--------------+------+-----+---------+-------+
5 rows in set (0.02 sec)

select * from information_schema.columns where table_schema = 'db' # 表所在数据库 and table_name = 'tablename'; # 你要查看的表名称
mysql> SELECT column_name, column_comment FROM information_schema.columns WHERE table_schema = 'wind' and table_name = 'asharecalendar';
+-------------------+-----------------------+
| column_name       | column_comment        |
+-------------------+-----------------------+
| OBJECT_ID         | 对象ID                |
| TRADE_DAYS        | 交易日                |
| S_INFO_EXCHMARKET | 交易所英文简称        |
| OPDATE            |                       |
| OPMODE            |                       |
+-------------------+-----------------------+
5 rows in set (0.02 sec)

只查询列名和注释
select column_name, column_comment from information_schema.columns where table_schema='db' and table_name = 'tablename';

查询表的注释
select table_name, table_comment from information_schema.tables where table_schema = 'db' and table_name = 'tablename' 

查看表生成的DDL
show create table table_name; 
mysql> show create table asharecalendar\G
*************************** 1. row ***************************
       Table: asharecalendar
Create Table: CREATE TABLE `asharecalendar` (
  `OBJECT_ID` varchar(100) NOT NULL DEFAULT '' COMMENT '对象ID',
  `TRADE_DAYS` varchar(12) DEFAULT NULL COMMENT '交易日',
  `S_INFO_EXCHMARKET` varchar(60) DEFAULT NULL COMMENT '交易所英文简称',
  `OPDATE` datetime DEFAULT NULL,
  `OPMODE` varchar(1) CHARACTER SET utf8 DEFAULT NULL,
  PRIMARY KEY (`OBJECT_ID`),
  KEY `index_trade_days` (`TRADE_DAYS`),
  KEY `index_s_info_exchange` (`S_INFO_EXCHMARKET`)
) ENGINE=InnoDB DEFAULT CHARSET=gbk
1 row in set (0.01 sec)

表操作命令：
复制表结构：create table table1 like table; 
复制数据: insert into table1 select * from table; 

机器授权：
grant select on *.* to 'reader'@'%' identified by '123456' WITH GRANT OPTION flush privileges;

插叙数据直接插入
insert into t_visual_domain(`user_id`, `domain`, `group`) select id, 'www.baidu.com' as doamin, 'group' from t_visual_user;

修改表结构
alter table competitor_goods add sku_id bigint(20) unsigned DEFAULT NULL COMMENT '商品销售'
```

Changing MySQL wait_timeout variable
------------------------------------

> wait_timeout variable, for a session or globally.
> If we set the wait_timeout variable for a session, it will valid only for a particular session. But when we set the wait_timeout variable globally it will valid for all the sessions.
```
mysql> show session variables like '%wait_timeout%';
+-------------------------------------+----------+
| Variable_name                       | Value    |
+-------------------------------------+----------+
| innodb_lock_wait_timeout            | 50       |
| innodb_print_lock_wait_timeout_info | OFF      |
| lock_wait_timeout                   | 31536000 |
| wait_timeout                        | 28800    |
+-------------------------------------+----------+
4 rows in set (0.53 sec)

Default wait_timeout value is 28800 seconds. 

If we need to set this timeout for a session we can use below command.
mysql> SET session wait_timeout=300; 

If we need to change the wait_timeout global value we should follow below steps:
    1. Open the my.cnf file which resides in /etc/mysql/ directory 
    2. Add below value with the mysqld blog to my.cnf file 
```
