MySQL Crash Course
==================
> The offical way to pronounce "MySQL" is "My Ess Que Ell" is an open source relational database management system (RDBMS).
> MySQL is written in C and C++. Its SQL parser is written in yacc, but it uses a home-brewed lexical analyzer.
```
(MacOSX)
$ brew install mysql-client 
$ vim ~/.zshrc
add /usr/local/opt/mysql-client/bin/mysql to path 
```

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
mysql> GRANT SELECT, UPDATE, DELETE ON *.* TO 'newuser'@'%';

# To grant the SELECT privilege on table t to the authorization IDs maria and harry, use the following syntax:
mysql> GRANT SELECT, UPDATE, TRIGGER, EXECUTE ON TABLE t TO maria,harry;

# revoke a permission
mysql> REVOKE type_of_permission ON database_name.table_name FROM 'username'@'localhost';
# revoke all privileges of the user
mysql> REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'username'@'localhost';

# MySQL query to get column names?
mysql> SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='yourdatabasename' AND `TABLE_NAME` = 'yourtablename';

# check the privileges of the user
mysql> SHOW GRANTS FOR user;

# drop user 
mysql> DROP USER 'username'@'%';

# log out 
mysql> quit 

# Don't forget reload all the privileges, 
$ FLUSH PRIVILEGES; 刷新权限
```

Reset Root Password in MySQL
----------------------------
* Reset MySQL Root Password Using - init-file 
```
# One of the ways to reset the root password is to create a local file and then start the MySQL service using --init-file option as shown.
$ vim /home/user/init.file.txt 

# It is important that you make sure that file is readable by the mysql user. Within that file paste the following:
    ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';

# Now make sure that the MySQL service is stopped. 
$ sudo systemctl stop mysqld.service            # for distros using systemd 
$ sudo /etc/init.d/mysqld stop                  # for distros using init 

# Then run the following:
$ sudo mysqld --user=mysql --init-file=/home/user/init-file.txt --console 

# This will start the MySQL service and during the process it will execute the init-file that you have created and thus the password for the root user will be updated. Make sure to delete the file once the password has been reset.

# Make sure to stop the server and start it normally after that.
$ systemctl stop mysqld.service         # for distros using systemd 
$ systemctl restart mysqld.service      # for distros using systemd 

$ sudo /etc/init.d/mysqld stop          # for distros using init 
$ sudo /etc/init.d/mysqld restart       # for distros using init

# You should now be able to connect to the MySQL server as root using the new password 
$ mysql -u root -p 
```

* Reset MySQL Root Password Using -skip-grant-tables 
```
# The second option to start the MySQL service with the --skip-grant-tables option. This is less secure as while the service is started that way, all users can connect without password.

If the server is started --skip-grant-tables, the option for --skip-networking is automatically activated so remote connections will not be available.

# First make sure that the MySQL service is stopped.
$ sudo systemctl stop mysqld.service    # for distros using systemd 
$ sudo /etc/init.d/mysqld stop          # for distros using init 

# Then start service with the following option.
$ sudo mysqld --skip-grant-tables --user=mysql & 

# Then, you can connect to the mysql server by simply running.
$ mysql 

# Since account-management is disabled when the service is started with --skip-grant-tables option, we will have to reload the grants. That way will be able to change the password later.
mysql> FLUSH PRIVILEGES; 

# Now can run the following query to update the password. Make sure to change "new_password" with the actual password you wish to use.
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'new_password';

# Now stop the MySQL server and start it normally
$ sudo systemctl stop mysqld.service        # for distros using systemd 
$ sudo systemctl restart mysqld.service     # for distroes using systemd 
$ sudo /etc/init.d/mysqld stop              # for distros using init 
$ sudo /etc/inid.d/mysqld restart           # for distros using init

# You should be able to connect with your new password.
$ mysql -u root -p 
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


FQA & Shadowscosk
-----------------
```
https://stackoverflow.com/questions/2675323/mysql-load-null-values-from-csv-data
MySQL load NULL values from csv data 
    
    LOAD DATA infile '/tmp/testdata.txt'
    INTO TABLE moo 
    fields terminated BY ","
    lines terminated BY "\n"
    (one, two, three, @vfour, file) 
    SET four = nullif(@vfour, '');

https://dev.mysql.com/doc/refman/5.5/en/packet-too-large.html
MySQL Packet Too Large:
    A communication packet is a single SQL statement sent to the MySQL server, a single row that is sent to the client, or a binary log event sent from a master replication server to a slave.

    Both the client and the server have thier own max_allowed_packet variable, so if you want to handle big packets, you must increase this variable both in the client and in the server.
    
    If you are using the mysql client program, its default max_allowed_packet variable is 16MB. To set a larger value, start mysql like this:
        shell> mysql --max_allowed_packet=32M 

    The server's default max_allowed_packet value is 1MB. You can increase the if the server needs to handle big queries(for example, if you are working with big BLOB columns).
        shell> mysqld --max_allowed_packet=16M 

    You can also use an option file to set max_allowed_packet.
    [mysqld]
    max_allowed_packet = 16M 
```

SHOW ENGINE 
-----------
```
# SHOW ENGINE displays operational information about a storage engine. 
mysql> SHOW ENGINE engine_name {STATUS | MUTEX}
    # display extensive information from the stadard InnoDB Monitor about the state of the InnoDB storage engine.
    SHOW ENGINE INNODB STATUS 
    # display InnoDB mutex and rw-lock
    SHOW ENGINE INNODB MUTEX
    SHOW ENGINE PERFORMANCE_SCHEMA STATUS 
```

How to Backup & Restore A MySQL Database  
----------------------------------------
```
Back up From the Command Line with mysqldump
    The mysqldump client utility can dump a database including the SQL statements required to rebuild the database. 
    By default, the dump file includes the SQL commands to restore the tables and data
    1. The simplest case is the whole database dumping:
        $ mysqldump -u [username] -p[password] [database_name] > [the_whole_database_dump].sql 
    2. Sometimes, there's a need to dump a single table from your database 
        $ mysqldump -u username -ppassword database_name table_name > single_table_dump.sql 
        # Can also specify several tables separated by whitespace to dump these tables only 
        $ mysqldump -u username -ppassword database_name table_name1 table_name2 table_name3 > single_table_dump.sql 
    3. If you want to dump only rows that meet a specific criteria. you can add 'where' option to your mysqldump command. 
        For example, dump only rows where date_created is today.
        $ mysqldump -u username -ppassword database_name table_name --where="date_created='2019-08-01'" > few_rows_dump.sql 
    4. To backup of an entire Database Management System:
        $ mysqldump --all-databases --single-transaction --quick --lock-tables=false -u root -ppasswd > full-backup-$(date +%F).sql 
    5. To include more than one database in the backup dump file:
        $ sudo mysqldump -u [user] -p[password] [database_1] [database_2] [database_3] > [filename].sql

How to Restore MySQL with mysqldump 
    1. Restore MySQL Dump 
    To restore a MySQL backup
    $ mysql -u [user] -p[password] [database_name] < [filename].sql 
```

