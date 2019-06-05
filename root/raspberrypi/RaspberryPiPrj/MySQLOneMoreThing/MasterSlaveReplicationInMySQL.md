Set Up Master Slave Replication in MySQL
========================================

* About MySQL replication
> MySQL replication is a process that allows you to easily maintain multiple copies of a MySQL data by having them copied automatically from a master to a slave database. This can helpful for many reasons including facilating a backup for the data,a way to analyze it without using the main database, or simply as a means to scale out.

```
Master Database: 192.168.31.127 
Slave  Database: 192.168.31.156 
```

* Install MySQL
```
$ sudo apt-get install mysql-server mysql-client 
$ mysql --version 
mysql  Ver 14.14 Distrib 5.7.26, for Linux (aarch64) using  EditLine wrapper
```

* Step One - Configure the Master Database 
```
# Open up the mysql configuration file on the master server.
$ sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf

# Once inside that file, we need to make a few changes.

# The first step is to find the section that looks like this, binding the server to the locat host:
bind-address  = 127.0.0.1 
# Replace the standard IP address with the IP address of server.
bind-address = 192.168.31.156

# The next configureation change referes to the server-id, location in the [mysqld] section. You can choose any number for this spot(it may just be easier to start with 1), but the number must be unique and cannot match any other server-id in your replication group. I'm going to go ahead and call this one 1.
# Make sure this line is uncommented 
server-id = 1 

# Move on to the log_bin line. This is where the real details of the replication are kept. The slave is going to copy all of the changes that are registered in the log. For this step we simply need to uncomment the line that refers to log_bin:
log_bin = /var/log/mysql/mysql-bin.log

# Finally, we need to designate the database that will be replicated on the slave server. You can include more than one database by repeating this line for all of the databases you will need.
binlog_do_db = newdatabase 

# After you make all of the changes, go ahead and save and exit out of the configuration file.
# Refresh MySQL 
$ sudo systemctl restart mysql 

# Open up the MySQL shell.
$ mysql -u root -p 

# We need to grant privileges to the slave. You can use this line to name your slave and set up their password. The command should be in this format:
mysql> GRANT REPLICATION SLAVE ON *.* TO 'slave_user'@'%' IDENTIFIED BY 'password';

# Follow up with:
mysql> FLUSH PRIVILEGES;

# The next part is a bit finicky. To accomplish the task you will need to open a new window or tab in addition to the one that you are already using a few steps down the line.
mysql> USE newdatabase; 

# Following that, lock the databases to prevent any new changes:
mysql> FLUSH TABLES WITH READ LOCK;

# Then type in:
mysql> SHOW MASTER STATUS;

# You will see a table that should lock something like this:
mysql> SHOW MASTER STATUS;
+------------------+----------+--------------+------------------+-------------------+
| File             | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
+------------------+----------+--------------+------------------+-------------------+
| mysql-bin.000001 |      154 | newdatabase  |                  |                   |
+------------------+----------+--------------+------------------+-------------------+
1 row in set (0.00 sec)

# This is the position from which the slave database will start replicating. Record these numbers, they will come in useful later.
# If you make any new changes in the same window, the database will automatically unlock, For this reason, you should open the new tab or window and continue with the next steps there.
# Procedding the with the database still locked, export your database using mysqldump in the new window (make sure you are typing this command in the bash, not in MySQL)
$ mysqldump -u root -p --opt newdatabase > newdatabase.sql

# Now, returning to your original window, unlock the databases (making them writeable again). Finish up by exiting the shell. 
mysql> UNLOCK TABLES:
mysql> QUIT;

# Now you are all done with the configuration of the master database.
```

