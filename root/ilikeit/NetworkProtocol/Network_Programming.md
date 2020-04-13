# Network Programming
```
1. TCP/IP 网络模型协议 
  > OSI & TCP/IP 
    OSI 参考模型                        TCP/IP 协议栈
      应用层 
      表示层    ---------------------   应用层 
      会话层 
      传输层    ---------------------   传输层 [TCP, UDP]
      网络层    ---------------------   网络层 [IPV4, IPV6]
      数据链路层 --------------------   网络接口层
      物理层
  TCP 关心连接 
  UDP 关心报文
  IP & PORT: 
    > IP: 表示网络地址
    > PORT: 16位整数 65536
  客户端-服务器主要是编程模型不同
  套接字 (socket) (clientaddr:clientport, serveraddr: serverport)
  保留网段: 10.0.0.0 - 10.255.255.255; 172.16.0.0-172.31.255.255; 192.168.0.0-192.168.255.255
  子网掩码:网络地址位数由子网掩码Netmask表示
  DNS域名系统:网站和IP对应关系
  TCP:字节流套接字Stream Socket - SOCK_STREAM - TCP 套接字
    - TCP 通过连接管理，拥塞控制，数据流，窗口管理，超时，重传,提供高质量的端到端的通信方式
  UDP:数据报套接字Datagram Socket - SOCK_DGRAM - UDP 套接字
    - 广播或多播技术使用UDP
    - UDP可以做到很高的可靠性，可靠性需要应用程序进行设计处理,对报文编号，设计Request-Ack机制，重新传递
客户端                              服务器 
Socket                              Socket 
  |                                 Bind 
  |                                 Listen 
Connect --连接请求TCP三次握手 --    Accept 
read write                          read write 
close                               close

TCP Three-way Handshake 三次握手 
连接建立，数据传递就不再是单向而是双向
socket是建立连接 传输数据的唯一途径

套接字地址格式:
/* POSIX.1g */
typedef unsigned short int sa_family_t;
/*描述通用套接字地址*/
struct sockaddr {
  sa_family_t sa_family;    /* 地址族 16-bit*/
    AF_LOCAL: 表示本地地址 Unix套接字 - AF_UNIX,AF_FILE 
    AF_INET: 因特网使用的IPv4地址 
    AF_INET6: 因特网使用的IPv6地址 
    AF: Address Family 
    PF: Protocol Family 
  char sa_data[14];         /* 具体的地址值 112-bit */
}

FTP: 21端口 
TELNET: 23 Telnet protocol
SSH: 22端口 
HTTP: 80端口
大于5000的端口可以作为我们自己应用程序的端口使用

服务端准备连接的过程:
  > 服务器端通过创建socket,bind,listen完成初始化，通过accept完成连接的建立 
  - 创建套接字 
    - int socket(int domain, int type, int protocol)
      - domain: PE_INT, PF_INET6, PF_LOCAL -- 表示什么样的套接字 
      - type: SOCK_STREAM, SOCK_DGRAM, SOCK_RAW 
      - protocol: 0 
  - 绑定套接字和套接字地址 
    - bind(int fd, sockaddr * addr, socklen_t len)
客户端通过场景socket, connect发起连接建立请求:
  

TCP 三次握手 
  客户端                            服务器 
socket,connect(阻塞)            socket,bind,listen
  (主动打开)                        (被动打开)
  SYN_SENT      -- SYN j -->      accept(阻塞)  
connect 返回 <-- SYN k, ACK j+1 --  SYN_RCVD
ESTABLISED   -- ACK k+1 -->       accept返回 
                                  read阻塞 
                                  ESTABLISED
1. 客户端协议栈向服务器端发送SYN包,并告诉服务器当前发送序列号j,客户端进入SYNC_SENT状态 
2. 服务器端的协议栈收到这个包之后，和客户端进行ACK应答，应答值为j+1,表示对SYN包j的确认，同时服务器也发送一个SYN包，告诉客户端当前发送序列号k,服务端进行SYNC_RCVD状态
3. 客户端协议栈收到ACK之后，使得应用程序从connect调用返回,表示客户端到服务器端的单向连接建立成功,客户端状态为 ESTABLISHED,统一客户端协议栈会对服务器端的SYN包进行应答，应答数据为k+1
4. 应答包到达服务器端后，服务器端协议栈使得accept阻塞调用返回，这个时候服务器端到客户端的单向连接建立成功，服务器端进入ESTABLISHED状态


  套接字缓冲区
  拥塞控制
  数据包、数据流
  本地套接字(UNIX域套接字)

2. 异常处理
  TCP 数据流处理
  半关闭连接
  TCP连接有效性侦测 

3. 高并发网络处理程序 
  C10K 问题 
  进程、线程、多路复用、非阻塞、异步、事件驱动
```