MySQL 数据库优化
----------------
> 一个成熟的数据库架构并不是一开始设计就具备高可用、高伸缩特性，是随着用户量的增加，基础架构才逐渐完善，一下主要介绍MySQL数据库发展周期所面临的问题以及优化方案
```
1. 数据库表设计
开发人员对表结构设计，对于数据库来讲，如果表设计不合适，会直接影响访问速度和用户体验，影响因素很多，比如满查询、低效的查询语句、没有适当建立索引、数据库堵塞(死锁)

2. 数据库部署
单台部署应该足以应对1500QPS(每秒查询率).考虑高可用性，可采用MySQL著丛复制和Keepalived做双击热备，常用的集群软件有Keepalived, Heartbeat.

3. 数据库性能优化
如果将MySQL部署到普通PC电脑上，不经过任何优化情况下，MySQL理论值正常可以处理2000左右QPS。经过优化后，有可能提升到2500左右的QPS。否则，当访问量达到1500左右的并发连接时，数据库处理性能就会变很慢。往往操作系统和数据库默认配置都比较保守，会对数据库发挥有一定的限制。客队这些配置进行适当的调整，尽可能的处理更多连接数。
    3.1: 数据库配置优化
        MySQL常用的两种存储引擎:
            MyISAM: 不支持事务处理，读性能处理快，表级别锁
            InnoDB: 支持事务处理(ACID),设计目标是为处理大容量数据发挥最大性能，行级别锁
        表锁：开销小，锁定粒度大，发生死锁概率高，相对并发比较低
        行锁：开销大，锁定粒度小，发生死锁概率低，相对并发比较高
        使用表锁和行锁主要是保证数据的完整性
        
        connect_timeout = 
        net_read_timeout=600
        net_write_timeout=180
        wait_timeout=86400
        interactive_timeout = 86400
        max_allowed_packet = 128M 
        
        max_connections = 151 -- 同时处理最大连接数，推荐设置最大连接数是上限连接数的80%左右
        sort_buffer_size = 2M -- 查询排序时缓冲区大小，只对ORDER BY 和 GROUP BY起作用，可增大此值为16M 
        open_files_limit = 7048 -- 打开文件数限制，如果show global status like 'open_files' 查看的值等于或者大约open_files_limit值，程序会无法连接数据库或卡死.

    InnoDB 参数默认值:
        innodb_buffer_pool_size = 128M -- 索引和数据缓冲区大小，一般设置物理内存的60%-70% 
        innodb_buffer_pool_instances = 1 -- 缓冲池实例个数，推荐设置4个或8个
        innodb_flush_log_at_trx_commit = 1 --
        0代表大约每秒写入到日志并同步到磁盘，数据库故障会丢失1秒左右的事务数据，1为没执行一条SQL后写入到日志并同步到磁盘，I/O开销大，执行完SQL要等待日志读写，效率低。2代表只把日志写入到系统缓存区，再每秒同步到磁盘，效率很高，如果服务器故障，才会丢失事务数据，对数据安全性要求不是很高的推荐设置为2，性能高，修改后效果明显
        innodb_file_per_table = OFF -- 默认是开启共享表空间，共享表空间idbdata文件不断增大，影响一定的I/O性能。推荐开启独立表空间模式，每个表的索引和数据都存在自己独立的表空间中，可以实现单表不同数据库中移动
        innodb_log_buffer_size = 8M -- 日志缓冲区大小，由于日志最长每秒钟刷新一次，所以一般不用超过16M
    
    3.2 系统内核优化(Linux操作系统的一些参数会影响MySQL性能，一下对Linux内核进行适当优化)
        net.ipv4.tcp_fin_timeout = 30  -- TIME_WAIT超时时间，默认是60s 
        net.ipv4.tcp_tw_reuse = 1 -- 1表示开启复用，允许TIME_WAIT socket重新用于新的TCP连接,0表示关闭
        net.ipv4.tcp_tw_recycle = 1 -- 1表示开启TIME_WAIT socket快速回收，0表示关闭
        net.ipv4.tcp_max_tw_buckets = 4096 -- 系统保持TIME_WAIT socket最大数量，如果超过这个数，系统将随机清除一些TIME_WAIT并打印警告信息
        net.ipv4.tcp_max_syn_backlog = 4096 -- 进入SYN队列最大长度，加大队列长度可以容纳更多的等待连接.
        在Linux系统中，如果进程打开的文件句柄数量超过默认值1024，就会提示"too many files open"信息，所以要调整打开文件句柄限制
        $ vim /etc/security/limits.conf # 加入一下配置, *代表所有用户 也可以指定用户，重启系统生效
        * soft nofile 65535 
        * hard nofile 65535 
        $ ulimit -SHn 65535  # 立刻生效

    3.3 硬件配置
        加大物理内存，提高文件系统性能，Linux内核会从内存中分配出缓存区（系统缓存和数据缓存）来存放热数据，通过文锦啊系统延迟写入机制，等满足条件时（如缓存区大小到达一定百分比或者执行sync命令）才会同步到磁盘，物理内存越大，分配缓存区越大，混存数据越多，当然，服务器故障会丢失一定的缓存数据
        SSD硬盘代替SAS硬盘，将RAID级别调整为RAID1+0,现对于RAID1和RAID5有更好的读写性能(IOPS),毕竟数据库的压力主要来自磁盘IO方面。

4. 数据库架构扩展
随着业务量增加，单台数据库服务器性能无法满足业务需求，需要组件集群，主要思想是分而治之，分解单台数据库负载，突破磁盘I/O性能，热数据存放缓存中，降低磁盘I/O访问频率。
    4.1: 主从复制与读写分离
        因为生产环境中，数据库大多数都是读操作，所以部署主从架构，主数据库负责写操作，并做双击热备，多台从数据库做负载均衡，负责读操作，主流的负载均衡器有LVS，HAProxy,Nginx
        如何实现读写分离，大多数企业是在代码层实现读写分离，效率比较高，另一种方式通过代理程序实现读写分离，常用的代理程序有MySQL Proxy, Amoeba. 这样的数据库集群架构中，大大增加数据库高并发能力，解决单台性能瓶颈问题。如果从数据库一台从库能处理2000QPS，那么5台就能处理1WQPS，数据库横向扩展性很容易.
        如果，面对大量写操作的应用时，单台写性能达不到业务需求，如果做双主，就会遇到数据库数据不一致现象，产生这个原因是应用程序不同的用户会有可能操作两台数据库，同时的更新操作造成两台数据库发生冲突或者不一致,单库时MySQL利用存储引擎机制表锁和行锁来保证数据完整性. 有一台基于perl语言开发的主从复制管理工具，MySQL-MMM(Master-Master replication manager for MySQL,
        MySQL主主复制管理器)，这个工具最大的优点是在同一时间只提供一台数据库写操作，有效保证数据库一致性
    
    4.2: 增加缓存
        给数据库增加缓存系统，把热数据缓存到内存中，如果缓存中有要请求的数据就不再去数据库中返回结果。提高读性能，缓存实现有本地缓存和分布式缓存，本地缓存是将数据缓存到本地服务器内存中或文件中，分布式缓存可以缓存海量数据，扩展性好，主流的分布式缓存系统有Memcached,redis;
        memcached性能稳定，数据缓存在内存中，速度很快，QPS可达8W左右，数据库持久化存则使用redis

    4.3: 分库
        分库是业务不同把相关的表切分到不同的数据库中，如果业务量很大，还可以将切分后的库做主从架构，进一步避免单个库压力过大。

    4.4: 分表
        数据量的增加，数据库中某个表有千万条数据，导致查询和插入耗时太长，可以考虑将表拆分成小表，来减轻单个表的压力。提高处理效率，此方法称为分表。
        分表技术比较麻烦，要修改程序代码的SQL语句，还要手动创建其他表，可以使用merge存储引擎实现分表，相对简单许多，分表后，程序是对一个总表进行操作，这个总表不存放数据，只要一些分表的关系，以及更新数据的方式，总表会根据不同的查询，将压力分到不同的小表上，因此提高并发能力和磁盘I/O性能.
        分表分为垂直拆分和水平拆分：
            垂直拆分：把原来的一个很多字段拆分很多各表，解决表的宽度问题，可以将不常用的字段单独放在一个表中，也可以把大字段独立放一个表中，或者把关系密切的字段放一个表中。
            水平拆分：把原来一个表拆分成多个表，每个表的结构都一样，解决单个表数据量过大的问题.
    
    4.5: 分区
        分区是把一张表的数据根据表结构中的字段(range, list, hash)分成多个区块，这些区块可以在一个磁盘上，也可以在不同的磁盘上，分区后，表面上还是一张表，但是数据散列在多个位置，这样依赖
        
    
mysql> show processlist;
+-----+------+-----------------------+---------+---------+-------+-------------+------------------------------------------------------------------------------------------------------+
| Id  | User | Host                  | db      | Command | Time  | State       | Info                                                                                                 |
+-----+------+-----------------------+---------+---------+-------+-------------+------------------------------------------------------------------------------------------------------+
| 110 | root | WIN-UHA4VHLFV5N:55510 | history | Query   | 50621 | System lock | load data local infile 'E:/2018/S_L_20180316.csv' into table history_20180316 character set 'gbk' fi |
| 111 | root | WIN-UHA4VHLFV5N:55582 | history | Query   | 38615 | System lock | load data local infile 'E:/2018/S_L_20180319.csv' into table history_20180319 character set 'gbk' fi |
| 112 | root | WIN-UHA4VHLFV5N:55606 | history | Query   | 35584 | System lock | load data local infile 'E:/2018/S_L_20180320.csv' into table history_20180320 character set 'gbk' fi |
| 113 | root | WIN-UHA4VHLFV5N:55618 | history | Query   | 33028 | System lock | load data local infile 'E:/2018/S_L_20180321.csv' into table history_20180321 character set 'gbk' fi |
| 114 | root | WIN-UHA4VHLFV5N:55677 | history | Query   | 25121 | System lock | load data local infile 'E:/2018/S_L_20180322.csv' into table history_20180322 character set 'gbk' fi |
| 115 | root | WIN-UHA4VHLFV5N:55678 | history | Query   | 24778 | System lock | load data local infile 'E:/2018/S_L_20180323.csv' into table history_20180323 character set 'gbk' fi |
| 117 | root | WIN-UHA4VHLFV5N:55690 | history | Query   | 22468 | System lock | load data local infile 'E:/2018/S_L_20180326.csv' into table history_20180326 character set 'gbk' fi |
| 118 | root | WIN-UHA4VHLFV5N:55718 | history | Query   | 18940 | System lock | load data local infile 'E:/2018/S_L_20180327.csv' into table history_20180327 character set 'gbk' fi |
| 120 | root | WIN-UHA4VHLFV5N:55770 | history | Query   | 11592 | System lock | load data local infile 'E:/2018/S_L_20180328.csv' into table history_20180328 character set 'gbk' fi |
| 121 | root | WIN-UHA4VHLFV5N:55776 | history | Query   | 11154 | System lock | load data local infile 'E:/2018/S_L_20180329.csv' into table history_20180329 character set 'gbk' fi |
| 123 | root | 192.168.1.241:55002   | history | Sleep   |  2530 |             | NULL                                                                                                 |
| 124 | root | 192.168.1.241:55449   | history | Query   |     0 | init        | show processlist                                                                                     |
| 126 | root | 192.168.1.215:48556   | history | Query   |     2 | update      | INSERT INTO `history_20190813` VALUES (353339,0,'2019-08-13 09:30:51','002638',0,0,'002638.SZ','勤   |
+-----+------+-----------------------+---------+---------+-------+-------------+------------------------------------------------------------------------------------------------------+
13 rows in set (0.00 sec)

1. 分库分表的可能性
mysql> SELECT TABLE_SCHEMA AS "Database Name", ROUND(SUM(data_length + index_length)/1024/1024, 2) AS "Size in (MB)" FROM information_schema.TABLES GROUP BY TABLE_SCHEMA;
+--------------------+--------------+
| Database Name      | Size in (MB) |
+--------------------+--------------+
| history            |   9193633.81 |
| information_schema |         0.01 |
| mysql              |     17635.23 |
| performance_schema |         0.00 |
+--------------------+--------------+
4 rows in set (2 min 34.79 sec)

# How to fix Error Code 2013 Lost connection to MySQL server
Starting backup of source database hq, table history_20190813 -> destination database history
mysqldump: [Warning] Using a password on the command line interface can be insecure.
mysql: [Warning] Using a password on the command line interface can be insecure.
ERROR 2013 (HY000) at line 1106: Lost connection to MySQL server during query
Delete file : hq.history_20190813.sql completed.
[ '2019-08-14 12:47:19' ] 'migrate_db' (('rm-bp10t403rcn80qaxmio.mysql.rds.aliyuncs.com:3306:root:K5pMwOrXgPlRc4MZ', '192.168.1.22:3306:root:Cn123456', 'hq.history_20190813>history', 'backup', True), {}) 9401.07 sec
[ '2019-08-14 12:47:19' ] 'run' ((), {}) 9401.08 sec
    This error appears when the connection between MySQL client and MySQL server times out. Essentially, it took too long for the query to return data so the connection gets dropped.

# How to easily import multiple sql files into a MySQL databases?
    In Windows(powershell), open a terminal, go to the content folder and write:
        $ copy /b *.sql all_files.sql   
        This concate all files in only one, making it really quick to import with PhpMyAdmin. 
        $ cat *.sql | C:mysql.exe -u user -p database 
    In Linux and macOS(Bash), Put the result in a separate directory to be safe 
        $ mkdir concatSql 
        $ cat *.sql > ./concatSql/all_files.sql 
        $ cat *.sql | mysql -u user -p database 
```

