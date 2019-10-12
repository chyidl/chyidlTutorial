Monitor MySQL
=============

* Monitoring MySQL: metrics and alerts
```
    - MySQL process running 

|Metric|Comments|Suggested Alert|
|:---|:---|:---|
|mysqld process count|Right binary daemon process running.|When process count /usr/sbin/mysqld != 1|

    - System Metrics on a SQL Server 
> These are the top system resources to monitor on a database server. When you experience ant issue or bottleneck, these are the first you need to have a look at:

|Metric|Comments|Suggested Alert|
|:---|:---|:---|
|Load|An all-in-one performance metric. Understanding Linux Load.|When load is > factor x(number of cores).|
|CPU usage|A high CPU usage is not a bad thing as long as you don't reach the limit|None|
|Memory usage|Ideally your entire database should be stored in memory, but this is not always possible.Give MySQL as much as you can afford but leave enough for other processes to function|None|
|Swap usage|Swap is for emergencies only, and it should not be used.|When used swap is >128MB.|
|Network bandwidth|Unless doing backups or transferring huge amount of data, it shouldn't be the bootleneck.|None|
|Disk usage|Make sure you always have free space for new data, temporary files,snapshot or backups.|When database, logs and temp is > 85% usage.|

> Disk is one of the most common bottlencks, so it's worth keeping an eye on some detailed metrics here. You can get those with iostat(for more info on iostat) check out Monitoring IO performance using iostat & pt-diskstats.

|Metric|Comments|Suggested Alert|
|:---|:---|:---|
|Read/Write requests|IOPS (Input/Output operations per second)|None|
|IO Queue length|Tracks how many operations are waiting for disk access. If a query hits the cache, it doesn't create any disk operation. If a query doesn't hit the cache (i.e. a miss), it will create multiple disk operations|None|
|Average IO wait|Time that queue operations have to wait for disk access.|None|
|Average Read/Write time|Time it takes to finish disk access operations (latency).|None|
|Read/Write bandwidth|Data transfer from and towards your disk.|None|

    - MySQL Metrics 
> Monitoring MySQL availability and connections 

|Metric|Comments|Suggested Alert|
|:---|:---|:---|
|Uptime|Seconds since the server was started. We can use this to detect respawns|When uptime is <180|
|Threads_connected|Number of clients currently connected. If none or too high, something is wrong|show status like 'Threads_connected';|
|Max_used_connections|Max number of connections at a time since server started.(max_used_connections / max_connections) indicates if you could run out soon of connection slots.|When connections usage is > 85%.|
|Aborted_connects|Number of failed connection attempts. When growing over a period of time either some credentials are wrong or we are being attacked.|show status like 'Aborted_connects'; When aborted connects/min > 3.(only on not public exposed servers, otherwise will generate noise)|

    - MySQL typical errors

|Metric|Comments|Suggested Alert|
|:---|:---|:---|
|Erros|Are there any errors on the mysql.log file?|None|
|Log files size|Are all log files being rotated?|None|
|Deleted log files|Were any log files deleted but the file descriptor is still open?|None|
|Backup space|Do you have enough disk space for backups?|None|

    - Monitoring MySQL queries 

|Metric|Comments|Suggested Alert|
|:---|:---|:---|
|Questions|Number of statements sent by clients|show processlist;|
|Queries|Number of executed statements (including stored procedures)|None|
|Read/Writes|Reads: selects\+ cache hits Writes: inserts|+ updates \+ deletes|None|

> These metrics keep track of the queries that are affecting your server's performance:

|Metric|Comments|Suggested Alert|
|:---|:---|:---|
|Slow_queries|Number of queries that took more than long_query_time seconds to execute. Slow queries generate excessive disk reads, memory and CPU usage. Check slow_query_log to find them.| None|
|Select_full_join|Number of full joins needed to answer queries. If too high, improve your indexing or database schema|None|
|Created_tmp_disk_tables|Number of temporary tables (typically for joins) stored on slow spinning disks, instead of faster RAM.|None|
|Full table scans Handler_read%|Number of times the system reads the first row of a table index. Sequential reads might indicate a faulty index.|show global status like 'Handler_read%'|

    - Monitoring MySQL caches, buffers, and locks

|Metric|Comments|Suggested Alert|
|:---|:---|:---|
|Innodb_row_lock_waits|Number of times InnoDB had to wait before locking a row|show global status like 'Innodb_row_lock_waits'|
|Innodb_buffer_pool_wait_free|Number of times InnoDB had to wait for memory pages to be flushed, If too high innodb_buffer_pool_size is too small for current write load.|None|
|Open_tables|Number of tables currently open. If this is low and table_cache is high, we can reduce cache size. If opposite, we should increase. If you increase table_cache you might have to increase available file descriptors for the mysql user.|None|
|Long running transactions|Tracks whether too many transactions are locked by other idle transactions, or because of a problem in InnoDB.|None|
|Deadlocks|Deadlocks happen when 2 transactions mutually hold. These are unavoidable in InnoDB and apps should deal with them|None|
```

