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
        第二位到第十二位：指数部分: 大小范围是0-2047,IEE754规定，指数部分的值在0-2047之间(开区间)，有效数字的第一位默认为1，不保存在64位浮点数之中,
        第十三位到六十四位：小树部分(有效数字) JavaScript提供有效数字最长数字只能53个二进制位，绝对值小于2的53次方的整数-2⁵³-2⁵³都可以精确表示:
> Math.pow(2, 53)
9007199254740992
> Math.pow(2, 53) + 1  // 大于2的53次方以后，整数运算的结果开始出现错误
9007199254740992
> Math.pow(2, 53) + 2
9007199254740994
> Math.pow(2, 53) + 3
9007199254740996
> Math.pow(2, 53) + 4
9007199254740996
        JavaScript能够表示数值范围为2¹⁰²⁴到2⁻¹⁰²³ 
> Math.pow(2, 1024)
Infinity
> Math.pow(2, -1075)
0
> Number.MAX_VALUE   // 最大值 
1.7976931348623157e+308
> Number.MIN_VALUE   // 最小值
5e-324
JavaScript自动将数值转为科学计数法表示:
> 1234567890123456789012  // 小数点前的数字多于21位
1.2345678901234568e+21 
> 0.0000003 // 小数点后的零多于5个
3e-7
> 0.000003
0.000003
JavaScript整数提供四种进制表示方法:
    十进制：没有前导0的数值
    八进制: 前缀0o, 0O,或者前导0,且只用到0-7, 出现数值8,9视为十进制
    十六进制: 前缀0x, 0X
    二进制: 0b, 0B
JavaScript 正零+0,负零-0区别是64位浮点数表示法的符号位不同.
(1/+0) === (1/-0) // false  +Infinity != -Infinity 
JavaScript中的NaN表示非数字(Not a Number),NaN不是独立的数据类型，而是特殊数值，数据类型属于Number, NaN不等于任何值，包括自己本身.数组indexOf方法内部使用严格相等运算符，[NaN].indexOf(NaN) // -1, NaN布尔运算为false,NaN与运算都得NaN.
JavaScript Infinity表示“无穷”,表示正的数值太大，或者负的数值太小，无法表示，另一种是非0数值除以0，得到Infinity.
由于JavaScript数值正向溢出OverFlow、负向溢出underflow和被0除，都不报错
Infinity大于一切数值(除了NaN)，-Infinity小于一切数值(除了NaN); Infinity与NaN比较总是返回false.
> 0 * Infinity
NaN
> 0 / Infinity
0
> Infinity / 0
Infinity
Infinity与null运算，null会自动转换为0，等同于与0计算
Infinity与undefined运算，返回都是NaN.

parseInt用于将字符串转为整数;字符串转为整数，是一个个字符依次转换，遇到不能转为数字的字符就不再进行下去，返回已经转好的部分,如果第一个字符不能转为数字，返回NaN,因此parseInt返回值只有两种可能，要么是十进制整数，要么是NaN.如果字符串以0x或0X开头，parseInt将按照十六进制解析，如果字符串以0开头，将按照10进制解析.parseInt第二参数表示被解析的值的进制。第二参数不是数值会被自动转为一个整数，这个整数只有2到36之间，才能得到有意义的结果，超出范围返回NaN.如果第二参数为0，undefiend,null直接忽略.
JavaScript不再允许将带有前缀0的数字视为八进制数，而是要求忽略这个0

parseFloat用于将字符串转为浮点数,parseFloat会将空字符串转为NaN.

isNaN()判断一个值是否为NaN.isNaN只对数值有效，如果传入其他值，会被先转成数值，isNaN为true有可能不是NaN,而是一个字符串.[]可以被Number函数转为数值.判断NaN最好的方法是利用NaN不等于自身的值这一特点.

isFinite()方法返回一个布尔值，表示某个值是否为正常的数值.除了Infinity、-Infinity、NaN和undefined返回false,isFinite对于其他数值都返回true.

字符串String:
    由于HTML语言的属性值使用双引号，所以很多项目约定JavaScript语言的字符串只使用单引号.
    转义符:
        \0  : null \u0000
        \b  : 后退键\u0008
        \f  : 换页符\u000C
        \n  : 换行符\u000A
        \r  : 回车键\u000D
        \t  : 制表符\u0009
        \v  : 垂直制表符\u000B
        \'  : 单引号 \u0027
        \"  : 双引号 \u0022
        \\  : 反斜杠 \u005C 
    \HHH: 反斜杠紧跟三个八进制数代表一个字符
    \xHH: \x紧跟两个十六进制代表一个字符
    \uXXXX: \u紧跟四个十六进制数，代表一个字符
    在非特殊字符前面使用反斜杠，反斜杠自动省略

