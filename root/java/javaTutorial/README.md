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
Java语言支持的变量类型:
    类变量: 独立于方法之外的变量，用static修饰,静态变量存储在静态存储区，经常被声明为常量，常量是指声明为public/private,final,static类型的变量。静态变量可以通过ClassName.VariableName方式访问，类变量被声明为public static final类型时，类变量名称一般建议使用大写字母，如果静态变量不是public和final类型，其命名方式与实例变量以及局部变量的命名方式一致。
    实例变量:
    独立于方法之外的变量，不过没有static修饰,实例变量在对象创建的时候创建，在对象被销毁的时候销毁，实例变量可以声明在使用前或使用后，访问修饰符可以修饰实例变量，实例变量对于类中的方法，构造方法或者语句快是可见的，一般情况下应该把实例变量设为私有，通过使用访问修饰符可以使实例变量对子类可见。实例变量具有默认值，数值型变量的默认值是0，布尔型变量默认值是false，引用类型的变量的默认值是null，变量的值可以在声明时指定，也可以在构造方法中指定。实例变量可以直接通过变量名访问，但在静态方法以及其它类中，就应该使用限定名:ObjectReference.VariableName.
    局部变量: 类的方法中的变量，访问修饰符不能用于局部变量，局部变量只在声明他的方法、构造方法或者语句块中可见，局部变量是在栈上分配的，局部变量没有默认值，所以局部变量被声明后，必需经过初始化，才可以使用.
```

Controlling Access to Members of a Class
----------------------------------------
> Access level modifiers determine whether other classes can use a particular fields or invoke a particular method. There are two levels of access control:
> At the top level - public, or package-private (no explicit modifier)
> At the member level - public, private, protected, or package-private (no explicit modifier)

| modifier    | Class | Package | Subclass | World |
| :---------- | :---- | :------ | :------- | :---- |
| public      | Y     | Y       | Y        | Y     |
| protected   | Y     | Y       | Y        | N     |
| no modifier | Y     | Y       | N        | N     |
| private     | Y     | N       | N        | N     |

```
访问修饰符
    default: 在同一个包内可见，不使用任何修饰符，使用对象：类，接口。变量，方法
    private: 在同一类内可见，使用对象、变量、方法
    public: 对所有类可见，使用对象：类，接口，变量，方法
    protected: 对同一包内的类和所有子类可见，使用对象：变量、方法 
访问控制和继承
    父类中声明为public的方法在子类中必须为public
    父类中声明为protected的方法在子类中要么声明为protected，要么声明为public，不能声明为private.
    父类中声明为private方法，不能够被继承
非访问修饰符
    static 修饰符: 用来修饰类方法和类变量
    final 修饰符: 用来修饰类、方法和变量，final修饰的类不能被继承，修饰的方法不能被继承重新定义，修饰的变量为常量，是不可以修改的。final方法可以被子类继承，但是不能被子类修改，声明final方法的主要目的是防止该方法的内容被修改
    abstract 修饰符: 用来创建抽象类和抽象方法，抽象类不能用来实例化对象，声明抽象类的唯一目的是为了将来对该类进行补充，
    synchronzied和volatile修饰符: 主要用于线程编程,synchronized关键字声明的方法同一时间只能被一个线程访问,volatile修饰的成员变量在每次被线程访问的时，都强制从共享内存中重新读取该成员变量的值，而且，当成员变量发生变化时，会强制线程将变化值会写到共享内存中，两个不同线程总能看到某一个成员变量的同一个值。
```

Java运算符
---------
```
算术运算符
    +、-、*、/、%、++、--
    前缀自增自减法(++a,--a)先进行自增或者自减运算，再进行表达式运算 
    后缀自增自减法(a++, a--)先进性表达式运算，在进行自增或者自减运算 
关系运算符
    ==、!=、>、<、>=、<=
位运算符
    Java定义的位运算符，应用于整数类型，长整型，短整形，字符型，字节型。位运算符作用在所有的位上，并且按位运算
    &、|、^、~、<<、>>、>>>
逻辑运算符
    &&、||、!
    短路逻辑运算符，两个操作数都为true时，结果才为true,但是当得到第一个操作为false其结果必定为false，这时候就不用判断第二个操作数
赋值运算符
    =、+=、-=、*=、/=、%=、<<=、>>=、&=、^=、|=
其他运算符
    条件运算符 ?: 也被称为三元运算符，该运算符有3个操作数，并且需要判断布尔表达式的值
    instanceof运算符,检查该对象是否是一个特定的类型
```
Java 循环结构 for while do while
--------------------------------
```
while循环
do while循环
for循环
if else 条件语句
switch语句
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

Java核心技术
-----------

* 1. Java基础 
    - Java平台的理解
