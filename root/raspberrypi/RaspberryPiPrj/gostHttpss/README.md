Go Simple Tunnel - gost
=======================

Features
--------
* Listening on multiple ports - 多端口监听
* Multi-level forward proxy - proxy chain - 可设置转发嗲里，支持多级转发(代理链)
* Standard HTTP/HTTPS/HTTP2/SOCK4(A/SOCKS5 proxy protocols support 支持标准HTTP/HTTPS/HTTP2/SOCKS4(A)/SOCKS5代理协议
* Probing resistence support for web proxy - Web代理支持探测防御
* Support multiple tunnel types - 支持多种隧道类型
* TLS encryption via negotiation supports for SOCKS5 proxy - SOCKS5代理支持TLS协议加密
* Tunnel UDP over TCP - 
* Transparent TCP proxy - TCP 透明代理
* Local/remote TCP/UDP port forwarding - 本地/远程TCP/UDP端口转发
* Shadowsocks (TCP/UDP) protocol - 支持Shadowsocks(TCP/UDP)协议 
* SNI proxy - 支持SNI代理
* Permission control - 权限控制 
* Load balancing - 负载均衡
* Routing control - 路由控制
* DNS control - DNS控制 

Install
-------
```
$ go get -u github.com/ginuerzh/gost/cmd/gost 
```

Quick Start
-----------
```
$ gost -h 
Usage of gost:
  -C string
        configure file
  -D    enable debug log
  -F value
        forward address, can make a forward chain
  -L value
        listen address, can listen on multiple ports
  -V    print version
  -obfs4-distBias
        Enable obfs4 using ScrambleSuit style table generation

# 开启监听在8080端口的HTTP/SOCKS5 代理服务服务
$ gost -L :8080 

# 开启多个代理服务 
$ gost -L http2://:443 -L socks5://:1080 -L ss://aes-256-gcm:password:port 
```