* Step Two - Configure the Slave Database 
```
# Once you have configured the master database. You can put it aside for a while, and we will now begin to configure the slave database.
# Log into your slave server, open up the MySQL shell and create the new database that you will be replicating from the master (then exit):
mysql> CREATE DATABASE newdatabase;
mysql> EXIT;

# Import the database that you previously exported from the master database.
$ mysql -u root -p newdatabase < /path/to/newdatabase.sql 

# Now we need to configure the slave configuration in the same way as we did the master.
$ sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf

# We have to make sure that we have a few things set up in this configuration. The first is the server-id. This number, as mentioned before needs to be unique. Since it is set on the default(still 1), be sure to change it's something different. 
server-id = 2

# Following that, make sure that you have the following three criteria appropriately filled out:
relay_log = /var/log/mysql/mysql-relay-bin.log 
log_bin = /var/log/mysql/mysql-bin.log 
binlog_do_db = newdatabase 

# You will need to add in the relay-log line: it is not there by default. Once you have made all of the necessary changes, save and exit out of the slave configuration file.

# Restart MySQL once again:
$ sudo service mysql restart 

# The next step is to enable the replication from within the MySQL shell.
# Open up the MySQL shell once again and type in the following details, replacing the values to match your information:
mysql> CHANGE MASTER TO MASTER_HOST="192.168.31.156", MASTER_USER='slave_user', MASTER_PASSWORD='password', MASTER_LOG_FILE='mysql-bin.000001', MASTER_LOG_POS= 154;

# This command accomplishes several things at the same time:
    1. It designate the current server as the slave of our master server.
    2. It provides the server the correct login credentials 
    3. Last of all, it lets the slave server know where to start replicating from; the master log file and log position come from the numbers we wrote down previously.

# With that - you have configured a master and slave server.
# Activate the slave server:
mysql> START SLAVE;

# You be able to see the details of the slave replication by typing in this command. The \G rearranges the text to make it more readable. 
mysql> SHOW SLAVE STATUS\G
*************************** 1. row ***************************
               Slave_IO_State: Waiting for master to send event
                  Master_Host: 192.168.60.122
                  Master_User: chyidl
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: mysql-bin.000009
          Read_Master_Log_Pos: 73091744
               Relay_Log_File: mysql-relay-bin.000013
                Relay_Log_Pos: 3755276
        Relay_Master_Log_File: mysql-bin.000009
             Slave_IO_Running: Yes
            Slave_SQL_Running: Yes
              Replicate_Do_DB:
          Replicate_Ignore_DB:
           Replicate_Do_Table:
       Replicate_Ignore_Table:
      Replicate_Wild_Do_Table:
  Replicate_Wild_Ignore_Table:
                   Last_Errno: 0
                   Last_Error:
                 Skip_Counter: 0
          Exec_Master_Log_Pos: 73091744
              Relay_Log_Space: 43933689
              Until_Condition: None
               Until_Log_File:
                Until_Log_Pos: 0
           Master_SSL_Allowed: No
           Master_SSL_CA_File:
           Master_SSL_CA_Path:
              Master_SSL_Cert:
            Master_SSL_Cipher:
               Master_SSL_Key:
        Seconds_Behind_Master: 0
Master_SSL_Verify_Server_Cert: No
                Last_IO_Errno: 0
                Last_IO_Error:
               Last_SQL_Errno: 0
               Last_SQL_Error:
  Replicate_Ignore_Server_Ids:
             Master_Server_Id: 1
                  Master_UUID: d0da05f5-6718-11e9-ac13-b827eb532b1b
             Master_Info_File: /var/lib/mysql/master.info
                    SQL_Delay: 0
          SQL_Remaining_Delay: NULL
      Slave_SQL_Running_State: Slave has read all relay log; waiting for more updates
           Master_Retry_Count: 86400
                  Master_Bind:
      Last_IO_Error_Timestamp:
     Last_SQL_Error_Timestamp:
               Master_SSL_Crl:
           Master_SSL_Crlpath:
           Retrieved_Gtid_Set:
            Executed_Gtid_Set:
                Auto_Position: 0
         Replicate_Rewrite_DB:
                 Channel_Name:
           Master_TLS_Version:
1 row in set (0.01 sec)

If there is an issue in connecting, you can tru starting slave with a command to skip over it:
mysql> SET GLOBAL SQL_SLAVE_SKIP_COUNTER = 1; SLAVE START;
```