字符串与数组，无法该比那字符串中的单个字符。'string'.length返回字符串的长度，该属性无法改变.
JavaScript使用Unicode字符集，JavaSCript引擎内部使用Unicode表示，JavaScript自动识别字符是字面形式表示还是Unicode形式表示，输出给用户的时候，所有字符都会转成字面形式.JavaScript内部每个字符都是使用16位的UTF-16格式存储，对于码点U+10000到U+10FFFF之间的字符，JavaScript总是认为是两个字符，length属性为2,JavaScript返回的字符串长度可能是不正确的.

Base64转码: 编码方式，将任意值转成0-9,A-Z,a-z,+,/ 64个字符组成的可打印字符，使用目的不是为了加密，而是为了不出现特殊字符，简化程序处理.
    JavaScript原生提供两个Base64方法：这两种方法不适合非ASCII字符，会报错，要将非ASCII字符转为Base64编码，中间需要转码
        btoa(): 将任意值转为Base64编码
        atob(): Base64编码转为原来的值
    $ npm install --save buffer 
    Ensure Buffer, btoa, and atob are loaded as a globals:
        global.Buffer = global.Buffer || require('buffer').Buffer;
        if (typeof btoa === 'undefined') {
            global.btoa = function(str) {
                return new Buffer(str. 'binary').toString('base64');
            };
        }

        if (typeof atob === 'undefined') {
            global.atob = function(b64Encoded) {
                return new Buffer(b64Encoded, 'base64').toString('binary');
            };
        }

        function b64Encode(str) {
            return btoa(encodeURIComponent(str));
        }

        function b64Decode(str) {
            return decodeURIComponent(atob(str));
        }
        b64Encode('你好')
        b64Decode('')

JavaScript Object: 是一组“健值对key-value集合”是一种无序的复合数据集合.所有键名都是字符串(ES6引入Symbol值作为键名),键名是数值，会被自动转为字符串.如果键名不符合标识名的条件(比如第一个字符为数字，或者含有空格或运算符)且也不是数字，则必须加上引号，否则会报错.
    对象的每一个键名称为"属性"property: 键值可以是任何数据类型,如果键值为函数，则把属性称为“方法”.如果属性的值还是一个对象，就形成链式引用.属性可以动态创建，不必在对象声明时就指定
    值拷贝，对象引用, JavaScript引擎如果遇到行首是大括号，无法确定是对象还是代码块，一律解释为代码块.如果要解释为对象，对好在大括号前加上圆括号.
    eval解释
    读取对象的属性的两种方法: 点运算符, 方括号运算符(键名必须放在引号里面，否则当作变量处理, 数字键可以不加引号，会自动转成字符串,数字键名不能使用点运算符,只能使用方括号运算符)
    查看一个对象本身的所有属性名:使用Object.keys; 属性的函数delete命令，delete命令只能删除对象本身的属性，无法删除继承的属性.属性是否存在: in运算符(不能识别那些属性是对象自身，那些属性是继承). hasOwnProperty方法判断是否对象自身属性
    属性的遍历 for...in循环:[1. 遍历对象所有可遍历enumerable属性，跳过不可遍历的属性; 2.不仅遍历对象自身属性，还遍历继承的属性; hasOwnProperty判断属性是否是对象自身的属性]
    with语句：操作同一个对象的多个属性提供方便,如果with区块内部有变量的赋值操作，必须是当前对象已经存在的属性，否则会创造一个当前作用域的全局变量,因为with区块没有改变作用域，内部依然是当前作用域,建议不要使用with语句，可以考虑使用临时变量代替with.

