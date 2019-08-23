Introduction to Golang
======================
```
Creators:
    Robert Griesemar、Rob Pike、Ken Thompson

Why a New Language?
    Python + Java + C/C++ 
    Python: Easy to use, but slow 
    Java: Increasingly complex type system
    C/C++: Complex type system Slow compile times
    Go: Concurrency

Go (golang)
    Strong and statically typed 
    Excellent community 
    Key features
        Simplicity 
        Fast compile times 
        Garbage collected 垃圾回收机制
        Built-in concurrency 原生并发编程(goroutine, channel, go)
        Compile to standalone binaries 
    Go本身是由Go语言编写、静态类型和编译型、跨平台、完善的构建工具:获取、编译、测试、安装、运行、分析
    Go支持多编程范式：函数式编程、面向对象编程，有接口类型和实现类型的概念，使用嵌入替代继承
    代码风格强制统一、丰富的标准库

https://golang.org
https://golang.org/doc/
https://golang.org/doc/effective_go.html 
https://golang.org/pkg/
https://golang.org/project/
https://golang.org/help/
https://golangbridge.org/
https://play.golang.org/ -- The Go Playground 
```

Install Golang on MacOS With Homebrew!
--------------------------------------
```
Installing Go via the Terminal 
$ brew install go 

go 语言相关文件
.
├── CONTRIBUTING.md
├── CONTRIBUTORS
├── PATENTS
├── VERSION
├── api                 --  用于存放Go版本顺序的API增量列表文件， 用于Go语言API检查
├── bin                 --  用于存放主要的标准命令文件，包含go, godoc, gofmt 
├── doc                 --  存放标准的HTML格式的程序文档，可以通过godoc命令启动Web程序展示文档
├── favicon.ico
├── lib                 --  存放特殊的库文件
├── misc                --  存放辅助类的说明和工具
├── pkg                 --  存放Go标准库后的所有归档文件
├── robots.txt
├── src                 -- 存放Go自身、Go标准工具以及标准库的所有源代码文件
└── test                -- 检测和验证Go本身的所有相关文件

8 directories, 6 files

Setup the GOPATH environment variable
$ vim ~/.zshrc 
# Keep in mind that $HOME is equal to "~" AKA /Users/your_username. 
First of all export some paths, and save them in your .zshrc or .bashrc files for easy use. Use sudo if you get error.
# Go development 
# Set variables in .zshrc file
# don't forget to set path correctly!
export GOPATH=$HOME/golang
export GOROOT="$(brew --prefix golang)/libexec"
export PATH=$PATH:$GOPATH/bin:$GOROOT/bin
$ test -d "${GOPATH}" || mkdir "${GOPATH}"
$ test -d "${GOPATH}/src/github.com" || mkdir -p "${GOPATH}/src/github.com"

# Also a bunch of dev tools!
$ go get golang.org/x/tools/cmd/godoc 
$ go get github.com/golang/lint/golint 

Setting up the VS Code text editor for Go 
Open VS Code via spotlight. Press Command + Space and type "VS Code" then press enter 
When VS Code opens, press command + shift + p and type "shell".
"Shell Command: Install 'code' command in PATH"
Click "Auto Save" in the file dropdown at the top of the screen. 

Go 工程结构
    工作区: 一般情况下，Go源码文件必须放在工作区中，但是对于命令源码文件来讲不是必须的
        src目录 -- 用于以代码包的形式组织保存Go源码文件
        pkg目录 -- 用于存放通过go install 命令安装后的代码包的归档文件
        bin目录 -- 用于存放通过go install 命令安装后保存Go命令源码文件生成的可执行文件

        命令源码文件: 就是声明属于main代码包并且包含无参数声明和结果声明的main函数的源码文件
        库源码文件: 存在于某个代码包中的普通源码文件.
        测试源码文件: 可以通过执行go test命令运行当前代码包下的所有测试源码文件
            测试源码文件需要：
                文件名以"_test.go"结尾 
                文件中需要至少包含一个名称以Test开头或Benchmark开头，且拥有一个类型为*testing.T或*testing.B的参数的函数，testing.T和testing.B是两个结构体类型，而*testing.T和*testing.B分别为前两者的指针类型，分别是功能测试和基准测试所需要.

代码包
    Go源码文件都必须以包声明语句作为文件中代码的第一行. package main
    Go源码文件导入语句. import 
    Go源码文件标识符可以是Unicode字符集中任意能表示自然语言文字的字符、数字以及下划线。标识符不能以数字或下划线开头.标识符的首字符的大小写控制对应程序实体的访问权限。

包初始化
    Go会在程序真正执行前对整个程序的依赖进行分析，并初始化相关的代码包，所有代码包初始化函数都会在main函数执行前执行完毕。当前代码包中所有全局变量的初始化会在代码包初始化函数执行前完成. 同一个代码包中可以存在多个代码包初始化函数，甚至代码包内的每一个源码文件都可以定义多个代码包初始化函数。Go不会保证每一个代码包中多个代码初始化函数的执行顺序。
```

