Network Protocol
================

* 编译原理
```
源代码 -> 词法分析 -> 语法分析 -> 语义分析 -> 代码生成 -> 目标文件

```

* 应用层协议
```
DHCP:动态主机配置协议(Dynamic Host Configuration Protocol)
    DHCP Discover: 新加入的机器使用IP:0.0.0.0发送广播包255.255.255.255，广播包封装在UDP里面, UDP封装在BOOTP里面
        MAC 头 -- 新用户Mac地址 + 广播MAC ff:ff:ff:ff:ff:ff
        IP  头 -- 新用户IP地址0.0.0.0 + 广播IP 255.255.255.255 
        UDP 头 -- 源端口: 68 目标端口: 67 
      BOOTP 头 -- Boot request 
        新用户MAC地址 + 需要分配IP 
    DHCP Offer: 
        MAC 头 -- DHCP Server Mac地址 + 广播MAC ff:ff:ff:ff:ff:ff
        IP  头 -- DHCP Server IP地址  + 广播IP 255.255.255.255 
        UDP 头 -- 源端口: 67 目标端口: 68 
      BOOTP 头 -- Boot reply 
        新用户MAC地址 + 分配IP地址、子网掩码、网关和IP地址租用期
    DHCP Request:
        MAC 头 -- 新用户Mac地址 + 广播MAC ff:ff:ff:ff:ff:ff
        IP  头 -- 新用户IP地址0.0.0.0  + 广播IP 255.255.255.255 
        UDP 头 -- 源端口: 68 目标端口: 67 
      BOOTP 头 -- Boot request 
        新用户MAC地址 + 准备租用哪一个DHCP Server分配的IP地址 
    DHCP ACK:
        MAC 头 -- DHCP Server Mac地址 + 广播MAC ff:ff:ff:ff:ff:ff
        IP  头 -- DHCP Server IP地址192.168.1.2  + 广播IP 255.255.255.255 
        UDP 头 -- 源端口: 67 目标端口: 68 
      BOOTP 头 -- Boot reply
        DHCP ACK, 新用户IP是由DHCP Server组用
        
DNS:
HTTP:
HTTPS:
RTMP:
RPC:
P2P:
GTP:

HTTP Header: POST, URL, HTTP 1.1, Body: JSON 
```

* 传输层协议
```
UDP:无连接协议
TCP:面向连接协议(Client端口,Server端口)
    TCP建立连接的三次握手🤝协议（IP层和MAC层对应都有那些操作）
        TCP发送的每条消息都会带上IP层和MAC层，因为TCP每发送一条消息，IP层和MAC层的所有机制都要运行一遍

TCP Header: client:9527, server:9528
```