aliyun RDS config
-----------------
```
automatic_sp_privileges = ON
auto_increment_increment = 1
auto_increment_offset = 1
back_log = 3000
binlog_cache_size = 2048KB
binlog_checksum = CRC32
binlog_order_commits = ON
binlog_rows_query_log_events = OFF
binlog_row_image = full
binlog_stmt_cache_size = 32768
block_encryption_mode = "aes-128-ecb"
bulk_insert_buffer_size = 4194304
character_set_client = utf8
character_set_filesystem = binary
character_set_server = utf8
concurrent_insert = 1
connect_timeout = 10
default_storage_engine = InnoDB
default_time_zone = SYSTEM
default_week_format = 0
delayed_insert_limit = 100
delayed_insert_timeout = 300
delayed_queue_size = 1000
delay_key_write = ON
disconnect_on_expired_password = ON
div_precision_increment = 4
end_markers_in_json = OFF
eq_range_index_dive_limit = 10
explicit_defaults_for_timestamp = false
flush_time = 0
ft_max_word_len = 84
ft_min_word_len = 4
ft_query_expansion_limit = 20
group_concat_max_len = 1024
host_cache_size = 643
innodb_adaptive_flushing = ON
innodb_adaptive_flushing_lwm = 10
innodb_adaptive_hash_index = ON
innodb_adaptive_max_sleep_delay = 150000
innodb_additional_mem_pool_size = 2097152
innodb_autoextend_increment = 64
innodb_autoinc_lock_mode = 1
innodb_buffer_pool_dump_at_shutdown = OFF
innodb_buffer_pool_instances = 8
innodb_buffer_pool_load_at_startup = OFF
innodb_change_buffering = all
innodb_change_buffer_max_size = 25
innodb_checksum_algorithm = innodb
innodb_cmp_per_index_enabled = OFF
innodb_commit_concurrency = 0
innodb_compression_failure_threshold_pct = 5
innodb_compression_level = 6
innodb_compression_pad_pct_max = 50
innodb_concurrency_tickets = 5000
innodb_disable_sort_file_cache = ON
innodb_flush_method = O_DIRECT
innodb_flush_neighbors = 1
innodb_ft_cache_size = 8000000
innodb_ft_enable_diag_print = OFF
innodb_ft_enable_stopword = ON
innodb_ft_max_token_size = 84
innodb_ft_min_token_size = 3
innodb_ft_num_word_optimize = 2000
innodb_ft_result_cache_limit = 2000000000
innodb_ft_sort_pll_degree = 2
innodb_ft_total_cache_size = 640000000
innodb_io_capacity = 2000
innodb_io_capacity_max = 4000
innodb_large_prefix = OFF
innodb_lock_wait_timeout = 50
innodb_log_compressed_pages = OFF
innodb_lru_scan_depth = 1024
innodb_max_dirty_pages_pct = 75
innodb_max_dirty_pages_pct_lwm = 0
innodb_max_purge_lag = 0
innodb_max_purge_lag_delay = 0
innodb_monitor_disable = 
innodb_monitor_enable = 
innodb_old_blocks_pct = 37
innodb_old_blocks_time = 1000
innodb_online_alter_log_max_size = 134217728
innodb_open_files = 3000
innodb_optimize_fulltext_only = OFF
innodb_print_all_deadlocks = OFF
innodb_purge_batch_size = 300
innodb_purge_threads = 1
innodb_random_read_ahead = OFF
innodb_read_ahead_threshold = 56
innodb_read_io_threads = 4
innodb_rollback_on_timeout = OFF
innodb_rollback_segments = 128
innodb_sort_buffer_size = 1048576
innodb_spin_wait_delay = 30
innodb_stats_auto_recalc = ON
innodb_stats_method = nulls_equal
innodb_stats_on_metadata = OFF
innodb_stats_persistent = ON
innodb_stats_persistent_sample_pages = 20
innodb_stats_sample_pages = 8
innodb_stats_transient_sample_pages = 8
innodb_status_output = OFF
innodb_status_output_locks = OFF
innodb_strict_mode = OFF
innodb_support_xa = ON
innodb_sync_array_size = 1
innodb_sync_spin_loops = 100
innodb_table_locks = ON
innodb_thread_concurrency = 0
innodb_thread_sleep_delay = 10000
innodb_write_io_threads = 4
interactive_timeout = 7200
join_buffer_size = 432KB
key_cache_age_threshold = 300
key_cache_block_size = 1024
key_cache_division_limit = 100
lc_time_names = en_US
lock_wait_timeout = 31536000
log_queries_not_using_indexes = OFF
log_throttle_queries_not_using_indexes = 0
long_query_time = 1
loose_gap_lock_raise_error = OFF
loose_gap_lock_write_log = OFF
loose_max_statement_time = 0
loose_optimizer_trace = enabled=off,one_line=off
loose_optimizer_trace_features = greedy_search=on,range_optimizer=on,dynamic_range=on,repeated_subselect=on
loose_rds_indexstat = OFF
loose_rds_max_tmp_disk_space = 10737418240
loose_rds_set_connection_id_enabled = ON
loose_rds_tablestat = OFF
loose_rds_threads_running_high_watermark = 50000
loose_thread_handling = "one-thread-per-connection"
loose_thread_pool_oversubscribe = 10
loose_thread_pool_size = 64
loose_thread_pool_stall_limit = 30
loose_tokudb_auto_analyze = 30
loose_tokudb_buffer_pool_ratio = 0
loose_validate_password_length = 8
low_priority_updates = 0
master_verify_checksum = OFF
max_allowed_packet = 1024M
max_binlog_stmt_cache_size = 18446744073709547520
max_connect_errors = 100
max_error_count = 64
max_heap_table_size = 16777216
max_join_size = 18446744073709551615
max_length_for_sort_data = 1024
max_prepared_stmt_count = 16382
max_seeks_for_key = 18446744073709500000
max_sort_length = 1024
max_sp_recursion_depth = 0
max_write_lock_count = 102400
metadata_locks_cache_size = 1024
min_examined_row_limit = 0
myisam_sort_buffer_size = 262144
net_buffer_length = 16384
net_read_timeout = 30
net_retry_count = 10
net_write_timeout = 60
old_passwords = 0
open_files_limit = 65535
optimizer_prune_level = 1
optimizer_search_depth = 62
optimizer_trace_limit = 1
optimizer_trace_max_mem_size = 16384
optimizer_trace_offset = -1
performance_schema = OFF
preload_buffer_size = 32768
query_alloc_block_size = 8192
query_cache_limit = 1048576
query_cache_min_res_unit = 4096
query_cache_size = 3145728
query_cache_type = 0
query_cache_wlock_invalidate = OFF
query_prealloc_size = 8192
range_alloc_block_size = 4096
rds_reset_all_filter = 0
slave_net_timeout = 60
slow_launch_time = 2
slow_query_log = ON
sort_buffer_size = 848KB
sql_mode = 
stored_program_cache = 256
table_definition_cache = 512
table_open_cache = 2000
table_open_cache_instances = 1
thread_cache_size = 100
thread_stack = 262144
tls_version = TLSv1,TLSv1.1,TLSv1.2
tmp_table_size = 2097152
transaction_alloc_block_size = 8192
transaction_isolation = READ-COMMITTED
transaction_prealloc_size = 4096
updatable_views_with_limit = YES
wait_timeout = 86400        
```

