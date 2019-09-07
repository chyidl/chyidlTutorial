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
    $ ./configure --prefix=/usr/local/openresty --with-http_ssl_module 
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
```

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
