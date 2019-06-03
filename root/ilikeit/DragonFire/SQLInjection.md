SQL injection 
=============

> SQL injection is a code injection technique, used to attack data-driven applications, in which malicious SQL statements are inserted into an entry field for execution. 

SQL: Structured Query Language 结构化查询语句
IPS: Intrusion Prevention System 入侵防护系统
URL: Uniform Resource Locator 统一资源定位符

* SQL注入攻击简介
```
结构化查询语句SQL是和关系数据库进行交互的文本语言.允许用户对数据进行有效的管理，包括对数据的查询、操作、定义和控制等几个方面.
关系数据库广泛用于网站中，用户一般通过动态网页和数据库间接进行交互,常见的动态网页一般都通过http://domain-name/page.html?agr=value等带有参数的URL来访问,网页中有一个或多个参数，参数类型可能是整形或字符串型。
安全性开绿不周的网站应用程序使得攻击者能够构造并提交恶意URL，将特殊构造的SQL语句插入到提交的参数中，在和关系数据库进行交互时获得私密信息。或者直接篡改Web数据，这就是SQL注入攻击。

SQL注入攻击的主要方式是构造巧妙的SQL语句,

错误用法:
sql = "SELECT id, type, name FROM table_name WHERE id = %s and type = %s" % (id, type)
cur.execute(sql)
这种用法就是常见的拼接字符串导致SQL注入漏洞的产生, 并不是预编译语句被绕过，而是在构造带入的预编译语句的时候拼接了用户输入字符串，还未带入查询的预编译语句已经被注入，之后带入正确的参数.

正确用法:
execute() 函数本身就接受SQL语句参数位，
args = (id, type)
cur.execute('SELECT id, type, name from table_name where id = %s and type = %s', args)


```