* 网络层协议
```
ICMP:
IP协议:(源IP地址,目标IP地址)
    IP地址的分类
        A类     0 + [网络号(7位)] + [主机号(24位)]
            IP地址范围: 0.0.0.0  ~ 127.255.255.255 
            私有IP地址: 10.0.0.0 ~ 10.255.255.255
            最大主机数: 16777214
        B类     10 + [网络号(14位)] + [主机号(16位)]
            IP地址范围: 128.0.0.0   ~ 191.255.255.255 
            私有IP地址: 172.16.0.0  ~ 172.31.255.255 
            最大主机数: 65534
        C类     110 + [网络号(21位)] + [主机号(8位)]
            IP地址范围: 192.0.0.0   ~ 223.255.255.255 
            私有IP地址: 192.168.0.0 ~ 192.168.255.255 
            最大主机数: 254 
        D类     1110 + [多播组号(28位)]
        E类     11110 + [留待后用(27位)]
    CIDR:无类型域间选路-将32位IP地址一分为二，前面是网络号，后面是主机号
        10.100.122.2/24 -- CIDR表,表示前24位是网络号，后8位是主机号
        10.100.122.255: 广播地址
        255.255.255.0:  子网掩码 
        IP地址 AND 子网掩码 = 网络号

1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
        valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000  -- 网络设置的状态标识(net_device flags)
        UP: 表示网卡处于启动状态 
        BROADCAST: 表示网卡有广播地址,可以发送广播包
        MULTICAST: 表示网卡可以发送多播包
        LOWER_UP: 表示L1是启动的，网线插着
        MTU 1500: 最大传输单元是以太网的默认值--L2 MAC层的概念，以太网规定连MAC头+正文总共不允许超过1500个字节
        qdisc(queueing discipline - 排队规则):
            pfifo: 不对进入的数据包做任何处理，数据包采用先入先出的方式通过队列
            pfifo_fast: 队列包括三个波段band,每个波段band内部采用先进先出的规则
                band0:优先级最高，band2:优先级最低，如果band0里面有数据包，系统就不会处理band1里面的数据包，band1和band2之间也是一样 
                数据包是按照服务类型(Type of Service, TOS) 被分配到三个波段band, TOS是IP头里面的一个字段，代表了当前的包是高优先级,还是低优先级
    link/ether 00:16:3f:00:7f:58 brd ff:ff:ff:ff:ff:ff   -- MAC 地址
    inet 172.16.111.136/20 brd 172.16.111.255 scope global dynamic eth0
        valid_lft 314484741sec preferred_lft 314484741sec

lo: loopback 环回接口
MAC 地址的通信范围比较小，局限在一个子网里面
IP地址有定位的功能，MAC是身份标示，无定位功能 

OSPF:
BGP: 
IPSec: 
GRE:

IP Header: client IP addr: 192.168.1.1, server IP addr: 192.168.1.2 
```

* 数据链路层协议
```
MAC: Medium Access Control 媒体访问控制:控制往媒体上发数据的时候，谁先发、谁后发的问题，防止发生混乱
    1. 信道划分: 
    2. 轮流协议: 
    3. 随机接入协议: 
链路层地址--常称为MAC地址 
CRC:循环冗余检测: 通过XOR异或的算法来计算整个包是否在发送的过程中出现错误，
ARP: 已知IP地址，获取MAC地址的协议
    缓存IP-MAC映射表
RARP: 已知MAC地址，获取IP地址
网络包格式:
    [目标MAC(6 byte)][源MAC(6 byte)][类型(2 byte)][数据 (46 - 1500 byte)][CRC (4 byte)]
                                        |
                                        |_ 类型0800: IP数据包; 0806: ARP请求,应答

交换机:
    转发表
VLAN:
The Spanning Tree Protocol (STP):生成树协议
    Root Bridge: 根交换机
    Designated Bridge: 指定交换机
    Bridge Protocol Data Units (BPDU): 网桥协议数据单元 
    Priority Vector:优先级向量 
        Root Bridge ID:
        Root Path Cost: 
        Bridge ID:
        Port ID:
    
拓扑结构: 
    环路问题: -- 怎么破除环路?
    解决广播问题和安全问题?
        1. 物理隔离
        2. 虚拟隔离 
            VLAN-虚拟局域网: 在二层头部加上一个TAG(VLAN ID 12位 - 可以划分位4096个VLAN)
            Trunk 口:可以转发属于任何VLAN口，交换机之间可以通过这种口相互连接 
         
ICMP (Internet Control Message Protocol) 互联网控制报文协议
    ping是基于ICMP协议工作
    ICMP报文封装在IP包内
        [IP 头][ICMP报文]
                  |
                [类型 8位][代码 8位][校验和 16位][...]
                                                |
                                                1. 请求与响应 [标识符 16位][序号 16位][数据]
                                                2. 差错报文   [unused 16位][unused 16位][IP 头][8 Byte正文]
    

    
```

* 物理层协议
```
RJ45接口定义
    1: TX+      (数据发送正端)
    2: TX-      (数据发送负端)
    3: RX+      (数据接收正端)
    4: 未用     
    5: 未用
    6: RX-      (数据接收负端)
    7: 未用
    8: 未用
网络跳线: 将一端1号3号线,2号和6号互换位置，就能够在物理层实现一端发送的信号另一端能收到
Hub集线器:将包转发到所有端口

```

