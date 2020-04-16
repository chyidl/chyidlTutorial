# Configure MySQL Master-Slave Replication on Ubuntu 18.04
> MySql replication is a process that allows data from one database server to be automatically copied to one or more servers.

```
MySQL supports a number of replication topologies with Master/Slave topology being one of the most well-known topologies in which one database server acts as the master, while one or more servers act as slaves. By default, the replication is asynchronous where the master sends events that describe database modification to its binary log and slaves request the events when they are ready.
```

* Prerequisties
```
Master IP: 192.168.1.2 
Slave IP: 192.168.1.7 
```

* Install MySQL 
```
To avoid any issues, it is best to install the same MySQL version on both servers. 

Install MySQL on the Master/Slave server 
Step 1 - Adding the MySQL Software Repository 
  $ cd /tmp 
  $ curl -OL https://dev.mysql.com/get/mysql-apt-config_0.8.15-1_all.deb 
    -O : output to a file instead of standard output 
    -L : make curl follow HTTP redirects, necessary in this case because the address we copied actually redirects us to another location before the file download.
  $ sudo dpkg -i mysql-apt-config* 
  $ sudo apt update 
  $ rm mysql-apt-config* 

Step 2 - Installing MySQL 
  $ sudo apt install mysql-server 
$ sudo apt-get update 
$ sudo apt-get install mysql-server 
```

* Configure the Master Server 
```
# Set the MySQL server to listen on the private IP 
# Set a unique server ID 
# Enable the binary logging 
To do so open the MySQL configuration file and uncomment or set the following.
-Master 
  $ sudo vim /etc/mysql/mysql.conf.d/mysqld.conf 
    bind-address  = 192.168.1.2 
    server-id = 1 
    log_bin = /var/log/mysql/mysql-bin.log
   
  # Restart the MySQL service for changes to takes effect.
  $ sudo systemctl restart mysql 
  
  # Create a new replication user. Login in to the MySQL server as the root user
  $ sudo mysql 

  # Run the following SQL queries that will create the replica user and grant the REPLICATION SLAVE privilege to the user. 
  mysql> CREATE USER 'replica'@'%' IDENTIFED BY 'replica_password';
  mysql> GRANT REPLICATION SLAVE ON *.* TO 'replica'@'%'; 
  # Will print the binary filename and position
  mysql> SHOW MASTER STATUS\G
  *************************** 1. row ***************************
               File: mysql-bin.000001
           Position: 601
       Binlog_Do_DB:
   Binlog_Ignore_DB:
  Executed_Gtid_Set:
  1 row in set (0.00 sec)
==================================================================================
-Slave 
  $ sudo vim /etc/mysql/mysql.conf.d/mysqld.conf 
    bind-address = 192.168.1.7 
    server-id = 2 
    log_bin = /var/log/mysql/mysql-bin.log 
  # restart the MySQL service for changes to takes effect. 
  $ sudo systemctl restart mysql 
  # The next step is to configure the parametes that the slave server will use to connect to the master server.
  $ sudo mysql 
  # First, stop the slave threads 
  mysql> STOP SLAVE;
  # Run the following query that will set up the slave to replicate the master.
  mysql> CHANGE MASTER TO 
  mysql> MASTER_HOST='192.168.1.2',
  mysql> MASTER_USER='replica',
  mysql> MASTEr_PASSWORD='replica_password',
  mysql> MASTER_LOG_FILE='mysql-bin.000001',
  mysql> MASTER_LOG_POS=601;
  # Start the slave threads.
  mysql> START SLAVE.
```

* Test the Configuration 
```
At This point, you should have work Master/Slave replication setup. 
To Verify that everything works as expected, we'll create a new database on the master server:
$ sudo mysql 
mysql> CREATE DATABSE replicatest; 
```

![Master-Slave](/imgs/ilikeit/MySQLCrashCourse/Master-Slave-MySQL.png?raw=true)