```
Java是一种面向对象的语言
    Write Once, run anywhere.
    GC, Garbage Collection: Java通过垃圾收集器(Garbage Collector) 回收分配内存 
    JRE, Java Runtime Environment: Java运行环境(包括JVM,Java类库)
    JDK, Java Development Kit(JRE超集，提供更多工具，比如编译器、各种诊断工具)
    .java文件(源代码) -- javac编译 -- .class（字节码）-- Java虚拟机(JVM)解释器将字节码转换成最终的机器码. Oracle JDK 提供Hosspot JVM,提供JIT（Just-In-Time）编译器-动态编译器，JIT能够在运行时将热点代码编译成机器码，这种情况下部分热点代码就属于编译执行而不是解释执行.
    JVM通过类加载器(Class-Loader)加载字节码，解释或者编译执行,JDK8是解释和编译混合的一种模式，即所谓的混合模式(-Xmixed).运行在Server模式的JVM，会进行上万次调用收集足够的信息进行高效的编译,Client模式的JVM门限石1500次，Oracle Hotspot JVM内置两个不同的JIT compiler，C1对应前面讲的client模式，适用于启动速度敏感的应用(普通Java桌面应用),C2对应server模式,优化长时间运行的服务器端应用设计.默认采用分层编译(Tiered Compilation).
    JVM虚拟机启动时可以指定不同参数对运行模式进行选择
        -Xint: JVM只进行解释执行,不对代码进行编译,这种模式抛弃JIT带来的性能优势
        -Xcomp: 不进行解释执行,最大优化级别，会导致JVM启动变慢，同时有些JIT编译器优化方法，比如分支预测，如果不进行profiling往往并不能进行有效的优化
    AOT（Ahead-of-Time Compilation):直接将字节码编译成为机器代码。避免JIT预热开销，JDK9引入实验性的AOT特征，并且增加新的jaotc工具
        # 下面命令将某个类或某个模块编译成AOT库
        $ jaotc --output libHellWorld.so HelloWorld.class 
        $ jaotc --output libjava.base.so --module java.base 
        # 启动时直接指定
        $ java -XX:AOTLibrary=./libHellWorld.so,./libjava.base.so HelloWorld
    JVM作为强大的平台，不仅仅只有Java语言可以运行在JVM上，本质上合规的字节码都可以运行，类似Clojure,Scala,Grovy,JRuby,Jypthon 

    Java语言特性
        面向对象
        反射
        泛型
    Java类库
        核心类库: 
            IO/NIO
            网络
            utils 
        安全类库:
        jdk,management类库:
        第三方类库:
    Java虚拟机
        垃圾收集器
        运行时
        动态编译
        辅助功能、JFR 
    Java辅助工具
        辅助工具:
            jlink
            jar
            jdeps 
        编译器
            javac: Javac编译，编译Java源代码生成.class文件字节码
            sjavac 
        诊断工具
            jmap
            jstack 
            jconsole 
            jcmd 
```
    - Exception 和 Error区别?
```
    Exception 和 Error都是继承Throwable类，Java中只有Throwable类型的实例才可以被抛出(throw)或者捕获(catch).是异常处理机制的基本组成类型
        Exception是程序正常运行中可以预料的意外情况，可以并且应该被捕获并处理.
            Exception分为可检查异常(checked)和非检查异常(unchecked)
            可检查异常再源代码中必须显式进行捕获处理
            不检查异常就是所谓的运行时异常 NullPointException, ArrayIndexOutOfBoundsException
        Error是程序正常情况下不大可能出现的情况，绝大部分的Error都会导致程序(JVM本身)处于非正常、不可恢复状态。比如OutOfMemoryError
        Object -> Throwable -> Error  [OutOfMemoryError,StackOverflowError,VirtualMachineError,NoClassDefFoundError,ExceptionInInitializerError]
                            -> Exception [IOException, RuntimeException, NullPointerException,ClassCastException,SecurityException]

    try-catch-finally, throw, throws
    try-with-resources, multiple catch. 
        try (BufferedReader br = new BufferedReader(...); BufferedWriter writer = new BufferedWriter())
```             
    - ClassNotFoundException vs. NoClassDefFoundError?
```
    > ClassNotFoundException, It is an exception. It is of type java.lang.Exception. It occurs when an application tries to load a class at run time which is not updated in the classpath. It is thrown by the application itself. It is thrown by the methods like Class.forName(), loadClass() and findSystemClass(). It occurs when classpath is not updated with required JAR files.

    > NoClassDefFoundError: It is an error. It is of type java.lang.Error. It occurs when Java runtime system doesn't find a class definition, which is present at compile time, but missing at run time. It is thrown by the Java Runtime System. It occurs when required class definition is missing at runtime.
```
    - final、finally、finalize?
