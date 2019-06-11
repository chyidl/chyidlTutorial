JVM, JRE, JDK
=============
```
JRE stands for "Java Runtime Environment". The Java Runtime Environment provides the minimum requirements for executing a Java application; it consists of the Java Virtual Machine (JVM), core classes, and supporting files.

JDK stands for "Java Development Kit". The Java Development Kit provides development environment used for developing Java applications and applets. It includes the Java Runtime Environment (JRE), and interpreter/loader (Java), a compiler (javac), an archiver(jar), a documentation generator(Javadoc) and other tools needed in Java development.

JVM standas for "Java Virtual Machine". JVM is responsible for executing the java program line by line hence it is also known as interpreter.

HotSpot is the open-source Java VM implementation by Oracle.
Java虚拟机(JDK中的HotSpot)优势:
    1. 一次编写，到处运行
    2. 虚拟机提供一个托管环境(Managed Runtime),提供自动内存管理与垃圾回收，数组越界，动态类型，安全权限等动态检测

HotSpot: 内置多个即时编译器 C1(Client), C2(Server):
    C1: Client 编译器，面向的是对启动性能有要求的客户端GUI程序
    C2: Server 编译器，面向的是对峰值性能有要求的服务端程序，

Java7以后, HotSpot默认采用分层编译方式，热点方法首先会被C1编译，而后热点方法中的热点会进一步被C2编译。
```
