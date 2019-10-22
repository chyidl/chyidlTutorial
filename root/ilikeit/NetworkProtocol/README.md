Network Protocol
================

* 编译原理
```
源代码 -> 词法分析 -> 语法分析 -> 语义分析 -> 代码生成 -> 目标文件

```

* 应用层协议
```
DHCP:
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
OSPF:
BGP: 
IPSec: 
GRE:

IP Header: client IP addr: 192.168.1.1, server IP addr: 192.168.1.2 
```

* 链路层协议
```
ARP:
VLAN:
STP:
```

* 物理层协议
```
网络跳线
```

* 网络协议常用命令
```
linux/Mac:
    ifconfig (net-tools) -- 查看IP地址
    ip addr (iproute2)  -- Shows addresses assigned to all network interfaces.
Windows:
    ipconfig 
```

* 分层思想
```
数据库层
缓存层
Compose层
Controller层
接入层
```