```
    1. final可以用来修饰类、方法、变量:
        final修饰class代表不可以继承扩展
        final修饰方法不可以重写(override)
        final修饰变量不可以修改

    2.finally是Java保证代码一定被执行的一种机制
        try-finally 或 try-catch-finally进行类似关闭JDBC连接、保证unblock锁
    
    3. finalize是基础java.lang.Object的方法，目的是保证对象在被垃圾收集前完成特定资源的回收。finalize机制已不推荐使用，并在JDK9开始被标记deprecated.
        Java平台目前逐步使用java.lang.ref.Cleaner来替代原有的finalize实现. Cleaner的实现利用了幻想引用(PhantomReference).
资源用完即显式释放、或者利用资源池来尽量重用
```
    - 强引用、软引用、弱引用、幻想引用?
```
不同的引用类型，主要体现的是对象不同的可达性reachable状态和对垃圾收集的影响
    Strong Reference: 强引用: 最常见的普通对象引用，只要还有强引用指向一个对象，就能表明对象“还活着”，垃圾收集不会回收次对象。

    Soft Reference: 软引用,是一种相对于强引用弱化一些的引用，可以让对象豁免一些垃圾回收，只有当JVM认为内存不足，才会试图回收软引用指向的对象。JVM会确保抛出OutOfMemoryError之前，清理软引用指向的对象。软引用通常用来实现内存敏感的缓存，

    Weak Reference:弱引用,不能使对象豁免垃圾收集，仅仅能提供一种访问在弱引用状态下对象的途径。维护一种非强制的映射关系

    幻想引用，不能通过它访问对象，幻想引用仅仅是提供了一种确保对象被finalize以后，做某些事情的机制。

    Java定义的不同可达性级别(reachability level):
        Strong Reachable 强可达： 就是当一个对象可以有一个或多个线程可以不通过各种引用访问到的情况
        Softly Reachable:软可达,只能通过软引用才能访问到对象的状态 
        Weakly Reachable:弱可达: 只能通过弱引用访问的状态
        Phantom Reachable: 幻想可达，
        unreachable:不可达: 意味着对象可以被清除
    
    对于软引用、弱引用、垃圾收集可能会存在二次确认的问题，保证处于弱引用状态的对象，没有改变为强引用

    Reference Queue:引用队列:
```
    - String, StringBuffer, StringBuilder?
```
String：典型Immutable类的实现，被声明成为final class.所有属性也都是final.

StringBuffer:可以用append或者add方法，把字符串添加到已有序列的末尾或者指定位置。StringBuffer本质是一个线程安全的可修改字符序列，(线程安全是通过把各种修改数据的方法都加上synchronized关键字实现的) 保证了线程安全。随之带来额外的性能开销，除非有线程安全的需要，不然还是推荐使用后继者，StringBuild.

StringBuilder: 能力上和StringBuffer没有本质区别，唯一缺少线程安全。

“过早优化是万恶之源”，考虑可靠性、正确性和代码可读性才是大多数引用开发最重要的因素
StringBuffer 和 StringBuild底层都是利用可修改的char数组(JDK 9以后是byte数组)，二者都继承AbstractStringBuilder. 里面包含基本操作，区别仅在于最终的方法是否加上symchronized.

数组扩容会产生多重开销，因为要抛弃原有数组，查创建新的数组，还要进行array copy.

$ javac # JAVA编译
$ javap -v # JAVA反编译
JDK8中，字符串拼接操作会自动被javac转换为StringBuilder操作.
JDK9里面因为Java9为更加统一字符串操作优化，提供StringConcatFactory. 作为一个统一的入口

String在Java 6以后提供intern()方法，目的是提示JVM将响应字符串缓存起来，以备重复使用,JVM会将所有类似“abc”这样的文本字符串、或者字符串常量之类缓存起来

Java历史字符串是使用char数组来存储数据，Java中的char是两个bytes大小; Java9中引入Compact Strings设计，对字符串数组存储方式从char数组，改变为一个byte数组加上一个标识编码的所谓coder.
```
    - Java反射机制、动态代理的原理?
```
编程语言中的
    动态类型和静态类型就是区分语言类型信息是在运行时检查还是编译时检查.
    强类型和弱类型就是不同类型变量赋值时，是否需要显式地(强制)进行类型转换

Java语言属于静态强类型语言，但是因为提供类似反射机制，具备了部分动态类型语言的能力

反射机制时Java语言提供的一种基础功能,赋予程序在运行时自省(introspect)的能力，通过反射可以直接操作类或者对象

动态代理是一种方便运行时动态构建代理，动态处理代理方法调用的机制，
```
    - int vs. Integer?