* 网络协议常用命令
```
linux/Mac: 
    ifconfig (net-tools) -- 查看IP地址
        $ sudo ifconfig eth1 10.0.0.1/24 
        $ sudo ifconfig eth1 up 
    ip addr (iproute2)  -- Shows addresses assigned to all network interfaces.
        $ sudo ip addr add 10.0.0.1/24 dev eth1 
        $ sudo ip link set up eth1 
Windows:
    ipconfig 


PXE(Pre-boot Execution Environment 预启动执行环境):
BIOS:读取硬盘MBR启动扇区，将GRUB启动起来，GRUB加载内核，加载作为根文件系统的initramfs文件，然后启动内核，初始化整个操作系统.
    PXE协议分为客户端和服务端，由于还没有操作系统，只能先把客户端放在BIOS里面，当计算机启动时，BIOS把PXE客户端调如内存里面，就可以连接到服务端做一些操作

DHCP Server配置:
    ddns-update-style interim;
    ignore client-updates;
    allow booting;
    allow bootp;
    subnet 192.168.1.0 netmask 255.255.255.0
    {
        option routers 192.168.1.1;
        option subnet-mask 255.255.255.0;
        option time-offset -18000;
        default-lease-time 21600;
        max-lease-time 43200;
        range dynamic-bootp 192.168.1.240 192.168.1.250;
        filename "pxelinux.0";      # 初始化启动文件filename 
        next-server 192.168.1.180;  # PXE 服务器的地址
    }

TFTP协议: 
    pxelinux.cfg -- 计算机配置信息
```

* 分层思想
```
数据库层
缓存层
Compose层
Controller层
接入层
```

net-tools vs. iproute2
----------------------
```
ifconfig, route, arp, netstat command-line tools, collectively known as net-tools. Originally rooted in the BSD TCP/IP toolkit,  the net-tools was developed to configure network functionality of older Linux kernels. Its development in the Linux community so far has ceased since 2001. Some Linux distros such as Arch Linux and CentOS/RHEL 7 have already deprecated net-tools, and others are planning to do so in favor of iproute2.

iptoute2, which is another family of network configuration tools, emerged to replace the functionality of net-tools. While net-tools accesses and changes kernel network configurations via procfs(/proc) and ioctl system call.iproute2 communicates with the kernel via netlink socket interface. The /proc interface is known to be more havyweight than netlink interface. 

the user interface of iproute2 is more intuitive than that of net-tools.
```

