#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pymssql


class MsSQLDB:
    """the basic DB class; config is dict"""
    def __init__(self, config):
        self._conn = pymssql.connect(**config)
        self._cursor = self._conn.cursor()

    # Using the magic methods (__enter__, __exit__) allows you to implement
    # object which can be used easily with the with statement
    def __enter__(self):
        # When the "with" statement is executed, then call the __enter__
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # make sure the dbconnection gets closed
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def rows(self):
        return self.cursor.rowcount