```
Java 语言原始数据类型和包装类
    Java 8个原始数据类型(Primitive Types):
        boolean, byte, short, char, int, float, double, long 
        Boolean, Bytes, Short， Character, Integer, Float, Double, Long, (BigInteger, BigDecimal没有响应的基本类型，主要用于高精度运算)
    
    Integer包装类型中静态工厂方法valueOf会利用缓存机制, 缓存-128-127之间
    自动装箱boxing, Integer.valueOf() 放生在编译阶段，生成的字节码是一致的
    自动拆箱unboxing, Integer.intValue()

    AtomicInteger, AtomicLong 线程安全类
```
    - Vector, ArrayList, LinkedList?
```
Vector, ArrayList, LinkedList都是实现集合框架中的list(有序集合)接口.    
    Vector是Java早期提供的线程安全的动态数组, Vector内部是使用对象数组来保存数据，当数组已满时会创建新的数组，并拷贝原有数组数据 Vector扩容会提高一倍
    ArrayList是应用更加广泛的动态数组实现，线程不安全，ArrayList扩容则增加50%
    LinkedList是Java提供的双向链表,线程不安全

    Vector和ArrayList作为动态数组适合，内部元素以数组形式顺序存储，适合随机访问
    LinkedList，插入+删除比较高效，但是随机访问性能则比动态数组慢 

Collection接口: 
    List有序集合:
        AbstratcList:几种各种List操作的通用部分
    Set不允许重复元素
        TreeSet是利用TreeMap实现
        HashSet是利用HashMap实现
        TreeSet支持自然顺序访问，添加、删除、包含操作比较低效log(n) 
        HashSet利用哈希算法，可以提供常数时间的添加、删除、包含操作，不保证有序
        LinkedHashSet:内部构建一个记录插入顺序的双向链表，提供按照插入顺序便利的能力，
    Queue/Deque: 队列接口 FIFO(First In First Out); LIFO(Last In First Out)

    Java提供的默认排序算法:
        Arrays.sort() 
        Collections.sort() 
        对于原始数据类型，目前使用的是所谓双轴快速排序(Dual-Pivot QuickSort) --改进版快速排序 
        对于对象数据类型，目前使用TimSort() 归并和二分插入排序,

    Java8 之后，Java平台支持Lambda和Stream, 

    java.util.concurrent: 线程安全容器
```
    - Hashtable, HashMap, TreeMap?
```
Hashtable, HashMap, TreeMap常见的一些Map实现，是以键值对的形式存储和操作数据的容器类型
    Hashtable线程安全，不支持null键
    HashMap不是同步的，支持null键和值，HashMap进行put和get操作时间复杂度O(1)
    TreeMap基于红黑树的一种提供顺序访问的Map, get,put,remove操作时间复杂度O(log(n))

    HashMap的性能表现依赖于哈希码的有效性，hashCode和equals的基本约束
        equals相等，hashCode一定相等
        重写hashCode也要重写equals
        hashCode需要保持一致性，状态改变返回的哈希值仍然要一致
        equals的对称、反射、传递等特性
    LinkedHashmap提供遍历顺序符合插入顺序，
    TreeMap顺序是由键的顺序关系决定,通过Comparator或Comparable自然顺序决定

    HashMap源码分析：
        capcity容量 
        load factor:负载系数 
        树化
        HashMap内部结构可以看作数组(Node[] table)和链表结合组合的复合结构,数组被分为一个个桶bucket.哈希值相同的键值对则以链表形式存储，如果链表大小如果超过阀值(TREEIFY_THRESHOLD, 8).链表会被改造为树形结构

        负载因子 * 容量 > 元素数据
```
    - 集合线程安全、ConcurrentHashMap如何实现高效线程安全?
```
Java语言的并发包java.util.concurrent，提供线程安全容器类
    并发容器 ： ConcurrentHashMap, CopyOnWriteArrayList
    线程安全队列(Queue/Deque): ArrayBlockingQueue, SynchronousQueue.
    各种有序容器的线程安全版本

Synchronized Wrapper同步包装器
保证线程安全:synchronize方式、分离锁实现的ConcurrentHashMap,

ConcurrentHashMap vs. Hashmap:
    Hashtable比较低效，实现基本将put,get,size方法加上"synchronized",导致并发操作都要竞争同一把锁，一个线程在进行同步操作，其他线程只能等待，大大降低并发操作的效率. Hashtable和同步包装版本只适合非高度并发的场景下

    ConcurrentHashMap:
        早期ConcurrentHashMap实现:
            分离锁,就是将内部进行分段Segment, 里面则是HashEntry的数组，和HashMap类似，哈希相同的条目也是链表形式存放 
            HashEntry内部使用volatile的value字段来保证可见性,也利用不可变对象的机制以改进利用Unsafe提供的底层能力.
            Segment的数量由concurrentcyLevel决定,默认是16.
        Java 8 版本ConcurrentHashMap操作
            数据存储利用volatile保证可见性 
            使用CAS操作，在特定场景进行无锁并发操作 
            使用Unsafe, LongAdder底层手段进行极端情况的优化

    synchronized比ReentrantLock使用更少的内存消耗
```
    - IO, NIO?
