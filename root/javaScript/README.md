JavaScript 教程
===============

导论
----
```
JavaScript 是一种轻量级的脚本语言。所谓“脚本语言",指的是不具备开发操作系统的能力，而是只用来编写控制其他大型应用程序(比如浏览器)的“脚本”.

JavaScript是一种嵌入式(embedded)语言，本身提供的核心语法不算很多，只能用来做一些数学和逻辑运算。JavaScript本身不提供任何与I/O相关的API，都要靠宿主环境提供，所以JavaScript只适合嵌入更大型应用程序环境，去调用宿主环境提供的底层API。

目前嵌入JavaScript宿主环境有多种，最常见的环境就是浏览器，另外还有服务器环境Node项目.

JavaScript语言是一种“对象模型”语言，各种宿主环境通过对象模型描述自己的功能和操作接口，从而通过JavaScript控制这些功能，但是，JavaScript并不是纯粹的面向对象语言，还支持函数式编程，

JavaScript 核心语法相当精简，指包括两部分：基本语法构造(操作符、控制结构、语句)和标准库(Array,Date,Math)各种宿主环境提供的API（只能在该环境使用的接口）
    浏览器提供的API：
        1. 浏览器控制类：操作浏览器
        2. DOM类：操作网页的各种元素
        3. Web类：实现互联网的各种功能
    操作系统提供的API：
        操作系统API：文件操作API，网络通信API

JavaSCript作为浏览器的内置脚本语言，为网页开发者提供操控浏览器的能力。
    浏览器的平台化：
    Node项目：使得JavaScript可以用于开发服务器端的大型项目，网站前后端都用JavaScript开发已经成为现实.
    数据库操作:NoSQL数据库概念本身就是在JSON（JavaScript Object Notation）格式的基础上诞生，大部分NoSQL数据库允许JavaScript直接操作，基于SQL语言的开源数据库PostgreSQL支持JavaScript作为操作语言，可以部分取代SQL查询语言.
    移动平台开发:JavaScript开始成为手机应用的开发语言，安卓平台使用Java语言Kolin, iOS平台使用Object-C或swift语言开发，JavaScript成为各个平台的通用开发语言.
        PhoneGap项目将JavaScript和HTML5打包在一个容器之中，使得同时在iOS和安卓上运行，Facebook公司的ReactNative项目将JavaScript写的组件，编译成原生组件，从而具备优秀的性能.Mozila基金会的手机操作系统Firefox OS,直接将JavaScript作为操作系统的平台语言。
    内嵌脚本语言: 越来越多的应用程序将JavaScript作为内嵌的脚本语言.
    跨平台的桌面应用程序: Chromium OS, windows 8操作系统直接支持JavaScript编写应用程序，Mozila的Open Web Apps项目，Google的Chrome App项目，gitHub的Electron项目，以及TideSDK项目都可以用来编写运行与Windows,MacOS,android桌面平台的程序，不依赖浏览器

    "Any application that can be written in JavaScript will eventually be written in JavaScript" -- Jeff Atwood.

JavaScript的性能优势：
    1. 灵活的语法、表达力强：JavaScript支持类似C语言的过程式编程、也支持灵活的函数式编程。可以写并发处理(concurrent),这些语法特性被证明适用异步编程.
    2.支持编译运行：JavaScript语言本身虽然是一种解释性语言，但是在现代浏览器中，JavaScirpt都是编译后运行，程序被高度优化，运行效率接近二进制程序，WebAssembly格式是JavaScript引擎的中间码格式，全部都是二进制代码，由于跳过编译步骤，可以达到接近原生二进制代码的运行速度，各种语言（主要C，C++）通过编译成WebAssembly,就可以在浏览器里面运行.
    3. 事件驱动和非阻塞式设计: JavaScript程序可以采用事件驱动(event-driven)和非阻塞式(non-blocking)设计，在服务器适合高并发环境，普通硬件可以承受很大的访问量.

JavaScript开放性:
    JavaScript是一种开放的语言，标准ECMA-262是ISO国际标准，该标准主要实现(V8 和 SpiderMonkey引擎)都是开放的， 而且质量很高，这保证这门语言不属于任何公司或个人。不存在版权和专利的问题.

实验环境:
    推荐安装Chrome浏览器：Chrome开发者工具Developer Tools里面的控制台console就是运行JavaScript代码的理想环境.
    进入Chrome浏览器控制台： Option+Command+J 
    进入控制台以后，就可以在提示符输入代码，Enter执行代码，Shift Enter代码换行
```

