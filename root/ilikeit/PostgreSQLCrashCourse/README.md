PostgreSQL Crash Course
=======================
> PostgreSQL Slogan "世界上最先进的开源关系型数据库"
> Relational database management systems are a key component of many web sites and applications. They provide a structured way to store, organize, and access information.

> PostgreSQL, is a relational database management system that provides an implementation of the SQL querying language. supporting reliable transactions and concurrency without read locks.
```
RDBMS: 关系型数据库存储和管理大数据量；建立在关系模型基础上的数据库，
ORDBMS: 对象关系数据库系统 
  数据库：关系表的集合
  数据表: 数据的矩阵
  冗余：存储多组数据，冗余降低性能，提高数据的安全性
  主键：数据表中只能包含一个主键
  复合键：将多列作为索引键 
  索引：使用索引可以快速访问数据表中特定的信息，索引是对数据表中一列或多列的值进行排序的一种结构
  参照完整性:参考的完整性要求关系中不允许引用不存在的实体
  实体完整性: 保证数据的一致性
  函数: 可以在数据库服务器执行指定程序
  触发器: 触发器是由SQL语句查询所触发的事件 触发器通常是由INSERT、UPDATE语句触发 
  多版本并发控制MVCC(Multiversion concurrency control) 系统进行并发控制，该系统向每个用户提供一个数据库的“快照” 用户在事务内所做的每个修改对于其他用户都不可见，直到该事务成功提交
  数据类型:文本、任意精度的数值数组、JSON数据、枚举类型、XML数据
  全文搜索: Tsearch2 或 OpenFTS 

```
Step1 - Installing PostgreSQL
-----------------------------
```
$ sudo apt-get update 
# postgresql-contrib package that adds additional utilities and functionality
$ sudo apt-get install postgresql postgresql-contrib postgresql-client

# 安装完成系统默认创建超级用户postgres,密码空
$ sudo -i -u postgres

# Checking postgreSQL status 
$ sudo systemctl status postgresql.service 
or 
$ sudo systemctl status postgresql@10-main 

# Allow remote access to PostgreSQL server
# Step 1 - Update postgresql.conf 
$ vim /etc/postgresql/10/main/postgresql.conf
# search for postgresql.conf 
$ sudo find / -name "postgresql.conf"
# - Connection Settings - 
# What IP address(es) to listen on;
# comma-separated list of addresses;
# default to 'localhost'; use '*' for all 
listen_addresses = '*'

# Step 2. Configuring pg_hba.conf 
# Add the following line in the pg_hba.conf file to allow access to all databases for all users with an encrypted passworde, also change address 
# from IPv4 127.0.0.1/32 to 0.0.0.0/0 and IPv6 from ::1/128 to ::0/0. 
$ vim /etc/postgresql/10/main/pg_hba.conf 

# Step 3. Restart PostgreSQL Server 
$ sudo systemctl restart postgresql 

# Step 4. Adjusting Firewall (optional)
$ sudo ufw allow 5432/tcp 
```

Step2 - Using PostgreSQL Roles and Databases
--------------------------------------------
```
PostgreSQL use "roles" to handle in authentication and authorization. 

The installation procedure created a user account called postgres that is associated with the default Postgres role. In order to use Postgres, you can log into that account.


# Switching Over to the postgres Account
$ sudo -i -u postgres
# access a Postgres
postgres@RPi3BPlus:~$ psql
psql (10.7 (Ubuntu 10.7-0ubuntu0.18.04.1))
Type "help" for help.

# Exit out of the PostgreSQL prompt 
postgres=# \q

# Accessing a Postgres Prompt without Switching Accounts 
$ sudo -u postgres psql
psql (10.7 (Ubuntu 10.7-0ubuntu0.18.04.1))
Type "help" for help.

postgres=# \q
```

Step3 - Creating a New Role 
---------------------------
```
# Currently, you just have the postgres role configured within the database. create new roles from the command line with the `createrole` command.
$ sudo -u postgres createuser --interactive
Enter name of role to add: pi
Shall the new role be a superuser? (y/n) y
```

