Enable the MySQL Slow Query Log
===============================

```
$ sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf 

# Here you can see queries with especially long duration
slow_query_log      = 1
# Set the path to the slow query log
slow_query_log_file = /var/log/mysql/mysql-slow.log
# default is 10 seconds 
long_query_time = 0  
log-queries-not-using-indexes

Confirm the changes are active by entering the MySQL shell and running the following command:
mysql> SHOW VARIABLES LIKE '%slow%';
+---------------------------+-------------------------------+
| Variable_name             | Value                         |
+---------------------------+-------------------------------+
| log_slow_admin_statements | OFF                           |
| log_slow_slave_statements | OFF                           |
| slow_launch_time          | 2                             |
| slow_query_log            | ON                            |
| slow_query_log_file       | /var/log/mysql/mysql-slow.log |
+---------------------------+-------------------------------+
5 rows in set (0.09 sec)

Restart the MySQL service:
$ sudo systemctl restart mysql
```

```
# As of MySQL 5.7.2, the log_timestamps system variable controls the timestamp
# time zone of messages written to the error log (as well as to general query log
# and slow query log files). Permitted values are UTC (the default) and SYSTEM (
# local system time zone). Before MySQL 5.7.2, message uses the local system time zone.
log_timestamps = SYSTEM
```