```
mysql> show status;
+-----------------------------------------------+-------------+
| Variable_name                                 | Value       |
+-----------------------------------------------+-------------+
| Aborted_clients                               | 3           | -- 客户端没有正确关闭连接已经死掉，已经放弃连接数量
| Aborted_connects                              | 0           | -- 尝试已经失败的MySQL服务器的连接的次数
| Binlog_cache_disk_use                         | 418         | -- 
| Binlog_cache_use                              | 418         |
| Binlog_stmt_cache_disk_use                    | 0           |
| Binlog_stmt_cache_use                         | 9           |
| Bytes_received                                | 243         |
| Bytes_sent                                    | 192         |
| Com_admin_commands                            | 0           |
| Com_assign_to_keycache                        | 0           |
| Com_alter_db                                  | 0           |
| Com_alter_db_upgrade                          | 0           |
| Com_alter_event                               | 0           |
| Com_alter_function                            | 0           |
| Com_alter_procedure                           | 0           |
| Com_alter_server                              | 0           |
| Com_alter_table                               | 0           |
| Com_alter_tablespace                          | 0           |
| Com_alter_user                                | 0           |
| Com_analyze                                   | 0           |
| Com_begin                                     | 0           |
| Com_binlog                                    | 0           |
| Com_call_procedure                            | 0           |
| Com_change_db                                 | 0           |
| Com_change_master                             | 0           |
| Com_check                                     | 0           |
| Com_checksum                                  | 0           |
| Com_commit                                    | 0           |
| Com_create_db                                 | 0           |
| Com_create_event                              | 0           |
| Com_create_function                           | 0           |
| Com_create_index                              | 0           |
| Com_create_procedure                          | 0           |
| Com_create_server                             | 0           |
| Com_create_table                              | 0           |
| Com_create_trigger                            | 0           |
| Com_create_udf                                | 0           |
| Com_create_user                               | 0           |
| Com_create_view                               | 0           |
| Com_dealloc_sql                               | 0           |
| Com_delete                                    | 0           |
| Com_delete_multi                              | 0           |
| Com_do                                        | 0           |
| Com_drop_db                                   | 0           |
| Com_drop_event                                | 0           |
| Com_drop_function                             | 0           |
| Com_drop_index                                | 0           |
| Com_drop_procedure                            | 0           |
| Com_drop_server                               | 0           |
| Com_drop_table                                | 0           |
| Com_drop_trigger                              | 0           |
| Com_drop_user                                 | 0           |
| Com_drop_view                                 | 0           |
| Com_empty_query                               | 0           |
| Com_execute_sql                               | 0           |
| Com_flush                                     | 0           |
| Com_get_diagnostics                           | 0           |
| Com_grant                                     | 0           |
| Com_ha_close                                  | 0           |
| Com_ha_open                                   | 0           |
| Com_ha_read                                   | 0           |
| Com_help                                      | 0           |
| Com_insert                                    | 0           |
| Com_insert_select                             | 0           |
| Com_install_plugin                            | 0           |
| Com_kill                                      | 0           |
| Com_load                                      | 0           |
| Com_lock_tables                               | 0           |
| Com_optimize                                  | 0           |
| Com_preload_keys                              | 0           |
| Com_prepare_sql                               | 0           |
| Com_purge                                     | 0           |
| Com_purge_before_date                         | 0           |
| Com_release_savepoint                         | 0           |
| Com_rename_table                              | 0           |
| Com_rename_user                               | 0           |
| Com_repair                                    | 0           |
| Com_replace                                   | 0           |
| Com_replace_select                            | 0           |
| Com_reset                                     | 0           |
| Com_resignal                                  | 0           |
| Com_revoke                                    | 0           |
| Com_revoke_all                                | 0           |
| Com_rollback                                  | 0           |
| Com_rollback_to_savepoint                     | 0           |
| Com_savepoint                                 | 0           |
| Com_select                                    | 1           |
| Com_set_option                                | 0           |
| Com_signal                                    | 0           |
| Com_show_binlog_events                        | 0           |
| Com_show_binlogs                              | 0           |
| Com_show_charsets                             | 0           |
| Com_show_collations                           | 0           |
| Com_show_create_db                            | 0           |
| Com_show_create_event                         | 0           |
| Com_show_create_func                          | 0           |
| Com_show_create_proc                          | 0           |
| Com_show_create_table                         | 0           |
| Com_show_create_trigger                       | 0           |
| Com_show_databases                            | 0           |
| Com_show_engine_logs                          | 0           |
| Com_show_engine_mutex                         | 0           |
| Com_show_engine_status                        | 0           |
| Com_show_events                               | 0           |
| Com_show_errors                               | 0           |
| Com_show_fields                               | 0           |
| Com_show_function_code                        | 0           |
| Com_show_function_status                      | 0           |
| Com_show_grants                               | 0           |
| Com_show_keys                                 | 0           |
| Com_show_master_status                        | 0           |
| Com_show_open_tables                          | 0           |
| Com_show_plugins                              | 0           |
| Com_show_privileges                           | 0           |
| Com_show_procedure_code                       | 0           |
| Com_show_procedure_status                     | 0           |
| Com_show_processlist                          | 0           |
| Com_show_profile                              | 0           |
| Com_show_profiles                             | 0           |
| Com_show_relaylog_events                      | 0           |
| Com_show_slave_hosts                          | 0           |
| Com_show_slave_status                         | 0           |
| Com_show_status                               | 1           |
| Com_show_storage_engines                      | 0           |
| Com_show_table_status                         | 0           |
| Com_show_tables                               | 0           |
| Com_show_triggers                             | 0           |
| Com_show_variables                            | 0           |
| Com_show_warnings                             | 0           |
| Com_slave_start                               | 0           |
| Com_slave_stop                                | 0           |
| Com_stmt_close                                | 0           |
| Com_stmt_execute                              | 0           |
| Com_stmt_fetch                                | 0           |
| Com_stmt_prepare                              | 0           |
| Com_stmt_reprepare                            | 0           |
| Com_stmt_reset                                | 0           |
| Com_stmt_send_long_data                       | 0           |
| Com_truncate                                  | 0           |
| Com_uninstall_plugin                          | 0           |
| Com_unlock_tables                             | 0           |
| Com_update                                    | 0           |
| Com_update_multi                              | 0           |
| Com_xa_commit                                 | 0           |
| Com_xa_end                                    | 0           |
| Com_xa_prepare                                | 0           |
| Com_xa_recover                                | 0           |
| Com_xa_rollback                               | 0           |
| Com_xa_start                                  | 0           |
| Compression                                   | OFF         |
| Connection_errors_accept                      | 0           |
| Connection_errors_internal                    | 0           |
| Connection_errors_max_connections             | 0           |
| Connection_errors_peer_address                | 0           |
| Connection_errors_select                      | 0           |
| Connection_errors_tcpwrap                     | 0           |
| Connections                                   | 18          | -- 尝试连接MySQL服务器的次数
| Created_tmp_disk_tables                       | 0           |
| Created_tmp_files                             | 8           |
| Created_tmp_tables                            | 0           | -- 创建临时表的数量
| Delayed_errors                                | 0           |
| Delayed_insert_threads                        | 0           | -- 延迟插入处理器线程的数量
| Delayed_writes                                | 0           | --  Insert delayed 写入的行数
| Flush_commands                                | 1           | -- 执行FLUSH命令的次数
| Handler_commit                                | 0           |
| Handler_delete                                | 0           | -- 请求从一张表中删除行的次数
| Handler_discover                              | 0           |
| Handler_external_lock                         | 0           |
| Handler_mrr_init                              | 0           |
| Handler_prepare                               | 0           |
| Handler_read_first                            | 0           | -- 请求读入表中第一行的次数
| Handler_read_key                              | 0           | -- 请求数字基于健读行
| Handler_read_last                             | 0           | -- 
| Handler_read_next                             | 0           |
| Handler_read_prev                             | 0           |
| Handler_read_rnd                              | 0           |
| Handler_read_rnd_next                         | 0           |
| Handler_rollback                              | 0           |
| Handler_savepoint                             | 0           |
| Handler_savepoint_rollback                    | 0           |
| Handler_update                                | 0           |
| Handler_write                                 | 0           |
| Innodb_buffer_pool_dump_status                | not started |
| Innodb_buffer_pool_load_status                | not started |
| Innodb_buffer_pool_pages_data                 | 511387      |
| Innodb_buffer_pool_bytes_data                 | 4083597312  |
| Innodb_buffer_pool_pages_dirty                | 4951        |
| Innodb_buffer_pool_bytes_dirty                | 81117184    |
| Innodb_buffer_pool_pages_flushed              | 3370514     |
| Innodb_buffer_pool_pages_free                 | 8102        |
| Innodb_buffer_pool_pages_misc                 | 4799        |
| Innodb_buffer_pool_pages_total                | 524288      |
| Innodb_buffer_pool_read_ahead_rnd             | 0           |
| Innodb_buffer_pool_read_ahead                 | 113         |
| Innodb_buffer_pool_read_ahead_evicted         | 0           |
| Innodb_buffer_pool_read_requests              | 470742403   |
| Innodb_buffer_pool_reads                      | 1354537     |
| Innodb_buffer_pool_wait_free                  | 0           |
| Innodb_buffer_pool_write_requests             | 185052399   |
| Innodb_data_fsyncs                            | 204698      |
| Innodb_data_pending_fsyncs                    | 0           |
| Innodb_data_pending_reads                     | 0           |
| Innodb_data_pending_writes                    | 0           |
| Innodb_data_read                              | 1586827264  |
| Innodb_data_reads                             | 1406797     |
| Innodb_data_writes                            | 3524553     |
| Innodb_data_written                           | 834403840   |
| Innodb_dblwr_pages_written                    | 3370514     |
| Innodb_dblwr_writes                           | 66220       |
| Innodb_have_atomic_builtins                   | ON          |
| Innodb_log_waits                              | 0           |
| Innodb_log_write_requests                     | 38821748    |
| Innodb_log_writes                             | 63212       |
| Innodb_os_log_fsyncs                          | 64300       |
| Innodb_os_log_pending_fsyncs                  | 0           |
| Innodb_os_log_pending_writes                  | 0           |
| Innodb_os_log_written                         | 14942577152 |
| Innodb_page_size                              | 16384       |
| Innodb_pages_created                          | 38571       |
| Innodb_pages_read                             | 1402983     |
| Innodb_pages_written                          | 3370514     |
| Innodb_row_lock_current_waits                 | 0           |
| Innodb_row_lock_time                          | 0           |
| Innodb_row_lock_time_avg                      | 0           |
| Innodb_row_lock_time_max                      | 0           |
| Innodb_row_lock_waits                         | 0           |
| Innodb_rows_deleted                           | 0           |
| Innodb_rows_inserted                          | 1244414     |
| Innodb_rows_read                              | 0           |
| Innodb_rows_updated                           | 0           |
| Innodb_num_open_files                         | 257         |
| Innodb_truncated_status_writes                | 0           |
| Innodb_available_undo_logs                    | 128         |
| Key_blocks_not_flushed                        | 0           |
| Key_blocks_unused                             | 6698        |
| Key_blocks_used                               | 0           |
| Key_read_requests                             | 0           |
| Key_reads                                     | 0           |
| Key_write_requests                            | 0           |
| Key_writes                                    | 0           |
| Last_query_cost                               | 0.000000    |
| Last_query_partial_plans                      | 0           |
| Max_used_connections                          | 4           |
| Not_flushed_delayed_rows                      | 0           |
| Open_files                                    | 18          |
| Open_streams                                  | 0           |
| Open_table_definitions                        | 313         |
| Open_tables                                   | 303         |
| Opened_files                                  | 394         |
| Opened_table_definitions                      | 0           |
| Opened_tables                                 | 0           | -- 已经打开表的数量
| Performance_schema_accounts_lost              | 0           |
| Performance_schema_cond_classes_lost          | 0           |
| Performance_schema_cond_instances_lost        | 0           |
| Performance_schema_digest_lost                | 0           |
| Performance_schema_file_classes_lost          | 0           |
| Performance_schema_file_handles_lost          | 0           |
| Performance_schema_file_instances_lost        | 0           |
| Performance_schema_hosts_lost                 | 0           |
| Performance_schema_locker_lost                | 0           |
| Performance_schema_mutex_classes_lost         | 0           |
| Performance_schema_mutex_instances_lost       | 0           |
| Performance_schema_rwlock_classes_lost        | 0           |
| Performance_schema_rwlock_instances_lost      | 0           |
| Performance_schema_session_connect_attrs_lost | 0           |
| Performance_schema_socket_classes_lost        | 0           |
| Performance_schema_socket_instances_lost      | 0           |
| Performance_schema_stage_classes_lost         | 0           |
| Performance_schema_statement_classes_lost     | 0           |
| Performance_schema_table_handles_lost         | 0           |
| Performance_schema_table_instances_lost       | 0           |
| Performance_schema_thread_classes_lost        | 0           |
| Performance_schema_thread_instances_lost      | 0           |
| Performance_schema_users_lost                 | 0           |
| Prepared_stmt_count                           | 0           |
| Qcache_free_blocks                            | 1           |
| Qcache_free_memory                            | 1031432     |
| Qcache_hits                                   | 0           |
| Qcache_inserts                                | 0           |
| Qcache_lowmem_prunes                          | 0           |
| Qcache_not_cached                             | 11          |
| Qcache_queries_in_cache                       | 0           |
| Qcache_total_blocks                           | 1           |
| Queries                                       | 892         |
| Questions                                     | 2           | -- 查询数量
| Select_full_join                              | 0           |
| Select_full_range_join                        | 0           |
| Select_range                                  | 0           |
| Select_range_check                            | 0           |
| Select_scan                                   | 0           |
| Slave_heartbeat_period                        | 0.000       |
| Slave_last_heartbeat                          |             |
| Slave_open_temp_tables                        | 0           |
| Slave_received_heartbeats                     | 0           |
| Slave_retried_transactions                    | 0           |
| Slave_running                                 | OFF         |
| Slow_launch_threads                           | 0           |
| Slow_queries                                  | 0           |
| Sort_merge_passes                             | 0           |
| Sort_range                                    | 0           |
| Sort_rows                                     | 0           |
| Sort_scan                                     | 0           |
| Ssl_accept_renegotiates                       | 0           |
| Ssl_accepts                                   | 0           |
| Ssl_callback_cache_hits                       | 0           |
| Ssl_cipher                                    |             |
| Ssl_cipher_list                               |             |
| Ssl_client_connects                           | 0           |
| Ssl_connect_renegotiates                      | 0           |
| Ssl_ctx_verify_depth                          | 0           |
| Ssl_ctx_verify_mode                           | 0           |
| Ssl_default_timeout                           | 0           |
| Ssl_finished_accepts                          | 0           |
| Ssl_finished_connects                         | 0           |
| Ssl_server_not_after                          |             |
| Ssl_server_not_before                         |             |
| Ssl_session_cache_hits                        | 0           |
| Ssl_session_cache_misses                      | 0           |
| Ssl_session_cache_mode                        | NONE        |
| Ssl_session_cache_overflows                   | 0           |
| Ssl_session_cache_size                        | 0           |
| Ssl_session_cache_timeouts                    | 0           |
| Ssl_sessions_reused                           | 0           |
| Ssl_used_session_cache_entries                | 0           |
| Ssl_verify_depth                              | 0           |
| Ssl_verify_mode                               | 0           |
| Ssl_version                                   |             |
| Table_locks_immediate                         | 75          | -- 立即释放表锁数
| Table_locks_waited                            | 0           | -- 等待的表锁数
| Table_open_cache_hits                         | 0           |
| Table_open_cache_misses                       | 0           |
| Table_open_cache_overflows                    | 0           |
| Tc_log_max_pages_used                         | 0           |
| Tc_log_page_size                              | 0           |
| Tc_log_page_waits                             | 0           |
| Threads_cached                                | 2           |
| Threads_connected                             | 2           |
| Threads_created                               | 4           |
| Threads_running                               | 1           | -- 运行的线程数量
| Uptime                                        | 12163       | -- 服务器工作时间
| Uptime_since_flush_status                     | 12163       |
+-----------------------------------------------+-------------+
341 rows in set (0.01 sec)

mysql>
```

