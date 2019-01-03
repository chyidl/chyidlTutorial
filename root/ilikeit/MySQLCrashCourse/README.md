# MySQL 

The offical way to pronounce "MySQL" is "My Ess Que Ell" is an open source relational database management system (RDBMS).

## MySQL Infrastructure

Client --> Connector --> Query Cache --> Analyzer --> Optimizer --> Executor --> Storage Engine.

**Connector**
    * $ mysql -h$host -P$port -u$user -p 
    * After the user successfully establishes the connection, the modification of the user rights will not affect the existing connection, and only the newly established connection will use the new permission setting.
    * mysql> SHOW PROCESSLIST; show which threads are running 
    * mysql> SHOW VARIABLES LIKE '%max_connections%'; 
    * mysql> SET GLOBAL max_connections = 5000; to change max_connections 
    * 数据库中，长连接是指连接成功后，如果客户端持续有请求，则一直使用同一个连接，短连接则是指每次执行完很少的几次查询就断开连接，下次查询再重新建立连接

