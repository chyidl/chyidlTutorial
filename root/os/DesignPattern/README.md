Software Design Pattern
-----------------------
> In software engineering, a software design pattern is a general, reusable solution to a commonly occurring problem within a given context in software design. Design patterns are formalized best practices that the programmer can use to solve common problems when designing an application or system.

```
面向过程编程: 是一种编程范式或编程风格，它以过程(可以为理解方法、函数、操作)作为组织代码的基本单元，以数据(可以理解为成员变量、属性)与方法相分离为最主要的特点，面向过程风格是一种流程化的编程风格，通过拼接一组顺序执行的方法来操作数据完成一项功能.
面向过程编程语言:是一种编程语言,不支持类和对象两种语法概念，不支持丰富的面向对象编程特性(继承、多态、封装),仅支持面向过程编程

面向过程 vs. 面向对象 
    面向过程风格的代码被组织成一组方法集合及其数据结构(struct User)，方法和数据结构的定义是分开的.
    面向对象风格的代码被组织成一组类，方法和数据结构被绑定一起，定义在类中
        1. 面向对象编程能够应对大规模复杂程序的开发
        2. 面向对象风格的代码更易复用、易扩展、易维护

数据结构和算法 - 写出高效率代码 
设计模式 - 
    大部分设计模式要解决的都是代码的可扩展性问题
    经典的设计模式有23种,随着编程语言的演进，一些设计模式(比如Singleton)随之过时，甚至成为反模式，一些则被内置在编程语言中(比如Iterator),另外还有一些新的模式诞生(Monostate)
    如何写出可扩展、可读、可维护的高质量代码 
    23中经典设计模式分为三大类: 创建型、结构型、行为型
        1. 创建型
             1.1: 常用: 单例模式、工厂模式(工厂方法和抽象工厂)、构造者模式 
             1.2: 不常用: 原型模式 
        2. 结构型
            2.1: 常用: 代理模式、桥接模式、装饰者模式、适配器模式
            2.2: 不常用: 门面模式、组合模式、享元模式 
        3.  行为型:
            3.1: 常用: 观察者模式、模版模式、策略模式、职责链模式、迭代器模式、状态模式
            3.2: 不常用: 访问者模式、备忘录模式、命令模式、解释器模式、中介模式

编码规范 -  可读性
    编程规范只要解决代码的可读性问题
    《重构》、《代码大全》、《代码整洁之道》

重构技巧 - 
    持续重构可以时刻保持代码的可维护性
    重构是软件开发中非常重要的一个环节，持续重构是保持代码质量不下降的有效手段，能有效避免代码腐化到无药可救的地步
    1. 重构的目的(Why), 对象(What), 时机(When), 方法(How)
    2. 保证重构不出错的技术手段：单元测试和代码的可测试性
    3. 两种不同规模的重构: 大重构(大规模高层次)和小重构(小规模低层次)

设计原则 - 
    SOLID 原则 - (Single Responsibility - SR) 单一职责原则:类或者对象最好只有单一职责，在程序设计中如果发现某个类承担着多种义务，可以考虑进行拆分 
    SOLID 原则 - (Open-Close, Open for extension, close for modification - OCP) 开关原则: 设计要对扩展开放，对修改关闭 
    SOLID 原则 - (Liskov Substitution - LS) 里式替换: 进行继承关系抽象时，凡是可以用父类或者基类的地方，都可以用子类替换 
    SOLID 原则 - (Interface Segregation - IS) 接口分离: 拆分成功能单一的多接口、将行为进行接耦.
    SOLID 原则 - (Dependency Inversion - DI) 依赖反转: 实体应该依赖于抽象而不是实现，也就说高层次模块,高层次模块应该基于抽象
    DRY 原则 
    KISS 原则 
    YAGNI 原则 
    LOD 法则
    单一职责、DRY、基于接口而非实现、里式替换原则 - 可复用、灵活、可读性好、易扩展、易维护
    基于接口而非实现编程 - 
        “Program to an interface, not an implementation” 
        应用这条原则，可以将接口和实现相分离,封装不稳定的实现，降低耦合性，提高扩展性
    基于抽象而非实现编程 - 
        越抽象、越顶层、越脱离集体某一实现的设计，越能提高代码的灵活性，越能应对未来的需求变化，好的代码设计、不仅应对当下的需求，而且在将来需求发生变化的时候，能够在不破坏原有代码设计的情况下灵活应对
        抽象是提高代码扩展性、灵活性、可维护性最有效的手段之一 
        1. 函数的命名不能暴露任何实现细节
        2. 封装具体的实现细节
        3. 实现类定义抽象的接口
    抽象意识、封装意识、接口意识

面向对象设计思想 - 
    OOP(Object Oriented Programming): 面向对象编程
        - 面向对象编程是一种编程范式或编程风格，以类和对象作为组织代码的基本单元，并将封装、抽象、继承、多台四个特征作为代码设计和实现的基石。
        Class(类)
        Object(对象)
    OOPL(Object Oriented Programming Language): 面向对象编程语言
        - 面向对象编程语言是支持类或对象的语法机制，并有现成的语法机制，能方便地实现面向对象编程四大特征(封装、抽象、继承、多态)的编程语言
    面向对象的四大特征: 
        封装(Encapsulation): 封装也叫做信息隐藏或者数据访问保护。
            Java: public, private, protected 访问权限控制语句
        抽象(Abstraction): 隐藏方法的具体实现，调用者只需要关心方法提供那些功能，并不需要知道这些功能是如何实现
            Java: interface(接口类), abstract(抽象类)
        继承(Inheritance): 继承是用来表示类之间的is-a关系. “多用组合少用继承”
            单继承(一个子类只继承一个父类)、多继承(一个子类可以继承多个父类)
            Java: extends 实现继承 - 支持单继承
            C++: Class B: Public A - 支持多继承
            Python: paraentheses()  - 支持多继承
        多态(Polymorphism): 子类可以替换父类
            多态需要三种语法机制实现:
                1. 编程语言支持父类对象可以引用子类对象
                2. 编程语言要支持继承
                3. 编程语言要支持子类可以重写(override)父类中的方法
            多态特性的实现方式除了利用"继承加方法重写"这种实现方式之外，
            还可以利用接口类语言 - 类必须实现对应的接口
            和duck-typing语法(Python, JavaScript) - 两个类具有相同的方法，就可以实现多态，并不要求两个类之间有任何关系
    OOA(Object Oriented Analysis)面向对象分析:
    OOD(Object Oriented Design)面向对象设计
    UML(Unified Model Language)统一建模语言:
    主流的编程范式分别是面向过程、面向对象、函数式编程
    面向对象编程因为具有丰富的特征(封装、抽象、继承、多态)可以实现很多复杂的设计思路，是很多设计原则、设计模式编码实现的基础。
        1. 面向对象的四大特征: 封装、抽象、继承、多态
        2. 面向对象编程与面向过程编程的区别和联系
        3. 面向对象分析、面向对象设计、面向对象编程 
        4. 接口和抽象类的区别以及各自的应用场景 
        5. 基于接口而非实现编程的设计思想
        6. 多用组合少用继承的设计思想
        7. 面向过程的贫血模型和面向对象的充血模式
    继承、多态 --可复用性

maintainability(可维护性):
    代码易维护:在不破坏原有代码设计、不引入新的Bug的情况下，能够快速地修改或者添加代码

readability(可读性):
    code review 是一个很好的测验代码可读性的手段

extensibily(可扩展性):

flexibility(灵活性):

simplity(简洁性):
    尽量保持代码简单、代码简单、逻辑清晰，也就意味着易读、易维护。
    思从深而行从简，真正的高手能云淡风轻地用最简单的方法解决最复杂的问题，

reusability(可复用性):
    代码的可复用性可以简单地理解为，尽量减少重复代码的编写，复用已有的代码。
    面向对象特征: 继承、多态是为了提高代码的可复用性

testability(可测试性):

静态方法将方法和数据分离，破坏了封装特性，是典型的面向过程风格
Java语言中Collections.unmodifiableList()方法不可修改的集合

传统的MVC (Model层， Controller层， View层)
前后端分离之后，三层结构在后端开发中分为Controller层,Service层,Repository层;每一层中会定义响应的VO(View Object)、BO(Business Object)、Entity
    Controller层负责暴露接口给前端调用
    Service层负责核心业务逻辑 
    Repository层负责数据读写 

违反面向对象编程风格的典型代码设计:
    1. 滥用getter、setter方法 :在设计实现类的时候，除非真的需要，否则尽量不要给属性定义setter方法，防止集合内部数据被修改
    2. Constants类，Utils类的设计问题

抽象类 vs. 接口类
    - 接口类实现面向对象的抽象特征、多态特征和基于接口而非实现的设计原则 
        Java中interface关键字定义一个Filter接口，
            AuthencationFilter、RateLimitFilter是接口的两个实现类
        接口不能包含属性 (就是成员变量)
        接口只能声明方法，方法中不能包含代码实现 
        类实现接口的时候，必须实现接口中声明的所有方法 接口表示一种has-a 关系,又称为协议contract

        接口侧重于解耦,接口是对行为的一种抽象

    - 抽象类实现面向对象的继承特征和模版设计模式
        抽象类使用场景(模版设计模式)
            Logger是日志的抽象类 
            FileLogger、MessageQueueLogger继承Logger,分别实现不同的日志记录方式;记录日志到文件和记录日志到消息队列
        抽象类不允许被实例化，只能被继承    
        抽象类可以包含属性和方法,方法既可以包含代码实现也可以不包含代码实现(抽象方法)
        子类继承抽象类，必须实现抽象类中的所有抽象方法

        抽象类是一种特殊的类，这种类不能被实例化为对象，只能被子类继承，继承关系是一种is-a关系
        抽象类是为了代码复用，多个子类继承抽象类中定义的属性和方法，避免在子类中重复编写相同的代码

        Java语言即支持抽象类也支持接口
        C++语言只支持抽象类、不支持接口
        Python语言既不支持抽象类、也不支持接口(通过Metaclass模拟实现抽象类、接口类语法)

    - 什么时候使用抽象类，什么时候使用接口?
        is-a  关系 - 抽象类 : 是一种自下而上的设计思路，现有子类的代码复用，然后在抽象成上层的父类
        has-a 关系 - 接口 : 是一种自上而下的设计思路，

组合 vs. 继承 
    "组合优于继承、多用组合少用继承"
    "最小知识原则 (Least Knowledge Principle) - 迪米特法则"
    继承最大的问题就在于: 继承层次过深，继承关系过于复杂会影响到代码的可读性和可维护性
        继承主要的三个作用: 
            is-a关系 -- 可以使用组合和接口的has-a关系代替
            支持多态 -- 可以使用接口实现
            代码复用 -- 可以通过组合和委托实现
        模版模式(template pattern) - 使用继承 
    组合(composition)、接口、委托(delegation)三种技术解决继承存在的问题?
        装饰器模式(decorator pattern)、策略模式(strategy pattern)、组合模式(composite pattern) - 使用组合关系

贫血模型 vs. 充血模型
    贫血模型(Anemic Domain Model): 数据和业务逻辑被分割到不同的类中    -- 面向过程编程风格
    充血模型(Rich Domain Model): 数据和对象的业务逻辑被封装到同一个类中 -- 面向对象编程风格

Web MVC三层架构：M 表示(Model), V 表示(View), C 表示(Controller)
    项目分为三层: 展示层、逻辑层、数据层
Web 前后端分离架构: 后端暴露接口，前端调用
    后端项目分为 Repository层、Service层、Controller层
        Repository层负责数据访问
        Service负责业务逻辑
            基于贫血模型的传统开发模式: Service层包含Service类(业务逻辑)和BO类(只包含数据，不包含具体的业务逻辑)
            基于充血模型的DDD开发模式：Service层包含Service类和Domain类(既包含数据也包含业务逻辑)
        Controller层负责暴露接口
    违背面向对象编程风格，是一种面向过程的编程风格，被称为反模式(anti-pattern) 

领域驱动设计(Domain Driven Design, DDD): 指导如何解耦业务系统、划分业务模块、定义业务领域模型及其交互。
微服务(Micro Service): 监控、调用链追踪、API网关，针对业务合理地做微服务拆分，而领域设计恰好就是用来指导划分服务，微服务加速领域驱动设计的盛行。
SQL-Driven(SQL驱动开发): 
领域模型相当于可复用的业务中间层,新功能需求的开发都是基于定义好的这些领域模型完成
        

软件开发中唯一不变的就是变化

标准的Java开发库:
    JDK 
    Apache Commons 
    Google Guava 
```


