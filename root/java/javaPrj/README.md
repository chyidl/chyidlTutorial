Java (programming language)
===========================

> Java is a general-purpose computer-programming language that is concurrent, class-based, object-oriented, and specifically designed to have as few implementation dependencies as possible. It is intended to let application developers "write once, run anywhere"(WORA), meaning that compiled Java code can run on all platforms that support Java without the need for recompilation. Java applications are typicalling compiled to "bytecode" that can run on any Java virtual machine (JVM) regardless
> of the underlying computer architecture.

- [IntelliJ IDEA's Java反编译](/root/java/javaPrj/java-decompiler/README.md)
- [OpenJDK asmtools](/root/java/javaPrj/AsmTools/README.md)

Spring Family
-------------
* Spring Framework History
```
诞生于2002年，成型于2003年，最早作者为Rod Johnson.
    《Expert One-on-One J2EE Designed Development》
    《Expert One-on-One J2EE Development without EJB》
目前发展到Spring 5.x版本，支持JDK8-11及Java EE 8

Spring: the source for modern java 
https://spring.io/projects 

Spring Framework:用于构建企业级应用的轻量级一站式解决方案
Spring Boot: 快速构建基于Spring的应用程序 
Spring Cloud: 简化分布式系统的开发
    配置管理
    服务注册与发现
    熔断
    服务追踪

What's New in Spring Framework 5.x Release notes:
    JDK Version Range:
        Spring Framework 5.x: JDK 8+ 、Kotlin 
        (Java 8 新特性 Lambda表达式)
    Spring WebFlux:
        Support for Kotlin Coroutines: 异步编程模式

Spring Boot 和 Spring Cloud 出现是必然:
    开箱即用、与生态圈深度整合、注重运维、Cloud Native
```

Hello Spring
------------
```
https://start.spring.io
Spring Initializr Boorstrap your application 

# Install Maven on macOS using Homebrew
$ brew install maven 

# Maven package command 
$ mvn clean package -Dmaven.test.skip
$ cd target 
$ java -jar hello-spring-0.0.1-SNAPSHOT.jar   

Spring JDBC & ORM 
    数据源相关:
        DataSource
    事务相关
        PlatformTransactionManager (DataSourceTransactionManager)
        TransactionTremplate 
    操作相关:
        JdbcTemplate

Spring Boot Actuator:
    https://www.baeldung.com/spring-boot-actuators
    Spring Boot 2.x Actuator: Monitoring our app, gathering metrics, understanding traffic or the state of our database becomes trivial with this dependency.
    Actuator comes with most endpoints disabled.Thus, the only two available by default are /health and /info.
        
        management.endpoints.web.exposure.include=* . Althernatively, we could list endpoints which should be enabled.

    Actuator is mainly used to expose operational information about the running application - health, metrics, info, dump, env, etc. It uses HTTP endpoints or JMX beans to enable us to interact with it.
        http://localhost:8080/actuator/health   
        http://localhost:8080/actuator/beans
```

| 修饰符    | 当前类 | 同包  | 子类  | 其他包 |
| :-------- | :----: | :---: | :---: | :----: |
| public    |   ✅    |   ✅   |   ✅   |   ✅    |
| protected |   ✅    |   ✅   |   ✅   |   🚫   |
| default   |   ✅    |   ✅   |  🚫   |   🚫   |
| private   |   ✅    |  🚫   |  🚫   |   🚫   |
