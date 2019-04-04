Java (programming language)
===========================

> Java is a general-purpose computer-programming language that is concurrent, class-based, object-oriented, and specifically designed to have as few implementation dependencies as possible. It is intended to let application developers "write once, run anywhere"(WORA), meaning that compiled Java code can run on all platforms that support Java without the need for recompilation. Java applications are typicalling compiled to "bytecode" that can run on any Java virtual machine (JVM) regardless
> of the underlying computer architecture.

主要特性
--------
```
1. Java语法与C语言和C++语言很接近，Java语言不使用指针，而是引用。
2. Java语言是面向对象，Java语言提供类、接口和继承，支持类之间的单继承，支持接口之间的多继承。
3. Java支持Internet应用开发(java net)网络应用接口，提供网络应用编程的类库，包括URL、URLConnection、Socket、ServerSocket，Java RMI远程方法激活机制
4. Java语言健壮，强类型机制，异常处理，垃圾自动回收
5. Java提供安全管理机制Security Manager,Java应用设置安全哨兵
6. Java语言是体系结构中立，在Java平台上被编译为体系结构中立的字节码格式class，
7. Java语言是可移植，JVM使用ANSI C实现 
8. Java高性能,Java的运行速度随着JIT(Just-In-Time)编译器技术越来越接近C++ 
9.
Java多线程，线程是一种特殊的对象，必需由Thread类或子类创建，通常有两种方法来创建线程，其一，使用型构为Thread(Runnable)的构造子将一个实现Runnable接口的对象包装成一个线程，其二，从Thread类派生出子类并重写run方法，使用该子类创建的对象即为线程，Thread类已经实现了Runnable接口，因此，任何一个线程均有run方法，而run方法中包含了线程所要运行的代码，线程的活动由一组方法来控制，Java语言支持多线程同步，并提供多线程之间的同步机制 synchronized.
10. Java语言的设计目标之一是适应动态变化的环境，Java程序需要的类能够动态地载入运行环境，也可以通过网络载入多需要的类，这也有利于软件的升级
```

Java基础语法
------------
```
对象: 类的一个实例，有状态和行为 
类：一个模版，描述一类对象的行为和状态
方法：行为，一个类可以有很多方法
实例变量：每个对象都有独特的实例变量，对象的状态由这些实例变量的值决定

Java大小写敏感；类名首字母大写，方法名首字母小写，源文件名必需和类名相同；所有Java程序由public static void main(String[] args)开始
Java标识符首字母、下划线、$开始,关键字不能用作标识符
Java修饰符:
    访问修饰符: default, public, protected, private 
    非访问控制修饰符: final, abstract, static, synchronized, volatile
Java变量: 局部变量、类变量（静态变量）、成员变量(非静态变量)
Java数组: 存储在堆上，可以保存多个同类型变量
Java枚举：enum 
Java关键字: 
    abstract: 抽象方法，抽象类修饰符
    assert: 断言条件是否满足
    boolean: 布尔数据类型
    break: 跳出循环或者label代码段
    byte: 8 bit 有符号数据类型
    case: switch语句一个条件
    catch：和try搭配捕捉异常信息
    char：16 bit Unicode 字符数据类型
    class: 定义类
    const: -- 
    continue: 不执行循环体剩余部分
    default: switch语句中默认分支
    do: 循环语句，循环体至少会执行一次
    double: 64bit 双精度浮点数
    else: if条件不成立时执行的分支
    enum: 枚举类型
    extends: 表示一个类是另一个类的子类
    final: 表示一个值在初始化之后不能在更改，表示方法不能被重写，或者一个类不能由子类
    finally: try,catch,finally 无论有没有异常发生都执行代码
    float: 32-bit单精度浮点数
    for: for循环
    goto: - 
    if: 条件语句
    implements: 表示一个类实现了接口
    import: 导入类
    instanceof: 测试一个对象是否是某个类的实例
    int: 32位整数 
    interface: 接口，一种抽象的类型，仅有方法和常量的定义
    long: 64位整形数
    native: 表示方法非java代码实现
    new: 分配新的实例
    package: 一系列相关类组成一个包
    private: 表示私有字段，或者方法，只能从类内部访问
    protected: 表示字段只能通过类或其子类访问子类或者同在一个包的其他类
    public 共有属性和方法
    return: 方法返回值
    short: 16位数字
    static: 表示在类级别的定义，所有实例共享
    strictfp: 浮点数，使用比较严格的规则
    super: 表示基类 
    switch: 选择语句
    synchronized: 表示同一时间只能由一个线程访问的代码块
    this: 表示调用当前实例，或者调用另一个构造函数
    throw: 抛出异常
    throws: 定义方法可能抛出的异常
    transient: 修饰不要序列化的字段
    try: 表示代码快要做异常处理或者和finally配合表示是否抛出异常都执行finally中的代码
    void: 标记方法，不返回任何值
    volatile: 标记字段kennel会被多线程同时访问，而不做同步
    while: while 循环
Java注释
    单行注释：// 
    多行注释: /**/ 
java继承：超类super class, 派生类sub class 
Java接口：对象间相互通信的协议，接口在继承中扮演很重要的角色，接口只定义要用到的方法，但是方法的具体实现取决于派生类
```