```
    java.io包基于流模型实现，提供一些IO功能: 
        File抽象、输入输出流;交互方式是同步、阻塞的方式
    java.net提供的部分网络API，Socket、ServerSocket、HttpURLConnection也是同步阻塞IO类，因为网络通信同样是IO行为
    java.nio包提供Channel、Selector、Buffer新的抽象，可以构建多路复用、同步非阻塞IO程序；Java7引入AIO(Asynchronous IO)异步非阻塞IO方式,异步IO操作基于事件和回调机制

区分同步/异步(synchronous/asynchronous)：同步是一种可靠的有序运行机制、异步通过事件、回调机制实现任务次序关系
区分阻塞/非阻塞(blocking/non-blocking),进行阻塞操作时，当前线程回处于阻塞状态,非阻塞是不管IO操作是否结束，直接返回，响应操作在后台继续处理
    IO操作包括文件操作和Socket通信
    输入流/输出流(InputStream/OutputStream)用于读取或写入字节，操作图片文件 
    Reader/Writer用于操作字符，增加字符编码等功能
    BufferedOutputStream带有缓冲区的实现，可以避免频繁的磁盘读写，提高IO处理效率，flush 

Java NIO:
    Buffer, 高效的数据容器，除了布尔类型，所有原始数据类型都有相应的Buffer实现
    Channel,类似Linux之类操作系统上看到的文件描述符，是NIO中被用来支持批量式IO操作的一种抽象
        File,Socket比较高层次的抽象，Channel比较系统底层的一种抽象。
    Selector, 是NIO实现多路复用的基础，提供一种高效的机制，可以检测到注册在Selector上的多个Channel是有有Channel处于就绪状态，进而实现单线程对多个Channel的高效管理
    Charset,提供Unicode字符串定义，NIO也提供相应的编解码器

Java语言目前的线程实现比较重量级，启动或者销毁一个线程有明显开销.每个线程都有单独的线程栈等结构，需要占用非常明显的内存;这是同步阻塞方式地扩展性劣势
```
    - Java文件拷贝方式 
```
1. 利用java.io类库,直接为源文件构建一个FileInputStream读取，目标文件构建一个FileOutputStream.
2. 利用java.nio类库,提供transferTo或transferFrom方式实现 

拷贝实现机制分析:
    用户态空间User Space和内核态空间Kernel Space；使用输入输出流进行读写时，实际上时进行多次上下文切换，比如应用读取数据时，现在内核态将数据从磁盘读取到内核缓存，在切换到用户态将数据从内核缓存读取到用户缓存.
    基于NIO transferTo的实现，会使用零拷贝技术，数据传输不需要用户态参与，省去上下文切换的开销和不必要的内存拷贝
    java.nio.file.Files.copy: 

如何提高拷贝IO操作的性能?
    1. 使用缓存机制，减少IO次数 
    2. 使用transferTo机制，减少上下文切换和额外IO操作 
    3. 减少不必要的转换过程，编码解码，对象序列化反序列化，

Buffer：[ByteBuffer, CharBuffer, DoubleBuffer, FloatBuffer, IntBuffer, LongBuffer, ShortBuffer]
    capcity: Buffer，数组的长度 
    position: 要操作的数据起始位置
    limit:操作的限额 
    mark:上一次postion的位置

Direct Buffer: 创建和销毁过程中，都会比一般的堆内Buffer增加部分开销，所以通常都建议用于长期使用、数据较大的场景
MappedByteBuffer: 
垃圾收集过程中，不会主动收集Direct Buffer，显式调用System.gc()强制触发;
JVM堆外内存不仅仅只有Direct Buffer
JDK 8之后，使用Native Memory Tacking(NMT)进行诊断Direct Buffer;
```
    - 接口和抽象类?
```
接口和抽象类时Java面向对象设计的两个基本机制.
    接口是对行为的抽象,是抽象方法的集合,利用接口可以达到API定义和实现分离的目的。接口不能实例化，不能包含任何非常量成员，任何field都是隐含着public static final的意义。只能有抽象方法和静态方法。
    抽象类是不能实例化的类，

Java类实现interface使用implements关键字，继承abstract class则是使用extends关键词.
Java不支持多继承，Java8增加函数式编程的支持,
面向对象编程: SOLID
    单一职责(Single Responsibility): 
throw 抛出异常，throws声明函数抛出异常  
```
    - 设计模式?