JavaScript: 有三种声明函数的方法:
    1. function命令声明的代码区块，就是一个函数，function命令后面是函数名，函数名后面是一对圆括号，里面是传入函数的参数，函数体放在大括号内.
    2. 函数表达式: var print = function(s) {console.log(s);} 采用函数表达式声明函数，function命令后面不带有函数名,如果加上函数名，函数名只在函数体内部有效[1: 可以在函数体内部调用自身 2: 调试共建显示函数调用栈将显示函数名，不再显示匿名函数]
    3. Function构造函数: 可以传递任意数量的参数给Function构造函数，最后一个参数被当做函数体，如果只有一个参数，该参数就是函数体.
    函数被多次声明，后面的声明就会覆盖前面的声明

    JavaScript语言中称函数为第一等公民.JavaScript引擎被函数名视为变量名，采用function命令声明函数，整个函数会像变量声明一样.被提升到代码头部,如果同时采用function命令和赋值语句声明同一个函数，最后总是采用赋值语句的定义。
    函数的name属性返回函数名; 函数的length属性返回函数预期传入的参数个数,length属性提供一种机制，判断定义时含调用时参数的差异，以便实现面向对象编程的“方法重载”overload.
    函数的toString方法返回一个字符串，内容是函数的源码.对于原生函数，toString()方法返回function() {[native code]}, 函数内部注释可以
    函数作用域: scope, ES5规范中JavaScript只有两种作用域[1.全局作用域global variable, 2:函数作用域local variable] ES6新增快级别作用域; 对于var命令，局部变量只能在函数内部声明，在其他区块中声明，一律都是全局变量.
    函数内部的变量提升,var命令声明的变量，不管在什么位置，变量声明都会被提升到函数体的头部.
    函数执行时所在的作用域时定义时的作用域，而不是调用时所在的作用域.函数体内部声明的函数，作用域绑定函数体内部
    函数参数: 省略靠前的参数需要显式传入undefined.函数参数的传递方式: 原始类型的值(数值、字符串、布尔值)传递方式是传值传递(passes by value),如果函数参数是复合类型的值(数组、对象、其他函数)传递方式是传址传递(pass by reference)
    函数同名参数，取最后出现的值,
    JavaScript允许函数有不定数目的参数, arguments对象包含函数运行时所有的参数，arguments只有在函数体内部使用,严格模式下，arguments对象与函数参数不具有联动关系，修改arguments对象不会影响到实际的函数参数.通过arguments.length属性可以判断函数调用时到底带几个参数.argument很像数组，但是一个对象，数组专用方法(slice, forEach)不能在arguments对象上直接使用. 可以将arguments对象转为数组 var args = Arrays.prototype.slice.call(arguments);
    arguments对象带有callee属性，返回对应的原函数,这个属性在严格模式里面是禁止使用，因此不建议使用.
    闭包closure: JavaScript语言特有的“链式作用域”结构chain scope. 子对象会一级一级向上寻找所有父对象的变量，所以，父对象的所有变量，对子对象都是可见的. 闭包简单理解为“定义在一个函数内部的函数”闭包就是将函数内部和函数外部连接起来的一座桥梁.
        闭包两大用处：[1. 读取函数内部的变量。 2.让变量始终保持在内存中]闭包可以看作函数内部作用域的一个接口
        闭包另外用处, 是封装对象的私有属性和私有方法: 外层函数每次运行，都会生成一个新的闭包，而这个闭包只会保留外层函数的内部变量，所以内存消耗很大，因此不能滥用闭包，否则会造成网页的性能问题.
    JavaScript的圆括号()是一种运算符，JavaScript引擎规定，如果function关键字出现在行首，认为是函数的定义，不应该以圆括号结尾.解决办法就是将其放在一个圆括号里面,转变为表达式 "立刻调用的函数表达式Immediately Invoked Function Expression" IIFE.通常情况下只对匿名函数使用这种"立刻执行的函数表达式"好处是不必为函数命名，避免污染全局变量，IIFE内部形成一个单独的作用域.
    eval命令: 接收一个字符串作为参数,并将字符串当作语句执行,如果eval参数不是字符串，那么会原样返回.eval没有自己的作用域,JavaScript规定，使用严格模式，eval内部声明的变量不会影响外部作用域,eval常见场合解析JSON数据的字符串,正确的做法应该是使用原生的JSON.parse方法.为了保证eval别名不影响代码优化，JavaScript标准规定，凡事使用别名执行eval，eval内部一律是全局作用域.
    eval.call(null, '...') window.eval('...') (1, eval)('...') (eval, eval)('...') 别名调用，作用域都是全局作用域.

JavaScript Array:
    任何类型的数据都可以存放数组.数组属于一种特殊的对象，typeof运算符会返回数组的类型是object 数组的特殊性体现在，键名是按次序排列的一组整数(0,1,2) JavaScript语言规定，对象的键名一律为字符串，所以，数组的键名其实也是字符串。数组成员只能使用方括号arr[0]表示(方括号是运算符，可以接收数值)
    数组的length属性，返回数组的成员数量.JavaScript使用一个32位整数,保存数组的元素个数,意味着，数组成员最多只有2³²-1
    (4294967295)，数组的length属性是一个动态值，等于键名中最大整数加上1.JavaScript数组是一种动态的数据结构，可以随时增减数组的成员.length属性是可写的，如果人为设置一个小于当前成员个数的值，该数组的成员会自动减少到length设置的值.清空数组的一个有效方法，就是将length属性设为0,数组本身是一种对象，所以可以为数组添加属性，但是这不影响length属性的值, 
    in运算符检查键名是否存在，适用于对象，也适用数组.如果数组的某个位置是空位，in运算符返回false. 
    for...in 循环和数组的遍历: for...in不仅会遍历数组所有的数字键，还会遍历非数字键.数组遍历可以考虑使用for循环或while循环.数组forEach方法，用来遍历数组, 数组的空位是可以读取的，返回undefined.使用delete命令删除一个数组成员，会形成空位，并且不会影响length属性. 使用数组forEach方法、for...in结构，Object.keys方法遍历，空位会被跳过,空位就是数组没有
        

tyepof 用来检查一个没有声明的变量而不报错.
```