Java对象和类
-----------
```
类:
对象
多态
继承
封装
抽象
实例
方法
消息解析

源文件声明规则：
    一个源文件中只能有一个public类
    一个源文件中可以有多个非public类
    源文件的名称应该和public类的类名保持一致
    如果一个类定一个在某个包中，那么package语句应该在源文件的首行 
    如果源文件中包含import语句，那么应该放在package语句和class定义之间，如果没有package语句，应该放在源文件中最前面
    import语句和package语句对源文件中定义的所有类都有效，在同一源文件中，不能给不同的类不同的包声明
```
Java基本数据类型
---------------
```
Jav两大数据类型:
    内置数据类型
    引用数据类型
Java提供八种内置基本类型：
    byte: 8bit 有符号。以二进制补码表示整数，最小值-2^7,最大值2^7-1,默认值0
    short: 16bit有符号，以二进制补码表示整数,最小值-2^16,最大值2^16-1,默认值0
    int:32bit有符号以二进制补码表示整数,最小值-2^32,最大值2^32-1,默认值是0
    long: 64bit有符号以二进制补码表示的整数,最小值是-2^64最大值2^64-1默认值是0L
    float:单精度,32bit，默认值0.0f,
    double:双精度64bit,默认值0.0d
    boolean:1bit,true,false,默认false
    char:16bitunicode字符，最小值'\u0000',最大值'\uffff'
Jav引用类型:
    引用类型变量由类的构造函数创建，可以使用他们访问所引用的对象，这些变量在声明时被指定为一个特定的类型，对象、数组都是引用数据类型，所有引用类型的默认值都是null,一个引用变量可用用来引用与任何与之兼容的类型。
Java常量： Java final标示声明常量类型，前缀0表示8进制，前缀0x表示16进制
```
Java变量类型
-----------
```

```

