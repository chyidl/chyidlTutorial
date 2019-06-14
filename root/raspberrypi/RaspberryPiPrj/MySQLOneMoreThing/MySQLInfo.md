MySQL Server Info
=================

* SHOW VARIABLES - SHOW [GLOBAL | SESSION] VARIABLES [LIKE 'pattern' | WHERE expr] 
> SHOW VARIABLES shows the values of MySQL system variables. This statement does not require any privilege. It requires only the ability to connect to the server.

* SELECT VERSION();

* mysql> status; 
mysql> status;
--------------
```
mysql  Ver 14.14 Distrib 5.7.26, for Linux (aarch64) using  EditLine wrapper

Connection id:          73
Current database:
Current user:           chyidl@localhost
SSL:                    Not in use
Current pager:          less
Using outfile:          ''
Using delimiter:        ;
Server version:         5.7.26-0ubuntu0.18.04.1-log (Ubuntu)
Protocol version:       10
Connection:             Localhost via UNIX socket
Server characterset:    utf8mb4
Db     characterset:    utf8mb4
Client characterset:    utf8mb4
Conn.  characterset:    utf8mb4
UNIX socket:            /var/run/mysqld/mysqld.sock
Uptime:                 2 days 3 hours 49 min 53 sec

Threads: 2  Questions: 1188  Slow queries: 0  Opens: 160  Flush tables: 1  Open tables: 153  Queries per second avg: 0.006
--------------

mysql>
```

* SHOW ENGINE INNODB STATUS\G 
```
mysql> pager less 
PAGER set to 'lesss'
mysql> show engine innodb status\G 

# Now you are inside **less** and you can easily navigate through the result set(use q to quit, space to scroll down, etc.)

# Reminder: If you want to leave your custom pager, this is easy, just run \n:
mysql> \n 
PAGER set to stdout 

# You can pass the output of queries to most Unix programs that are able to work on text.
mysql> pager cat > /dev/null 
PAGER set to 'cat > /dev/null' 

# Trying an execution plan 
mysql> SELECT * FROM temp_20190610 LIMIT 10;
10 rows in set (0.01 sec)

# Another execution plan 
mysql> SELECT * FROM temp_20190610;
670788 rows in set (21.84 sec)
```

* SHOW PROCESSLIST;
```
Customize `show processlist` in MySQL

# Newer version of SQL support the process list in information_schema:
mysql> SELECT * FROM INFORMATION_SCHEMA.PROCESSLIST; 

mysql> SELECT * FROM INFORMATION_SCHEMA.PROCESSLIST WHERE `INFO` LIKE 'SELECT %';
mysql> SELECT * FROM INFORMATION_SCHEMA.PROCESSLIST WHERE `INFO` NOT LIKE 'NULL';

# pager: the most common usage of pager is to set it to a Unix pager such as less. 
# It can be very useful to view the result of a command spanning over many lines.
mysql> pager grep -v Sleep | more; show full processlist;

# Cleaning up SHOW PROCESSLIST
# Count How many connections are sleeping 
mysql> pager grep Sleep | wc -l 
PAGER set to 'grep Sleep | wc -l'
mysql> show processlist; 

# Show the number of connections for each status:
mysql> pager awk -F '|' '{print $6}' | sort | uniq -c | sort -r 
PAGER set to 'awk -F '|' '{print $6}' | sort | uniq -c | sort -r'
mysql> show processlist; 

# For instance, counting the number of sleeping connections can be done with:
mysql> SELECT COUNT(*) FROM INFORMATION_SCHEMA.PROCESSLIST WHERE COMMAND = 'Sleep';
# Counting the number of connection for each status can be done with:
mysql> SELECT COMMAND, COUNT(*) TOTAL FROM INFORMATION_SCHEMA.PROCESSLIST GROUP BY COMMAND ORDER BY TOTAL DESC;
```