JavaScript语言历史
------------------
```
1990年，Tim Berners-Lee 发明万维网world wide Web.最早的网页只能在操作系统的终端里浏览
1992年，美国国家超级电脑应用中心NCSA开始开发一个独立的浏览器，Mosaic,从此网页可以在图形界面的窗口浏览
1994年, NCSA的主程序员Marc Andressen联合风险投资家Jim Clark成立Mosaic，不久改名Netscape,开发面向普通用户的新一代浏览器Netscape Navigator.
1995年，NetScape公司雇佣Brendan Eich有很强的函数式编程背景，希望以Scheme语言(函数式语言鼻祖LISP语言的一种方言)为蓝本，实现这种新语言.
1995年，Brendan Eich只用10天，就设计完成这种语言的第一版，语法有多个来源:
    基本语法: 借鉴C语言和Java语言
    数据结构:借鉴Java语言，包括将值分为原始值和对象两大类
    函数的用法：借鉴Schema语言和Awk语言,将函数当作第一等公民，并且引入闭包
    原型继承模型：借鉴Self语言(Smaltalk的一种变种)
    正则表达式：借鉴Perl语言
    字符串和数组处理: 借鉴Python语言
对于其他语言，需要学习各种功能，对于JavaScript需要学习各种解决问题的模式，而且由于来源多样，JavaScript的编程风格是函数式和面向对象编程的一种混合体.

JavaScript与Java的关系:
    JavaScript基本语法和对象体系是模仿Java而设计，但是,JavaScript没有采用Java静态类型。JavaScript原来的意思是“很像Java的脚本语言”
    JavaScript语言的函数是一种独立的数据类型，以及采用原型对象prototype的继承链，这是与Java最大的两点区别。
    Java语言需要编译，JavaScript语言则运行时由解释器直接执行
    JavaScript原始设计目标是一种小型的、简单的动态语言，与Java有足够的相似性。

JavaScript 与 ECMAScript的关系:
    ECMAScript和JavaScript的关系是，前者是后者的规格，后者是前者的一种实现.

JavaScript的版本:
    1997年7月，ECMAScript 1.0发布
    1998年6月，ECMAScript 2.0发布
    1999年12月, ECMAScript 3.0发布, 成为JavaScript的通行标准，得到广泛支持
    2008年7月，ECMAScript 3.1改名为ECMAScript 5
    2015年6月，ECMAScript 6正式发布，更名为“ECMAScript 2015” 

周边大事记:
    1996年，样式表标准CSS第一版发布
    1997年，DHTML(Dynamic HTML,动态HTML)发布，允许动态改变网页内容，这标志着DOM模式(Document Object Model,文档对象模型)正式应用
    1998年，Netscape公司开源浏览器，导致Mozila项目诞生，美国在线AOL宣布并购Netscape
    1999年，IE 5部署XMLHttpRequest接口，允许JavaScript发出HTTP请求，为后来大行其道的Ajax应用创造了条件
    2000年，KDE项目重写浏览器引擎KHTML，为后台的WebKit和Blink引擎打下基础，
    2001年，微软公司时隔5年之后，发布IE浏览器下一个版本Internet Explore 6
    2001年，Douglas Crockford提出JSON格式，用于取代XML格式，进行服务器和网页之间的数据交换，JavaScript可以原生支持这种格式，不需要格外部署代码
    2002年，Mozila项目发布浏览器第一版，起名Firefox 
    2003年，苹果公司发布Safari浏览器的第一版
    2004年，Google公司发布Gmail，促成互联网应用程序Web Application这个概念的诞生
    2004年，Dojo框架诞生，为不同浏览器提供同一接口，并为主要功能提供便利的调用方法，标志JavaScript编程框架的时代开始来临
    2004年，WHATWG组织成立，致力于加速HTML语言的标准化进程
    2005年，苹果公司在KHTML引擎的基础上，建立了WebKit引擎
    2005年，Ajax方法（Asynchronous JavaScript and XML）正式诞生，Jesse James Garrett发明这个词汇，开始流行的表示是2月份发布的Google Maps项目大量采用该方法，几乎成了新一代网站的标准做法，促成Web2.0时代的来临
    2005年，Apache基金会发布的CouchDb数据库，这是一个基于JSON格式的数据，可以JavaScript函数定义视图和索引，本质上有别于传统的关系型数据库，标志着NoSQL类型的数据库诞生
    2006年：jQuery函数库诞生，作者为John Resig,jQuery为操作网页DOM结构提供非常强大易用的接口，成为最广泛的函数库，并且让JavaScript语言的应用难度大大降低，推动这种语言的流行
    2006年，微软发布IE7，标志重新开始启动浏览器的开发
    2006年，Google推出Google Web Toolkit (GWT),提供Java编译成JavaScript的功能，开创将其他语言转为JavaScript的先河
    2007年，WebKit引擎在iPhone手机中得到部署，最初基于KDE项目，2003年苹果公司首先采用，2005年开源，标志着JavaScript语言开始在手机中使用，意味着有可能写出在桌面电脑和手机中都能使用的程序
    2007年，Douglas Crockford发表名为《JavaScript: The good parts》的演讲，次年O'Reilly出版社出版，标志软件行业开始严肃对待JavaScript语言，对他的语法开始重新认识
    2008年，V8编译器诞生，这是Google公司为Chrome浏览器而开发，特点是让JavaScript运行变得非常快，提高JavaScript性能，推动语法的改进和标准化，改变外界对JavaScript的不佳印象，同时V8是开源，任何人想要一种快速的嵌入式脚本语言，都可以采用V8，这扩展了JavaScript的应用领域
    2009年，Jeremy Ashkenas 发布CoffeScript的最初版本，CoffeScript可以被转换为JavaScript运行，但是语法比JavaScript简洁，这开启其他语言转为JavaScript的风潮
    2009年，PhoneGap项目诞生，将HTML5和JavaScript引入移动设备的应用程序的开发，主要针对iOS和Android平台，使得JavaScript可以用于跨平台的应用程序开发
    2009年，Google发布Chrome OS,号称是以浏览器为基础发展成操作系统，允许直接使用JavaScript编写应用程序，类似的项目还有Mozila的Firefox OS.
    2010年，三个重要的项目诞生，分别是NPM，BackboneJS 和Require JS标志着JavaScript进入模块化开发的时代.
    2011年，微软公司发布Windows8操作系统，将JavaScript作为应用程序的开发语言，直接提供系统支持
    2011年，Google发布Dart语言，目标是为了结束JavaScript语言在浏览器中的垄断地位，提供更合理、更强大的语法和能力，Chromium浏览器有内置Dart虚拟机，可以运行Dart程序，但Dart程序也可以被编译成JavaScript程序运行.
    2011年，微软工程师Scott Hanselman提出，JavaScript语言将是互联网的汇编语言，因为他无处不在，而且郑子啊变得越来越快，其他语言的程序可以转成为JavaScript语言，然后在浏览器中运行.
    2012年，单页面应用程序框架(Single page app framework)开始崛起，Angular Js项目和Ember项目都发布了1.0版本
    2012年，微软发布TypeScript语言，该语言被设计成JavaScript的超集，意味着所有JavaScript程序，都可以不经过修改在TypeScript中运行，同时TypeScript添加很多语法特性，主要目的是为了开发大型程序，然后还可以编译成JavaScript运行.
    2012年，Mozila基金会提供asm.js 规格，asm.js是JavaScript的一个子集，所有符合asm.js的程序都可以在浏览器中运行
    2013年，Mozila基金会发布手机操作系统Firefox OS,该操作系统的整个用户界面都是用JavaScript  
    2013年，ECMA正式推出JSON的国际标准，意味着JSON格式已经变得与XML格式一样中重要和正式
    2013年5月，Facebook发布UI框架库React引入新的JSX语法，使得UI层可以用组件开发，同时引入网页应用是状态机的概念
    2014年，微软推出JavaScript的Windows库WinJS,标志微软公司全面支持JavaScript与Windows操作系统的融合
    2014年11月，由于对Joyent公司垄断Node项目、以及该项目进展缓慢的不满，一部分开发者离开Node.js创造了io.js项目，这是一个更开放、更新更频繁的Node.js版本，很短时间内发布到2.0版本，三个月之后，Joyent公司宣布放弃对Node项目的控制，将其转交给新成立的开发性标志Node基金会，随后，io.js项目宣布回归Node,两版本将合并
    2015年，Facebook公司发布React Native项目，将React 框架移植到手机端，可以用来开发手机App,会将JavaScript代码转为iO平台的Object-C代码或者Android平台的Java代码，从而为JavaScript语言开发高性能的原生App打开一条道路.
    2015年，Angular框架宣布，2.0版本基于微软公司的TypeScript语言开发，这等于为JavaScript语言引入强类型
    2015年，Node模块管理器NPM超越CPAN，标志着JavaScript成为实际上软件模块最多的语言
    2015年，Google公司的Polymer框架发布1.0版，该项目的目标是生产环境可以使用WebComponent组件，如果能够达到目标，WEb开发将进入一个全新的以组件为开发基础的阶段
    2015年，ECMA标准化组织正式批准了ECMAScript6语言标准，定名为《ECMAScript2015标准》JavaScript语言正式进入下一个阶段，成为一种企业级的、开发大规模应用的语言，这个标准从提出到批准，历时10年，而JavaScript语言从诞生至今也已经20年
    2015年，Mozila在asm.js基础上发布WebAssembly项目，这是一种JavaScript引擎的中间码格式，全部都是二进制，类似于Java字节码，有利于移动设备加载JavaScript脚本，执行速度提高20+被，意味着将来的软件，会发布JavaScript二进制包
    2016年，《ECMAScript2016标准》发布，与前一年发布的版本相比，只增加了两个较小的特性
    2017年，ECMAScript2017标准，发布，正式引入async函数,使得异步操作的写法出现根本型的变化
    2017年，所有主流浏览器全部支持WebAssembly，意味着任何语言都可以编译成JavaScript,在浏览器运行
```

