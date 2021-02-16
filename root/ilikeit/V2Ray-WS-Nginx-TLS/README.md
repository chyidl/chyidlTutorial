V2Ray WS Nginx TLS
==================

* Project V
> Project V is a set of tools to help you build your own privacy network over internet.
```
Features:
    Multiple inbound/outbound proxies: one V2Ray instance supports in parallel multiple inbound and outbound protocols. Each protocol works independently.
    Customizable routing: incoming traffic can be sent to different outbounds based on routing configuration. It is easy to route traffic by target region or domain.
    Multiple protocols: V2Ray supports multiple protocols, including Socks, HTTP, Shadowsocks, VMess etc. Each protocol may have its won transport, such as TCP, mKCP, WebSocket etc.
    Reverse proxy: General support of reverse proxy. Can be used to build tunnels to localhost.

    UDP转发: VMess是基于TCP的协议，对于UDP包V2Ray会转成TCP再传输，即 UDP over TCP
    时间： 使用V2Ray要保证时间准确

工作机制:

    1. 单服务器模式
        V2Ray 服务器可同时支持多台设备，使用不同的代理协议访问，同时，经过合理的配置，V2Ray可以识别并区分需要代理和不需要代理的流量，直连的流量不需要绕路
    2. 桥接模式
        设置一台中转服务器，用于接收客户端发来的所有流量，然后在服务器中进行转发判断

工作原理:

    [inbound...] -> Dispatcher/Router/DNS -> [outbound...]
    inbound: 入站协议负责与客户端通信:
        1. 入站协议通常可以配置用户认证
        2. 入站协议收到数据之后 会交给分发器(Dispatcher)进行分发
    outbound: 出战协议负责将数据发给服务器
    路由会在必要时查询DNS以获取更多信息来进行判断

Linux 安装脚本:

    V2Ray提供一个在Linux自动化安装脚本
    $ wget https://raw.githubusercontent.com/v2fly/fhs-install-v2ray/master/install-release.sh
    ❯ ./install-release.sh                                                                                                                                 14:30:02
    info: Installing V2Ray v4.34.0 for x86_64
    Downloading V2Ray archive: https://github.com/v2fly/v2ray-core/releases/download/v4.34.0/v2ray-linux-64.zip
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100   626  100   626    0     0   2407      0 --:--:-- --:--:-- --:--:--  2398
    100 11.8M  100 11.8M    0     0  22.8M      0 --:--:-- --:--:-- --:--:-- 22.8M
    Downloading verification file for V2Ray archive: https://github.com/v2fly/v2ray-core/releases/download/v4.34.0/v2ray-linux-64.zip.dgst
    info: Extract the V2Ray package to /tmp/tmp.ZuH0VikgyY and prepare it for installation.
    rm: cannot remove '/etc/systemd/system/v2ray.service.d/10-donot_touch_multi_conf.conf': No such file or directory
    rm: cannot remove '/etc/systemd/system/v2ray@.service.d/10-donot_touch_multi_conf.conf': No such file or directory
    info: Systemd service files have been installed successfully!
    warning: The following are the actual parameters for the v2ray service startup.
    warning: Please make sure the configuration file path is correctly set.
    # /etc/systemd/system/v2ray.service
    [Unit]
    Description=V2Ray Service
    Documentation=https://www.v2fly.org/
    After=network.target nss-lookup.target

    [Service]
    User=nobody
    CapabilityBoundingSet=CAP_NET_ADMIN CAP_NET_BIND_SERVICE
    AmbientCapabilities=CAP_NET_ADMIN CAP_NET_BIND_SERVICE
    NoNewPrivileges=true
    ExecStart=/usr/local/bin/v2ray -config /usr/local/etc/v2ray/config.json
    Restart=on-failure
    RestartPreventExitStatus=23

    [Install]
    WantedBy=multi-user.target

    # /etc/systemd/system/v2ray.service.d/10-donot_touch_single_conf.conf
    # In case you have a good reason to do so, duplicate this file in the same directory and make your customizes there.
    # Or all changes you made will be lost!  # Refer: https://www.freedesktop.org/software/systemd/man/systemd.unit.html
    [Service]
    ExecStart=
    ExecStart=/usr/local/bin/v2ray -config /usr/local/etc/v2ray/config.json

    installed: /usr/local/bin/v2ray                     # 执行文件
    installed: /usr/local/bin/v2ctl                     # 工具
    installed: /usr/local/share/v2ray/geoip.dat         # IP 数据文件
    installed: /usr/local/share/v2ray/geosite.dat       # IP数据文件
    installed: /usr/local/etc/v2ray/config.json         # 配置文件
    installed: /var/log/v2ray/
    installed: /var/log/v2ray/access.log
    installed: /var/log/v2ray/error.log
    installed: /etc/systemd/system/v2ray.service
    installed: /etc/systemd/system/v2ray@.service
    removed: /tmp/tmp.ZuH0VikgyY
    info: V2Ray v4.34.0 is installed.
    You may need to execute a command to remove dependent software: apt purge curl unzip
    Please execute the command: systemctl enable v2ray; systemctl start v2ray

```

* V2Ray Install
```
软件V2Ray不区分服务器版和客户端版
```


Appendix
--------
* Set Up Time Synchronization
```
Introduction
    Accurate timekeeping has become a critical component of modern software deployments.

    Ubuntu has time synchronization built in and acticated by default using systemd's timesyncd service.

Navigating Basic Time Commands:
    # find out the time on your server
    $ date

    # list the available time zones
    $ timedatectl list-timezones

    # set the time zone with
    $ timedatectl set-timezone Asia/Hong_Kong

Controlling timesyncd with timedatectl
    most network time synchronization was handled by the Network Time Protocol daemon or ntpd. This service connects to a pool of other NTP servers that provide it with constant and accurate time updates.

NTPD
    $ sudo timedatectl set-ntp no

    # Verify that timesyncd is off
    $ timedatectl

    ntpd will be started automatically after install, can query ntpd for status information to verify
    $ ntpq -p
```