* MySQL Monitoring Methods and Tools
------------------------------------
```
# MySQL queries / mysqladmin 
    
    $ mysql -u root -p 
    SHOW GLOBAL STATUS;
    [...]
    SHOW GLOBAL STATUS LIKE 'aborted_connects';
    [...]
    SHOW PROCESSLIST;
    [...]
```

How MySQL 'queries' and 'questions' are measured
------------------------------------------------
```
Queries:
    The number of statements executed by the server. This variable includes statements executed within stored programs, unlike the Questions variable. It does not count COM_PING or COM_STATISTICS commands.

Questions:
    The number of statements executed by the server. This includes only statements sent to the server by clients and not statements executed within stored programs, unlike the Queries variable. This variable does not count COM_PING, COM_STATISTICS, COM_STMT_PERPARK, COM_STMT_CLOSE, or COM_STMT_RESET commands.

mysql> show status like 'queries';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| Queries       | 6137  |
+---------------+-------+
1 row in set (0.00 sec)

mysql> show status like 'questions';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| Questions     | 18    |
+---------------+-------+
1 row in set (0.00 sec)
```

Mytop to Monitor MySQL Performance
----------------------------------
> Mytop is an open source, command line tool used for monitoring MySQL performance. Mytop connects to a MySQL server and periodically runs the show processlist and show global status commands. It then summaries the information in a useful format. 
> Using mytop, monitor(in real-time) MySQL threads, queries, and uptime as well as see which user is running queries on which database, which are the slow queries, and more. All this information can be used to optimize the MySQL server performance.
```
Step 1 - Installing Mytop 
    $ sudo apt-get install mytop 

Step 2 - Cofiguring Mytop 
    $ vim ~/.mytop
    add the following content in the file and save and exit 
        host=localhost
        user=lplus
        password=Cn123456
        port=3306
        db=
        delay=5     # delay option specifies the amount of time in seconds between displat refreshes
        socket=
        batchmode=0
        color=1
        idle=1 # whether to allow idle(sleeping) thread to appear in the list in mytop display screen.

Step 3 - Connecting to Mytop
    $ mytop --prompt 

Step 4 - Viewing and Interpreting the Mytop Display
    The above display screen is broken into two parts. The top four lines comprises the header which can be roggled on or off by pressing SHIFT-H. The header contains summary information about your MySQL server.
    1. The first line identifies the hostname of the server and the version of MySQL it is running. The right-hand side shows the uptime of the MySQL server process in days+hours:minutes:seconds format as well as the current time.
    2. The second line displays the total number of queries the server has processed , the average number of queries per seconds.the number of slow queries, and the percentage of Select, Insert, Update, and Delete queries.
    3. The third line shows real-time values since last mytop refresh. The normal refresh (delay) time for mytop is 5 seconds,
    4. The fourth line displays key buffer efficiency(how often keys are read from the buffer rather than disk) and the number
```
