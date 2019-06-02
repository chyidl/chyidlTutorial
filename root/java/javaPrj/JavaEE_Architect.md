SSM(Spring + Spring MVC + MyBatis):
===================================

MyBatis 3.x框架:
----------------
    * MyBatis框架体系与ORM思想:
```
What is MyBatis?
    MyBatis is a first class persistence framework with support for custom SQL, stored procedures and advanced mappings.MyBatis eliminates almost all of the JDBC code and manual setting of parameters and retrieval of results. MyBatis can use simple XML or Annotations for configuration and map primitives, Map interfaces and Java POJOs(Plain Old Java Objects) to database records.



ORM思想/持久层框架/MyBatis与Hibernate对比/MyBatisUtil抽取/Mapperscanner/Environments设置/多数据源动态替换/源码中的dirty变量/OGNL表达式

MyBatis框架是JDBC的封装,主要目的简化JDBC开发流程,实现事务松耦合管理，将实体类与SQL命令进行动态对应.
```     
    * Single Table CRUD:
> last_insert_id()与@@identity应用/$与#与SQL注入/resultType与resultMap应用场景/Mapper动态代理/源码中MapperProxy/parameterType三种形态
    
    * Relational Query:
> one-many/many-one/many-many查询/collection配置/association配置/延迟加载策略/DirectLoading/侵入式延迟配置/深度延迟配置
        
    * MyBatis Annotain:
> CRUD annotain/DynamicSQL/SQLProvider
    
    * MyBatis高级开发:
> MyBatis自定义插件开发/反向代码生成器/MyBatisGenerator/MyBatis增强器MyBatis_Plus

SSM之Spring 5.x框架:
--------------------
    * Spring框架体系:
```
            Spring框架体系/侵入式与非侵入式/Spring容器/单例模式优点/Spring与解耦合/依赖注入与自动注入/SPEL注入/注解式注入
```
    * Spring 5 IOC 容器:
```
            IOC与DI关系/依赖注入与自动注入/SPEL注入/注解式注入
```
    * Spring 5 AOP容器:
```
            代理模式/AOP/AspectJ/CGLIB代理/AspectJ基于注解的AOP实现/五种通知
```
    * Spring 5高级应用:
```
            Spring与MyBatis整合/Druid数据源/AspectJ的AOP事务管理方式/Spring Web应用/Spring tool suit插件
```

SSM之Spring MVC框架:
--------------------
    * Spring MVC 核心组件:
```
            MVC设计模式/Spring MVC与Servlet的关系/DispatcherServlet/HandlerMapping/Controller/ModelAndView/ViewResoler
```
    * Spring MVC高级应用:
```
            多文件上传与下载/与AJAX交互/跨域解决方案/请求参数获取响应/Spring、SpringMVC、MyBatis整合
```

分布式系统与MySQL集群:
----------------------
    * 主从复制 Master-Slave实践:
```
            集中式系统与分布式系统/HAC高可用集群/MySQL主从复制(Master-Slave)实践/一主多从/双主多从/双主双从/MySQL主从同步延迟原理机解决方案
```
    * 读写分离Mysql-Proxy实践：
```
            MySQL集群工作效率分析/读写分裂实现高可用集群/MySQL_proxy/Atlas/Amoeba读写分离中间件
```
    * 高可用集群管理工具 MyCat:
```
            分布式系统的恶数据库架构演变/MyCat工作原理/水平拆分与垂直拆分/逻辑库(shcema)/分片节点(dataNode)/分片主机(dataHost)/MyCat实现MySQL主从复制+主备切换+读写分离
```
    * MySQL索引优化与锁:
```
            B-tree和Hash索引结构/SQL执行效率日志分析/最左前缀匹配原则/表级锁与行级锁/Table Read Lock和Table Write Lock/共享锁/排他锁/意向共享锁/意向排他锁区别/deadlock原因与解决方案
```

分布式系统与内存数据库Redis:
---------------------------
    * NoSQL, Redis, Memcached:
```
            关系数据库与非关系型数据库区别/NoSQL/redis与Memcached区别/key操作命令/五种数据类型
```
    * Redis应用实践:
```
            Redis主从复制集群/容灾冷处理/掌握事务管理/AOF与RDB/Redis Sentinel/高可用集群/HA主从集群/伪主从集群
```
    * Redis高级应用:
```
            Jredis/Spring整合Redis/缓存贯穿原因及解决方案
```

