C & C++ Tutorial 
================

C Programming Language 
----------------------

C++ Programming Language 
------------------------

* A Simple C++ Project Structure
```
# The Project Folder Tree 

bin: The output executables go here, both for the app and for any tests and spikes. 
build: This folder contains all object files, and is removed on a clean 
doc: Any notes, like my assembly notes and configuration files, are here. 
include: All project headers files. All necessary third-aprty headers files that do not exists under /usr/local/include are also placed here 
lib: Any libs that get compiled by the project, thierd party or any need in developement. 
spike: I often write smaller classes or files to test technologies or ideas, and keep them around for future reference. They go here, where they do not dilute the real application's files, but can still be found later.
src: The application and only the application's source files 
test: All test code files. 

.gitignore:

Since I use git for source code control, the .gitignore files is :
    # Ignore the build and lib dirs 
    build 
    lib/*

    # Ignore any executables
    bin/*

    # Ignore Mac specific files 
    .DS_Store 

Generic Makefile 
    
    #
    # TODO: Move `libmongoclient.a` to /usr/local/lib so this can work on production servers 
    # 

    CC := g++ # This is the main compiler 
    # CC := clang --analuze # and comment out the linker last line for sanity 
    SRCDIR := src
    BUILDDIR := build 
    TARGET := bin/runner 

    SRCEXT := cpp 
    SOURCES := $(shell find $(SRCDIR) -type f -name *.$(SRCEXT))
    OBJECTS := $(patsubst $(SRCDIR)/%,$(BUILDDIR)/%,$(SOURCES:/$(SRCEXT)=.o))
    CFLAGS := -g # -Wall 
    LIB := -pthread -lmongoclient -L lib -lboost_thread-mt -lboost_filesystem-mt -lboost_system-mt
    INC := -I include 

    $(TARGET): $(OBJECTS)
        @echo " Linking... "
        @echo " $(CC) $^ -o $(TARGET) $(LIB)"; $(CC) $^ -o $(TARGET) $(LIB)

    $(BUILDDIR)/%.o: $(SRCDIR)/%.$(SRCEXT)
        @mkdir -p $(BUILDDIR)
        @echo " $(CC) $(CFLAGS) $(INC) -c -o $@ $<"; $(CC) $(CFLAGS) $(INC) -c -o $@ $<

    clean:
        @echo " cleaning... "
        @echo " $(RM) -r $(BUILDDIR) $(TARGET)"; $(RM) -r $(BUILDDIR) $(TARGET)

    # Tests
    tester:
        $(CC) $(CFLAGS) test/tester.cpp $(INC) $(LIB) -o bin/tester 

    # Spikes 
    ticket:
        $(CC) $(CFLAGS) spikes/ticket.cpp $(INC) $(LIB) -o bin/ticket 

    .PHONY: clean
```

* Basic 
```
C++ 是一门多范式(支持面向对象编程、面向过程编程、泛型编程、函数式编程)的通用编程语言  
C++应用场景:
    - 大型桌面应用程序: Adobe Photoshop, Google Chrome, Microsoft Office 
    - 大型网站后台: Google搜索引擎
    - 游戏: StarCraft、Unreal、Unity 
    - 编译器: LLVM/Clang 和 GCC 
    - 解释器: JVM, V8 
    - 视觉引擎: OpenCV, TensorFlow 
    - 数据库: Microsoft SQL Server, MySQL, MongoDB 

Rust, C++: 支持高度抽象、高性能的通用编程语言
运算密集型或者内存密集型: 
C++中,所有的变量缺省都是值语义

alias g++="g++ -std=c++17 -W -Wall -Wfatal-errors " 
alias clang++="clang++ -std=c++17 -W -Wall -Wfatal-errors "

# 堆、栈、RAII - C++内存管理
    堆(heap): 动态分配内存的区域,需要手工释放，否则会造成内存泄漏 
        下面代码都会导致在堆上分配内存(并构建对象)
        堆上分配内存，需要涉及三个可能的内存管理器操作:
            1. 内存管理器分配一个某个大小的内存块

            2. 内存管理器释放一个之前分配的内存块
                不仅仅简单把内存标记为未使用，连续未使用的内存块需要合并

            3. 内存管理器进行垃圾收集操作，寻找不再使用的内存块并释放

            // C++ - 会做上面操作(1,2)
            auto ptr = new std::vector<int>(); 
            // Java - 会做上面操作(1,3)
            ArrayList<int> list = new ArrayList<int>();
            // Python - 会做上面操作(1,2,3)
            lst = list()
    自由存储区(free store): 使用new和delete来分配和释放内存的区域，这是堆的子集
        - new和delete操作的区域是free store (底层使用malloc和free实现)
        - malloc和free操作的区域是heap
    
    栈(stack): 函数调用过程中产生的本地变量和调用数据的区域，后进先出(Last-in-first-out LIFO)
        x86计算机体系架构中，栈的增长方向是低地址，本地变量的内存在栈上
        栈上的内存分配简单，移动栈指针；栈上的内存释放简单，由于后进先出的执行过程，不可能出现内存碎片
        栈帧(stack frame): 单一函数占用的栈空间
        C++中的简单类型，POD(Plain Old Data);
        对于有构造函数和析构函数的非POD类型，栈上的内存分配C++编译器会在生成代码的合适位置，插入对构造和析构函数的调用.
        编译器自动调用析构函数，包括栈函数执行发生异常情况
        栈展开(stack unwinding): 异常时对析构函数的调用

    RAII(Resource Acquisition Is Initialization): C++是唯一一个依赖RAII来做资源管理
        RAII依托栈和析构函数，对所有的资源--包括堆内存在内进行管理.RAII的存在也是垃圾收集器虽然理论上可以在C++使用，但从来没有真正流行过的主要原因
        C++支持将对象存储在栈上面

C++智能指针
    
```

* Advance
```
```

* Practical 
```
```

* Future 
```
```