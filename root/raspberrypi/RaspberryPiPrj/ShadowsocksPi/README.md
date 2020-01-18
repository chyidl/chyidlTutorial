Shadowsocks
===========
> SS 的全称是Shadowsocks,是一种加密的传输方式 (一种基于Socks5代理方式的网络数据加密传输包); SS是目前主流的科学上网方式，是目前最稳定最好用的科学上网工具之一。
> SSR 的全称是ShadowsocksR,是SS的修改版，也算是增强版，是在SS的基础上做了些功能的增加和修改。
> Shadowsocks分为服务端和客户端，在使用之前，需要先将服务器端部署到服务器上面，然后通过客户端连接并创建本地代理。

运行原理
--------
> Shadowsocks 的运行原理与其它代理工具基本相同，使用特定的中转服务器完成数据传输。在服务端部署完成后，用户需要按照指定的密码、加密方式和端口，使用客户端软件与其连接。在成功连接到服务器后，客户端会在本机上构建一个本地Socks5代理(或VPN、透明代理).
> 浏览网络时，网络流量会被分到本地Socks5代理，客户端将其加密之后发送到服务器，服务器以同样的加密方式将流量回传到客户端，依次实现代理上网.
* Shadowsocks使用自行设计的协议进行加密通信，加密算法有AES、Blowfish、IDEA、RC4,除了创建TCP连接外无需握手🤝,每次请求只转发一个连接，无需保持"一直在线"的状态，因此在移动设备上相对较为省电。
* 所有的流量都经过算法加密，允许自行选择算法.
* Shadowsocks通过异步IO和事件驱动程序运行，相应速度快
* 客户端覆盖多个主流操作系统和平台，包括Windows、OSX、Android、Linux、iOS、OpenWrt

安全性
-----
```
Shadowsocks
的最初设计目的只是为了绕过GFW，而不是提供密码学意义的安全，所以Shadowsocks自行设计的加密协议对双方的身份验证仅限于预共享密钥，Shadowsocks不能代替TLS或者VPN，本质上只是设置了密码的网络代理协议，不能用作匿名通信的方案，该协议的目标不在于提供完整的通信安全机制，主要是为了协助上网用户在严苛的网络环境中突破封锁。在某些极端的环境下，通过深度包检测DPI也有可能识别出协议特征，为了确保安全，用户应做好额外的加密和验证措施，以免泄漏信息，无论使用的服务器来源是否可靠。2017年9月21日，《The Random Forest
based Detection of Shadowsock's Traffic》的论文在IEEE发表，该论文介绍通过随机森林算法检测到Shadowsocks流量的方法，并自称可达到85%的检测精度，机器学习配合GFW已经实现深度数据包检测来识别网络流量特征的做法实际可行，而且还适用于网络代理协议而不仅仅局限于Shadowsocks.
```

Quick Guide
-----------
> Shadowsocks: A secure socks5 proxy, designed to protect your Internet traffic. Bleeding edge techniques using Asynchronous I/O and Event-driven programming. 

* Server Config File: Shadowsocks accepts JSON format configs like this:
```
// shadowsocks.json 
{
    "server":"server_ip",
    "port_password":{
        "25000":"25000PASSWORD",
        "25001":"25001PASSWORD",
    },
    "local_address":"0.0.0.0",
    "local_port":1080,
    "timeout":600,
    "method":"aes-256-cfb"
}

Explanation of each field: 
    server: your hostname or server IP (IPV4/IPv6)
    server_port: server port number.
    port_password: multi port and password.
    local_port: local port number.
    password: a password used to encrypt transfer.
    timeout: connections timeout in seconds.
    method: encryption method.
```

* /etc/systemd/system/shadowsocks.service: Shadowsocks Systemd Unit Files 
```
A unit file contains configuration directives that describe the unit and define its behavior. Serveral systemctl commands work with unit files in the background. the /etc/systemd/system/ directory is reserved for unit files created or customized by the system administrator.

[Unit]
Description=Shadowsocks Server 
After=network.target
 
[Service]
ExecStart=/usr/local/bin/ssserver -c /etc/shadowsocks/shadowsocks.json 
Restart=on-abort

[Install]
WantedBy=multi-user.target 

$ sudo systemctl start shadowsocks.service 
$ sudo systemctl status shadowsocks.service 
$ sudo systemctl enable shadowsocks.service
```

