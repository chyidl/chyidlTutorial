#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# mysql-connector-python
import mysql.connector
# Using this module create, manage and use the connection pool
import mysql.connector.pooling


class MySQLDB:
    """the basic DB class
    cfg = {
        'user':     config.mysql_user,
        'password': config.mysql_passwd,
        'host':     config.mysql_host,
        'port':     config.mysql_port,               # TCP/IP port of the MySQL server. default Value 3306
        'charset':  config.mysql_charset,            # default value of the charset argument is "utf8"
        'connection_timeout': config.mysql_connection_timeout,
        'pool_name': config.mysql_poolname,
        'pool_size': config.mysql_poolsize,
        'pool_reset_session':config.mysql_pollresetsession,
        'use_pure': config.mysql_usepure,            # use_pure is False means it the pure Python implementation
    }
    """
    def __init__(self, config, pool=True):
        try:
            self._pool = pool
            if self._pool:
                # mysql.connector.connect() method of MySQL Connector Python with required parameters to connect MySQL.
                #self._conn = mysql.connector.connect(**config)  # return MySQLConnection
                # Create a connection pool.
                self._conn_pool = mysql.connector.pooling.MySQLConnectionPool(**config)
                self._conn = self._conn_pool.get_connection() # Get connection object from a pool
                print("Printing connection pool properties")
                print(f'Connection Pool Name - {self._conn_pool.pool_name}')
                print(f'Connection Pool Size - {self._conn_pool.pool_size}')
            else:
                self._conn = mysql.connector.connect(**config)
            if self._conn.is_connected():  # verify is our python application is connected to MySQL
                # need to buffered=True to avoid MySQL Unread result error
                # need to prepared=True to allows the cursor to execute the prepared statement
                self._cursor = self._conn.cursor(buffered=False, prepared=False)  # Using MySQLCursor can execute SQL queries
        except mysql.connector.Error as err:
            print("Error while connecting to MySQL", err)

    # Using the magic methods (__enter__, __exit__) allows you to implement
    # object which can be used easily with the with statement
    def __enter__(self):
        # When the "with" statement is executed, then call the __enter__
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # make sure the dbconnection gets closed
        self.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    @property
    def connection_pool(self):
        return self._conn_pool

    def close(self):
        try:
            if self._conn.is_connected():
                self.cursor.close()  # can not execute any SQL statement
                self.connection.close()  #
                print("MySQL connection is closed")
        except mysql.connector.Error as error:
            print(f"Failed to close database connection {error}")

    def commit(self):
        # make changes persistent in the database
        self.connection.commit()

    def rollback(self):
        # rollback or reverse the changes if any database error occurred
        self.connection.rollback()

    def query(self, sql, params=None):
        try:
            self.cursor.execute(sql, params or ())
        except mysql.connector.errors.InterfaceError as error:
            # When the connection is not available
            print(f"mysql.connector.InterfaceError {error}, and reconnect...")
            self.connection.reconnect(attempts=3, delay=5)
            self.cursor.execute(sql, params or ())
        except mysql.connector.Error as error:
            self.rollback() # rollback if any exception occured
            print(f'query Exception: {error} {sql} {params}')

    def querymany(self, sql, seq_of_params=None):
        try:
            # use cursor's executemany() function to insert multiple records into a table
            self.cursor.executemany(sql, seq_of_params or [()])

        except mysql.connector.Error as error:
            self.rollback()
            print(f'querymany Exception: {error}')

    def callproc(self, proc_name, args=None):
        try:
            # cursor.callproc method calls the stored procedure mentioned in the proc_name argument
            self.cursor.callproc(proc_name, args or ())
        except mysql.connector.Error as error:
            self.rollback()
            print(f'callproc Exception : {error}, proc_name={proc_name}, agrs={args}')

    def fetchall(self):
        # Get resultSet from the cursor object
        return self.cursor.fetchall()

    def fetchmany(self, size=1):
        # fetchmany() method of cursor class to fetch fewer rows
        return self.cursor.fetchmany(size)

    def fetchone(self):
        return self.cursor.fetchone()

    def rowcount(self):
        # find number of
        return self.cursor.rowcount

    def version(self):
        try:
            db_info = self._conn.get_server_info()
            return db_info
        except mysql.connector.Error as error:
            print(f"Failed to read database version {error}")
            return error


if __name__ == '__main__':
    import time
    cfg = {
        'user': 'chyidl',
        'password': 'macintosh',
        'host': '192.168.82.56',
        'port': 3306,  # TCP/IP port of the MySQL server. default Value 3306
        'charset': 'utf8mb4',  # default value of the charset argument is "utf8"
        'connection_timeout': 10,
        'pool_name': 'dbcom',
        'pool_size': 5,
        'pool_reset_session': True,
        'use_pure': True,  # use_pure is False means it the pure Python implementation
    }

    with MySQLDB(cfg, pool=True) as db:
        count = 10
        while count > 0:
            count -= 1
            # db stuff
            sql = 'SELECT VERSION()'
            db.query(sql)
            print(f'MySQL Version: {db.fetchone()[0]}')
            time.sleep(5)