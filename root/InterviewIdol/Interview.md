面试总结
=======

Python Production Stack
-----------------------
```
Maximum Throughput
http://brianmcdonnell.github.io/pycon_ie_2013/#/15
Browser -> Nginx -> uWSGI -> [Django|Flask Python]

    Nginx: 
        Socket management 
        HTTP parsing 
        Rule matching 
    
    uWSGI:
        Socket management 
        Process management 
    
    (SYN)Django/Flask Frameworks:
        URL mapping
        Request wrapping
        Middleware 
    (ASYN)Tornado Twisted 

LOTS OF REQUESTS, SOCKETS, FILE HANDLES 
    Increase file handles
        $ sudo vim /etc/security/limits.conf 
            *   hard    nofile  131072
            *   soft    nofile  65536
        IN TERMINAL FOR CURRENT SESSION
            $ ulimit -Hn 131072
            $ ulimit -Sn 65536
    Increase listen backlogs
        $ sudo vim /etc/sysctl.conf 
            net.core.somaxconn = 8191
            net.ipv4.tcp_max_syn_backlog = 8191 
        IN TERMINAL FOR CURRENT SESSION 
            $ sudo sysctl -w net.core.somaxconn = 8191 
            $ sudo sysctl -w net.ipv4_max_syn_backlog = 8191 
        
$ weighttp -c 1 -n 1000 http://server.pycon.ie/hello 
Increase concurrent clients 
Monitor CPU saturation 
Monitor thoughput asymptoting 

Nginx Config:
    worker_processes 1;
    events {
        worker_connections 8191;
    }
    server {
        listen 80 backlog=8191;
        server_name server.pycon.ie;

        location /hello {
            return 200 'Hello from nginx';
        }
    }

Django 是同步框架 -- 单线程  runserver 
uWSGI 中间服务器 -- 开启多个django 进程处理request, 同时提供类似负载均衡
    [uwsgi]  # 指明该文件为uwsgi的配置文件

    # 对外提供 http 服务的端口
    http = :8010
    #用于和 nginx 进行数据交互的端口
    socket = 127.0.0.1:8899
    # django 程序的主目录。
    pythonpath = /usr/src/app
    # Django's wsgi file
    wsgi-file = panel/wsgi.py
    # 最大的工作进程数
    processes = 4
    # 在每个进程中的最大线程数
    threads = 2
    # 通过该端口可以监控 uwsgi 的负载情况
    stats = 127.0.0.1:9999
    # 清理环境出口
    vacuum = true
```