* Client Shadowsocks Config File 
```
Debian / Ubuntu
$ sudo -H python3 -m pip install shadowsocks 

➜  ~ sudo sslocal -c /etc/shadowsocks_client.json -d start
INFO: loading config from /etc/shadowsocks_client.json
2019-12-01 15:32:06 INFO     loading libcrypto from libcrypto.so.1.1
Traceback (most recent call last):
  File "/usr/local/bin/sslocal", line 8, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.7/dist-packages/shadowsocks/local.py", line 39, in main
    config = shell.get_config(True)
  File "/usr/local/lib/python3.7/dist-packages/shadowsocks/shell.py", line 262, in get_config
    check_config(config, is_local)
  File "/usr/local/lib/python3.7/dist-packages/shadowsocks/shell.py", line 124, in check_config
    encrypt.try_cipher(config['password'], config['method'])
  File "/usr/local/lib/python3.7/dist-packages/shadowsocks/encrypt.py", line 44, in try_cipher
    Encryptor(key, method)
  File "/usr/local/lib/python3.7/dist-packages/shadowsocks/encrypt.py", line 83, in __init__
    random_string(self._method_info[1]))
  File "/usr/local/lib/python3.7/dist-packages/shadowsocks/encrypt.py", line 109, in get_cipher
    return m[2](method, key, iv, op)
  File "/usr/local/lib/python3.7/dist-packages/shadowsocks/crypto/openssl.py", line 76, in __init__
    load_openssl()
  File "/usr/local/lib/python3.7/dist-packages/shadowsocks/crypto/openssl.py", line 52, in load_openssl
    libcrypto.EVP_CIPHER_CTX_cleanup.argtypes = (c_void_p,)
  File "/usr/lib/python3.7/ctypes/__init__.py", line 369, in __getattr__
    func = self.__getitem__(name)
  File "/usr/lib/python3.7/ctypes/__init__.py", line 374, in __getitem__
    func = self._FuncPtr((name_or_ordinal, self))
AttributeError: /usr/lib/arm-linux-gnueabihf/libcrypto.so.1.1: undefined symbol: EVP_CIPHER_CTX_cleanup
# 由于openssl 1.1.0废弃EVP_CIPHER_CTX_cleanup()函数而引入EVE_CIPHER_CTX_reset()函数导致，可以修改文件并替换函数名
➜  ~ sudo find / -name "openssl.py"
/usr/local/lib/python3.7/dist-packages/shadowsocks/crypto/openssl.py
$ sudo vim /usr/local/lib/python3.7/dist-packages/shadowsocks/crypto/openssl.py
# 搜索并替换

sslocal is the client software 
ssserver is the server software
$ which sslocal 
/usr/local/bin/sslocal
$ which ssserver 
/usr/local/bin/ssserver

# Create a Configuration File 
$ sudo vim /etc/shadowsocks_client.json 

```

Advanced - Optimize the shadowsocks server on Linux 
---------------------------------------------------
```
# First of all, upgrade your Linux kernel to 3.5 or later.
$ uname -a 
Linux ubuntu 4.15.0-43-generic #46-Ubuntu SMP Thu Dec 6 14:45:28 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux

# Step 1, increase the maximum number of open file descriptors 
# To handle thousands of concurrent TCP connections, we should increase the limit of file descriptors opened. 
$ sudo vim /etc/security/limits.conf 
    # Add these two lines 
    * soft nofile 51200 
    * hard nofile 51200 

Then, before you start the shadowsocks server, set the ulimit first 
$ ulimit -n 51200

# Step 2, Tune the kernel parameters 
The priciples of tuning parameters for shadowsocks are 
1. Reuse ports and connections as soon as possible 
2. Enlarge the queues and buffers as large as possible 
3. Choose the TCP congestin algorithm for large latency and high throughput

$ sudo vim /etc/sysctl.conf 
/etc/sysctl.conf - Configuration file for settig system variables 

fs.file-max = 51200

net.core.rmem_max = 67108864
net.core.wmem_max = 67108864
net.core.netdev_max_backlog = 250000
net.core.somaxconn = 4096

net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_fin_timeout = 30
net.ipv4.tcp_keepalive_time = 1200
net.ipv4.ip_local_port_range = 10000 65000
net.ipv4.tcp_max_syn_backlog = 8192
net.ipv4.tcp_max_tw_buckets = 5000
net.ipv4.tcp_fastopen = 3
net.ipv4.tcp_mem = 25600 51200 102400
net.ipv4.tcp_rmem = 4096 87380 67108864
net.ipv4.tcp_wmem = 4096 65536 67108864
net.ipv4.tcp_mtu_probing = 1
net.ipv4.tcp_congestion_control = hybla

$ sysctl -p # to reload the config at runtime
```

Prohibited Ping
---------------
```
#禁止PING 
$ sysctl -w net.ipv4.icmp_echo_ignore_all=1
$ sysctl -p 
#恢复PING
$ sysctl -w net.ipv4.icmp_echo_ignore_all=0
$ sysctl -p 
```