Step 4 - Relations, CRUD, and Joins
-----------------------------------
```
# Another assumption that the Postgres authentication system makes by default is that for any role used to log in, that role will have a database with the same name which is can access.
# createdb command create the appropriate database
$ createdb pi

# connect to a different database (PostgreSQL Client/Server framework, default port 5432, psql: Client)
$ psql -d another_db 

# check your current connection information 
$ psql -d pi
psql (10.7 (Ubuntu 10.7-0ubuntu0.18.04.1))
Type "help" for help.

# (#) as an administrator; ($) as a regular user.
pi=# \conninfo
You are connected to database "pi" as user "pi" via socket in "/var/run/postgresql" at port "5432".

# \h lists information about SQL command 
pi=# \h CREATE INDEX
Command:     CREATE INDEX
Description: define a new index
Syntax:
CREATE [ UNIQUE ] INDEX [ CONCURRENTLY ] [ [ IF NOT EXISTS ] name ] ON table_name [ USING method ]
    ( { column_name | ( expression ) } [ COLLATE collation ] [ opclass ] [ ASC | DESC ] [ NULLS { FIRST | LAST } ] [, ...] )
       [ WITH ( storage_parameter = value [, ... ] ) ]
       [ TABLESPACE tablespace_name ]
       [ WHERE predicate ]

# \? help with psql-specific commands 
pi=# \? 

# CRUD is a useful mnemonic for remembering the basic data management operations: Create, Read, Update, and Delete.

# Creating and Deleting Tables 
pi=# CREATE TABLE playground (
    equip_id serial PRIMARY KEY,  
    type varchar(50) NOT NULL, 
    color varchar(25) NOT NULL, 
    location varchar(25) check (location in ('north', 'south', 'west', 'east', 'northeast', 'southeast', 'southwest', 'northwest')),
    install_date date);
CREATE TABLE
pi=#

# the serial type. This data type is an auto-incrementing integer. 
# the primary key which means that the value must be unique and not null 
# install_date date, create a date column that records the date on which you installed the equipment.

# Check new table 
pi=# \d
                  List of relations
 Schema |          Name           |   Type   | Owner
--------+-------------------------+----------+-------
 public | playground              | table    | pi
 public | playground_equip_id_seq | sequence | pi
(2 rows)

pi=#

# playground_equip_id_sep, this keeps track of the next number in the sequence and is created automatically for column of this type.

# Check the table without the sequence 
pi=# \dt 

# Adding,Querying,and Deleting Data in a Table 
pi=# INSERT INTO playground (type, color, location, install_date) VALUES ('slide', 'blue', 'south', '2019-04-27');
INSERT 0 1
pi=# INSERT INTO playground (type, color, location, install_date) VALUES ('swing', 'yellow', 'northwest', '2019-04-27');
INSERT 0 1

# Retrieve the information 
pi=# SELECT * FROM playground;
  equip_id | type  | color  | location  | install_date
 ----------+-------+--------+-----------+--------------
         1 | slide | blue   | south     | 2019-04-27
         2 | swing | yellow | northwest | 2019-04-27
(2 rows)

# remove the row from your table by typing 
pi=# DELETE FROM playground WHERE type = 'slide';
DELETE 1

# Query the table again:
pi=# SELECT * FROM playground;
 equip_id | type  | color  | location  | install_date
----------+-------+--------+-----------+--------------
        2 | swing | yellow | northwest | 2019-04-27
(1 row)

# Adding and Deleting Columns from a Table 
# Add a column to show the last maintenance visit for each of equipment
pi=# ALTER TABLE playground ADD last_maint date;
ALTER TABLE
pi=# SELECT * FROM playground;
  equip_id | type  | color  | location  | install_date | last_maint
 ----------+-------+--------+-----------+--------------+------------
         2 | swing | yellow | northwest | 2019-04-27   |
(1 row)

# Deleting a column
pi=# ALTER TABLE playground DROP last_maint;
ALTER TABLE
pi=# SELECT * FROM playground;
  equip_id | type  | color  | location  | install_date
 ----------+-------+--------+-----------+--------------
         2 | swing | yellow | northwest | 2019-04-27
(1 row)

# Updating Data in a Table 
pi=# SELECT * FROM playground;
  equip_id | type  | color  | location  | install_date
 ----------+-------+--------+-----------+--------------
         2 | swing | yellow | northwest | 2019-04-27
(1 row)

pi=# UPDATE playground SET color = 'red' WHERE type = 'swing';
UPDATE 1
pi=# SELECT * FROM playground;
  equip_id | type  | color | location  | install_date
 ----------+-------+-------+-----------+--------------
         2 | swing | red   | northwest | 2019-04-27
(1 row)
```