```
设计模式是人们为软件开发中相同表征的问题，抽象出的可重复利用的解决方案，在某种程度上，设计模式代表了特定情况的最佳实践.
    1. 创建型模式:是对对象创建过程的各种问题和解决方案的总结
        工厂模式(Factory, Abstract Factory)
        单例模式(Singlton)
        构建器模式(Builder)
        原型模式(protoType)
    2. 结构型模式:对软件设计结构的总结，关注类、对象继承、组合方式的实践经验
        桥接模式(Bridge)
        适配器模式(Adaptor)
        装饰者模式(Decorator)
        代理模式(Proxy)
        组合模式(Composite)
        外观模式(Facade)
        享元模式(Flyweight)
    3. 行为型模式:是对类或对象之间的交互
        策略模式(Strategy)
        解释器模式(Interpreter)
        命令模式(Command)
        观察者模式(Observer)
        迭代器模式(Iterator)
        模版方法模式(Template Method)
        访问者模式(Visitor)

Spring 框架?
    BeanFactory和ApplicationContext应用了工厂模式 
    在Bean的创建中，Spring也为不同scope定义的对象，提供单例和原型等模式实现
    AOP领域是使用了代理模式、装饰器模式、适配器模式
    事件监听，使用观察者模式
    JdbcTemplate应用了模版模式 
```

* 2. Java进阶 
    - synchronized vs. ReentrantLock?
```
synchronized是Java内建的同步机制，Intrinsic Locking.固有锁,提供互斥的语义和可见性.当一个线程已经获取当前锁时，其他试图获取的线程只能等待或阻塞
ReentrantLock是重复锁，再入锁通过代码直接调用lock()方法获取，调用unlock释放

线程安全的定义? <Java Concurrency in Practice>
    线程安全是一个多线程环境下正确性的概念，保证多线程环境下共享的、可修改的状态的正确性
    保证线程安全的两种方法: 
        1. 封装: 通过封装可以将对象内部状态隐藏、保护起来 
        2. 不可变:final, immutable
    线程安全需要保证：
        1. 原子性: 相关操作不会中途被其他线程干扰，可以通过同步机制实现
        2. 可见性: 一个线程修改某个共享变量、其状态能够立即被其他线程知晓，将线程本地状态反映到主内存上，volatile负责保证可见性
        3. 有序性: 保证线程内串行语义，避免指令重排
synchronized: 无法进行公平性的选择，synchronized代码是由一对monitorrenter/monitorexit指令实现，Minitor对象是同步的基本实现单元
    所谓的synchronzied锁的升级、降级就是JVM优化synchronized运行的机制，当JVM检测到不同的竞争状况，会自动切换到适合的锁实现，这种切换就是锁的升级、降级
    JVM提供三种不同的Monitor实现:
        1. 偏斜锁Biased Locking : 没有竞争出现，默认使用偏斜锁,JVM利用CAS(Compare and Swap)在对象头上Mark word部分设置线程ID。表示对象偏向于当前线程
        2. 轻量级锁 : 当另外线程试图锁定某个已经被偏斜过的对象,JVM需要撤销revoke偏斜锁,切换到轻量级锁实现,轻量级锁依赖CAS操作Mark Word试图获取锁，如果成功就使用普通轻量级锁，否则进入重量级锁
        3. 重量级锁: 
    锁的降级当JVM进入安全点(SafePoint)时候，会检查是否有闲置的Monitor，然后试图进行降级 
    synchronized是JVM内部的Intrinsic Lock,偏斜锁、轻量级锁、重量级锁的实现不再核心类库，而是在JVM代码中
    ReentrantReadWriteLock: 读写锁实现
    StampedLock:提供读写锁的同时还支持优化读模式。优化读基于假设，大多数情况下操作并不会和写操作冲突，其逻辑是先试着修改，然后通过validate方法确认是否进入写模式，如果没有进入，就成功避免开销，如果进入，则尝试获取读锁

ReentrantLock: 再入锁：表示当一个线程试图获取一个他已经获取的锁时，这个获取动作就自动成功，这是对锁获取粒度的一个概念，就是锁的持有是以线程为单位而不是基于调用次数。
    ReentrantLock fairlock = new ReentrantLock(true);   // 再入锁设置公平性 fairness 
    公平性是指在竞争场景中，当公平性为真时，会倾向于将锁赋予等待时间最久的线程，公平性时减少线程“饥饿”.
自旋锁(spin-wait, busy-waiting):
```
    - 线程的声明周期和状态切换
