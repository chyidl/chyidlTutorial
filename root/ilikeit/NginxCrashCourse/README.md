Nginx Crash Course 
==================

* Nginx 
    - 高并发、高性能
    - 扩展性好 : 模块化
    - 高可靠性 ：
    - 热部署 ：不停止服务的情况下升级服务
    - BSD许可证 
* Apache 
* Tomcat 

初始Nginx
---------
```
Nginx三个主要应用场景:
    1. 静态资源服务：
        通过本地文件系统提供服务
    2. 反向代理服务：
        Nginx的强大性能
        缓存
        负载均衡
        HTTP request --> Nginx --> Application(Tomcat, Flask) <---> MySQL/Redis 
        Applicatoon service QPS，TPS并发比较低，所以需要将多个App 组成集群提高并发性能，App 集群需要Nginx的反向代理功能，可以将动态请求转发给应用服务，集群需要两种需求：动态扩容、冗灾性，这里需要Nginx的负载均衡功能。Nginx提供静态内容的缓存功能，
    3. API服务
        OpenResty 
        Nginx 直接操作数据库，Redis，利用Nginx强大的并发性能

Nginx出现的历史背景:
    1. 互联网的数据量的快速增长
    2. 摩尔定律，性能提升
    3. 低效Apache 
 
Nginx 组成:
    Nginx 二进制可执行文件：由各个模块源码编译出的一个文件
    Nginx.conf配置文件: 控制Nginx的行为
    access.log访问日志: 记录每一条Http请求信息
    error.log错误日志: 定位问题

Nginx版本发布情况mainline:
    2004年10月4号第一个版本0.1.0
    2005年重构http反向代理
    2009年0.7.5windows系统支持
    2011年: 1.0版本发布，支持上游keep alive http长链接 Nginx plus商业公司成立
    2013年：支持websocket, TFO协议
    2015年: 支持thread pool 提供stream四层反向代理支持reuse port特性 支持httpv2协议
    2016年: 支持动态模块
    2018年: 支持TLSv1.3 

开源版Nginx         http://nginx.org 
商业版Nginx Plus    http://nginx.com 
阿里巴巴Tengine: 是由淘宝网发起的Web服务器项目，他在Nginx的基础上，针对大访问量网站的需求，添加很多高级功能和特征，Tengine的性能和稳定性已经在大型网站淘宝网、天猫商城得到很好的检验，他的最终目标是打造一个高效、稳定、安全、易用的Web平台。从2011年12月开始，Tengine成为一个开源项目，Tengine团队在积极开发和维护。
开源版OpenResty     http://openresty.org  (Lua语言)
    开源Web平台主要由章亦春agentzh因为大部分Nginx模块都是由本软件包的维护者开发，所以可以确保所有这些模块及其他组件可以很好的一起工作.打包的各种软件组件版权属于各自版权所有.
商业版OpenResty     http://openresty.com 

# 编译Nginx
1. 下载(http://nginx.org/en/download.html)
    Mainline version 
    Stable version -- http://nginx.org/download/nginx-1.16.1.tar.gz 
    Legacy version 
    $ wget http://nginx.org/download/nginx-1.16.1.tar.gz 
    $ extract nginx-1.16.1.tar.gz 
    $ cd nginx-1.16.1 
    $ tree -L 1 .
        auto    -- 
        conf    -- 
        configure 
        contrib -- 
        html -- 
        man -- 
        src -- 源代码
        objs -- ./configure 中间生成文件
            ngx_modules.c -- 指定编译时那些模块
2. 编译 
    $ ./configure --help 
    $ ./configure --prefix=/usr/local/openresty --with-http_ssl_module --add-module=../tengine-2.3.2/modules/ngx_slab_stat/
    $ make -j4 
    $ sudo make install 
    $ nginx   # 启动nginx 
    # If you get following error, when you try to start nginx... 
    nginx: [emerg] bind() to 0.0.0.0:80 failed (98: Address already in use)
    nginx: [emerg] bind() to [::]:80 failed (98: Address already in use)
    # Then it means nginx or some other process is already using port 80. 
    # you can kill it using:
    $ sudo fuser -k 80/tcp 
3. Nginx配置语法
    配置文件由指令与指令快构成
    每条指令以;分号结尾，指令与参数间以空格符号分隔
    指令快以{}大括号将多条指令组织在一起
    include语句允许组合多个配置文件以提升可维护性
    使用#符号添加注释、提高可读性
    使用$符号使用变量
    部分指令的参数支持正则表达式
配置参数: 时间单位
    ms : milliseconds 
    s : seconds 
    m : minutes
    h : hours
    d : days
    w : weeks 
    M : months, 30 days 
    y : years, 365 days 
配置参数: 空间单位
        : bytes
    k/K : kilobytes 
    m/M : megabytes 
    g/G : gigabytes 
Http配置的指令快
    http 
    server  -- 域名
    upstream  -- 上游服务
    location -- URL表达式

Nginx命令行
$ nginx -s reload 
    -? -h 帮助
    -c 指定配置文件
    -g 指定配置指令
    -p 指定运行目录
    -s 发送信号 
        stop  立刻停止服务
        quit 优雅停止服务
        reload 重载配置文件
        reopen 重新开始记录日志文件
    -t -T  测试配置文件是否有语法错误
    -v -V 打印nginx的配置信息、编译信息

# -- Nginx 热部署 
# 查看nginx运行状态
$ ps -ef | grep nginx 
root     13635  0.0  0.2   4600  2192 ?        Ss   22:54   0:00 nginx: master process ./sbin/nginx                              
nobody   13675  0.0  0.2   5324  2728 ?        S    22:56   0:00 nginx: worker process
pi       13697  0.0  0.0   4376   676 pts/0    S+   22:57   0:00 grep --color=auto --exclude-dir=.bzr --exclude-dir=CVS --exclud$-dir=.git --exclude-dir=.hg --exclude-dir=.svn nginx   
# Nginx 热更新，仅仅是替换nginx二进制文件
$ kill -USR2 13635  # nginx master进程
$ ps -aux | grep nginx
root     13635  0.0  0.2   4600  2192 ?        Ss   22:54   0:00 nginx: master process ./sbin/nginx
nobody   13675  0.0  0.2   5324  2728 ?        S    22:56   0:00 nginx: worker process
root     13784  0.0  0.2   4464  2716 ?        S    23:01   0:00 nginx: master process ./sbin/nginx   -- 新启动的Master
nobody   13785  0.0  0.2   5212  2612 ?        S    23:01   0:00 nginx: worker process
pi       13787  0.0  0.0   4376   676 pts/0    S+   23:01   0:00 grep --color=auto --exclude-dir=.bzr --exclude-dir=CVS --exclude-dir=.git --exclude-dir=.hg --exclude-dir=.svn nginx
$ kill -WINCH 13635 # 关闭old nginx  worker进程
$ ps -aux | grep nginx 
root     13635  0.0  0.2   4600  2192 ?        Ss   22:54   0:00 nginx: master process ./sbin/nginx  # nginx old master 进程不会主动退出，保留以防用户做版本回退
root     13784  0.0  0.2   4464  2716 ?        S    23:01   0:00 nginx: master process ./sbin/nginx
nobody   13785  0.0  0.2   5212  2612 ?        S    23:01   0:00 nginx: worker process
pi       13866  0.0  0.0   4376   724 pts/0    S+   23:05   0:00 grep --color=auto --exclude-dir=.bzr --exclude-dir=CVS --exclude-dir=.git --exclude-dir=.hg --exclude-dir=.svn nginx

# -- Nginx 切割日志文件
$ mv logs/access.log /logs/access.log.bak 
╭─    ~/chyidl.com/nginx/logs ─────────────────────────────────────────────────────────────────────────────── ✔  pi@RPi3B 
╰─ ll
total 16K
-rw-r--r-- 1 pi   pi   434 Aug 30 22:55 access.log.bak
-rw-r--r-- 1 pi   pi   828 Aug 30 23:01 error.log
-rw-r--r-- 1 root root   6 Aug 30 23:01 nginx.pid
-rw-r--r-- 1 root root   6 Aug 30 22:54 nginx.pid.oldbin
╭─    ~/chyidl.com/nginx/logs ───────────────────────────────────────────────────────────────────────────── 1 ↵  pi@RPi3B 
╰─ sudo ../sbin/nginx -s reopen
[sudo] password for pi: 
╭─    ~/chyidl.com/nginx/logs ─────────────────────────────────────────────────────────────────────────────── ✔  pi@RPi3B 
╰─ ll
total 16K
-rw-r--r-- 1 nobody root    0 Aug 30 23:40 access.log
-rw-r--r-- 1 pi     pi    434 Aug 30 22:55 access.log.bak
-rw-r--r-- 1 nobody pi   1.1K Aug 30 23:40 error.log
-rw-r--r-- 1 root   root    6 Aug 30 23:01 nginx.pid
-rw-r--r-- 1 root   root    6 Aug 30 22:54 nginx.pid.oldbin
日常每周、每天、每月做日志切割
$ crontab -l   # 添加到定时任务中
0 0 1 * * root /home/pi/chyidl.com/nginx/logs/rotate.sh 
$ vim rotate.sh 
#!/binbash                                                                                                                 
#Rotate the Nginx logs to prevent a single logfile from consuming too much disk space.
LOGS_PATH=/home/pi/chyidl.com/nginx/logs/history
CUR_LOGS_PATH=/home/pi/chyidl.com/nginx/logs
YESTERDAY=$(date -d "yesterday" + %Y-%m%d)
mv ${CUR_LOGS_PATH}/access.log ${LOGS_PATH}/access_$(YESTERDAY).log
mv ${CUR_LOGS_PATH}/error.log ${LOGS_PATH}/error_$(YESTERDAY).log
# 向Nginx主进程发送USR1信号, USR1信号是重新打开日志文件
kill -USR1 ${cat /home/pi/chyidl.com/nginx/logs/nginx.pid}

# Nginx 搭建静态资源Web服务器
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    gzip on;
    gzip_min_length 10;
    gzip_comp_level 2;
    gzip_types text/plain application/x-javascript text/css application/xml text/javascript applicatio/x-httpd-php image/jpeg image/gif image/png; 

    alias chyidlTutorial/;
    autoindex on; # Enables or disables the directory listing output.
    set $limit_rate 10k; -- limits the rate of response transmission to a client. 

# Nginx 搭建具备缓存功能的反向代理服务
    反向代理 + 多个上游服务

    upstream local {
        server 127.0.0.1:8080; 
        ...
    }
    
    proxy_cache_path /tmp/nginxcache levels=1:2 keys_zone=my_cache:10m max_size=1g 
        inactive=60m use_temp_path=off;

    location / {
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr; 
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

        proxy_cache my_cache;
        proxy_cache_key $host$uri$is_args$args;
        proxy_cache_valid 200 304 302 1d;

        proxy_pass http://local;
    }

# GoAccess 实施分析Access log文件
https://goaccess.io 
GoAccess is an open source real time Web log analyzer and interactive viewer that runs in a terminal in linux systems or through your browser.
$ sudo apt-get install goaccess 
Websocket: 协议
    
    location /report.html {
        alias /home/chyi/chyidl.com/ReverseProxy/nginx/html/report.html;
    }

$ sudo goaccess logs/access.log -o  html/report.html --real-time-html  --time-format='%H:%M:%S' --date-format='%d/%b/%Y' --log-format=COMBINED 
WebSocket server ready to accept new client connections


# TLS/SSL 安全协议 
SSL: Secure Sockets Layer
TLS: Transport Layer Security 
1995 SSL3.0 -> 1999 TLS1.0 -> 2006 TLS1.1 -> 2008 TLS1.2 -> 2018 TLS1.3 
ISO/OSI七层模型: 物理层-> 数据链路层 -> 网络层 -> 传输层 -> 会话层 -> 表示层 -> 应用层 
四层模型: 链路层 -> 网络层 -> 传输层 -> 应用层 
HTTP协议所属于应用层
SSL/TLS 所属于表示层
    握手
    交换密钥
    告警
    对称加密应用数据
SSL/TLS安全密码套件: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 
    ECDHE: 密钥交换 -- 密钥交换算法
    RSA:身份验证 -- 身份验证算法
    AES_128_GCM: 密码, AES算法、128强度、GCM模式 -- 对称加密算法、强度、分组模式
    SHA256: MAC 或 PRF -- 签名hash算法

# 对称加密算法和非对称加密算法
对称加密:
    RC4序列算法: 密钥序列1010、明文0110、密钥 异或 明文 = 密文1100
    异或运算有对称特性
非对称加密算法:
    公钥加密后的明文转变为密文，密文只能使用私钥才能解密
    私钥加密后的明文转变为密文，密文只能使用公钥才能解密

# PKI公钥基础设施
    CA机构负责颁发证书
    证书类型:
        域名验证 domain validated DV证书 
        组织验证 organization validated OV证书 
        扩展验证 extended validation EV证书 
    证书链:
        根证书-二级证书-子证书

# TLS/SSL 通讯过程
    验证身份   
    打成安全套件共识
    传递密钥
    加密通讯
    1. Client Hello         --->   
                    - Support Ciphers 
                    - Random number 
                    - Seconds ID(if any) 
                            <---      2. Server Hello 
                    - choose ciphers 
                    - random number 
                    - Session ID 
                    - (Re-use, or new) 
                            <---      3. Server Certification 
    Check Certificate validity
                            <---      4. Server Hello Done 
    5. Create Key           --->      
Exchange Message    - Encrypted       6. Key generation 
                    premanter secret
    6. Key generation
    CipherSpec Exchange     --->    
    7. Finished
                            <---      7. CipherSpec Exchange 
                                        Finished.

# Encrypt with Nginx Server
Certificate Authority(CA) that provides an easy way to obtain and install free TLS/SSL certificates, thereby enabliing encrypted 
    Installing Certbot 
    $ sudo add-apt-repository ppa:certbot/certbot   # First, add the repository 
    $ sudo apt-get update  # Then, update the package list to pick up the new repository package information 
    $ sudo apt-get install python-certbot-nginx  # Finally, install Cerbot's Nginx package with apt-get.
    Config HTTPS 
    $ certbot --nginx --nginx-server-root=/home/chyi/chyidl.com/ReverseProxy/nginx/conf/ -d chyidl.com

# OpenResty & Lua Language
OpenResty is a dynamic web platform based on NGINX and LuaJIT.
    # Download Source Code 
    $ wget https://openresty.org/download/openresty-1.15.8.1.tar.gz 
    $ tar -xvf openresty-1.15.8.1.tar.gz 
    $ cd openresty-1.15.8.1 
    $ tree -L 1
    .
    ├── bundle   -- Nginx 源代码存储位置
    ├── configure
    ├── COPYRIGHT
    ├── patches
    ├── README.markdown
    ├── README-windows.txt
    └── util
    3 directories, 4 files
    $ ./configure --prefix=/home/chyi/chyidl.com/openresty 
    $ make -j2
    $ make install 
    
    location /lua {
        default_type text/html;
        content_by_lua 'ngx.say("User-Agent: ", ngx.req.get_headers()["User-Agent"])';
    }
    
``` 
![PKI 公钥基础设施](/imgs/raspberry/NginxCrashCourse/pki.png?raw=true)

