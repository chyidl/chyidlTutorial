High Performance MySQL Third
============================

Chapter 1. MySQL Architecture and History
-----------------------------------------

* MySQL's Logical Architecture 
    - The topmost layer: connection handling, authentication, security 
```
Each client connection gets threads within the server process. The server caches threads, so they don't need to be created and destroyed for each new connection.

Authentication is based on username, host, password, port. Once a client has connected, the server verifies whether the client has privileges for each query.
```
    - The second layer: query parsing, analysis, optimization, caching, built-in function(e.g., dates, times, math, and encryption). Any functionality privided across storage engines lives at this level: stored procedures, triggers, and views
```
MySQL parses queries to create an internal structure (the parse tree), and then applies a variety of optimizations. These can include rewriting the query,determining the order in which it will read tables, choosing which index to use, and so on.

Concurrency Control :
    MySQL has to do this at two levels: the server level and the storage engine level.
    How MySQL deals with concurrent readers and writers

    Read/Write Locks: These locks are usually known as shared locks and exclusive locks, or read locks and write locks.
```
    - The third layer: storage engines. They are responsible for storing and retrieving all data stored in MySQL.