MySQL 写压力性能监控与调优
--------------------------
```
1. OS 层面的监控: iostat -x 
$ iostat -x [yum install sysstat]
    写入吞吐量: wkB/s 
    监控系统的io状况: 主要查看%util, r/s, w/s 

2. DB层面监控, 监控各种pending （挂起）
mysql> show global status like '%pend%';
+------------------------------+-------+
| Variable_name                | Value |
+------------------------------+-------+
| Innodb_data_pending_fsyncs   | 2     | -- 被挂起的fsync 
| Innodb_data_pending_reads    | 0     | -- 被挂起的物理读
| Innodb_data_pending_writes   | 0     | -- 被挂起的写
| Innodb_os_log_pending_fsyncs | 1     | -- 被挂起的日志fsync 
| Innodb_os_log_pending_writes | 0     | -- 被挂起的日志写 
+------------------------------+-------+
5 rows in set (0.00 sec)

3. 写入速度监控: 日志写，脏页写
mysql> show global status like '%log%written'; -- 日志写入速度监控
+-----------------------+-------------+
| Variable_name         | Value       |
+-----------------------+-------------+
| Innodb_os_log_written | 11863974912 |
+-----------------------+-------------+
1 row in set (0.00 sec)

mysql> show global status like '%a%written'; -- 脏页写入速度监控
+----------------------------+------------+
| Variable_name              | Value      |
+----------------------------+------------+
| Innodb_data_written        | 2395576320 | -- 目前为止写的总的数据量，单位字节
| Innodb_dblwr_pages_written | 1806643    |
| Innodb_pages_written       | 1806688    | -- 写数据页的数据
+----------------------------+------------+
3 rows in set (0.00 sec)

mysql> SELECT @@sql_mode;
+----------------------------------------------------------------+
| @@sql_mode                                                     |
+----------------------------------------------------------------+
| STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION |
+----------------------------------------------------------------+
1 row in set (0.00 sec)

# To change the SQL mode at runtime, set the global or session sql_mode system variable using a SET statement
    SET GLOBAL sql_mode = 'modes';
    SELECT @@GLOBAL.sql_mode;

    SET SESSION sql_mode = 'modes';
    SELECT @@SESSION.sql_mode;

# Important 
    SQL mode and user-defined partitioning. Changing the server SQL mode after creating and inserting data into partitioned tables can cause major changes in the behavior of such tables, and could lead to loss or corruption of data. It is strongly recommended that you never change the SQL mode once you have created tables employing user-defined partitioning.
    When replicating partitioned tables, differing SQL modes on the master and slave can also lead to problems. For best results, you should always use the same server SQL mode on the master and slave.

更改/etc/my.cnf 
    [mysqld]
    sql_mode=NO_ENGINE_SUBSTITUTION 
考虑到数据的兼容性和准确性，MySQL就应该运行在严格模式下，无论开发环境还是生产环境，否则代码移植到线上可能产生隐藏的问题.

sql_mode常用值说明:
    SQL语法支持类:
        ONLY_FULL_GROUP_BY: 对于GROUP BY聚合操作，如果在SELECT中的列，HAVING或者ORDER BY子句的列，没有在GROUP BY中出现，那么这个SQL是不合法的。
        ANSI_QUOTES: 启动ANSI_UOTES后，不能用双引号来引用字符串，因为“”被解释为标识符，作用与`一样，设置之后，update t set f1="" ... 
        PIPES_AS_CONCAT: 启动PIPES_AS_CONCAT将||视为字符窜的连接操作而非或运算符，这和Oracle数据库是一样的，也和字符串的拼接函数CONCAT()相类似.
        NO_TABLE_OPTIONS: 启用后，使用SHOW CREATE TABLE不会输出

    ANSI: This mode changes syntax and behavior to conform more closely to standard SQL. Equivalent to [REAL_AS_FLOAT, PIPES_AS_CONCAT, ANSI_QUOTES, IGNORE_SPACE,ONLY_FULL_GROUP_BY]

    
    STRICT_TRANS_TABLES: INSERT、UPDATE出现少值或无效值如何处理
        1. 转给int的空值，严格模式下非法，若启用非严格模式则变为0，产生一个warning
        2. Out of Range, 变成插入最大边界值
        3. A value is missing when a new row to be inserted does not contain a value for a non-NULL column that has no explicit DEFAULT clause in its definition.
    
    NO_ZERO_IN_DATE:
    
    NO_ZERO_DATE:
    
    ERROR_FOR_DIVISION_BY_ZERO:
    
    NO_AUTO_CREATE_USER:
    
    NO_ENGINE_SUBSTITUTION:
```

Drop multiple tables with name pattern
--------------------------------------
```
# 1. Get the list of the Table to Drop 
We can easily retrieve the table list making a selection in sys.tables using the where condition to filter the result to obtain only the record where name start with Tabx the following code make it.
mysql> SELECT table_name FROM information_schema.tables WHERE table_schema like 'history%';
+------------------+
| TABLE_NAME       |
+------------------+
| history_20190624 |
| history_20190625 |
| history_20190626 |
| history_20190627 |
| history_20190628 |
| history_20190701 |
| history_20190702 |
| history_20190703 |
| history_20190704 |
| history_20190705 |
| history_20190708 |
| history_20190709 |
| history_20190710 |
| history_20190711 |
| history_20190712 |
| history_20190715 |
| history_20190716 |
| history_20190717 |
| history_20190718 |
| history_20190719 |
| history_20190720 |
| history_20190722 |
| history_20190723 |
| history_20190724 |
| history_20190725 |
| history_20190726 |
| history_20190729 |
| history_20190730 |
| history_20190731 |
| history_20190801 |
| history_20190802 |
| history_20190805 |
| history_20190806 |
| history_20190807 |
| history_20190808 |
| history_20190809 |
| history_20190812 |
| history_20190813 |
| history_20190814 |
| history_20190815 |
| history_20190816 |
| history_20190819 |
+------------------+
42 rows in set (0.01 sec)

