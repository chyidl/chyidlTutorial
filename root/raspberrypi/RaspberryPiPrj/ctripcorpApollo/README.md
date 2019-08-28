Apollo - 分布式配置中心
======================
> Apollo (阿波罗) 携程分布式配置中心，能够集中化管理应用不同环境，不同集群的配置，配置修改能够实时推送到应用端，并且具备规范的权限，流程治理等特性，使用于微服务配置管理场景.
* 服务端基于Spring Boot和Spring Cloud开发，打包后可以直接运行，不需要额外安装Tomcat等应用容器.
* Java客户端不依赖任何框架，能够运行于所有Java运行环境，同时对Spring/Spring Boot环境也有较好的支持

Apollo配置中心介绍
------------------
```
1. What is Apollo
    Apollo（阿波罗）是携程框架部门研发的开源配置管理中心，能够集中化管理应用不同环境、不同集群的配置，配置修改后能够实时推送到应用端、并且具备规范的流程、流程治理等特性.

    Apollo支持4个纬度管理Key-Value格式的配置:
        1. application 应用
        2. environment 环境
        3. cluster 集群
        4. namespace 命名空间
    
    配置基本概念
        1. 配置是独立于程序的只读变量 [常见的配置有: DB Connection Str、Thread Pool Size、Buffer Size、Request Timeout、Feature Switch、Server Urls]
        2. 配置伴随应用的整个声明周期 [配置贯穿应用的整个生命周期，应用在启动时通过读取配置来初始化，在运行时根据配置调整行为]
        3. 配置可以有多种加载方式 [常见有程序内部hard code, 配置文件, 环境变量,启动参数,基于数据库]
        4. 配置需要治理 
             权限控制: [由于配置能改变程序的行为，不正确的配置甚至能引起灾难，所以对配置的修改必须有比较完善的权限控制]
             不同环境、集群配置管理: [同一份程序在不同的环境 (开发，测试，生产)、不同的集群 (不同的数据中心)经常需要有不同的配置，所以需要有完善的环境、集群配置管理]
             框架类组件配置管理: 

2. Why Apollo
    Apollo设计之初就有治理能力的配置发布平台
        统一管理不同环境(environment)、不同集群(cluster)、不同的命名空间(namespace)的配置
        同一份代码部署在不同的集群，可以有不同的配置，比如zookeeper地址
        通过命名空间(namespace)可以方便支持多个不同应用共享同一份配置，同时还允许应用对共享的配置进行覆盖
        Apollo修改完配置并发布后，客户端实时接收到最新的配置，并通知应用程序
        所有的配置发布都有版本概念，从而可以方便支持配置回滚
        支持配置的灰度发布，比如发布只对部分应用实例生效，观察一段时间再推送给所有的实例
        权限管理、发布审核、操作审计：应用和配置的管理都有完善的权限管理机制，对配置的管理还分为编辑和发布两个环节，从而减少人为的错误.所有的操作都有审计日志，可以方便追踪问题
        客户端配置信息监控，可以方便在界面上查看配置被那些实例使用
        提供Java和Net原生客户端，方便应用集成，支持Spring Placeholder, Annotation和Spring Boot的ConfigurationProperties方便应用使用(需要Spring 3.1.1+),提供HTTP接口，非Java和.Net应用可以方便使用
        提供开放平台API:Apollo自身提供比较完善的统一配置管理界面、支持多环境、多数据中心配置管理、权限、流程治理等特性
        部署简单：配置中心作为基础服务，可用性要求非常高，这就要求Apollo对外部依赖尽可能少，目前唯一的外部依赖是MySQL,所以部署非常简单，主要安装好Java和MySQL就可以

3. Apollo at a glance
    基础模型:
        1.用户在Apollo配置中心对配置进行修改并发布
        2.配置中心通知Apollo客户端有配置更新
        3.Apollo客户端从配置中心拉取最新的配置，更新本地配置并通知到应用
```

Local Quick Start
-----------------
```
OS: CentOS7 

1. Java Version: 1.8+ 
$ java -version 
openjdk version "1.8.0_222"
OpenJDK Runtime Environment (build 1.8.0_222-b10)
OpenJDK 64-Bit Server VM (build 25.222-b10, mixed mode)

2. MySQL: 5.6.5+ 
    2.1: Adding the MySQL Yum Repository 
        $ wget mysql80-community-release-el7-3.noarch.rpm  
        $ sudo rpm -Uvh mysql80-community-release-el7-3.noarch.rpm  
    2.2: Selecting a Release Series 
        $ yum repolist all | grep mysql 
        $ sudo yum-config-manager --disable mysql80-community 
        $ sudo yum-config-manager --enable mysql57-community 
    2.3: Installing MySQL 
        $ sudo yum install mysql-community-server 
    2.4: Starting the MySQL Server 
        # Start the MySQL server with the following command
        $ sudo service mysqld start 
        $ sudo service mysqld status 
        # For EL7 and EL8-based platforms, this is the preferred command
        $ sudo systemctl start mysqld.service 
        $ sudo systemctl status mysqld.service 
        
        # MySQL Server Initialization: At the initial start up of the server, the following happens, given that the data directory of the server is empty:
            The server is initialized
            An SSL certificate and key files are generated in the data directory 
            The validate_password plugin is installed and enabled 
            A superuser account 'root'@'localhost' is created. A password for the superuser is set and stored in the error log file. To reveal it, use the following command:
                $ sudo grep 'temporary password' /var/log/mysqld.log
            Change the root password as soon as possible by logging in with the generated, temporary password and set a custom password for the superuser account.
                $ mysql -uroot -p
                mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY '';
                # 检查MySQL版本
                mysql> SHOW VARIABLES WHERE Variable_name = 'version';
```
* 3. Env deployment
    - Apollo支持一下环境：
        * DEV: 开发环境
        * FAT: 测试环境,相当于alpha环境(功能测试)
        * UAT: 集成环境,相当于beta环境 (回归测试)
        * PRO: 生产环境
### ![ctrip apollo deployment](/imgs/raspberrypi/ctripcorpApollo/apollo-deployment.png?raw=true)
```
PROD部署在生产环境的机房，通过它直接管理FAT，UAT，PROD等环境配置
Meta Server、Config Service和Admin Service 在每个环境中都单独部署，都使用独立的数据库
Meta Server、Config Service和Admin Service在生产环境部署在两个机房实现双活
Meta Server、Config Service部署在同一个JVM进程内，Admin Service部署在同一台服务器的另一个JVM进程内
```
