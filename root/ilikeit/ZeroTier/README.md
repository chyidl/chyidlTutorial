# ZeroTier
> ZeroTier is a smart Ethernet switch for planet Earth.
```
分布式网络虚拟机管理程序，建立在加密安全的全球对等网络上，提供与企业SDN交换机同等高级网络虚拟化和管理功能，可以跨本地和广域网连接任何类型的应用程序和设备.

P2P(Peer to Peer) 根据服务器R记录路径信息，设备A能通过Zerotier唯一地址标识找到需要连接的设备B
  1. A 需要将数据包发送到B，但由于没有直接路径，需要将其上发到R
  2. 如果R直接链接到B，就会转发数据包给B
  3. R还向A发送名为会和的消息，包含有关如何到达B的提示，同时将会和发送给B,通知B他如何到达A
  4. 如果无法建立直接路径怎通信可以继续中继

Zerotier官方搭建根服务器Earth,根服务器唯一且免费，记录所有的路径信息,一般情况下大家直接使用这个免费套餐，连接时的延迟可能会很高，灵位由于Earth在国外，一些不确定的因素会影响到使用，考虑到网络的不确定性，Zerotier能自己创建根服务器Moons，这样就能在大局域网中得到更好的体验.
```

```
   1. 注册: https://my.zerotier.com/
   Free: 
    Connect up to 100 devices to unlimited networks.
    Get help from our documentation, knownledge base, and community
  2. 创建网络 
    Network -> Create a Network 

  3. 连接 
    直接在客户端输入刚才创建的Network ID 

目前情况来看，使用ZeroTier做内网穿透还是不错的,使用门槛较低
```

## Getting Started 
> After installing and starting the service (which happens automatically on most platforms) your device will generate a ZeroTier address. This is a ten-digit address that looks like 89e92ceee5
> To actually connect to anything you will need to join a network. These have 16-digit network IDs that look like 8056c2e21c000001. You can get a network ID from someone else or you can create your own network at my.zerotier.com
> Mac and Windows platforms have graphical interfaces that provide tray or task bar icons. All platforms have the zerotier-cli command line interface. Use zerotier-cli help to get help. On Unix-like systems you may need to preface this with sudo. while on Windows you will need to use an adminitrator-mode command prompt.
```
Linux (DEB/RPM)
$ curl -s https://install.zerotier.com | sudo bash 

*** Enabling and starting zerotier-one service...
Synchronizing state of zerotier-one.service with SysV service script with /lib/systemd/systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install enable zerotier-one

*** Waiting for identity generation...

*** Success! You are ZeroTier address [ 83aa770747 ].

# 启动或查看状态
$ sudo systemctl status zerotier-one 
$ sudo systemctl enable zerotier-one 

# 获取地址和服务状态
zerotier-cli status 

# 加入、离开、列出网络 
zertier-cli join   <network>    - Join a network 
zerotier-cli leave <network>    - Leave a network
zerotier-cli listnetworks       - List all networks
```