Go Running 
----------
```
go build        -- 编译代码包或源码文件
go clean        -- 清除因执行其他go命令而遗留下来的临时目录和文件
go doc          -- 现实Go语言代码包以及程序实体的文档
go env          -- 打印Go语言相关的环境信息
go fix          -- 用于修正制定代码包的源码文件中包含的过时语法和代码调用
go fmt          -- 格式化制定代码中Go源码文件
go generate     -- 识别制定代码包中源码文件中的go:generate注释
go get          -- 下载、编译并安装指定的代码包及其依赖包
go install      -- 用于编译并安装指定的代码包及其依赖包
go list         -- 现实指定代码包的信息
go run          -- 编译并运行指定的命令源码文件
go test         -- 测试指定的代码包
go tool         -- 运行Go语言的特殊工具
    proof : 用以交互方式访问一些性能概要文件: 概要文件CPU概要文件、内存概要文件、程序阻塞概要文件
    trace : 读取Go程序踪迹文件，并以图形化的方式展示出来。
go vet          -- 检查指定代码包中的Go语言源码,报告可以代码问题
go version      -- 显示当前安装的Go语言的版本信息以及计算环境

-a : 强行重新编译所有Go语言代码包
-n : 使命令仅打印执行过程中用到的所有命令，而不是真正执行，如果只想查看或验证命令的执行过程，而不想改变任何东西
-race : 检测并报告指定Go语言程序中存在的数据竞争问题
-v : 打印命令执行过程中涉及的代码包
-work : 打印命令执行时生成和使用的临时工作目录的名字,且命令执行完成后不删除
-x : 打印执行过程中用到的所有命令，同时执行
```

Go Fundation
------------
> Go 语言符号共包括5类内容--标识符(identifier)、关键字(keyword)、字面量(literal)、分隔符(delimiter)、操作符(operator)
```
identifier: 标识符
    _ = x 空标识符

keyword: 关键字
    程序声明关键字> import、package 
    程序实体声明定义> chan、const、func、interface、map、struct、type、var 
    程序流程控制> go、select、break、case、continue、default、defer、else、fallthrough、for、goto、if、range、return、switch
    
    关键字type:类型声明
        type myString string 
    在Go语言中，任何类型都是空接口类型的实现类型

literal: 字面量

operator: 操作符
    Go操作符分为5类：算数操作符、比较操作符、逻辑操作符、地址操作符、接收操作符
    || 逻辑或操作，二元操作符
    |  按位或操作,二元操作符
    ^  按位异或操作
    << 按位左移
    >> 按位右移
    &^ 按位清除操作 ????
    ! 逻辑非操作,一元操作符
    <- 接收操作,一元操作符
    && 逻辑与操作，二元操作符
    ++\--是语句而不是表达式

表达式:
    选择表达式: 选择一个值中的字段或方法 context.Speaker // content是变量名
    索引表达式: 选取数组、切片、字符串或字典值中的某个元素 // array1[1] // array1表示一个数组值
    切片表达式: 选取数组、数组指针、切片或字符串中的某个范围的元素 slice[0:2] // slice表示切片值
    类型断言: 判断一个接口值的实际类型是否位某个类型 
    调用表达式: 调用一个函数或一个值的方法

关键字var,在一条语句中同时位多个变量赋值的方式叫平行赋值
    
```
* Variables (type value address)
    - Type -> What kind of information can be stored inside the variable 
    - Value -> The stored value inside the variable.
    - Address -> Where the variable can be found in computer memory 
