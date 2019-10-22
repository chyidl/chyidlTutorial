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
STP:Spanning Tree Protocol
    Root Bridge: 根交换机
    Designated Bridge: 指定交换机
    Bridge Protocol Data Units (BPDU): 网桥协议数据单元 
    Priority Vector:优先级向量 
        Root Bridge ID:
        Root Path Cost: 
        Bridge ID:
        Port ID:
    

拓扑结构: 
    环路问题: 

    
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