2. Compose a Drop Command
For each record of the result of the first step to compose the sql Drop Command.
mysql> SELECT CONCAT('DROP TABLE ', table_name, ';') AS `DROP Command` FROM information_schema.tables WHERE table_schema like 'history_%';
+------------------------------+
| Drop Command                 |
+------------------------------+
| DROP TABLE history_20190624; |
| DROP TABLE history_20190625; |
| DROP TABLE history_20190626; |
| DROP TABLE history_20190627; |
| DROP TABLE history_20190628; |
| DROP TABLE history_20190701; |
| DROP TABLE history_20190702; |
| DROP TABLE history_20190703; |
| DROP TABLE history_20190704; |
| DROP TABLE history_20190705; |
| DROP TABLE history_20190708; |
| DROP TABLE history_20190709; |
| DROP TABLE history_20190710; |
| DROP TABLE history_20190711; |
| DROP TABLE history_20190712; |
| DROP TABLE history_20190715; |
| DROP TABLE history_20190716; |
| DROP TABLE history_20190717; |
| DROP TABLE history_20190718; |
| DROP TABLE history_20190719; |
| DROP TABLE history_20190720; |
| DROP TABLE history_20190722; |
| DROP TABLE history_20190723; |
| DROP TABLE history_20190724; |
| DROP TABLE history_20190725; |
| DROP TABLE history_20190726; |
| DROP TABLE history_20190729; |
| DROP TABLE history_20190730; |
| DROP TABLE history_20190731; |
| DROP TABLE history_20190801; |
| DROP TABLE history_20190802; |
| DROP TABLE history_20190805; |
| DROP TABLE history_20190806; |
| DROP TABLE history_20190807; |
| DROP TABLE history_20190808; |
| DROP TABLE history_20190809; |
| DROP TABLE history_20190812; |
| DROP TABLE history_20190813; |
| DROP TABLE history_20190814; |
| DROP TABLE history_20190815; |
| DROP TABLE history_20190816; |
| DROP TABLE history_20190819; |
+------------------------------+
42 rows in set (0.01 sec)