JavaScript 基本语法
-------------------
```
语句(statement)和表达式(expression)的区别在于，语句主要为了进行某种操作，一般情况下不需要返回值，后者的是为了得到返回值，一定会返回一个值。
语句以分号结尾，一个分号就表示一个语句结束，多个语句可以写在一行内。表达式不需要分号结尾，一旦在表达式后面添加分号，JavaScript引擎就将表达式视为语句.

JavaScript的变量名区分大小写,如果只是声明变量而没有赋值，则该变量的值是undefined.
JavaScript是一种动态类型语言，变量的类型没有限制，变量可以随时更改类型。如果使用var重新声明一个已经存在的变量，是无效的。如果第二次声明还进行赋值，则会覆盖前面的值.

JavaScript引擎的工作方式，先解析代码，获取所有被声明的变量，然后再一行一行的运行。造成的结果就是所有的变量的声明语句，都会被提升到代码的头部。这就叫做变量的提升(hoisting).

标识符identifier: 
    1. 第一个字符可以是任意Unicode字母以及美元符号$和下划线
    2. 第二个字符及后面字符，除了Unicode字母、美元符号和下划线还可以使用数字
JavaScript保留字：
    arguments, break, case, catch, class, const, continue, debugger, default, delete, do, else, enum, eval, export, extends, false, finally, for, function, if, implements, import, in, instanceof, interface, let, new, null, package, private, protected, public, return, static, super, switch, this, throw, true, try, typeof, var, void, while, with, yield

JavaScript提供两种注释:
    单行注释 // 
    多行注释 /* */ 

JavaScript Block: 区块
    区块对于var命令不构成单独的作用域，与不属于区块的情况没有任何区别

 =   : 赋值表达式
 === : 严格相等运算符
 ==  : 相等运算符 

JavaScript条件语句:
    if - else : 
    switch    :  注意，switch语句后面的表达式与case语句后面的表达式比较运算结果时，采用的是严格相等运算符(===)而不是相等运算符(==),意味着比较时不会发生类型转换
    三元运算符 (条件) ? 表达式1: 表达式2 

JavaScript循环语句:
    while: 
    do ... while: 
    for: 初始化表达式initialize, 条件表达式test, 递增表达式increment
    break: 跳出代码块或循环
    continue: 立刻终止本轮循环、返回循环结构的头部
    break语句和continue语句只针对最内层循环

JavaScript: 
    标签label: 相当于定位符，用于跳转程序的任意位置
```

