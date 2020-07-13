HTTP - Hyper Text Transfer Protocol
===================================
> 超文本传输协议
```
WEB: World wide web 
URI: 统一自阿远标识符，互联网资源唯一身份 
HTML: 超文本标记语言，描述超文本文档 
HTTP: 超文本传输协议，用来传输超文本
  HTTP/0.9: 纯文本格式 
    GET: 请求/响应 断开连接
  
  HTTP/1.0: 
    1. 增加HEAD，POST 方法。 
    2. 增加响应状态码，
    3. 协议版本号概念
    4. HTTP Header(头部)
    5. 传输数据不再仅限于文本

  HTTP/1.1:
    1. 增加PUT，DELETE新防范 
    2. 增加缓存管理和控制 
    3. 连接管理 允许持久连接 
    4. 允许响应数据分块chunked 可以传输大文件
    5. 强制要求Host头

  HTTP/2: (SPDY协议)
    1. 二进制协议
    2. 可以发起多个请求，废弃1.1里管道 
    3. 使用专门算法压缩头部，减少数据传输量 
    4. 允许服务器主动向客户端推送数据
    5. 增加安全性 

  HTTP/3: (QUIC协议)
    
HTTP 是一个用在计算机世界里的协议，使用计算机能够理解的语言确立了一种计算机之间交流通信的规范，以及相关的各种控制和错误处理方式
HTTP 协议是一个"双向协议"
HTTP 是一个在计算机世界里专门用来在两点之间传输数据的约定和规范
HTTP是一个在计算机世界里专门在两点之间传输文字、图片、音频、视频等超文本数据的约定和规范

HTTP 
  TCP/IP协议栈 
    IP协议实现寻址和路由
    TCP协议实现可靠数据传输
  DNS协议实现域名查找 
  SSL/TLS协议实现安全通信 

TCP/IP 网络分层模型
  application layer HTTP 
    传输单位则是消息或报文
  transport Layer   TCP/UDP -- 传输层 保证数据在IP地址标记两点之间“可靠传输”
    TCP: 有状态协议 需要先建立连接然后才能发送数据，而且保证数据不丢失不重复
    UDP: 无状态协议 不需要事先建立连接就可以任意发送数据，但不保证数据一定发送到对方
    TCP 数据是连续的字节流，有先后顺序 
    UDP分散的小数据包，是顺序发 乱序收
    TCP层传输单位是段segment 
  internet layer    IP  -- 网络层 -- 
    传输单位是包 packet
  link layer        MAC -- 链路层 -- 负责以太网/WiFi底层网络上发送原始数据包 工作在网卡
    传输单位是帧 Frame
```

HTTP 协议工作的全过程
--------------------
```
“三次握手”建立与Web服务器的连接
  [SYN]
  [SYN, ACK]
  [ACK]
GET / HTTP/1.1 
TCP 协议层面确认，刚才的报文收到
"HTTP/1.1 200 OK "
```