* KISS, an acronym for "keep it simple, stupid" or "keep it stupid simple"
```
is a design principle noted by the U.S.Navy in 1960. The KISS principle states that most systems work best if they are kept simple rather than made complicated; therefore, simplicity should be a key goal in design, and unnecessary complexity should be avoided.
```

```
Linus Torvalds:
    > "Talk is cheap, Show me the code." - Torvalds, Linus (2000-08-25). 

Date	Fri, 25 Aug 2000 11:09:12 -0700 (PDT)
From	Linus Torvalds <>
Subject	Re: SCO: "thread creation is about a thousand times faster than onnative
share

On Fri, 25 Aug 2000, Jamie Lokier wrote:
> 
> Well well.  I think it's possible to over the best of user-space "fake"
> threads plus the advantages of "true" kernel threads in one blindingly
> fast combination, in less than 8kB per thread.

Talk is cheap. Show me the code.
		Linus

Martin Fowler:
    > “Any fool can write code that a computer can understand. Good programmers write code that humans can understand.”

DRY(Don't Repeat Yourself)

重构火葬场:
    命名不规范、类设计不合理、分层不清晰、没有模块化概念、代码结构混乱、高度耦合

描述代码质量词汇:
    flexibility(灵活性)、extensibility(可扩展性)、maintainability(可维护性)、readability(可读性)、understandability(可理解性)、changeability(易修改性)、reusability(可复用性)、testability(可测试性)
    modularity(模块化)、high cohesion loose coupliing(高内聚低耦合)、high efficiency(高效性)、high performance(高性能)、security(安全性)、compatibility(兼容性)、usability(易用性)、clean(整洁)、clarity(清晰)、simple(简单)、straightforward(直接)、less code is more(少即是多)、well-documented(文档详尽)、well-layered(分层清晰)、correctness, bug free(正确性)、robustness(健壮性)、
    robustness(鲁棒性)、reliability(可用性)、scalability(可伸缩性)、stability(稳定性)、elegant(优雅)、good(好)、bad(坏)
```