```
Java线程不允许启动两次，第二次start()调用会抛出java.lang.IllegalThreadStateException,运行时异常，多次调用被认为是编译错误.
java.lang.Thread.State: 枚举类型
    NEW: 新建表示线程被创建出来还没有真正启动的状态,可以认为是Java内部状态 
    RUNNABLE:就绪，表示线程已经在JVM中执行，在就绪队列中排队等待分配计算资源 
    RUNNING:
    BLOCKED:阻塞，阻塞表示线程在等待Monitor lock
    WAITING：等待,表示正在等待其他线程采取操作，Thread.join()会让线程进入等待状态
    TIMED_WAIT:计时等待 public final native void wait(long timeout) throws InterruptedException; 
    TERMINATED:终止，

线程是操作系统调度的最小单元,一个进程可以包含多个线程，作为任务的真正运作者，有自己的栈Stack,寄存器Register,本地存储Thread Local.会和进程内其他线程共享文件描述符、虚拟地址空间
线程分为内核线程、用户线程: Java 1.2之后JDK已经抛弃所谓的Green Thread(用户调度的线程) 现在的模型是一对一映射到操作系统内核线程
线程中的yield是告诉调度器，主动让出CPU.
基类Object提供一些基础wait/notify/notifyAll方法，
并发类库中，CountDownLatch.await()会让当前线程进入等待状态，知道latch被基数为0，可以看作线程间通信的Signal.
ThreadLocal:Java提供的一种保存线程私有信息的机制，在整个线程声明周期内有效。
```
    - 死锁
```
死锁是一种特定的程序状态,指两个或多个线程之间，由于相互持有对方需要的锁，而永久处于阻塞的状态
定位死锁常使用jstack工具获取线程栈,然后定义相互之间的依赖关系。JConsole可以在通行界面进行有限的死锁检测
线程调度依赖于操作系统调度器，可以通过优先级进行影响但是具体是不确定

首先使用jps或ps确定进程ID (jps - Monitoring Tools)
然后调用jstack获取线程栈 $ jstack your_pid
FindBugs: 静态代码分析
```
    - Java并发包工具类 
```
java.util.concurrent包 
    1.提供比synchronized更加高级的各种同步结构, 
        CountDownLatch(倒计时锁存器): 不可重置，无法重用，countDown/await; CountDownLatch操作的是事件
        CyclicBarrier(循环屏障):可以重用， await, 当所有都调用await，才会继续进行任务，并自动进行重置
        Semaphore(信号量): 通过控制一定数量的允许(permit)的方式，来达到限制通用资源访问的目的
    2.各种线程安全的容器: 
        ConcurrentHashMap: 侧重放入或者获取速度，不在乎顺序
        ConcurrentSkipListMap: 大量数据非常频繁的修改，(O(nlogn))
        CopyOnWriteArrayList:  
        CopyOnWriteArraySet:是通过包装CopyOnWriteArrayList实现的
        CopyOnWrite: 任何修改操作(add, set, remove)都会拷贝原数据，修改后替换原来的数据 - 这种数据结构适合读多写少的操作
    3.各种并发队列实现: ArrayBlockingQueue, SynchronousQueue, PriorityBlockingQueue 
    4.Executor框架,可以创建各种不同类型的线程池，调度任务运行
```
    - ConcurrentLinkedQueue vs. LinkedBlockingQueue 
```
Concurrent类型基于lock-free,在常见的多线程访问场景，一般可以提供较高吞吐量
LinkedBlockingQueue内部则基于锁，并提供BlockingQueue等待性方法
java.util.concurrent包提供的容器(Queue, List, Set)、Map从名称区分为
    Concurrent: 没有类似CopyOnWrite容器相对较重的修改开销;提供较低的遍历一致性
    CopyOnWrite: 
    Blocking
Deque: 支持对队列头尾进行插入和删除
    尾部插入: addLast(e), offerLast(e)
    尾部删除: removeLast(), pollLast()
    ConcurrentLinkedDeque:基于CAS无锁技术，不需要在每次操作时候使用锁，所以扩展性表现更优异
    LinkedBlockingDeque
ArrayBlockingQueue:是最典型的有界队列,内部final数组保存数据，数组的大小决定队列的边界,
LinkedBlockingQueue:容易被误解为无边界，其实行为和内部代码都是基于有界的逻辑实现，只不过我们没有在创建队列时指定容量，那么容量限制自动被设置为Integer.MAX_VALUE.成为无界队列
SynchronousQueue:每个删除操作都要等待插入操作，每个插入操作都要等待删除操作，内部容量是0, 是Executors.newCachedThreadPool()的默认队列
PriorityBlockingQueue:无边界的优先队列，
DelayedQueue和LinkedTransferQueue:无边界队列，put操作不会出现BlockingQueu那种等待情况

Queue被广泛使用在生产者-消费者场景
ArrayBlockingQueue要比LinkedBlockingQueue空间利用率要紧凑，不需要创建所谓节点，初始化分配阶段需要一段连续的空间，所以初始化内存需求比较大
LinkedBlockingQueue吞吐量优于ArrayBlockingQueue,因为实现更加细粒度的锁操作 
ArrayBlockingQueue实现比较简单，性能更好预测，表现稳定
```
    - Java并发类库中线程池有哪些?