数据类型
--------
```
原始类型 primitive type:
    number: 数值 (整数和小数)
    string: 字符串 
    boolean: 布尔值 true, false 

合成类型 complex type: 
    object: 对象 各种值组成的集合
        object: 狭义的对象
        array: 数组
        function: 函数 -- JavaScript函数式编程
特殊类型:
    undefined: 未定义
    null: 空值
ES6新增类型
    symbol: 

JavaScript三种方法确定值类型:
    _instanceof_ 运算符:
    _Object.prototype.toString_方法
    _typeof_运算符: 返回一个值的数据类型
Welcome to Node.js v12.10.0.
Type ".help" for more information.
> typeof 123
'number'
> typeof '123'
'string'
> typeof true
'boolean'
> function f() {}
undefined
> typeof f
'function'
> typeof undefined
'undefined'
> typeof {}  // 对象
'object'
> typeof []  // 数组本质上只是一种特殊的对象
'object'
> var o = {};
undefined
> var a = [];
undefined
> o instanceof Array; // instanceof 运算符可以区分数组和对象
false
> a instanceof Array;
true
> typeof null // null 返回 对象
'object'
// null 与 undefined 都表示没有，if语句中都自动转换为false
> if (!undefined) {console.log('undefined is false')}
undefined is false
undefined
> if (!null) {console.log('null is false')}
null is false
undefined
> undefined == null // 
true
> Number(null) // null 表示空值，此处值现在为空, 可以自动转为0
0
> Number(undefined) // undefined表示未定义,转为数值为NaN 
NaN
> var i; // 变量声明，没有赋值
undefined
> i
undefined
> function f(x) {return x;} // 调用函数时，应该提供参数没有提供，参数等于undefined，
undefined
> f()
undefined
> var o = new Object(); // 对象没有赋值的属性
undefined
> o.p
undefined
> function f() {} // 函数没有返回值时，默认返回undefiend
undefined
> f()
undefined

_boolean布尔值_
    !Not
    ===, !==, ==, != 
    >, >=, <, <= 
JavaScript除了下面值转为false，其他值都为true 
    undefined、null、false、0、NaN、“”或者'' 空字符串
[]空数组、{}空对象对应的布尔值都是true

_Number_整数、浮点数
    JavaScript内部所有数字都是以64位浮点数形式存储，即使整数也是一样,JavaSript语言底层根本没有整数，所有数字都是小树(64位浮点数),某些运算需要整数，此时JavaScript自动将64位浮点数转为32位整数，然后参与运算.
> 1 == 1.0
true
> 1 == 1.0
true
> 0.1 + 0.2 === 0.3 // 由于浮点数不是精确的值
false
> 0.3 / 0.1
2.9999999999999996
> (0.3 - 0.2) === (0.2 - 0.1)
false
    国际标准IEEE 754, JavaScript浮点数64位二进制表示:
        第一位：符号位，0表示整数，1表示负数
        第二位到第十二位：指数部分: 大小范围是0-2047
        第十三位到六十四位：小树部分(有效数字)
        如果指数部分值在0-2047之间，有效数字的




tyepof 用来检查一个没有声明的变量而不报错.
```
