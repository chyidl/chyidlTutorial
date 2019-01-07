#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: dob
__version__ = '0.0.1'

"""
MySQL Driver BenchMarks 

Python MySQL Tutorial Using MySQL Connector Python 

    Python: is dynamic and enterprise language and it has all the support to build large and complex enterprise applications
    MySQL: is the world's most powerful and used open source database provided by Oracle.

    'OSError: mysql_config not found'

    for mysql-server: sudo apt-get install libmysqlclient-dev 
    for mariadb     : sudo apt-get install libmariadbclient-dev 

    There are total 5 modules available in python to communicate with a MySQL and provides MySQL database support to our application.

    1. python3 -m pip install mysql-connector-python (mysql-connector-python-8.0.13) 
        official Oracle-supported driver to work with MySQL and python. 
        is Written in Pure Python
        A little slow
        It is Python 3 compatible 
        Not compatible with MySQLdb  

        Verifying MySQL Connector/Python installation 
        > import mysql.connector 

    2. python3 -m pip install pymysql (pymysql-0.9.3)
        Pure Python
        Faster than mysql-connector 
        Almost completely compatible with MySQLdb, after calling pymysql.install_as_MySQLdb() 

    3. python3 -m pip install cymysql (cymysql-0.9.12)
        fork of pymysql with optional C speedups 

    4. python3 -m pip install mysqlclient (mysqlclient-1.3.14)
        Django's recommended library 
        Friendly fork of the original MySQLdb, hopes to merge back some day 
        The fastest implemenation, as it is C based
        The most compatible with MySQLdb, as it is a fork 

    Note: Above all interfaces or modules are adhere the Python Database API Specification v2.0 that means the syntax,
    method and the way of access database is same in all. 

    CRUD: Create(data insertion),Read(data retrieval),Update(date update),Delete(data delete)

"""

"""
MsSQL

"""