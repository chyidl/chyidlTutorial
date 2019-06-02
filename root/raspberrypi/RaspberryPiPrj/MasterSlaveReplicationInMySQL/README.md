Set Up Master Slave Replication in MySQL
========================================

* About MySQL replication

```
MySQL replication is a process that allows you to easily maintain multiple copies of a MySQL data by having them copied automatically from a master to a slave database. This can helpful for many reasons including facilating a backup for the data,a way to analyze it without using the main database, or simply as a means to scale out.

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

```
