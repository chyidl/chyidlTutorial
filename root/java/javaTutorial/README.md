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

Java 修饰符
-----------
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
    NoClassDefFoundError和ClassNotFoundException区别?
        ...
    try-catch-finally, throw, throws
    try-with-resources, multiple catch. 
        try (BufferedReader br = new BufferedReader(...); BufferedWriter writer = new BufferedWriter())
```             

* 2. Java进阶
```
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