分布式系统与文档模型数据库MongoDB:
---------------------------------
    * MongoDB体系:
```
            关系模型和文档模型的区别/MongoDB/CouchDB/Terrastore/RavenDB/文档CRUD/Primary/Secondary/Arbiter三种角色/分片/聚合
```
    * MongoDB高级应用:
```
            MongoDB关联关系/覆盖查询/分析查询/Spring与MongoDB集成
```

分布式架构-反向代理服务器Nginx:
-------------------------------
    * 反响代理原理:
```
            正向代理/反向代理服务器/Nginx在Linux下的makefile源码安装/Nginx-h/-t/-s/-c选项命令用法/通过配置调整使Nginx命令随处可用/在没有获取CA证书的情况下Nginx Server访问时的注意事项
```
    * 静态代理:
```
            请求定位模块的配置/后缀拦截策略/目录拦截策略/location请求路径与root参照路径的关系/默认资源index配置及指定资源访问/使用regexp定位静态资源
```
    * 负载均衡:
```
            F5/Array等硬件负载均衡/upstream模块配置/proxy_pass配置/upstream的域名制定/负载server的均衡配置/proxy_pass与upstream域名关
```
    * 动静分离:
```
            搭建一个集群：在多台Web Server上部署web应用集群，在多台的Nginx Server上部署静态资源，再由Nginx负责负载均衡
```
    * 虚拟主机:
```
            虚拟主机与Server模块/端口虚拟主机PortServer的配置/域名虚拟机DomainServer的配置
```

分布式架构 - 协调服务器Zookeeper:
---------------------------------
    * zk基础:
```
            ZK配置维护/域名服务/分布式同步/集群管理功能/ZKmode/Zookeeper Atomic Broadcast/域名服务中的服务消费者/提供者与zk/Leader选举机制/read request高并发下的Observer/write request与Leader/恢复模式/广播模式/同步模式
```
    * zookeeper配置与实践:
```
            初始时限initLimit与同步时限syncLimit相对设置/高延迟网络环境下的syncLimit设置/zoo配置/zkServer/start/restart/status/stop命令用法
```
    * zkHA集群搭建:
```
            server.id/connPort/elecPort/epoch/zxid
```

分布式架构-微服务框架Dubbo:
---------------------------
    * 服务的提供者与消费者:
```
            RPC通信协议/SOA体系架构/Dubbo的三段论/暴露服务/订阅服务/async广播/sync调用/async统计/N/A registry/zkClient
```
    * zk/zkHA注册中心:
```
            registry backup注册与protocol注册/服务注册dubbo:service/服务消费dubbo:reference
```
    * 多版本控制欲服务分组:
```
            理解多版本控制的应用场景/服务分组的应用场景/多版本控制与服务分组的区别与联系
```
    * Dubbo监控平台:
```
            Dubbo Monitor的安装/配置/启动/查看/dubbo-master/dubbo-admin/register zk registry
```

企业级现代数据访问技术 - Spring Data:
-------------------------------------
    * Docker:
```
            Docker的守护式容器/Docker的数据卷容器/跨主机网络访问/网桥实现跨主机容器连接
```
    * Spring Data Redis:
```
            实时/非实时数据缓存/API访问/annotation访问
```
    * Spring Data MongoDB:
```
            CrudRepository/PagingAndSortingRepository
```
    * Spring Data JPA:
```
            JPA annotation/方法命令规则/JPQL/JpaRepository
```
    * 高级响应式Web开发之Spring WebFlux:
```
            WebFlux集成Redis/MongoDB
```

分布式架构 - Spring Session:
----------------------------
    * 集群Session共享/同域名异工程Session共享:
```
            集群Session共享下的RedisHttpSessionConfiguration配置/同域名异工程Session共享下的Cookie会话策略设置/同根域名异二级域名Session共享下的默认CookieSerializer设置
```

微服务架构 - Spring Boot:
-------------------------
    * Spring Boot基础:
```
            Spring Tools Suite/boot 下的mvnw/Thymeleaf模版/yml与yaml/热部署
```
    * Spring Boot Core:
```
            SpringBootTest/Profile实现多环境选择/读取自定义配置属性/读取自定义配置文件/boot与mybatis整合/boot下的事务支持/logback日志/boot下的redis/boot与dubbo整合
```

微服务架构 - Spring Cloud:
-------------------------
    * Cureka服务注册中心:
