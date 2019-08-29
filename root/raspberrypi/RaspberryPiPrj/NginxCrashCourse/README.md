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
开源版OpenResty     http://openresty.org 
    开源Web平台主要由章亦春agentzh因为大部分Nginx模块都是由本软件包的维护者开发，所以可以确保所有这些模块及其他组件可以很好的一起工作.打包的各种软件组件版权属于各自版权所有.
商业版OpenResty     http://openresty.com 
```

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