Java Thread
-----------
```
进程：每个进程都有一个独立的代码和数据空间（进程上下文）,进程间切换的成本比较大，一个进程可以包含1个或多个线程，进程是资源分配的最小单位
线程：同一类线程共享代码和数据空间，每个线程有独立的运行栈和程序计数器PC,线程切换开销小，线程是CPU调度的最小单元.

线程的完整周期: new创建状态->start()方法->就绪状态->run()方法->运行状态|阻塞状态->终止状态
多进程是指操作系统中同时运行多个任务(程序),
多线程是指同一个程序中有多个顺序流在执行

Runnable接口比继承Thread类具有的优势：
    适合多个相同的程序代码的线程去处理同一个资源
    可以避免java中单继承的限制
    增加程序的健壮性，代码可以被多个线程共享，代码和数据独立
    线程池只能放入实现的Runnable或callable类线程，不能直接放入继承Thread类
Java中所有的线程都是同时启动的，至于是么时候执行，完全由看谁先得到CPU资源
Java中，每个程序运行至少启动两个线程，一个是main线程，一个是垃圾回收线程，

阻塞状态Blocked:
    等待阻塞: 运行的线程执行wait()方法，JVM会把该线程放入等待池中(wait会释放持有的锁)
    同步阻塞: 运行的线程在获取对象的同步锁时，若该同步锁被别的线程占用，则JVM会把该线程放入锁池中
    其他阻塞:运行的线程执行sleep()或join()方法，或者发出IO请求时，JVM会把该线程设置为阻塞状态,当sleep()超时，join()等待线程终止或者超时，或者IO处理完毕，线程重新转入就绪状态，(sleep不会释放持有的锁)

Java线程优先级: 1-10 
    static int MAX_PRIORITY 10  
    static int MIN_PRIORITY 1
    static int NORM_PRIORITY 5 

Thread类的setPriority()和getPriority()方法分别用来设置和获取线程的优先级,主线程默认优先级为Thread.NORM_PRIORITY,线程优先级有继承关系，

线程睡眠: Thread.sleep(long millis)方法，线程转为阻塞状态,当睡眠结束后，就转为就绪Runnable状态
线程等待: Object类中wait()方法，导致当前线程等待，知道其它线程调用此对象的notify()或notifyAll()唤醒方法，
线程让步: Thread.yield()方法，暂停当前正在执行的线程对象，把执行机会让给相同或者更高优先级的线程
线程加入: join()方法，等待其它线程终止，在当前线程中调用另一个线程的join(),则当前线程转入阻塞状态，直到另一个进程运行结束,当前线程再由阻塞转为就绪状态

yield()从未导致线程转到等待/睡眠/阻塞状态，在大多数情况下，yield()将导致线程从运行状转为可运行状态，yield()方法对应如下操作，先检查当前是所有的yield()方法称为"退让"，他把运行机会让给同等优先级的其它线程。sleep()方法允许较低优先级的线程获得运行机会，但yield方法执行时，当前线程仍处于可运行状态，所以不可能让出低优先级的线程获得CPU占有权，在一个运行系统中，如果较高优先级的线程没有调用sleep()方法，又没有收到IO阻塞，那较低优先级的线程只能等待较高优先级的线程运行结束，才有有机运行

主线程: JVM调用程序main()所产生的线程
当前线程: Thread.currentThread()获取的线程
后台线程: 守护线程，JVM的垃圾回收就是一个后台守护线程,用户线程和守护线程的却别在于是否等待主线称依赖于主线程结束而结束
前台线程：isDaemon,setDaemon判断或设置线程

sleep() 线程睡眠 
isAlive() 判断线程是否存活
join():等待线程终止
activeCount():进程中活跃的线程数
enumerate(): 枚举程序中的线程
currentThread():当前线程
isDaemon():判断一个线程是否为守护线程
setDaemon():设置线程为守护线程
setName():线程设置一个名称 
wait():线程等待
notify():通知一个线程继续运行
setPriority():设置一个线程的优先级

```

计算机基础
----------
```

机器数：一个数在计算机中的二进制表示形式叫做这个数的机器数
真值：带符号位的机器数对应的真正数值称为机器数的真值
原码：符号位加上真值的绝对值。第一位表示符号位，其余表示值,8位二进制的取值范围[-127, 127]
反码: 正数的反码是其本身，负数的反码是在其原码的基础上，符号位不变，其余位取反
补码：正数的补码是其本身，负数的补码是在其原码基础上，符号位不变，其余位取反，最后加1
使用补码，不仅仅修复0的符号以及存在两个编码的问题，而且还能够多表示一个最低数，使用补码表示的范围为[-128, 127] 
```