```
# If declare a variable without a value, the  it'll have a zero-value depending on the type of the variable.
    zero-values 
    booleans    ->  false 
    float       ->  0.0 
    integers    ->  0 
    strings     ->  "" 

# Long Declaration [declare name type = value]
    =  assigning values
# Short Declaration [name := value]
    := declare and assign 
# type-inferring 
# Multiple declarations [declare name type = value name2 type, name3 type = value2, value3]
# Multiple short declaration [name, name2 := value, value2]

Can't redeclare variables, but can shadow them.
All variables must be used 

Use a long declaration when you can't know what data to store beforehand, otherwise, use a short declaration. 
Use the multiple declarations when you want to define multiple variables together or as a hint for code readability that the variables will be used together.

Can't use short declarations outside of functions including the main function. Or: you will meet with this error: "syntax error: non-declaration statement outside function body". Not good.

# Making a variable accessible to other packages 
This is called exporting. To define a variable in the package scope, you can only use a long declaration or a multiple declaration. After that, you need to capitalize its first letter.

# Visibility 
    lower case first letter for package scope 
    upper case first letter to export 
    no private scope 

# Naming conventions 
    Pascal or camelCase 
        Capitalize acronyms (HTTP, URL)
    As short as reasonable 
        longer names for longer lives 

# type conversions 
    destination Type (variable)
    use strconv package for strings 
```

* PRIMITIVES:基本类型
```
    - Boolean type 
        * values are true and false 
        * not an lias for other types 
        * zero value is false 
    - Arithmetic operations 
        * Addition 
        * Subtraction 
        * Multiplication 
        * Division 
        * Remainder 
    - Bitwise operations 
        * And 
        * Or 
        * Xor 
        * Not 
    - Numeric types 
        * Integers (Signed integers, Unsigned integers)
            - int8:     -128 ~ 127 
            - uint8:    0   ~ 255 
            - byte: 可以看作类型uint8的别名类型
            - int16     -32768 ~ 32767
            - uint16    0   ~ 65535 
            - int32     -2147483648 ~ 2147483647 
            - rune: 存储Unicode字符，由32位二进制数表示的有符号整数类型,可以看作int32的别名类型
            - uint32    0   - 4294967295 
            - int64     -9223372036854775808 - 9223372036854775807 
        * Floating point 
            - Follow IEEE-754 standard 
            - Zero value is 0 
            - 32 and 64 bit version 
            - Literal styles 
                * Deciaml (3.14)
                * Exponential (13e18 or 2E10)
                * Mixed (13.7e12)
        * Complex numbers 
            - Zero value is (0+0i)
            - 64 and 128 bit versions 
            - complex - make complex number from two floats 
            - real - get real part as float 
            - imag - get imaginary part as float 
    - Text types 
        * String 
            - UTF-8 
            - Immutable : 不可变，一旦创建、其内容就不可改变
            - Can be concatenated with plus (+) operator 
            - Can be converted to []byte 
            - 字符串的字面量有两种表示形式: [1. 原生字符串字面量(由反引号"`"包裹), 2. 解释型字符串字面量(由双引号"包裹)]
        * Rune 
            - UTF-32 
            - Alias for int32 
            - Special methods normally required to process 