Appendix
--------
```
1. DNS: -- Domain Name System 域名系统
  域名用"."分隔多个单词级别从左到右逐级升高
  根DNS 
  顶级DNS
  权威DNS
  本地DNS
  负载均衡: 因为域名解析可以返回多个IP地址，所以一个域名可以对应多台主机，客户端收到IP地址后，就可以使用轮询
  域名屏蔽: 对请求的域名不解析 
  域名劫持: 域名污染
  域名的总长度限制在253个字符以内，而每一个级域名长度不能超过63个字符
  域名是大小写无关，域名大多是两级或者三级，四级以上很少见

2. 底层协议:
  可靠数据传输 
  四层与七层模型 
  IPv4/IPv6 TCP/IP 
  TCP/IP协议实际上是一系列网络通信协议的统称
    TCP/UDP: 传输层: Transmission Control Protocl: 传输控制协议
      提供字节流形式的通信
    IP : 网络层 Internet Protocol: 解决寻址和路由问题
    ICMP 
    ARP
  UNIX Domain Socket 
  HTTP over TCP/IP 

3. Proxy
  代理Proxy是HTTP协议中请求方和应答方中间的一个环节，可以转发客户端的请求，也可以转发服务器的应答
  匿名代理: 外界只看到代理服务器
  透明代理: 传输过程中是透明开放，外界知道代理也知道客户端
  正向代理: 靠近客户端，代理客户端向服务器发送请求
  反向代理: 靠近服务端,代理服务器响应客户端的请求
  proxy协议-V1 -- HAProxy
  proxy协议-V2 -- HAProxy
  3.1: 负载均衡: 把访问请求均匀分散到多台机器，实现访问集群化
  3.2: 内容缓存,暂存上下行的数据，减轻后端的压力

4. URI/URL:
  URI: Uniform Resource Identifier 统一资源标识符
  协议名://主机名/路径
  URL: Uniform Resource Locator 统一资源定位符
  协议名 
  查询参数 
  编码 

5. HTTP/1.1 
  FRC文档
    RFC2616 
    RFC7230 
  请求/应答
    请求方法: GET HEAD POST 
    请求头+请求体 
    响应头+响应体
    状态码
  无状态 
  长连接机制 
  缓存 
  MIME 

6. HTTPS:
  HTTP over SSL/TLS 运行在SSL/TLS协议上的HTTP
  SSL/TLS 负责加密通信的安全协议
  SSL - Secure Socket Layer: 
  TLS - Transport Layer Security 
  对称加密
    AES
    ChaCha 
  非对称
    RSA 
    DH 
  摘要算法
    SHA-2 
  证书 
    CA 
    X509 
  SSL/TLS 
    SNI 
    OCSP 
    连接优化 

7.HTTP/2
  SPDY 
  HPACK
  Server Push
  gRPC 

8. HTTP/3 
  基于UDP QUIC 

9. 抓包工具 
  Wireshark: 网络抓包工具
  tcpdump: 
  telnet: 虚拟终端 基于TCP协议远程登陆主机, 模拟浏览器行为，连接服务器后手动发送HTTP请求

10. 编码 
  Base64 
  chunked 
  压缩 
    gzip 
    deflate 

11. WebSocket 
  全双工 
  二进制帧
  有状态 

12. 网络 
  局域网 
  广域网
  因特网
    FTP
    IMAP/POP3
    BT 
    Magnet 
  万维网
    www 

13. Web Browser aka: User Agent
  Chrome -- Google : HTTP/1.1 HTTPS. HTTP/2 QUIC 
  Firefox -- Mozila
  Safari  -- Apple 
  IE/Edge  -- Microsoft
  浏览器是一个HTTP协议的请求方
    HTML排版引擎--展示页面 
    JavaScript引擎实现动态效果
    开发者工具调试网页 
  wget, curl command line 

14. Web Server
  Nginx: 
    高性能、高稳定、易扩展
    OpenResty : 是基于Nginx强化包，除了Nginx还有许多功能 不仅支持HTTP/HTTPS还集成脚本语言Lua简化Nginx二次开发，方便快速搭建动态网关，
  Apache:
  Microsoft-IIS 
  Tomcat
    Java 
    Servlet容器 

15. CDN -- Content Delivery Network 内容分发网络
  应用HTTP协议的缓存和代理技术，代替源站响应客户端请求
  CDN: 提供负载均衡，安全防护，边缘计算，跨运营商网络
  扮演透明代理和反向代理
  负载均衡 
  就近访问 
  Squid/Varnish/ATS 

16. 爬虫
  crawler/spider 
  robots.txt -- 协议

17. HTML -- 
  HTML4 
  HTML5 

18. Webservice  -- W3C定义的应用服务开发规范
  RESETFUL JSON 
  SOAP 
  RPC 

19. WAF -- 网络应用防火墙
  应用层防护 
  访问控制 
  审计
  检测HTTP流量，防护Web应用的安全技术
  ModSecurity: 阻止SQL注入，跨站脚本攻击
```