3. Execute
For each result of the step 2, to execute the command, 
```

Change MySQL Data Directory to New Location
-------------------------------------------
```
Step 1 - Moving the MySQL Data Directory 
# verify the current location
$ mysql -u root -p 
mysql> select @@datadir;
+-----------------+
| @@datadir       |
+-----------------+
| /var/lib/mysql/ |
+-----------------+
1 row in set (0.00 sec)

# to ensure the integrity of the data, should shut down MySQL before actually make change to the data directory
$ sudo systemctl stop mysqld 
# verify the mysql had shut down
$ sudo systemctl status mysqld 

# Now that the server is shut down, we'll copy the existing database directory to the new location with rsync. Using the -a flag preserves the permissions and other directory properties, while -v provides verbose output so you can follow the progress.
$ sudo rsync -av /var/lib/mysql /mnt/chyi_data

# Once the rsync is complete. renames the current folder with a .bak extension and keep it untile we've confirmed the move was successful. 
$ sudo mv /var/lib/mysql /var/lib/mysql.bak 

Step 2: Pointing to the New Data Location 
# MySQL has several ways to override configuration values. By default, the datadir is set to /var/lib/mysql in the /etc/my.cnf file. Edit this file to reflect the new data directory.
$ sudo vim /etc/my.cnf 
# need to update it to the new location:
    [mysqld]
    datadir=/mnt/chyi_data/mysql 
    socket=/mnt/chyi_data/mysql/mysql.sock 

# After updating the existing lines, we'll need to add configuration for the mysql client. Insert the following settings at the bottom of the file so it won't split yo directives in the [mysqld] block:
    [client]
    port=3306
    socket=/mnt/chyi_data/mysql/mysql.sock 

Step 3: Restarting MySQL 
$ sudo systemctl start mysqld 
$ sudo systemctl status mysqld 

# To make sure that the new data directory is indeed in use, start the MySQL monitor
$ mysql -u root -p 

# Look at the value for the data directory again
$ SELECT @@datadir; 
+-----------------------+
| @@datadir             |
+-----------------------+
| /mnt/chyi_data/mysql/ |
+-----------------------+
1 row in set (0.00 sec)

# Now that you've restarted MySQL and confimed that it's using the new location, take the opportunity to ensure that your database is fully functional. Once you've verified the integrity of any existing data, you can remove the backup data directory with 
$ sudo rm -Rf /var/lib/mysql.bak 
```

MySQL 关闭/定期自动清理/手动清理binlog日志文件 
----------------------------------------------
* 关闭mysql binlog日志 
```
# 查看当前日志情况
mysql> show master logs;
+----------------------------+-----------+
| Log_name                   | File_size |
+----------------------------+-----------+
| WIN-UHA4VHLFV5N-bin.000001 |       154 |
+----------------------------+-----------+
1 row in set (0.01 sec)

# 删除10天前的MySQL binlog日志,可以根据需求修改时间 
mysql> PURGE MASTER LOGS BEFORE DATE_SUB(CURRENT_DATE, INTERVAL 10 DAY);

# 删除清空日志 
mysql> reset master;
Query OK, 0 rows affected (0.19 sec)

# 修改mysql配置文件 
mysql> show variables like 'log_bin';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| log_bin       | ON    |
+---------------+-------+
1 row in set, 1 warning (0.01 sec)

mysql> show variables like 'binlog_format';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| binlog_format | ROW   |
+---------------+-------+
1 row in set, 1 warning (0.00 sec)

$ vim /etc/my.cnf
    # log-bin=mysql-bin
    # binlog_format=mixed 

# 自动清理binlog - 修改配置文件/etc/my.cnf,设置expire_logs_days
    $ vim /etc/my.cnf   // 修改expire_logs_days,表示自动删除的天数 
        expire_logs_days=7  // 日志自动删除的天数,默认值为0,表示"没有自动删除"

mysql> show variables  like 'expire_logs_days';
+------------------+-------+
| Variable_name    | Value |
+------------------+-------+
| expire_logs_days | 7     |
+------------------+-------+
1 row in set, 1 warning (0.00 sec)

$ systemctl restart mysql 
```

How to Open A Port In CentOS/REHL 7 
-----------------------------------
> A TCP/IP network connection may be either blocked, dropped, open, or filtered. These actions are generally controlled by the IPtables firewall the system uses and is independent of ant process or program that may be listening on a network port. This port will outline the steps to open a port required by application.
```
# Server details are as below:
$ uname -a 
Linux local-machine199 3.10.0-957.el7.x86_64 #1 SMP Thu Nov 8 23:39:32 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux

$ cat /etc/redhat-release 
CentOS Linux release 7.7.1908 (Core)

1. Check Port Status 
$ netstat -an | grep 3306 
tcp6       0      0 :::3306                 :::*                    LISTEN     
tcp6       0      0 :::33060                :::*                    LISTEN  

2. Check Port Status in iptables 
$ iptables-save | grep 3306 
-A INPUT -p tcp -m tcp --dport 3306 -j DROP

3. Add the port 
# Add the test port in /etc/services file and allow the port to accept packets. Test port can be added by editing /etc/services file in below format:
$ vim /etc/services 
# service-name  port/protocol  [aliases ...]   [# comment]
mysql           3306/tcp                        # MySQL
mysql           3306/udp                        # MySQL

4. Open firewall ports 
# Add Firewall rule to allow the port to accept packets 
$ iptables -A INPUT -p tcp -m tcp --dport 3306 -j ACCEPT
$ iptables -F   # --flush the selected chain (all the chains in the table if none is given). This is equivalent to deleting all the rules one by one.

5. Check newly added port status 
$ netstat -an | grep 3306 
tcp6       0      0 :::3306                 :::*                    LISTEN      127783/mysqld       
tcp6       0      0 :::33060                :::*                    LISTEN      127783/mysqld       
tcp6       0      0 192.168.1.199:3306      192.168.1.251:50908     ESTABLISHED 127783/mysqld 
```

Show Users, Privileges and Passwords
------------------------------------

| Tables | SqlString                                               | Notes                                                                                                                 |
| ------ | :------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------- |
| mysql> | SELECT user FROM mysql.user;                            | Show all MySQL users                                                                                                  |
| mysql> | SELECT DISTINCT user FROM mysql.user;                   | List only unique user names                                                                                           |
| mysql> | SELECT user, host FROM mysql.user;                      | Show MySQL users and hosts they are allowed to connect from                                                           |
| mysql> | SELECT user,host,authentication_string FROM mysql.user; | Show MySQL users, their passwords and hosts                                                                           |
| mysql> | SHOW GRANTS;                                            | Show privileges granted to the current MySQL user.                                                                    |
| mysql> | SHOW GRANTS FOR 'user_name';                            | Show privileges granted to the MySQL user(if you dontt specify a host for the user name, MySQL assumes % as the host) |
| mysql> | SHOW GRANTS FOR 'user_name'@'host';                     | Show privileges granted to a particular MySQL user account from a given host;                                         |

Auto-Restart MySQL When It Crashes During a Brute Force Attack
--------------------------------------------------------------
```
# Using a simple cronjob to check and restart MySQL if it is down
# Load the crontab editor in the terminal 
$ crontab -e 

* * * * * systemctl status mysql > /dev/null || systemctl restart mysql 

This checks If MySQL is running every minute and redirects stdout to null. Starting the service will not output anything unless something goes wrong, so there is no need to add the null redirect on the last command. 
The double pipe || means OR and will execute the second command only if the first command fails. 

In other words: If MySQL's status returns an exit code greater than zero(first command), start MySQL(second command).

*/5 * * * * systemctl status mysql > /dev/null || systemctl restart mysql 
```