```
线程是不能够重复启用，创建和销毁线程存在一定的开销，可以利用线程池技术来提高系统资源利用率，并简化线程管理
Executors目前提供5种不同的线程池创建配置
    newCachedThreadPool(): 用于处理大量短时间工作任务的线程池，会试图缓存线程并重用，当无缓存线程可用时，就会创建新的工作线程,如果线程闲置的时间超过60秒，则被终止并移出缓存，长时间闲置时，这种线程池不会消耗资源，内部使用SynchronousQueue作为工作队列.
    newFixedThreadPool(int nThreads): 重用指定数目nThreads的线程，使用的无界的工作队列，任何时候最多有nThreads工作线程是活跃的，使用LinkedBlockingQueue.
    newSingleThreadExecutor(): 工作线程数目限制为1，操作一个无界的工作队列，保证所有任务都是被顺序执行，最多会有一个任务处于活动状态，并且不允许使用者更改线程池实例
    newSingleThreadScheduledExecutor() vs. newScheduledThreadPool(int corePoolSize): 创建一个ScheduledExecutorService,可以进行定时或周期行的工作调度，区别在于单一工作线程还是多个工作线程.
    newWorkStealingPool(int parallelism): Java8加入，内部构建ForkJoinPool,利用Work-Stealing算法，并行处理任务，不保证处理顺序

ThreadPoolExecutor: 
ScheduledThreadPoolExecutor: 是ThreadPoolExecutor的扩展，主要增加了调度逻辑
ForkJoinPool: 是为ForkJoinTask定制的线程池，

应用于线程池交互和线程池内部工作过程
    应用 --> [提交新任务 execute()/submit()] --> 工作队列 --> [WorkerThread...] 工作线程管理(ThreadFactory) 
线程池需要在运行过程中管理线程创建、销毁
    corePoolSize: 核心线程数
    maximumPoolSize: 线程不够时能够创建的最大线程数
    keepAliveTime TimeUnit: 指定额外的线程能够闲置多久
    workQueue: 工作队列，必须是BlockingQueue.

线程池容易出现的问题:
    1. 避免任务堆积: newFixedThreadPool是创建指定数目的线程，但是工作队列是无界，如果工作线程数目太少，导致处理更不上入队的速度，很有可能占用大量的系统内存，甚至出现OOM，诊断可以使用jmap工具，查看是否有大量的任务对象入队
    2. 避免过度扩展线程: jstack工具检查当前线程，避免死锁。尽量避免使用线程池时操作ThreadLocal
如果线程任务主要进行CPU密集型计算,通常建议按照CPU核数目N或者N+1
如果较多的IO操作较多，可以参考Brain Goetz推荐
    线程数 = CPU核心数 * （1 + 平均等待时间/平均工作时间）
```
    - AtomicInteger CAS
```
AtomicInteger是对int类型的封装,提供原子性的访问和更新操作，其原子性的实现是基于CAS(compare-and-swap)技术
CAS(Compare and swap): 利用CAS指令进行更新，如果当前数值未变，代表没有其他线程进行并发修改，则成功更新，否则可能进行重试或者返回失败结果
CAS是Java并发中所谓lock-free机制的基础
atomic包提供最常用的原子性数据类型，甚至是引用、数组等相关原子类型和更新操作工具,是很多线程安全程序的首选
AQS(AbstractQueuedSynchronized) : 
```
    - 类加载过程 
```
Java通过引入字节码和JVM机制，提供强大的跨平台能力
Java类加载过程:
    1. 加载(loading)阶段:是Java将字节码数据从不同的数据源(jar文件、class文件、网络数据源)读取到JVM中，并映射为JVM认可的数据结构(Class 对象);如果输入的数据不是ClassFile的结构，则会抛出ClassFormatError 
    2. 链接(Linking)阶段: 
        2.1: 验证(Verification): JVM需要验证字节信息符合Java虚拟机规范;防止恶意信息或者不合规的信息危害JVM运行,验证阶段可能触发更多class的加载
        2.2: 准备(Preparation): 创建类或接口中的静态变量，并初始化静态变量的初始值。分配所需要的内存空间，不去执行更进一步的JVM指令
        2.3: 解析(Resolution): 将常量池中的符号引用symbolic reference替换为直接引用.
    3. 初始化(Initialization)阶段: 直接执行类初始化的代码逻辑，包括静态字段赋值动作,以及执行类定义中的静态初始化内的逻辑，

双亲委派模型:当类加载器(Class-Loader)试图加载某个类型的时候，除非父加载器找不到响应类型，否则尽量将这个任务代理给当前加载器的父加载器去做，使用委派模型的目的是避免重复加载Java类型
```

* 3. Java应用开发扩展
```
```

* 4. Java安全基础 
```
```

* 5. Java性能基础
```
```

```
CAS: Compare and swap:比较并交换


```