TCP/IP Protocol backlog
-----------------------
```
# backlog其实是一个连接队列:
-- Linux Kernel lower than 2.2
    半连接状态队列: 服务器处于Listen状态时收到客户端SYN报文时放入半连接队列中，SYN queue (服务器端口为: SYN_RCVD)
    + 
    全连接状态队列: TCP的连接状态从服务器(SYN+ACK)响应客户端后，到客户端的ACK报文到达服务器之前处于半连接状态，当服务器接收到客户端的ACK报文后，该条目将从半连接队列转移到全连接队列的尾部，accept queue (服务器端口状态为: ESTABLISHED)
-- Linux Kernel higher than 2.2
    半连接状态队列 SYN_RCVD状态     : 
    全连接状态队列 ESTABLISHED状态  : 
                  SYN queue 队列  : /proc/sys/net/ipv4/tcp_max_syn_backlog 指定，默认为2048 
               Accept queue 队列  : /proc/sys/net/core/somaxconn 和使用listen函数时传入的参数二者取最小的值，默认是128; 可以修改/etc/sysctl.conf中配置 net.core.somaxconn = 1024 

$ ss -l 
Netid    State    Recv-Q    Send-Q    Local Address:Port    Peer Address:Port
tcp      LISTEN   0         128       *:mysql               *:*
tcp      LISTEN   0         128       [::]:6379             [::]:*

LISTEN状态中，Send-Q即为Accept queue的最大值, Recv-Q则表示Accept Queue中等待被服务器accept() 
TCP三次🤝过程中，客户端connect()返回不代表TCP连接建立成功，有可能accept queue已满，系统回直接丢弃后续ACK请求，客户端误以为连接已建立，开始调用等待至超时;服务器则等待ACK超时，会重新传递SYN+ACK给客户端，重传次数受限net.ipv4.tcp_synack_retries,默认为5.表示重发5次，每次等待30～40秒，即半连接默认时间大约为180秒

查看SYN queue 溢出
$ netstat -s | grep LISTEN 

查看Accept queue 溢出 
$ netstat -s | grep TCPBacklogDrop


(Linux)
$ netstat -pant | grep LISTEN
    -p: show the program name/PID owning the socket 
    -a: show all connections 
    -n: show numerical addresses 
    -t: show only TCP connections 
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
tcp        0      0 127.0.0.1:587           0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:6379            0.0.0.0:*               LISTEN      -
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -
tcp        0      0 127.0.0.1:5432          0.0.0.0:*               LISTEN      -
tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN      -
tcp6       0      0 :::3306                 :::*                    LISTEN      -
tcp6       0      0 :::6379                 :::*                    LISTEN      -
tcp6       0      0 :::22                   :::*                    LISTEN      -

(macOS: List listening ports and programs using netstat)
$ netstat -an -ptcp | grep LISTEN
tcp4       0      0  *.7005                 *.*                    LISTEN     
tcp4       0      0  127.0.0.1.63342        *.*                    LISTEN     
tcp4       0      0  127.0.0.1.6942         *.*                    LISTEN     
tcp4       0      0  127.0.0.1.4301         *.*                    LISTEN     
tcp4       0      0  127.0.0.1.4300         *.*                    LISTEN     
tcp4       0      0  127.0.0.1.17603        *.*                    LISTEN     
tcp4       0      0  127.0.0.1.17600        *.*                    LISTEN     
tcp4       0      0  127.0.0.1.1086         *.*                    LISTEN     
tcp4       0      0  127.0.0.1.1087         *.*                    LISTEN     
tcp46      0      0  *.1089                 *.*                    LISTEN     
tcp4       0      0  *.1089                 *.*                    LISTEN     
tcp6       0      0  *.49160                *.*                    LISTEN     
tcp4       0      0  *.49160                *.*                    LISTEN     
tcp4       0      0  *.22                   *.*                    LISTEN     
tcp6       0      0  *.22                   *.*                    LISTEN

There seems to be no way to get the same kind of info using netstat on macOS. But everything is not lost. A tcp socket is just another type of file descriptor in Unix derivatives so we can lsof to get the same info on macOS:
$ lsof -i -P | grep -i "LISTEN"
rapportd    329 chyiyaqing    4u  IPv4 0x1dab9459a9e6d77f      0t0  TCP *:49160 (LISTEN)
rapportd    329 chyiyaqing    5u  IPv6 0x1dab9459a9e61087      0t0  TCP *:49160 (LISTEN)
QQ          413 chyiyaqing   37u  IPv4 0x1dab9459b085d3ff      0t0  TCP localhost:4300 (LISTEN)
QQ          413 chyiyaqing   38u  IPv4 0x1dab9459b525ac3f      0t0  TCP localhost:4301 (LISTEN)
Dropbox    1319 chyiyaqing  163u  IPv4 0x1dab9459b81c8cff      0t0  TCP localhost:17600 (LISTEN)
Dropbox    1319 chyiyaqing  170u  IPv4 0x1dab9459b81c797f      0t0  TCP localhost:17603 (LISTEN)
Shadowsoc  1397 chyiyaqing    5u  IPv4 0x1dab9459b085b6bf      0t0  TCP *:1089 (LISTEN)
Shadowsoc  1397 chyiyaqing    6u  IPv6 0x1dab9459a9e5fe87      0t0  TCP *:1089 (LISTEN)
privoxy    1428 chyiyaqing    3u  IPv4 0x1dab9459b3fefc3f      0t0  TCP localhost:1087 (LISTEN)
ss-local   1439 chyiyaqing    8u  IPv4 0x1dab9459b54c4fbf      0t0  TCP localhost:1086 (LISTEN)
pycharm   86095 chyiyaqing  192u  IPv4 0x1dab9459b0857c3f      0t0  TCP localhost:6942 (LISTEN)
pycharm   86095 chyiyaqing  418u  IPv4 0x1dab9459b77f277f      0t0  TCP localhost:63342 (LISTEN)
pycharm   86095 chyiyaqing  448u  IPv4 0x1dab9459b0072c3f      0t0  TCP *:7005 (LISTEN)
```
![TCP/IP backlog](/imgs/ilikeit/NetworkProtocol/tcp-backlog.png?raw=true)