```
            微服务原理/分布式服务的治理/使用Eureka服务注册与发现
```
    * Ribbon负载均衡:
```
            负载均衡strategy
```
    * Feign Web客户端、Hystrix熔断机制与Turbine框架
```
            Feign+Hystrix+客户端路由+服务降级
```
    * API Gateway与Spring Zuul实现
```
            利用Zuul/Spring Cloud Gateway实现分布式服务网关、鉴权、服务分发
```
    * 分布式架构配置中心Spring Cloud Config:
```
            分布式应用的配置中心原理/优点/配置变更
```

分布式文件系统FastDFS:
----------------------
    * FastDFS架构分析/上传下载：
    * FastDFS/Tracker Server/Storage Server安装配置及与Nginx集成/Storage Server内置的http服务器和Nginx的区别:
    * 使用Java客户端完成文件的上传下载流程/使用Java客户端对同一个文件的不同尺寸存储：
```
            FastDFS 具有高可用、高扩展、高性能的优势/FastDFS通过Tracker Server集群和Storage Server集群提供强大的分布式存储的能力，解决大容量小文件存储的性能问题.
```

分布式架构 - 消息服务器ActiveMQ:
--------------------------------
    * JMS/ActiveMQ/ActiveMQ消息传递模型详解:
    * ActiveMQ单机版:
    * ActiveMQ与Spring Boot集成:
    * ActiveMQ高级之ActiveMQ集群以及安全机制:
```
            解决多个系统之间的异步通信的问题，类似QQ，ActiveMQ解决系统与系统之间的通信问题
```

全文搜索引擎 - Lucene/Solr/ElasticSearch:
----------------------------------------
    * Lucene:
```
            Lucene全文检索流程分析、详解索引库的逻辑结构、Lucene的java开发(对索引库的增删改查操作) lkAnalyzer中文分词器的介绍和使用
            Field域的重点理解
            相关度排序的了解（百度竞价排名）
```
    * Solr:
```
            Solr和Lucene的区别，solr服务器单机版安装及配置、solr core和solr home的介绍
            两种Java客户端的使用，solrj客户端整合Spring的使用及spring data solr的使用
            solrconfig和schema配置文件的介绍及配置
            使用solr技术实现电商页面的实现
```
    * ElasticSearch:
```
            Elasticsearch 与 lucene区别/Elasticsearch分布式全文搜索实战。
```

大型互联网电商项目:
===================
```
    功能介绍:
        1. 登陆认证
        2. 权限验证
        3. CAS单点登录
        4. 基于REST接口的前后端分离开发模式
        5. 秒杀 (库存扣减、请求队列、订单ID生成)
        6. 搜索（包括品类、品牌过滤条件、关键字自动补全等搜索难点）
        7. 微信支付
        8. 详情页动静结合方式进行展示（访问模版技术生成的静态详情页、详情页中动态展示规格数据及是否有库存）
        9. 购物车功能（分店铺、购物车存储技术）
        10. 下单功能（库存扣减、订单ID生成）
        11. 上传图片（压缩和加水印功能）
        12. 静态页面缓存
        13. 四层负载&七层负载实现负载均衡
        14. SOA架构详解及serverless架构浅析
        15. 电商商品模块业务表的设计方式
    技术栈介绍：
        1. Maven
        2. SSM 框架
        3. MySQL数据库
        4. Angularjs （Vue）前端框架
        5. Git
        6. Dubbox
        7. Zookeeper
        8. Solr (ElesticSearch, ES)
        9. Redis
        10. ActiveMQ
        11. 微信支付接口
        12. Shiro
        13. CAS
        14. 阿里云.云服务之短信服务
        15. Spring Boot
        16. Nginx
        17. FastDFS
        18. Linux
    项目总结:
        本项目是一个大型BBC运营模式的互联网电商项目
        1. 学习架构技术(SOA 架构、Serverless架构)（高可用、高并发、高扩展、集群、分布式、限流、熔断思想）
        2. 锻炼项目综合能力(项目流程介绍、项目员工组成以及功能指责、需求分析及详细设计)（包括如何通过对数据库三范式的理解去编写数据库设计文档）、非功能性需求（并发需求、页面相应需求
        3. 技术应用（maven,dubbox, ssm, solr, redis）
        4. 互联网解决方案（秒杀方案、单点登录方案、搜索方案、购物车方案、商品详情页展示方案）
```
