FAQ
===

* 1. How to Prevent Blocked Host Connection from Many Connection Errors in MySQL.
```
max_connect_errors:
    prevent user from connecting to the database if they make too many connection errors for security reason.

mysql> SHOW VARIABLES LIKE 'max_connect_errors';
+--------------------+-------+
| Variable_name      | Value |
+--------------------+-------+
| max_connect_errors | 500   |
+--------------------+-------+
1 row in set (0.02 sec)

mysql> SHOW VARIABLES LIKE 'max_error_count';
+-----------------+-------+
| Variable_name   | Value |
+-----------------+-------+
| max_error_count | 64    |
+-----------------+-------+
1 row in set (0.01 sec)
```

Important Notice
----------------
* % vs localhost
```
The % character does not include the localhost, as the localhost means a connection over a UNIX socket instead of a standard TCP/IP.
```