Python 面试题
------------
https://zhuanlan.zhihu.com/p/54430650
```
1. 一行代码实现1-100之和
    sum(range(1,101))

2. 如何在一个函数内部修改全局变量
    利用global在函数内部声明全局变量

3. 列出5个Python标准库
    os: 提供与操作系统相关联的函数 os.name 
    sys: 提供命令行参数 sys.platform
    re: regular expression operations re.match(r'\d+', '12345')
    math: 数学运算 math.ceil(11.1) the smallest integer greater than or equal to x
    datetime: 

4. 字典如何删除del 合并 update两个字典

5. 谈一下Python GIL
    GIL python全局解释器锁，多线程中线程运行仍然有先后顺序，并不是同时进行
    多进程：每个进程都被系统分配资源，相当于每个进程有一个Python解释器，所以多进程可以实现同时运行，进程开销比较大

6. Python实现列表去重复
    集合转列表

7. def fun(*args, **kwargs) 中*args， **kwargs什么意思?
    不定数量的参数传递
    *args: 非键值对的可变数量的参数列表
    **kwargs: 键值对的可变数量的参数列表
        for k, v in kwargs.items() 

8. python2 和 python3 的range()区别
    python2 返回列表
    python3 返回迭代器 -- 节省内存

9. 装饰器原理?
    函数可以作为参数传递的语言，都可以使用装饰器

10. Python 内建的数据类型有哪些?
    int -- 整型
    bool 
    string
    list 
    set
    dict
    tuple 

11. 面向对象中 __new__ 和 __init__区别?
    __init__龙之初始化新的实例 创建对象后立刻被默认调用，可接受参数,不需要返回值 
    __new__ 控制创建新的实例 至少有一个参数cls, 代表当前类,必须有返回值
    Use __new__ when you need to control the creation of a new instance 
    Use __init__ when you need to control initialization of a new instance 
    __new__ is the first step of instance creation. It's called first, and is responsible for returning a new instance of your class. in constrast, __init__ doesn't return anything; it's only responsible for initializing the instance after it's been created.

    In general, you shouldn't need to override __new__ unless you're subclassing an inmutable type like str, in, unicode 

12. with方法
    'with' expression == try..finally blocks 
    with expression [as variable]:
        with-block 

    __enter__(): is called before with-block is executed and therefore can run set-up code. 
    __exit__(): after execution of the with-block is finished, the object __exit__() method is called.

    the context manager must have __enter__() and __exit__() method.
        __enter__() method is called. The value returned is assigned to var 
        __exit__(type, value, traceback)
    
    database support transaction:
        commit, roll back 
    
    db_connection = DatabaseConnection()
    with db_connection as cursor:
        cursor.execute('insert into ...')
        cursor.execute('delete from ...')
        # ... do more operation 


    class DatabaseConnection:
        # Database interface 
        def cursor(self):
            return a cursor object and starts a new transaction 
        
        def commit(self):
            "Commits current transaction"
        
        def rollback(self):
            "Rolls back current transaction"

        def __enter__(self):
            # Code to start a new transaction 
            cursor = self.cursor()
            return cursor 
        
        def __exit__(self, type, value, traceback):
            if traceback is None:
                # No exception, so commit 
                self.commit() 
            else:
                # exception occurred, so rollback 
                self.rollback() 
                # return False 
    
    from contextlib import contextmanager 

    @contextmanager 
    def db_transaction(connection):
        cursor = connection.cursor()
        try:
            # executed the __enter__() method 
            yield cursor 
        exception:
            connection.rollback()
            raise 
        else:
            connection.commit() 
    
    db = DatabaseConnection() 
    with db_transaction(db) as cursor:

13. map() 
    list(filter(lambda x: x>10 ,list(map(lambda x: x*x, list1)))) 


14. 生成随机整数，随机小数，0-1之间的小数
    random.randint(start, end): 生成区间内整数
    impoer numpy as np np.randn(5) 生成5个随机小数
    random.random() 随机小数 

15. r''表示原始字符串， 不转义特殊字符 

16. import re
    str = '<div class="name">中国</div>'
    res = re.findall(r'<div class=".*">(.*?)</div>', str)
    print(res)
 
 17. assert 断言方法
    assert() 

18. SQL 消除重复行
     select distinct name from student 

19. 10个Linux常用命令 
    ls, pwd, cd, touch, rm, rmdir, mkdir, tree, cp, mv, cat, more, grep,echo 

20. python2 和 python3的区别
    1. print 
    2. python2 使用ascii编码 python3 使用utf8 
    3. python2 range(1,10)返回列表 python3 返回迭代器 
    4. python2中unicode表示字符串序列，str表示字节序列 
        python3中str表示字符串序列，byte表示字节序列 
    5. python2中raw_input函数 python3中是input()函数 

21. 
    可变数据类型: list, dict 
    不可变数据类型: 数值类型、字符串类型、元组tuple id()

22. 
    s = "ajldjlajfdljfddd"
    s = set(s)
    s = list(s)
    s.sort(reverse=False)
    "".join(s)

23. sum = lambda x,y: x*y 
    print(sum(5, 4))

24. dic = {'name': "zhanghuihui", "age": 28, "city": "Hangzhou", "tel": "xxx"}
    sorted(dic.items, key=lambda x: x[0], reverse=False)

25. 利用collections Counter方法统计字符串每个单词出现的次数 
    from collections import Counter 

26. 
    re.compile将正则表达式编译成一个对象，加快速度，并重复利用 

27. str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + " 星期 " + str(datetime.datetime.now().isoweekday())

28. 数据库优化查询的方法
    外键、索引、联合索引、选择特定字段 
    CREATE TABLE `t_user` (
  `User_Id` bigint(20) NOT NULL COMMENT '用户 编号',
  `Lgn_Nm` varchar(20) DEFAULT NULL COMMENT '登录名',
  `Lgn_Pwd` varchar(50) DEFAULT NULL COMMENT '登录 密码',
  `Draw_Pwd` varchar(50) DEFAULT NULL,
  `P_Nm` varchar(100) DEFAULT NULL COMMENT '昵 称',
  `Simple_P_Nm` varchar(100) DEFAULT NULL,
  `Real_Nm` varchar(20) DEFAULT NULL COMMENT '真实 姓名',
  `Sex` tinyint(4) DEFAULT NULL COMMENT '1男0女',
  `Pho` varchar(20) DEFAULT NULL COMMENT '手机号',
  `IdCrd` varchar(20) DEFAULT NULL COMMENT '证件号码',
  `Id_Typ` varchar(20) DEFAULT NULL COMMENT '证件 类型',
  `Mail` varchar(100) DEFAULT NULL COMMENT '邮箱',
  `Pic` varchar(100) DEFAULT NULL COMMENT '头像',
  `Org_Pic` varchar(100) DEFAULT NULL,
  `Third_Lgn_Tkn` varchar(100) DEFAULT NULL COMMENT '第三方登录token',
  `Reg_Tm` datetime DEFAULT NULL COMMENT '注册 时间',
  `Ref_Id` bigint(20) DEFAULT NULL COMMENT '推荐人 编号',
  `User_Stat` smallint(6) DEFAULT NULL COMMENT '用户 状态',
  `Lst_Upd_Tm` datetime DEFAULT NULL COMMENT '最后修改时间',
  `Last_Use_Tm` datetime DEFAULT NULL,
  `Draw_Cnt` smallint(6) DEFAULT NULL,
  `Max_Draw_Cnt` smallint(6) DEFAULT NULL,
  `Track_Id` varchar(50) DEFAULT NULL,
  `Ref_Track_Id` bigint(20) DEFAULT NULL,
  `If_Lock_Draw` tinyint(1) DEFAULT NULL,
  `Lock_Instruction` varchar(100) DEFAULT NULL,
  `P_Nm_Encrypt` tinyint(1) DEFAULT NULL,
  `Device_Code` varchar(200) DEFAULT NULL,
  `Subscribe_Count` smallint(6) DEFAULT NULL,
  `Daily_Max_Track_Bonuses_Cnt` smallint(6) DEFAULT NULL,
  `If_Fsd_Reg` tinyint(1) DEFAULT NULL,
  `Game_Id` smallint(6) DEFAULT NULL,
  `Invite_Device_No_Alike_Total` smallint(6) DEFAULT NULL,
  `Adsense_Id` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`User_Id`),
  UNIQUE KEY `user_lg_nm` (`Lgn_Nm`),
  KEY `index_simple_p_nm` (`Simple_P_Nm`),
  KEY `index_device_code` (`Device_Code`(191)),
  KEY `index_user_id` (`User_Id`) USING BTREE,
  KEY `index_pho` (`Pho`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户'
```

Java --- 生态
-------------
```
Java 继承关系单一非多承 
Java -> 字节码 -> 
```