Nginx架构基础
--------
```
Master - Worker 架构模型，Worker数量与CPU核心数相匹配、多个Worker之间共享数据
#Nginx请求处理流程 
    Nginx 内部有三大状态机:
        传输层状态机    -- 传输层
        HTTP状态机      -- 应用层
        Mail状态机      -- 
    Nginx核心属于：非阻塞的事件驱动处理引擎(epoll)，通常使用异步需要使用状态机识别和处理.使用线程池处理磁盘阻塞调用。大多数Nginx作为负载均衡和反向代理使用
    Nginx可以通过协议将请求传输给HTTP,Mail,Stream(TCP)代理，或者利用应用层相关协议FastCGI, uWSGI, SCGI,代理应用服务器
    Web/Email/TCP流量 --> 

# Nginx进程结构
    1. 单进程结构 -- 适合开发调试使用
    2. 多进程结构 --  Nginx要提高高可用性，由于线程使用共享内存，所以个别线程错误会引发连锁反应导致Nginx不可用.
        Master Process -- 父进程 : 主要用作Worker进程的监控管理
        Worker Process -- 子进程 : 处理请求，需要和CPU核心数一致并且绑定，可以提高使用CPU缓存的命中率
        Cache Manager  -- 子进程 : 缓存的管理
        Cache loader   -- 子进程 ：缓存的加载
        Worker, Cache manager, Cache loader之间的进程间通信通过使用共享内存。

$ ps -ef | grep nginx  # 查看当前进程ID，父进程ID
pi       10280     1  0 Sep02 ?        00:00:00 nginx: master process ./sbin/nginx
pi       11958 10280  0 11:22 ?        00:00:00 nginx: worker process
pi       11959 10280  0 11:22 ?        00:00:00 nginx: worker process
$ sudo ./sbin/nginx -s reload  # 退出旧Worker进程,重新创建Worker进程
$ ps -ef | grep nginx
pi       10280     1  0 Sep02 ?        00:00:00 nginx: master process ./sbin/nginx
pi       11985 10280  0 11:26 ?        00:00:00 nginx: worker process
pi       11986 10280  0 11:26 ?        00:00:00 nginx: worker process
$ kill -SIGHUP 10280 
$ ps -ef | grep nginx
pi       10280     1  0 Sep02 ?        00:00:00 nginx: master process ./sbin/nginx
pi       11999 10280  0 11:29 ?        00:00:00 nginx: worker process
pi       12000 10280  0 11:29 ?        00:00:00 nginx: worker process
$ kill -SIGTERM 11999  # 退出Worker进程
$ ps -ef | grep nginx
pi       10280     1  0 Sep02 ?        00:00:00 nginx: master process ./sbin/nginx
pi       12000 10280  0 11:29 ?        00:00:00 nginx: worker process
pi       12011 10280  0 11:31 ?        00:00:00 nginx: worker process

Nginx许多命令本质上是向Nginx Master进程发送信号

# Nginx 进程管理: 信号
    Nginx多进程间通信使用共享内存、信号量，进程间管理通常使用信号
    Master进程:
        监控Worker进程
            CHLD: --当子进程终止会向父进程发送CHLD信号 
        管理Worker进程-接收信号
            TERM, INT -- 立刻停止Nginx进程 
            QUIT -- 优雅停止Nginx进程
            HUP -- 重新加载Nginx配置文件
            USR1 -- 重新打开日志文件，对日志文件进行切割
            USR2 -- kill -USR2 Nginx Master pid 
            WINCH -- kill -WINCH Nginx Master pid 
    Worker 进程-接收信号
            TERM, INT 
            QUIT 
            USR1
            WINCH 
    Nginx命令 
        reload: HUP  
        reopen: USR1
        stop: TERM 
        quit: QUIT 

# Nginx reload nginx.conf 原理
$ sudo ./sbin/nginx -s reload 
    1. 向Nginx Master进程发送HUP信号 (reload命令)
    2. Nginx Master 进程检验conf/nginx.conf配置语法是否正确
    3. Nginx master进程打开新的监听端口[子进程会继承所有父进程打开的端口和文件]
    4. Nginx Master 进程使用新配置文件启动新的Worker子进程
    5. Nginx Master 进程会向老的Worker子进程发送QUIT信号(优雅关闭)
    6. 老的Worker进程关闭监听句柄，处理完当前连接后结束进程

# Nginx 热升级原理
    1. 将旧的Nginx可执行文件替换成新的Nginx可执行文件(注意备份旧的Binary文件)
    2. 向旧的Nginx Master 进程发送USR2信号
    3. 旧的Nginx Master进程修改pid文件名，加上后缀.oldbin 
    4. 旧的Nginx Master进程使用新的Nginx binary文件启动新的Nginx Master进程 [目前新的Nginx Master 进程是就Nginx Master进程的子进程]
    5. 向旧的Nginx Master进程发送WINCH信号，关闭旧的Nginx Worker 进程 
    6. 回滚，向旧的Nginx Master 发送HUP，向新的Nginx Master发送QUIT.

# 关闭worker进程 
    QUIT Nginx Worker进程 HTTP 请求
        1. 设置定时器 Worker_Shutdown_Timeout 
        2. 关闭监听句柄 
        3. 关闭空闲的连接
        4. 再循环中等待全部连接关闭
        5. 退出进程

# Nginx事件
    Nginx属于事件(网络事件)驱动框架，每一个网络连接对应两个事件(读事件、写事件)

    应用层->传输层->网络层->链路层->[以太网]
                                        |--> 链路层->网络层
                                        |<-- 链路层 <--|
                                    [广域网]    
                                        |--> 链路层->网络层
                                        |<-- 链路层 <--|
    应用层<-传输层<-网络层<-链路层<-[以太网]

TCP Stream 报文: 
    TCP/IP 协议层级
        应用层:                                       DATA [HTTP, SMTP, POP3, IMAP, SSH, DNS]
        传输层:               Source Port/Dest Port + DATA [TCP, UDP]
        网络层:         Source IP/Dest IP + Source Port/Dest Port + DATA [IP, ICMP, DHCP, ARP]
    数据链路层:         Source Mac addr/Dest Mac addr + Source IP/Dest IP + Source Port/Dest Port + DATA + Footer(Ethernet) 

    HTTP协议拆分成小的报文，网络层报文MTU = 1500 byte，报文大小称为MSS

TCP协议与非阻塞接口:
    读事件:
        Accept 建立连接
        Read读消息
    写事件:
        Write写消息
        TCP协议         ：非阻塞接口
    请求建立TCP连接事件 : 读事件中Accep建立连接事件
    TCP连接可读事件     : 读事件中Read读消息
    TCP连接关闭事件     : 读事件中Read 
    TCP连接可写事件     : 写事件中Write
    异步读写磁盘事件    : 
    定时器事件          : 

    事件收集分发器: 事件属于生产者

# Wireshark 
    Capture using this filter: host 176.122.152.20 and port 443
    TCP三次握手 192.168.1.188   176.122.152.20.16clouds.com TCP 78  54927 → https(443) [SYN] Seq=0 Win=65535 Len=0 MSS=1460 WS=64 TSval=998541513 TSecr=0 SACK_PERM=1
        Transmission Control Protocol, Src Port: 54927 (54927), Dst Port: https (443), Seq: 0, Len: 0  [进程端口与进程端口通信]
        Internet Protocol Version 4, Src: 192.168.1.188 (192.168.1.188), Dst: 176.122.152.20.16clouds.com (176.122.152.20)
    TCP 三次握手:
        Src -> Dst  [SYN] 0x002
        Src <- Dst  [PSH, ACK] 0x018
        Src -> Dst  [ACK] 0x010
        Src <- Dst  [SYN, ACK] 0x012 

# Nginx 事件驱动模型
    Nginx事件循环 Nginx Event Loop 
        1. Wait For Event On Connections(epoll Wait) --> 2, 3 
        2. Linux Kernel 将事件存放在事件队列中 -- > 4 
        3. Get New Events 
        4. 事件存放队列 
        5. Process The Events 
    Nginx Events Queue Processing Cycle:
        
# epoll 原理
    Nginx如何快速从Linux Kernel中获取等待处理的事件
    epoll, Kqueue, Poll, Select : 网络事件收集分发器, epoll和Kqueue性能要远远好于poll, Select 
    epoll要求高并发连接中，每次处理活跃连接数量占比要很小
    epoll实现原理:
        红黑树: 
        链表: 
        
        eventpoll: 
            +lock
            +mtx
            +wq
            +poll_wait 
            +rdllist: 红黑树中每个结点都是基于epitem结构中的rdllink成员 
            +rbr: 红黑树中每个结点都是基于epitem结构中的rbn成员
            +ovflist 
            +user 
        
        epitem:
            +rbn 
            +rdllink 
            +next 
            +ffd 
            +nwait 
            +pwqlist 
            +ep 
            +fllink 
    epoll使用:
        创建 
        操作: 添加/修改/删除
        获取句柄
        关闭

# Nginx 请求切换
    Traditional Server: Apache, Tomcat : 线程仅处理一个连接，并且依赖OS进程调度实现并发
    Nginx Server: 线程同时处理多连接，用户态代码完成连接切换，尽量减少操作系统进程切换.
    操作系统分配的事件片的长度一般是5ms - 800ms,Nginx Worker将进程优先级配置-19,这样操作系统往往会分配比较大的时间片.
    
# 同步&异步 阻塞&非阻塞
    阻塞&非阻塞主要是操作系统底层C库提供的方法或者系统调用，方法可能会导致进程进入Sleep状态(当前条件不满足的情况下，操作系统主动切换进程)。非阻塞方法是操作系统不会在进程的事件片没有使用完之前提前切换进程.
    阻塞调用: 进程间主动切换
    非阻塞调用: 代码控制是否切换新任务
        非阻塞调用下的同步：
            Openresty同步调用代码
                local client = redis:new()
                client:set_timeout(30000)
                local ok, err = client:connect(ip, port) // 同步调用，内部实现是非阻塞方法
                if not ok then 
                    ngx.say('failed:', err)
                    return 
                end 

        标准的异步调用
            rc = ngx_http_read_request_body(r, ngx_http_upstream_init);
            if (rc >= NGX_HTTP_SPECIAL_RESPONSE) {
                return rc;
            }

# Nginx 模块
    使用Nginx第三方模块需要
        首先编译进Nginx binary 
        熟悉第三方模块提供哪些配置项
        熟悉第三方模块何时被开启
        熟悉第三方模块的变量
    $ ./configure 
    $ cd objs/
    $ vim ngx_modules.c 
        find ngx_module_t *ngx_modules[] 
    $ cd src/http/modules/
    $ vim ngx_http_gzip_filter_module.c 
        find ngx_command_t -- 表示支持的指令名

    Nginx模块：高内聚，抽象 

    Nginx 模块分类
        NGX_CORE_MODULE:
            events:
            core  
            errlog 
            thread_pool
            openssl 
            http
            mail
            stream
        NGX_CONF_MODULE: 负责解析nginx.conf文件
            ngx_conf_module 
        NGX_EVENT_MODULE:
            epoll
            event_core : 所有子模块共有通用模块 
        NGX_HTTP_MODULE:
            ngx_http_core_module 
            请求处理模块
            响应过滤模块
            upstream相关模块
        NGX_MAIL_MODULE:
            ngx_mail_core_module 
        NGX_STREAM_MODULE:
            ngx_stream_core_module 
         
# Nginx 连接池
    ngx_cycle_t 数据结构
        connections : 连接池数组 worker_connections default 512;
        read_events : default 与connections 数量大小一致
        write_events :  
        connections 指向的连接池中每个连接所需要的读写事件都以相同的数组序号对应着read_events, write_events读写事件数组，所以相同序号下三个数组的元素是配合使用的.

    ngx_connection_s : 每个连接使用结构体
        void            *data;
        ngx_event_t     *read;      读事件
        ngx_event_t     *write;     写事件
        ngx_socket_t    fd;
        ngx_recv_pt     recv;
        ngx_send_pt     send;   抽象解耦OS底层方法
        off_t           sent;   bytes_send变量
        ngx_log_t       *log;
        ngx_pool_t      *pool;  初始connection_pool_size配置
        int             type;
        struct socketaddr *sockaddr;
        socklen_t       socklen;
        ngx_str_t       addr_text;
        ngx_str_l       proxy_protocol_addr;
        in_port_t       proxy_protocol_port;
        ngx_buf_t       *buffer;
        ngx_queue_t     queue;
    ngx_event_s : 

    内存池：减少内存碎片的产生、
        连接内存池：connection_pool_size 256|512; bytes
        请求内存池：request_pool_size 4k; 

# Nginx Worker 进程间通讯
    Nginx进程间的通讯方式
        信号、共享内存(锁、Slab内存管理器)
    共享内存:跨worker进程通讯
        ngx_http_lua_api:  
        rbtree: 红黑树
            Ngx_stream_limit_conn_module  流控
            Ngx_http_limit_conn_module
            Ngx_stream_limit_req_module 
            Ngx_http_file_cache 
            Ngx_http_proxy_module 
            Ngx_http_scgi_module 
            Ngx_http_uwsgi_module 
            Ngx_http_fastcgi_module 
            Ngx_http_ssl_module 
            Ngx_mail_ssl_module 
            Ngx_stream_ssl_module 
        单链表: 
            Ngx_http_upstream_zone_module 
            Ngx_stream_upstream_zone_module 
    Slab内存分配管理:
        Bestfit: 最多两倍内存消耗
            合适小对象、避免碎片、避免重复初始化
        ngx_slab_stat: 统计Slab使用状态 
(Tengine) http://tengine.taobao.org/document/ngx_slab_stat.html
    $ wget http://tengine.taobao.org/download/tengine-2.3.2.tar.gz
    $ extract tengine-2.3.2.tar.gz 
    $ cd tengine-2.3.2/modules/ngx_slab_stat 
    $ cd openresty-1.15.8.1
    $ ./configure --prefix=/home/chyi/chyidl.com/openresty --add-module=../tengine-2.3.2/modules/ngx_slab_stat/

    location = /slab_stat {
        slab_stat;
    }

    $curl https://chyidl.com/set                
    STORED
    $ curl https://chyidl.com/get 
    8 
    $ curl https://chyidl.com/slab_stat        
    * shared memory: dogs
    total:       10240(KB) free:       10168(KB) size:           4(KB)
    pages:       10168(KB) start:00007FE18625E000 end:00007FE186C4E000
    slot:           8(Bytes) total:           0 used:           0 reqs:           0 fails:           0
    slot:          16(Bytes) total:           0 used:           0 reqs:           0 fails:           0
    slot:          32(Bytes) total:         127 used:           1 reqs:           1 fails:           0
    slot:          64(Bytes) total:           0 used:           0 reqs:           0 fails:           0
    slot:         128(Bytes) total:          32 used:           2 reqs:           2 fails:           0
    slot:         256(Bytes) total:           0 used:           0 reqs:           0 fails:           0
    slot:         512(Bytes) total:           0 used:           0 reqs:           0 fails:           0
    slot:        1024(Bytes) total:           0 used:           0 reqs:           0 fails:           0
    slot:        2048(Bytes) total:           0 used:           0 reqs:           0 fails:           0

# Nginx容器
    数组：
    链表：
    队列：
    哈希表：
        ngx_hash_t 
        ngx_hash_elt_t: 结构体
        Nginx hash表主要应用于静态不变的内容
            Max size
            Bucket size 需要考虑CPU Cache Size对齐问题 
            (http/stream) - variables: 
                variables_hash_bucket_size 
                variables_hash_max_size 
            (http/stream) - map:
                map_hash_bucket_size 
                map_hash_max_size 
            http proxy:
                proxy_headers_hash_bucket_size 
                proxy_headers_hash_max_size 
            ngx_http_uwsgi_module:
            ngx_http_scgi_module:
            ngx_http_fastcgi_module 
            http module:
                ngx_http_referer_module:
                    referer_hash_bucket_size 
                    referer_hash_max_size 
                ngx_http_ssi_module:
                    ngx_cacheline_size 
                    1024 
                ngx_http_scrache_filter_module:
                    ngx_cacheline_size 
                server name:
                    server_names_hash_bucket_size 
                    server_names_hash_max_size 
                MIME types:
                    types_hash_bucket_size 
        hash表遍历复杂度为O(n)
    红黑树：
        ngx_rbtree_t: 描述红黑树的结构体
            root
            sentinel 
            insert 
            ngx_rbtree_init() 
            ngx_rbtree_insert()
            ngx_rbtree_delete() 
        红黑树：根结点，左子节点、右子节点、NIL哨兵节点;二叉查找树
        红黑树做定时器，查找最小和最大值 
        自平衡二叉查找树：
            高度不会超过2倍的logn(n)
            增删改查算法复杂度O(log(n))
            遍历复杂度O(n)
        Nginx中使用红黑树的模块:
            ngx_conf_module: 
            ngx_event_timer_rbtree 
            Ngx_http_file_cache  
            Ngx_http_geo_module 
            Ngx_http_limit_conn_module 
            Ngx_http_limit_req_module 
            Ngx_http_lua_shdict:ngx.shared.DICT  LRU链表性质
            resolver 
            Ngx_stream_geo_module 
            Ngx_stream_limit_conn_module 
    基数数：

# Nginx 动态模块
    Nginx使用静态模块的过程：
        Nginx Source + Module Souce --> Nginx Build System --> Nginx Executable 
    动态模块-减少编译环节
        Nginx Source + Module Source --> Nginx Build System --> Nginx Executable + Module Shared Object 

    静态库:会将源代码直接编译到可执行二进制文件中
    动态库:会在二进制文件中保留动态库的位置，执行时直接调用动态库

    1. Configure 加入动态模块
    2. 编译进binary 
    3. 启动时初始化模块数组
    4. 读取load_module配置 指明动态模块的路径
    5. 打开动态库并加入模块数组
    6. 基于模块数组开始初始化
    
    --with-http_xslt_module=dynamic
    $ ./configure --prefix=/home/chyi/chyidl.com/nginx --with-http_image_filter_module=dynamic
    $ cd modules && ls 
    ngx_http_image_filter_module.so 
```     
![Nginx 网络事件抓包](/imgs/raspberrypi/NginxCrashCourse/Wireshark_Capture.png?raw=True)

详解HTTP模块
-----------
```

```

反向代理与负载均衡
-----------------
```
```

Nginx 和 OpenResty
------------------
```
```