Appendix 
--------
```
# 后端业务系统框架 
// Controller+VO(View Object) --- 接口层 //
public class UserController {
    // 通过构造函数或者IOC框架注入 
    private UserService userService;

    public UserVo getUserById(Long userId) {
        UserBo userBo = userService.getUser(userId);
        UserVo userVo = [...convert userBo to userVo...];
        return userVo;
    }    
}

public class UserVo {
    // 省略其他属性，get/set/construct方法 
    private Long id;
    private String name;
    private String cellphone;
}

// Service+BO(Business Object) --- 业务逻辑层// 
public class UserService {
    // 通过构造函数或者IOC框架注入
    private UserRepository userRepository;  

    public UserBo getUserById(Long userId) {
        UserEntity userEntity = userRepository.getUserById(userId);
        UserBo userBo = [///convert userEntity to userBO...];
        return userBo;
    }
}

public class UserBo {   // 只包含数据、不包含业务逻辑的类称为贫血模型(Anemic Domain Model)
    // 省略其他属性、get/set/construct方法
    private Long id;
    private String name;
    private String cellphone;
}

// Repository+Entity -- 数据访问层 // 
public class UserRepository {
    public UserEntity getUserById(Long userId) {
        
    }
}

public class UserEntity {
    // 省略其他属性、get/set/construct方法 
    private Long id;
    private String name;
    private String cellphone;
}
```

Spring Framework
----------------
```
名次解析:
Spring Boot DevTools: 自动应用代码更改到最新的App上面，原理是发现代码有更改之后，重新启动应用
    原理是使用两个ClassLoader, 一个ClassLoader加载那些不会改变的类(第三方包),另外一个ClassLoader加载会更改的类，成为restart ClassLoader.

Lombok: Project Lombok is a java library that automatically plugs into your editor and build tools. spicing up your java. Never write another getter and equals method again, with one annotation your class has a fully featured builder, Automate your logging variables, and much more.
    @Data 
    @Getter 
    @Setter
    @Cleanup



$ javac -cp lombok.jar Main.java
$ javap Main 

```

FQA
---
```
1. 编程语言是否支持多继承? 
```

IDEA ShortCut
-------------
```
1. two ^Space: A special variant of the Code Completion feature invoked
2. Option+Enter: inject SQL into a string
3. Option+Shift+Command+U: open a UML class diagram
4. Option+Command+U: open a UML class diagram
5. Option+Shift+Command+D: analyze changes using diagrams.
```