```     

* CONSTANTS
```
    - Immutable, but can be shadowed 
    - Replaced by the compiler at compile time 
        * Value must be calculable at compile time 
    - Naming convention 
        * PascalCase for exported constants 
        * camelCase for internal constans 
    - Typed constants work like immutable variables 
        * can interoperate only with same type 
    - Untyped constants 
        * Can interoperate with similar types 
    - Enumerated constants 
        * Special symbol itoa allows related constants to be created easily 
        * Itoa starts at 0 in each const block and increments by one
        * Watch out of constant values that match zero values for variables 
    - Enumeration expressions 
        * Operations that can be determined at compile time are allowed 
        * Arithmetic 
        * Bitwise operations 
        * Bitshifting 

itoa: Elegant Constants in Golang 
Golang is to use the itoa identifier, which simplifies constant definitions that use incrementing numbers, giving the categories exactly the same values as above.
```

* ARRAYS AND SLICES 
```
    - Arrays 
        * Collection of items with same type 
        * Fixed size 
        * Declaration styles 
            - a := [3]int{1, 2, 3}
            - a := [...]int{1, 2, 3}
            - var a [3]int 
        * access via zero-based index 
            - a := [3]int {1, 3, 5} // a[1] == 3 
        * len function returns size of array 
        * Copies refer to different underlying data 
    - Slices 
        * Backed by array 
        * 切片的类型字面值([]string)并不携带长度信息，切片的长度是可变的。切片值相当于对于底层数组的引用
        * Creation styles 
            - Slice existing array or slice 
            - Literal style 
            - Via make function  用于初始化切片、字典或通道类型的值
                * a := make([]int, 10)  // create slice with capacity and length == 10 
                * a := make([]int, 10, 100) // slice with length == 10 and capacity == 100 
        * len function returns length of slice 
        * cap function returns length of underlying array 
        * append function to add elements to slice 
            - May cause expensive copy operation if underlying array is too small 
        * Copies refer to same underlying array 
```

* MAPS AND STRUCTS 
```
    - Maps
        * Go中字典类型是散列表hash table的实现,散列表是一个实现关联数组的数据结构,关联数组是用于表示健值对的无序集合的一种抽象数据类型.
        * 字典类型是一个引用类型,字典类型的零值为nil.
    - Structs 
        * 结构体类型属于值类型. 
```

* 流程控制
```
没有do和while循环，只有一个更广义的for语句
switch语句灵活多变，还可以用于类型判断
if语句和switch语句都可以包含一条初始子语句
break语句和continue语句可以后跟一个标签label语句，已标识需要终止或继续的代码块
defer语句可以使我们更方便地执行异常捕获和资源回收任务
select语句用于多分枝选择，但只与通道配合使用
go语句用于异步启动goroutine并执行指定函数
```

* 代码块和代码包
```
代码块就是一个由花括号包裹的表达式和语句的序列
    所有Go代码形成一个最大的代码块：全域代码块
    每个代码块中的代码共同组成一个代码块：代码包代码块
    每一个源码文件都是一个代码块：源码文件代码块
    每一个if、for、switch、select语句都是一个代码块
    每一个在switch或select语句中的case分支都是一个代码块

作用域
    一个预定义标识符的作用域是全域代码块

```

* FUNC AND METHODS
```
    - func
        * Go中，函数类型是一等类型,意味着可以把函数当作一个值来传递和使用
        * 函数声明通常包括关键字func, 函数名,分别由圆括号的参数列表和结果列表，以及由花括号包裹的函数体
            - func divide(dividend int, divisor int) (int, error) {省略部分代码}
    - 值方法和指针方法
        * 值方法：
        * 指针方法: 
        * 内建函数new的功能是创建一个指定类型的值,并返回指向该值的指针.
```

* STD PACKAGES
```
errors: 一个标准库代码包的名称
    errors.New("division by zero")  // 专用于生成error类型的值
```
