Software Design Pattern
-----------------------
> In software engineering, a software design pattern is a general, reusable solution to a commonly occurring problem within a given context in software design. Design patterns are formalized best practices that the programmer can use to solve common problems when designing an application or system.

```
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
    SOLID 原则 - SRP 单一职责原则 
    SOLID 原则 - OCP 开闭原则 
    SOLID 原则 - LSP 里式替换原则 
    SOLID 原则 - ISP 接口隔离原则 
    SOLID 原则 - DIP 依赖倒置原则 
    DRY 原则 
    KISS 原则 
    YAGNI 原则 
    LOD 法则
    单一职责、DRY、基于接口而非实现、里式替换原则 - 可复用、灵活、可读性好、易扩展、易维护

面向对象设计思想 - 
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