HTTP/3 - HTTP over QUIC is the next generation 
----------------------------------------------
```
HTTP/1  (in ASCII over TCP)    -- 1996 
HTTP/1.1    -- Shipped January 1997 
    Many parallel TCP connections 
    Better but ineffective TCP use.
    HTTP head-of-line-blocking 
    Numberous work-arounds

HTTP/2 (Binary multiplexed over TCP)-- 2015 
    Uses single connection per host
    Many parallel streams
    TCP head-of-line-blocking 

Ossification
    Internet is full of boxes 
    Routes, geteways, firewalls, load balancers, NATs.
    Boxes run software to handle network data.
    Middle-boxes work on existing protocols.
    Upgrade much slower than edges.

HTTP/3 (binary over multiplexed QUIC)

    Under the hood 
    --------------
$ curl -v https://apple.com.cn 

> GET / HTTP/1.1
> Host: apple.com.cn
> User-Agent: curl/7.64.1
> Accept: */*

< HTTP/1.1 301 Moved Permanently
< Server: Apache
< Date: Tue Jun  1 12:48:03 PDT 1999 PDT
< Referer: http://apple.com/
< Location: https://www.apple.com/cn/
< Content-type: text/html
< Content-length: 266

HTTP started done over TCP.
TCP (publish in 1981): works over IP; 
    Establishes a "Connection"; 
    3-way handshake; 
    Resends lost packages;
    Delivers a byte stream;
    Clear text;

HTTPS means TCP + TLS + HTTP.
    TLS(Transport Layer Security) is done over TCP for HTTP/1 or 2;
        Additional handshake: another ping pong on top of the TCP 
        Privacy and security

Classic HTTP/1 and HTTP/2 Network Stack:
    IP -> TCP -> TLS 1.2+ -> HTTP/1/2
Classic HTTP/3 Network Stack:
    IP -> UDP -> TLS1.3 (QUIC) -> HTTP/3

QUIC : A new transport protocol
    Built on experiences by Google QUIC
        Google deployed "http2 frames over UDP" - QUIC in 2013 
        Widely used client.
        Widely used web services 
        Proven to work at web scale 
        Taken to the IETF in 2015.
        QUIC working group started 2016.
        IEFT QUIC is now every different than Google QUIC was
            transport protocol: 
            application protocol: 
    Improvements:
        TCP head of line blocking -- when we lose a packet 
        Faster handshakes 
        Earlier data 
        Connection-ID 
    Build on top of UDP:
    UDP isn't reliable, 
        Connection less 
        No resends 
        No flow control
    QUIC is:
        Uses UDP like TCP uses IP 
        Adds connections, resends and flow control on top 
Stream:
    QUIC provides streams
    Many logical flows within a single connection
    Similar to HTTP/2 but in transport layer 
    Independent streams

Application protocols over QUIC:
    Streams for free
    Could be "any protocol"
    HTTP worked on as the first 

HTTP - sample but different 
    > Request
        - method + path 
        - headers 
        - body 
    < Response
        - response code 
        - headers
        - body

HTTP/3 is faster
    Faster handshakes
    Early data that works 
    The independent streams 
    By how much remains to be measured.
    CPU intensive 
    Unoptimized UDP stacks 
    All QUIC stacks are user-land 

Implementations:
    Over a dozen QUIC implementations, almost as many HTTP/3 implementations 
        Google, Mozila, Apple, Facebook, Microsoft, Akamai, Fastly, Cloudflare, F5, LiteSpeed
    

HTTPS is TCP?
    HTTPS://URLs are everywhere 
    TCP (and TLS) on TCP port 443 
    
```
![HTTP/3 vs HTTP/2](imgs/ilikeit/../../../../../imgs/ilikeit/NetworkProtocol/HTTP-3.png?raw=true)