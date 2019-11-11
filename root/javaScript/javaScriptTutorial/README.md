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
    for...in 循环和数组的遍历: for...in不仅会遍历数组所有的数字键，还会遍历非数字键.数组遍历可以考虑使用for循环或while循环.数组forEach方法，用来遍历数组, 数组的空位是可以读取的，返回undefined.使用delete命令删除一个数组成员，会形成空位，并且不会影响length属性.
        使用数组forEach方法、for...in结构，Object.keys方法遍历，空位会被跳过,空位就是数组没有这个元素，所以不会被遍历到，而undefined表示数组有这个元素，值是undefined，所以遍历不会跳过.
    对象的所有键名都是正整数或零，并且有length属性，则这个对象称为“类似数组的对象”array-like object.类似数组的对象“根本特征”就是具有length属性，只要有length属性，就可以认为这个对象类似于数组
    数组的slice方法可以将“类似数组的对象”变成真正的数组.var arr = Array.prototype.slice.call(arrayLike);
    "类似数组的对象"可以使用数组的方法通过call()把数组的方法放到对象上面,这种方法比直接使用数组原生forEach要慢，所以最好还是将“类似数组的对象”转为真正的数组，然后再直接调用forEach方法.
tyepof 用来检查一个没有声明的变量而不报错.
```

运算符
------
```
_算术运算符_
    JavaScript提供10个算数运算符：
        1. 加法运算符 + 
            JavaScript允许非数值相加 true + true = 2 ; 两个字符串相加会变成连接运算符; 加法运算符是在运行时决定的，到底是执行加法还是连接，运算子的不同，导致不同的语法行为，这种现象称为“重载overload”. 除了加法运算符，其他算术运算符都不会发生重载. 减法、除法、和乘法运算符都是将字符串自动转为数值，然后再运算.
            对象obj向加，必须先转为原始类型的值[object Object], 对象自动调用valueOf()，返回对象本身,再调用对象toString()转为字符串 obj.valueOf().toString() 返回[object Object]
            toString() 方法有限valueOf()方法
        2. 减法运算符 - 
        3. 乘法运算符 * 
        4. 除法运算符 / 
        5. 指数运算符 ** 
            指数运算符是右结合,多个指数运算符连用时，先进性最右边的计算
        6. 余数运算符 % 
            运算结果的正负号由第一个运算子的正负号决定
        7. 自增运算符 ++x x++ 
        8. 自减运算符 --x x-- 
            自增自减运算符是一元运算符,只需要一个运算子,运算后，变量的值发生变化，这种效应叫做运算的副作用(side effect)
        9. 数值运算符 +x 
        10. 负数运算符 -x 
            数值运算符的作用可以将任何值转为数值（与Number函数的作用相同);数值运算符号和负数值运算符，返回一个新的值，而不会改变原始变量的值
        11. 赋值运算符
            赋值运算符(Assignment Operators) 用于变量赋值;赋值运算符与其他运算符结合，都是先进性指定运算，然后得到值返回给左边的变量

_比较运算符_
    1. 大于运算符 >
    2. 小于运算符 < 
    3. 小于或等于运算符 <= 
    4. 大于或等于运算符 >= 
    5. 等于运算符 == 
    6. 严格相等运算符 === 
    7. 不相等运算符 != 
    8. 严格不相等运算符 !== 
    
    非相等比较：算法先看两个运算子是否都是字符串，如果是，按照字典顺序比较(实际上比较Unicode码点)否则是将两个运算子转成数值，在比较数值大小;
    任何值(包括NaN本身)与NaN比较，返回的都是false. 对象转换成原始类型值，算法先调用valueOf方法：如果返回的还是对象，接着返回toString() 

    JavaScript提供两种相等运算符 == 和 === 
        ==: 比较两个值是否相等 
        ===: 严格相等运算符比较是否为“同一个值” NaN与任何值都不相等(包括自身); 复合类型(对象、数组、函数)的数据比较，不是比较值是否相等，而是比较是否指向同一个地址;对于两个对象的比较，严格相等运算符比较的是地址，而大于或小于运算符比较的是值
        undefined 和 null与自身严格相等; 由于变量声明后默认值是undefined,因此两个只声明未赋值的变量是相等的
    !== 严格不相等：算法就是先求严格先等运算符的结果，然后返回相反的值
    undefined 和 null与其他类型的值比较时，结果都为false,他们相互比较时结果是true.
    相等运算符隐藏类型转换，会带来一些违反直觉的结果,建议不要使用相等运算符==,最好使用严格相等运算符===

_布尔运算符_
    1. 取反运算符 !
        对一个值连续做两次取反运算，等于将其转为对应的布尔值，与Boolean函数作用相同.
    2. 且运算符 && 
        &&往往用于多个表达式的求值，如果第一个运算子的布尔值为true,则返回第二个运算子的值(注意是值，不是布尔值)如果第一个运算子的布尔值为false，则直接返回第一个运算子的值，且不再对第二个运算子求值
    3. 或运算符 ||
        如果第一个运算子的布尔值为true,返回第一个元算子的值，且不再对第二个运算子求值，如果第一个元算子的布尔值为false,则返回第二个运算子的值.或运算符用于对一个变量设置默认值
    4. 三元运算符 ?: 
        如果第一个表达式的布尔值为true,则返回第二个表达式的值，否则返回第三个表达式的值; if...else是语句没有返回值,三元条件表达式是表达式，具有返回值.

_二进制位运算符_
    1. 二进制或运算符(or) | 
    2. 二进制与运算符(and) & 
    3. 二进制否运算符(not) ~ 
        ~ 3 // -4 
        JavaScript内部将所有的运算子都转为32位二进制整数再进行运算: 3的32位整数形式00000000000000000000000000000011, 二进制否运算以后得到11111111111111111111111111111100,由于第一位(符号位)是1，所以这个数是一个负数，JavaScript内部采用补码形式表示负数，即需要将这个数减1，在取反，然后加上负号,才能得到这个负数对应的十进制.10000000000000000000000000000100,可以简单一个数与自身的取反值相加等于-1.
        二进制否运算符取整是所有取整方法中最快的一种;
        ~NaN // -1 
        ~null // -1
    4. 异或运算符(xor) ^ 
        异或运算：连续对两个数a和b进行三次异或运算，a^=b; b^=a; a^=b;可以互换他们的值，使用异或运算可以在不引入临时变量的前提下，互换两个变量的值.这是互换两个变量的值最快的方法;异或运算也可以用来取整
    5. 左移运算符(left shift) << 
        左移运算符<<表示将一个数的二进制值向左移动指定的位数，尾部补0，最高位的符号位一起移动.
        var color = {r: 186, g: 218, b:85}
        var rgb2hex = function(r, g, b) {
            return '#' + ((1 << 24) + (r << 16) + (g << 8) + b)
                .toString(16)  // 转成16进制，然后返回字符串
                .substr(1); // 去除字符串的最高位，返回后面六个字符串
        }
        rgb2hex(color.r, color.g, color.b)
    6. 右移运算符(right shift) >> 
        右移运算符(>>) 表示一个数的二进制向右移动指定的位数，如果是正数，头部全部补充0，如果是负数，头部全部补1，右移运算符基本相当于除以2的指定次方
    7. 头部补零的右移运算符(zero filled right shift) >>>
        将一个值转为32位无符号整数,查看一个负整数在计算机内部的存储形式，最快的方法就是使用这个运算符
    位运算只操作整数，运算子不是整数会自动转为整数，JavaScript内部数值都是以64位浮点数的形式存储，但是做位运算的时候，是以32位符号的整数进行运算,并且返回值也是一个32位带符号的整数.
    i = i | 0; 将i(不管是整数或小数)转为32位整数

_运算顺序_
    1. void 运算符
        void运算符作用是执行一个表达式，然后不反悔任何值，或者返回undefined; 主要用途是浏览器的书签工具Bookmarklet,以及在超链接中插入代码防止网页跳转.
    2. 逗号运算符
        逗号运算符用于对两个表达式求值，并返回后一个表达式的值
    3. 运算顺序
        JavaScript各种元算符的优先级别Operator Precedence是不一样，优先级高的运算符先执行，优先级低的运算符后执行.
        圆括号()可以用来提高运算符的优先级，圆括号两种用法：1. 把表达式放在圆括号之中，提升运算的优先级，另一种跟在函数的后面，作用是调用函数;圆括号之中，只能放置表达式，如果将语句放在圆括号中，就会报错
        左结合left-to-right associativity 从左边开始计算
        右结合right-to-left associativity （赋值元算符=， 三元条件运算符?:, **指数运算也是右结合）
```

语法专题
--------
```
_数据类型转换_
    JavaScript是一种动态类型语言，变量没有类型限制，可以随时赋予任意值.
    JavaScript强制类型转换主要使用Number(), String(), Boolean()
        Number()函数将字符串转为数值要比parseInt()函数严格的多, parseInt逐个解析字符，Number整体转换字符串的类型
        parseInt和Number函数都会自动过滤一个字符串前导和后缀的空格
        Number方法参数是对象时，返回NaN,除非包含单个数值的数组; 
        Number背后的转换规则：
            1. 调用对象的valueOf()如果返回原始类型值，直接对值使用Number函数，不再进行后续步骤
            2. 如果valueOf方法返回还是对象，该调用自身的toString方法，如果toString放回原始类型的值则对值使用Number函数,不再进行后续步骤
            3. 如果toString返回对象，则报错
    String()函数可以将任意类型的值转为字符串
        String方法背后的转换规则与Number方法基本相同，只是互换了valueOf方法和toString方法的执行顺序
            1. 先调用toString方法，如果返回原始类型的值，则对该值使用String函数，不再进行下面步骤
            2. 如果roString方法返回的是对象，再调用原对象的valueOf方法，如果valueOf方法返回原始类型值，则对该值使用String函数，不再进行一下步骤
            3. 如果valueOf()返回是对象，报错
    Boolean() 函数将任意类型的值转为布尔值
        所有对象(包括空对象)的转换结果都是true,甚至连false对应的布尔对象new Boolean(false) 也是true
    自动转换:
        1. 不同类型的数据互相运算
        2. 对非布尔值类型的数据求布尔值
        3. 对非数值类型的值使用一元运算符
        由于自动转换具有不确定性，而且不易除错，建议在预期位布尔值、数值、字符串的地方，全部使用Boolean, Number, String函数进行显示转换。
        JavaScript遇到预期位字符串的地方，就会将非字符串的值自动转为字符串，具体规则是，先将复合类型的值转为原始类型的值，在将原始类型的值转为字符串.
        一元运算符会把运算子转为数值

_错误处理机制_
    JavaScript原生提供Error构造函数，所有抛出的错误都是这个构造函数的实例;抛出Error实例对象以后，整个程序就中断在发生错误的地方
        var err = new Error('出错了');
        err.message // 错误提示信息
        err.name  // 错误名称 (非标准属性)
        err.stack // 错误的堆栈 (非标准)
    Error实例是最一般的错误类型，JavaScript还定义其他6种错误对象，存在Error的6个派生对象.
        1. SyntaxError: 对象是解析代码发生语法错误 
        2. ReferenceError: 对象是引用一个不存在的变量时发生错误 
        3. RangeError: 对象是一个值超出有效范围时发生的错误
        4. TypeError: 对象是变量或参数不是预期类型时发生错误
        5. URIError: 对象是URI相关函数的参数不正确时抛出的错误
            encodeURI() decodeURI() encodeURIComponent() decodeURIComponent() escapse() unescape() 
        6. EvalError: eval函数没有被正确执行时，该错误类型已经不再使用只是为了保证与以前代码兼容，才继续保留
    自定义错误:
        function UserError(message) {
            this.message = message || '默认信息';
            this.name = 'UserError';
        }

        UserError.prototype = new Error();
        UserError.prototype.constructor = UserError;
        new UserError('这是自定义的错误!');
    throw语句作用是手动中断程序的执行，抛出一个错误; throw可以抛出任何类型的值，参数可以是任意值;JavaScript引擎，遇到throw语句，程序就中止，引擎会接收到throw 抛出的信息，可能是错误实例也可能是其他类型的值
    try...catch结构:
        catch接收一个参数，表示try代码块抛出的值
    finally代码块: 表示不管是否出现错误，都必须在最后运行的语句;return语句的执行是排在finally代码之前只能等finally代码执行完毕后才返回,进入catch代码块之后，一遇到throw语句，就会去执行finally代码。

_编程风格_
    Programming style: 编程风格指的是编写代码的样式规则
    编译器规范叫做"语法规则" grammar.这是程序员必须遵守的，而编译器忽略的部分叫做"编程风格Programming style",这是程序员可以自由选择的,
    缩进: indent 不要Tab和空格混合使用
    区块: 建议使用大括号表示区块, 使用起首的大括号跟在关键字后面, 因为JavaScript自动会添加句末的分号，导致难以察觉的错误
    JavaScript 中圆括号有两种作用: 
        1. 表示函数的调用, 表示函数调用时，函数名与左括号之间没有空格，函数定义时，函数名与左括号之间没有空格
        2. 表达式的组合grouping : 其他前面的语法元素与左括号之间都有一个空格
    行尾的分号:
        for, while 循环行尾没有分号; do...while循环有分号;
        分支语句: if, switch, try: 没有分号
        函数声明语句没有分号; 函数表达式要使用分号
    ASI: Automatic Semicolon Insertion: 分号的自动添加; 如果一行行首是“自增++”或"自减--"运算符，则他们的前面会自动添加分号; continue, break, return, throw后面直接跟换行符，则会自动添加分号; 
    由于解释引擎自动添加分号的行为难以预测，因此编写代码的时候不应该省略行尾的分号，JavaScript代码压缩器uglifier不会自动添加分号，因此遇到没有分号的结尾，就会让代码保持原状，而不是压缩成一行，是的压缩无法得到最优的结果,不写结尾的分号可能会导致脚本合并出错.
    全局变量: 建议避免使用全局变量，使用大写字母表示变量名，这样更容易看出全局变量
    JavaScript会自动将变量声明“提升hoist”到代码块block的头部;所有函数都应该在使用之前定义，函数内部的变量声明都应该放在函数的头部
    相等和严格相等: 相等运算符会自动转换变量类型，造成很多意想不到的情况，建议不要使用相等运算符(==)只使用严格相等运算符(===)
    switch...case结构在每一个case语句之后必须是break语句，否则会接着运行下一个case.建议switch...case结构可以使用

_console_
    console对象是JavaScript原生对象，可以输出各种信息到控制台,并且还提供很多有用的辅助方法
        console常见用途:
            1. 调试程序，显示网页代码运行时错误信息
            2. 提供一个命令行接口，用来与网页代码互动
        Command + Option + i: 打开Chrome浏览器“开发者工具”
            Elements: 查看网页的HTML源码和CSS代码
            Sources: 查看网页加载的各种资源文件(代码文件、字体文件CSS，以及在硬盘上创建的各种内容)
            Network: 查看网页的HTTP通信情况
            Performance: 查看网页的性能情况，比如CPU，内存消耗
            Console: 运行JavaScript命令
    console.log() 方法用于在控制台输出信息,自动换行;如果第一个参数是格式化字符串(使用格式占位符).
        %s: 字符串 %d: 整数 %i: 整数 %f: 浮点数 %o: 对象的链接 %c: CSS格式字符串
    console.info是console.log方法的别名，console.info方法会在输出信息的前面加上一个蓝色图标
        ['log', 'info', 'warn', 'error'].forEach(function(method) {  // 显示结果添加当前时间
            console[method] = console[method].bind(
                console, new Date().toISOString()
            );
        });
    console.warn(), console.error() 
    log(),info()方法写入标准输出stdout, warn(), error()写入标准错误stderror
    console.table() 可以将复合类型的数据转为表格显示
        > var languages = [{name: 'JavaScript', fileExtension: '.js'},{name:'TypeScript', fileExtension: '.ts'}, {name: 'CoffeeScript', fileExtension: '.coffee'}];
        undefined
        > console.table(languages)
        ┌─────────┬────────────────┬───────────────┐
        │ (index) │      name      │ fileExtension │
        ├─────────┼────────────────┼───────────────┤
        │    0    │  'JavaScript'  │     '.js'     │
        │    1    │  'TypeScript'  │     '.ts'     │
        │    2    │ 'CoffeeScript' │   '.coffee'   │
        └─────────┴────────────────┴───────────────┘
        undefined
        >
    console.count() 用于计数，输出被调用多少次
    console.dir() 用来对一个对象进行检查inspect,并以易于阅读和打印的格式显示
    console.dirxml()主要用于目录树的形式显示DOM节点,如果参数不是DOM节点而是普通的JavaScript对象，console.dirxml等同于console.dir
    console.assert()程序运行过程中条件判断，两个参数：1.参数是表达式2.参数字符串,只有第一个参数位false才会提示有错误，在控制台输出第二个参数，否则不会有任何结果
    console.time(), console.timeEnd() 用于计时，算出一个操作花费的准确的时间 console.time()表示计时开始, console.timeEnd()表示计时结束,参数时计时器的名称，调用timeEnd方法之后控制台显示“计数器名称：所消耗的时间”
    console.group(), console.groupEnd(): 显示信息分组，console.groupCollapsed()第一次显示时是收起collapsed 
    console.trace() 显示当前执行的代码在堆栈中调用的路径
    console.clear() 清除当前控制台的所有输出,将光标回置到第一行
    preserve log: 保留日志
    
    控制台命令行API:
        $_: 返回上一个表达式的值
        $0 - $4: 控制台保存最近五个Elements面板选中的DOM元素, $0代表倒数第一个,$1代表倒数第二个
        $(selector): 返回第一个匹配的元素,等同于document.querySelector() 
        $$(selector): 返回选中的DOM对象,document.querySelectorAll 
        $x(path): 返回一个数组,包含匹配特定的XPath表达式的所有DOM元素
        inspect(object): 打开相关面板，并选中响应的元素
        getEventListeners(object): 返回一个对象，该对象成员为object登记回调函数的各种事件，每个事件对应一个数组，数组的成员为该事件的回调函数
        keys(object), values(object): keys(object)返回一个数组，包含object所有键名; values(object)方法返回一个数组，包含object所有键值
        moitorEvents(object[, events]), unmonitorEvents(object[, events]): 监听特定对象发生的特定事件，时间发生时，返回一个Event对象，包含该时间的相关信息，unmonitorEvents停止监听
            所有事件分为四大类:
                mouse: mousedown, mouseup, click, dblclick, mousemove, mouseover, mouseout, mousewheel 
                key: keydown, keyup, keypress, textInput 
                touch: touchstart, touchmove, touchend, touchcancel 
                control: resize, scroll, zoom, focus, blur, select, change, submit, reset.
        命令行API其他方法:
            clear() 清除控制台的历史
            copy(object):复制特定DOM元素到剪贴板 
            dir(object): 显示特定对象的所有属性是console.dir方法的别名
            dirxml(object)显示特定对象的XML形式，是console.dirxml方法的别名
        debugger语句: 设置断点，如果有正在运行的除错工具，程序运行到debugger语句时回自动停下，如果没有除错工具，debugger语句不会产生任何结果，JavaScript引擎自动跳过    
```

标准库
-----
```
_Object对象_
    JavaScript原生提供Object对象，其他所有对象都继承自Object对象，都是Object对象的实例,Object对象的原生方法分为两类: 
        1. Object本身的方法
            直接定义在Object对象的方法 Object.print = function (o) { console.log(o) };
        2. Object实例方法
            直接定义在Object原型对象Object.prototype上的方法.
            Object.prototype.print = function () { console.log(this); }; 
            直接定义在Object.prototype对象上面的属性和方法，将被所有实例对象共享就可以了
    Object本身是一个函数，可以将任意值转为对象,如果参数为空(或者undefiend, null)Object()返回一个空对象
        instanceof验证一个对象是否为指定的构造函数的实例
        如果参数是原始类型的值，Object方法将其转为对应的包装对象的实例
        如果Object方法的参数是一个对象，总是返回该对象，既不用转换
            function isObject(value) {
                return value === Object(value);
            }
    Object构造函数: Object(value)表示将value转为一个对象，new Object(value)表示新生成一个对象,值是value.
        Object.keys(): 遍历对象的属性，参数是一个对象，返回一个数组，成员都是对象自身(而不是继承)的属性名
        Object.getOwnPropertyNames(): 遍历对象的属性,返回一个数组，包含该对象自身的所有属性名. 
            涉及不可枚举属性：Object.keys()返回可枚举的属性, Object.getOwnPropertyNames返回所有枚举的属性名
        Object.keys().length: 计算对象属性个数的方法
    1. 对象属性模型的相关方法:
        Object.getOwnPropertyDescriptor(): 获取某个属性的描述对象
        Object.defineProperty():通过描述对象，定义某个属性
        Object.defineProperties():通过描述对象，定义多个属性
    2. 控制对象状态的方法:
        Object.preventExtensions():防止对象扩展
        Object.isExtensible()判断对象是否可以扩展
        Object.seal():禁止对象配置
        Object.isSealed():判断一个对象是否可配置
        Object.feeeze():冻结一个对象
        Object.isFrozen():判断一个对象是否被冻结
    3. 原型链相关方法
        Object.create(): 该方法可以指定原型对象和属性，返回一个新的对象
        Object.getPrototypeof():返回对象的Prototype 
    Object实例方法:
        定义在Object.prototype对象，所有的Object实例对象都继承这些方法
        Object.prototype.valueOf():返回当前对象对应的值
        Object.prototype.toString():返回当前对象对应的字符串形式
            对一个对象调用toString()方法，返回字符串[object Object]:第二个Object表示该值的构造函数,
            Object.prototype.toString.call(1)  [object Number]
            Object.prototype.toString.call('1') [object String]
            Object.prototype.toString.call(true) [object boolean]
            Object.prototype.toString.call(Undefined) [object Undefined]
            Object.prototype.toString.call(null) [object Null]
            Object.prototype.toString.call([1,2]) [object Array]
            Object.prototype.toString.call({}) [object Object]
            Object.prototype.toString.call(function(){}) [object Function]
            Object.prototype.toString.call(Error()) [object Error]
            Object.prototype.toString.call(new Date()) [object Date]
            Object.prototype.toString.call(RegExp()) [object RegExp]
            Object.prototype.toString.call(Math) [object Math]

            var type = function (0) {
                var s = Object.prototype.toString.call(o);
                return s.match(/\[object (.*?)\]/)[1].toLowerCase();
            }

            ['Null', 'Undefined', 'Object', 'Array', 'String', 'Number', 'Boolean', 'Function', 'RegExp'].forEach(function (t) {type['is' + t] = function (o) {return type(o) === t.toLowerCase();};});

            type.isObject({});
            type.isNumber(NaN);
            数组、字符串、函数、Date对象分别部署自定义的toString()方法
        Object.prototype.toLocalString():返回当前对象对应的本地字符串形式
            主要有三个对象自定义了toLocalString方法
                Array.prototype.toLocalString() 
                Number.prototype.toLocalString()
                Date.prototype.toLocalString()
                    > var date = new Date();
                    undefined
                    > date.toString();
                    'Thu Sep 19 2019 22:45:10 GMT+0800 (China Standard Time)'
                    > date.toLocaleString()
                    '9/19/2019, 10:45:10 PM'
        Object.prototype.hasOwnProperty():某个属性是否为当前对象自身的属性，还是继承自原型对象的属性
            自身属性返回true,继承属性返回 false 
        Object.prototype.isPrototypeOf():判断当前对象是否为另一个对象的原型
        Object.prototype.propertyIsEnumerable():判断某个属性是否可枚举

_属性描述对象_
    JavaScript提供一个内部数据结构，用来描述对象的属性，控制行为
    属性描述对象attributes object: 每一个属性都有自己对应的属性描述对象，保存属性的一些元信息.
        {
            value: 属性的属性值,默认为undefined; value属性是目标属性的值
            writeable:布尔值，表示属性值value是否可改变,默认为true;如果原型对象的某个属性的writeable为false,那么子对象将无法自定义这个属性
            enumerable:布尔值,表示属性是否可遍历，默认为true,如果为false,for...in,JSON.stringify循环 Object.keys()将跳过该属性
            configurable:布尔值，表示是否可配置，默认为true; writeable只有在false改为true会报错，true改为false允许；value,只要writable和configurable又一个为true,就允许改动
            get:函数，表示该属性的取值函数getter，默认为undefined.取值函数getter
            set:函数，表示该属性的存值函数setter,默认为undefined.存值函数setter
                对目标属性定义存取器，那么存取的时候都将执行对应的函数；取值函数get不能接受参数，存值函数set只能接受一个参数
        }
    Object.getOwnPropertyDescriptor()获取属性的描述对象.第一参数是目标对象，第二参数是一个字符串,只适用于自身属性，不适用于继承属性
    Object.getOwnPropertyNames(): 返回一个数组，成员是参数对象自身的全部属性的属性名,不管该属性是否可遍历
    Object.keys(): 值返回对象自身可遍历属性的全部属性名
    Object.prototype: 所有的实例继承它,自身的属性都是不可遍历
        > Object.getOwnPropertyNames(Object.prototype)
        [
          'constructor',
          '__defineGetter__',
          '__defineSetter__',
          'hasOwnProperty',
          '__lookupGetter__',
          '__lookupSetter__',
          'isPrototypeOf',
          'propertyIsEnumerable',
          'toString',
          'valueOf',
          '__proto__',
          'toLocaleString'
        ]
    Object.defineProperty():通过属性描述对象，定义或修改一个属性，然后返回修改后的对象
        Object.defineProperty(object, propertyName, attributesObject)
            object: 属性所在的对象
            propertyName: 字符串，属性名
            attributesObject:属性描述对象
        定义取值函数get需要设置writable为true.
        如果一次性定义或修改多个属性，可以使用Object.defineProperties()方法;一旦定义了取值函数get(或者存值函数set)就不能将writeable属性设为true,或者同时定义value属性
        writeable, configurable, enumerable三个属性都为false 
    Object.prototype.propertyIsEnumerable(): 返回布尔值，判断某个属性是否可以遍历,该方法只能判断自身属性，继承的属性返回false.
    writeable只有在false改为true会报错,true改为false是允许的
    value属性只要writeable和configurable有一个为true,就允许改动
    configurable:决定属性是否可以被删除
    get取值函数不能接受参数，存值函数set只能接受一个参数(属性值)

    对象的拷贝:
        var extend = function (to, from) {
            for (var property in from) {
                if (!from.hasOwnProperty(property)) 
                    continue;
                Object.defineProperty(to, property, Object.getOwnPropertyDescriptor(from, property));
            }
            return to;
        }

    控制对象状态:
        Object.preventExtensions : 使得对象无法添加新的属性
        Object.isExtensible: 检查是否可以为一个对象添加属性
        Object.seal : 使得对象无法添加新属性也无法删除旧属性;实质上是将属性描述符对象的configurable属性设为false,因此属性描述对象不在改变;只是禁止新增或删除属性，不影响修改某个属性的值
        Object.isSealed():检查一个对象是否使用了Object.seal()
        Object.freeze : 使得对象无法添加新属性、无法删除就属性，无法改变属性值，是的这个对象实际上变成常量
        Object.isFrozen(): 检查一个对象是否使用Object.freeze() 

_Array对象_
    Array是JavaScript的原生对象，也是一个构造函数
    Array构造函数的参数是一个正整数，返回数组成员都是空位,获取不到键名
    Array.isArray(): 返回一个布尔值，表示参数是否为数组,弥补typeof运算符的不足
        valueOf返回数组本身
        toString()返回数组的字符串形式
        push()在数组末端添加一个或多个元素,返回数组长度
        pop()方法用于删除数组的最后一个元素,返回该元素,空数组使用pop方法，返回undefined
        push,pop结合使用构成“后进先出”的栈结构(stack)
        shift()删除数组的第一个元素,并返回该元素
        push,shift结合使用构成“先进先出”的队列结构 queue 
        unshift()在数组第一个元素添加元素，并返回添加后的数组长度,接收多个参数
        join():指定参数作为分隔符，将所有数组成员连接为一个字符串返回,默认使用逗号分隔;如果数组成员是undefined或null或空位，会被转为空字符串
        Array.prototype.join.call(): 用于字符串或类似数组的对象
        concat()用于多个数组的合并，将新数组的成员，添加到原数组成员的后部，然后返回一个新数组,原数组不变
        reverse():颠倒排列数组元素,返回改变后的数组,
        slice(): 提取目标数组的一部分,返回一个新数组,原数组不变, slice()方法没有参数，实际上等于返回一个原数组的拷贝;slice方法一个重要应用是将类似数组的对象转为真正的数组
        splice():删除原数组的一部分数据,并可以在删除的位置添加新的数组成员，返回值是删除的元素
        sort():对数组成员进行排序，默认是按照字典顺序排序,排序后，原数组将被改变;数组自动转为字符串，在按照字典顺序比较;
            sort方法按照自定义方式排序，可以传入一个函数作为参数
            [10111, 1101, 111].sort(function (a, b){return a-b;}) ; 如果函数返回值大于0,表示第一个成员排在第二个成员的后面，其他情况下，都是第一个元素排在第二元素前面.
        map():将数组所有成员一次传入参数函数,然后把每一次执行的结果组成一个新数组返回,原数组不变
            map方法接受一个函数作为参数，该函数调用时，map方法向它传入三个参数，当前成员、当前位置和数组本身
            [1, 2, 3].map(function(elem, index, arr){
                return elem * index;
            });
            map方法接受第二参数，用来绑定回调函数内部的this变量
                var arr = ['a', 'b', 'c'];
                [1,2,3].map(function (e) {return this[e];}, arr) // 将回调函数内部的this对象指向arr数组
            数组上的空位(除了undefined, null)会被map方法回调函数跳过
        forEach()与map()方法类似，同样是对数组所有成员依次执行参数函数，forEach方法不返回值，只用来操作数据, forEach方法无法中断执行，总是会将所有成员遍历完，无法使用break语句,forEach回跳过数组的空位
        filter():过滤数组成员，满足条件的成员组成一个新数组返回,参数是一个函数，所有数组成员依次执行该函数，返回结果为true的成员组成一个新数组返回,原数组不变
        some():只要有一个成员的返回值是true,整个some方法返回值为true,否则false; 空数组some方法返回false,回调函数不执行
        every():所有成员的返回值都是true,整个every方法才返回true.否则返回false;空数组every方法返回true,回调函数不执行
        reduce(): 依次处理数组的每个成员，最终累计一个值，顺序是从左到右
        reduceRight(): 依次树立数组的每个成员，最终累计一个值，顺序是从右到左
            reduce方法和reduceRight方法的函数的四个参数
                1.累积变量:默认为数组的第一个成员
                2.当前变量:默认为数组的第二个成员
                3.当前位置(从0开始)
                4.原始数组
            [1,2,3,4,5].reduce(function (a, b){return a+b;}, 10);
        indexOf(): 返回给定元素在数组中第一次出现的位置,否则返回-1, 第二参数表示搜索的开始位置
        lastIndexOf(): 返回给定元素在数组中最后依次出现的位置，否则返回-1
            indexOf, lastIndexOf无法搜索NaN的位置，无法确定数组成员是否包含NaN,因为上述方法使用严格相等运算符(===)进行比较，而NaN是唯一一个不等于自身的值

_包装对象_
    原始类型的值：数值、字符串、布尔值--在一定条件下，会自动转为对象(wrapper-包装对象:Number, String, Boolean)
    对象是JavaScript语言中最主要的数据类型
    Number, String, Boolean:作为构造函数(new)时，可以使得原始类型的值转为对象;作为普通函数使用时(不带new)可以将任何类型的值，转为原始类型的值
    原始类型与实例对象的自动转换

_Boolean对象_
    双重否运算符!!可以将任何值转为对应的布尔值

_Number对象_
    Number对象的静态属性:
        Number.POSITIVE_INFINITY: 正无穷,指向Infinity
        Number.NEGATIVE_INFINITY: 负无穷,指向-Infinity
        Number.NaN: 表示非数值,
        Number.MIN_VALUE:表示最小的正数
        -Number.MIN_VALUE:
        Number.MAX_SAFE_INTEGER:表示精确表示的最大整数
        Number.MIN_SAFE_INTEGER:表示精确表示的最小整数
    Number.prototype.toString(): 将一个数值转为字符串形式; toString方法只能将十进制数转为其他进制的字符串，如果要将其他进制的数转回十进制，需要使用parseInt() 
    Number.prototype.toFixed():将数转为指定位数的小树,然后返回这个小树的字符串(有效范围为0-20,超出返回将抛出RangeError)
    Number.prototype.toExponential(): 将一个数转为科学计数形式，参数是小数点后有效数字的位数(范围是0到20)
    Number.prototype.toPrecision(): 将一个数转为指定位数的有效数字(范围是0-21)

_String对象_
    String.fromCharCode(): 方法的参数是一个或多个数值，代表Unicode码点，返回值是这些码点组成的字符串;不支持Unicode码点大于0xFFFF的字符(2个字节) UTF-16
    String.prototype.length: length属性返回字符串的长度
    String.prototype.charAt(): 返回指定位置的字符，参数是从0开始编号的位置;可以用数组下标替代;参数为负数或大于字符串的长度，charAt返回空字符串.
    String.prototype.charCodeAt(): 返回字符串指定位置的Unicode码点(十进制表示),没有参数，返回首字符的Unicode码点;如果参数为负数，或大于等于字符串的长度，charCodeArt返回NaN.
    String.prototype.concat(): 连接两个字符串，返回一个新字符串，不改变原字符串
    String.prototype.slice(): 从原字符串取出子字符串并返回,并不改变字符串.
    String.prototype.substring(): 用于从原字符串取出子字符串并返回，不改变原字符串.;如果第一参数大于第二参数，自动更换两个参数位置;如果参数是负数，substring方法自动将负数转为0.
        优先使用slice > substring 
    String.prototype.substr(): 用于从原字符串取出子字符串并返回，不改变原字符串.第一参数是开始位置，第二参数是字符串长度
    String.prototype.indexOf(): 第一次出现的位置，-1表示不匹配
    String.prototype.lastIndexOf():最后一次出现的位置，-1表示不匹配
    String.prototype.trim(): 去除字符串两端的空格，返回一个新字符串，不改变原字符串; 去除的包括(space, \t, \v, \n \r)
    String.prototype.toLowerCase(): 将字符串转为小写
    String.prototype.toUpperCase(): 将字符串转为大写
    String.prototype.match(): 确定原字符串是否匹配某个字符串;返回数组还有index属性和input属性，分别表示匹配字符串开始的位置和原始字符串;可以使用正则表达式作为参数
    String.prototype.search(): 返回匹配的第一个位置
    String.prototype.replace():替换匹配的子字符串，一般情况下只替换第一匹配(除非使用g修饰符的正则表达式)
    String.prototype.split(): 按照给定规则分隔字符串,返回一个分割的子字符串组成的数组;第二参数限定返回数组的最大成员数
    String.prototype.localeCompare(): 比较两个字符串;第二参数指定使用的语言(默认是英语)

_Math对象_
    Math是JavaScript原生对象，提供各种数学功能,该对象不是构造函数，不能生成实例，所有的属性和方法都必须在Math对象上调用.
    Math.E: 常数e 
    Math.LN2: 2的自然对数
    Math.LN10: 10自然对数
    Math.LOG2E: 以2为底的e的对数
    Math.LOG10E:以10为底的e的对数
    Math.PI:常数
    Math.SQRT_2: 0.5的平方根
    Math.SQRT2:2的平方根
    Math.abs(): 绝对值
    Math.ceil(): 向上取整: 大于参数值的最小整数
    Math.floor():向下取整: 小于参数值的最大整数
    Math.max(): 最大值: 参数如果为空，返回-Infinity
    Math.min():最小值:参数如果为空,返回Infinity
    Math.pow():指数运算:返回第一个参数为底数，第二个参数为幂的指数值
    Math.sqrt():平方根
    Math.log():自然对数
    Math.exp():e的指数
    Math.round():四舍五入
    Math.random():随机数返回0到1之间的一个伪随机数,可能等于0，一定小于1
        function getRandomInt(min, max) {   // 任意范围的随机整数的生成函数
            return Math.floor(Math.random() * (max - min + 1)) + min;
        }
        function getRandomArbitrary(min, max) { // 任意范围的随机数生成函数
            return Math.random() * (max - min) + min;
        }
        function random_str(length) { // 返回随机字符
            var ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
            ALPHABET += 'abcdefghijklmnopqrstuvwxyz';
            ALPHABET += '0123456789-_';
            var str = '';
            for (var i = 0; i < length; ++i) {
                var rand = Math.floor(Math.random() * ALPHABET.length);
                str += ALPHABET.substring(rand, rand + 1);
            }
            return str;
        }
    Math.sin(): 正弦(参数为弧度值)
    Math.cos(): 余弦(参数为弧度值)
    Math.tan(): 正切(参数为弧度值)
    Math.asin(): 反正弦(返回值为弧度值)
    Math.acos(): 反余弦(返回值为弧度值)
    Math.atan(): 反正切(返回值为弧度值)

_Date对象_
    Date对象是JavaScript原生的时间库,以国际标准时间UTC(1970.1.1.00:00:00)
    Date(): 返回当前时间的字符串
    new Date(): 构造函数参数为负数代表1970年元旦之前的时间;参数年、月、日多个整数，年和月不能省略，其他参数可以省略。
        年: 使用四位数年份,如果是负数，表示公元前
        月: 0表示一月
        日: 1到31
        小时: 0到23
        分钟: 0到59
        秒: 0到59 
        毫秒: 0到999 
    Date实例转为数值，等于对应的毫秒数、转为字符串字符串;两个实例对象进行减法运算，返回的是他们间隔的毫秒数,如果进行加法运算，返回的是两个字符串连接而成的新字符串
    Date.now(): 返回当前时间距离时间零点(1970年1月1日 00:00:00UTC)的毫秒数
    Date.parse(): 解析日期字符串,返回距离时间零点的毫秒数;当前时区
    Date.UTC(): 会被解释为UTC时区
    Date.prototype.valueOf(): 返回实例对象距离时间零点的毫秒数;等同于getTime()方法
    Date.prototype.toString(): 返回一个完整的日期字符串
    Date.prototype.toUTCString(): 返回对应的UTC时间
    Date.prototype.toISOString(): 返回对应时间的ISO8601,UTC时区的时间
    Date.prototype.toJSON(): 返回符合JSON格式的ISO日期字符串;与toISOString()方法返回结果一致
    Date.prototype.toDateString(): 返回日期字符串(不含小时、分钟、秒)
    Date.prototype.toTimeString(): 返回时间字符串(不含年月日)
    下面三个方法都有两个可选的参数:
    Date.prototype.toLocaleString(): 转为完整的本地时间
    Date.prototype.toLocaleDateString(): 本地日期(不含小时，分和秒)
    Date.prototype.toLocaleTimeString(): 本地时间(不含年月日)
        locales: 所用语言的字符串: 'en-US', 'zh-CN'
        options: 配置对象: weekday: 'long', year: 'numeric', month: 'long', day: 'numeric'
    getTime(): 返回实际距离1970.1.1.0 毫秒数; getUTCDate()
    getDate(): 返回对象每月几号; getUTCFullYear()
    getDay(): 返回星期几,星期日为0; getUTCDay()
    getFullYear(): 返回年份; getUTCFullYear()
    getMonth(): 返回月份(0表示1月); getUTCMonth()
    getHours(): 返回小时; getUTCHours();
    getMinutes(): 返回分钟; getUTCMinutes()
    getMilliseconds: 返回毫秒; getUTCMilliseconds()
    getSeconds(): 返回秒; getUTCSeconds()
    getTimezoneOffset(): 返回当前时间的UTC的时区差异，分钟表示，UTC时间减少当前时间
        
        function leftDays() { // 计算本年度剩余多少天
            var today = new Date();
            var endYar = new Date(today.getFullYear(), 11, 31, 23, 59, 59, 999);
            var msPerDay = 24 * 60 * 60 * 1000;
            return Math.round((endYear.getTime() - today.getTime()) / msPerDay);
        }

    setDate(date): 设置每月几号，返回时间毫秒数
    setFullYear(year): 设置四位年份
    setHours(hour): 设置小时
    setMilliseconds()设置毫秒
    setMinutes(min)设置分钟
    setMonth(month): 设置月份
    setSeconds()设置秒数
    setTime(miliseconds)设置毫秒时间戳

_RegExp对象_
    RegExp对象提供正则表达式的功能;JavaScript的正则表达式体系是参照Perl 5建立的
    新建正则表达式有两种方式
        1. 使用字面量,以斜杠表示开始和结束; 引擎编译代码时就会新建正则表达式, 效率较高
        2. RegExp构造函数; 在运行时新建正则表达式
    RegExp.prototype.ignoreCase: 返回一个布尔值,判断是否设置i修饰符
    RegExp.prototype.global: 返回一个布尔值，表示是否设置g修饰符 -- 表示全局搜索
    RegExp.prototype.multiline:返回一个布尔值，表示是否设置m修饰符
    RegExp.prototype.flags: 返回一个字符串,包含已经设置的修饰符,按字母排序
    RegExp.prototype.lastIndex: 返回一个整数,表示下一次开始搜索的位置
    RegExp.prototype.source: 返回正则表达式的字符串形式
    RegExp.prototype.test(): 返回布尔值，表示当前模式是否能匹配参数字符串
    RegExp.prototype.exec(): 返回匹配结果
        正则表达式包含圆括号(组匹配);第一个成员是整个匹配成功的结果,后面的成员就是圆括号对应的匹配成功组
    String.prototype.match(): 对字符串进行正则匹配，返回匹配结果
    String.prototype.search(): 返回第一个满足条件的匹配结果在整个字符串中的位置
    String.prototype.replace(): 替换匹配的值，第一个正则表达式表示搜索模式，第二个替换的内容
        var str = ' #id div.class ';
        str.replace(/^\s+|\s+$/g, '')
        $&: 匹配的子字符串
        $`:匹配结果前面的文本
        $':匹配结果后面的文本
        $n:匹配成功的第n组内容,n是从1开始的自然数
        $$:代美元符号 $
    String.prototype.split(): 按照正则规则分隔字符串，返回一个由分割后的各个部分组成的数组;接收两个参数，第一参数是正则表达式；表示分隔规则；第二参数是返回数组的最大成员数;如果正则表达式带有括号，则括号匹配的部分也会作为数组成员返回
    “字面量字符”: 字符只表示字面的含义
    "元字符 meta characters": 字符具有特殊含义，不代表字面的意思
    ".":点字符匹配回车\r,换行\n,行分割\u2028,段分隔符\u2029以外的所有字符;码点大于0xFFFF字符，点字符不能正确匹配，会认为这是两个字符
    ^: 表示字符串的开始位置
    $:表示字符串的结束位置
    |:或关系
    \:转义字符；正则表达式需要反斜杠转义: ^,.,[,$,(,),|,*,+,?,{,\; 使用RegExp方法生成正则表达式，转义需要使用\\双斜杠,因为字符串内部会先转义一次
    \cX: 表示Ctrl-[x], 其中的X是A-Z之中任一个英文字母，用来匹配控制字符
    [\b]: 匹配退格键U+0008,不要与\b混淆
    \n:匹配换行键
    \r:匹配回车键
    \t:匹配制表符 tab (U+0009)
    \v:匹配垂直制表符 (U+000B)
    \f:匹配换页符 (U+000C)
    \0:匹配null字符(U+0000)
    \xhh:匹配以两位十六进制数(\x00 - \xFF)表示的字符
    \uhhhh:匹配一个四位十六进制(\u0000 - \uFFFF)表示的unicode字符 
    [字符]可供选择的字符放在方括号内
    [^字符]: 表示除了字符类之中的字符
    [^]:匹配一切字符，包括换行符, (.) 不匹配换行符
    [-]:连字号用在方括号之中，表示连续的字符序列
    \d:匹配0-9之间的任一数字 [0-9]
    \D:匹配所有0-9之外的字符 [^0-9]
    \w:匹配任意的字母、数字和下划线 [A-Za-z0-9_]
    \W:匹配除所有字母、数字和下划线以外的字符[^A-Za-z0-9_]
    \s:匹配空格(包括换行符、制表符、空格符)相等于[\t\r\n\v\f]
    \S:匹配非空格字符相当于[^\t\r\n\v\f]
        [\S\s]只代一切字符 
    \b:匹配词的边界
    \B:匹配非词边界
    正则表达式遇到换行符\n就会停止匹配
    {}:表示精确的匹配次数
    贪婪模式: 匹配直到下一个字符不满足匹配规则为止
    ?:表示某个模式出现0次或1次 {0,1}
    *:表示某个模式出现0次或多次 {0,}
    +:表示某个模式出现一次或多次 {1,}
    贪婪模式改为非贪婪模式(一旦条件满足就不再往下匹配)，可以在量词符(?,*,+)后面加上问号
    +?:表示某个模式出现一次或多次，匹配时采用非贪婪模式
    *?:表示某个模式出现0次或多次,匹配时采用非贪婪模式
    ??:表示某个模式出现0次或1次，匹配时采用非贪婪模式
    修饰符(modifier):
        g:全局匹配global;每次都从上次匹配成功处开始向后匹配
        i:表示忽略大小写ignoreCase
        m:表示多行模式multiline
    ():分组匹配，括号中的模式可以用来匹配分组的内容;\n引用括号匹配的内容,n是从1开始的自然数，表示对应顺序的括号
    (?:x):非捕获组Non-capturing group:表示不返回该组匹配的内容，匹配的结果中不计入这个括号
    x(?=y):先行断言positive look-ahead. x只有在y前面才匹配，y不会计入返回结果;先行断言中括号里的部分是不会返回的
    x(?!y):先行否定断言Negative look-ahead, x只有不在y前面才匹配,y不会计入返回结果

_JSON对象_
    JSON格式JavaScript Object Notation是一种用于数据交换的文本格式，2001年Douglas Crockford提出，目的取代繁琐笨重的XML格式
        JSON格式书写简单、一目了然、复合JavaScript原生语法，可以由解释引擎直接处理,不同另外添加解释代码
        1. 复合类型的值只能是数组或对象，不能是函数，正则表达式对象，日期对象
        2. 原始类型的值只有四种:字符串、数值(十进制)、布尔值、null;不允许NaN, Infinity,-Infinity,undefined 
        3. 字符串必须使用双引号表示，不能使用单引号
        4. 对象的键名必须放在双引号里面
        5. 数组或对象最后一个成员的后面不能加逗号
        null, 空数组、空对象都是合法的JSON值
    JSON.stringify():将一个值转为JSON字符串，该字符串复合JSON格式并且可以被JSON.parse()还原
        对象属性undefiend、函数、XML对象，该属性会被JSON.stringify过滤
        数组成员是undefined,函数、XML对象，则这些值被转成null
        正则对象会被转为空对象
        JSON.stringify()会忽略对象的不可遍历的属性
        JSON.stringify方法接受一个数组，作为第二参数，指定需要转成字符串的属性;类似白名单最对对象的属性有效，对数组无效;
        JSON.stringify()方法第二参数还可以是一个函数,用来更改JSON.stringify()的返回值;递归处理所有的键
        JSON.stringify()方法第三参数，用于增加返回的JSON字符串的可读性;如果是数字表示属性前面增加的空格，如果字符串则该字符串添加在每行前面
        对象自定义的toJSON()，JSON.stringify会使用这个方法的返回值作为参数,而忽略愿对象其他的属性
    JSON.parse(): 将JSON字符串转换为对应的值
        JSON.parse()第二个参数:
```

面向对象编程
------------
```
_实例对象与new命令_
    面向对象编程Object Oriented Programming OOP: 面向对象编程具有灵活、代码可复用、高度模块化等特点，容易维护和开发;
    传统过程式编程procedural programming: 
    1. 对象是单个实物的抽象
    2. 对象是一个容器，封装了属性property和方法method 
    构造函数:
        类就是对象的模版、对象就是类的实例;JavaScript语言的对象体系不是基于类，而是基于构造函数constructor和原型链prototype. 
        构造函数名字的首字母大写
        构造体内部使用this关键字,代表所要生成的对象实例
        生成对象的时候，必须使用new命令
        new命令的作用就是执行构造函数，返回一个实例对象
        new命令本身可以执行构造函数，所以后面的构造函数可以带括号，也可以不带括号；避免不实用new命令，直接调用构造函数.
        
        function Fubar(foo, bar) {  // 不管加不加new命令，都会得到同样的结果
            if (!(this instanceof Fubar)) {
                return new Fubar(foo, bar);
            }
            this._foo = foo;
            this._bar = bar;
        }
        Fubar(1, 2)._foo;
        (new Fubar(1,2))._foo; 

    new命令的原理:
        1.创建一个空对象，作为将要返回的对象实例
        2.将这个空对象的原型，指向构造函数的prototype属性
        3.将这个空对象赋值给函数内部的this关键字
        4.开始执行构造函数内部的代码
    
    new命令总会返回一个对象，实例对象或return语句指定对象

    new命令简化的内部流程:
	function _new(/* 构造函数 */ constructor, /* 构造函数参数 */ params) {
		// 将 arguments 对象转为数组
		var args = [].slice.call(arguments);
		// 取出构造函数 
		var constructor = args.shift();
		// 创建一个空对象，继承构造函数的prototype属性
		var context = Object.create(constructor.prototype);
		// 执行构造函数
		var result = constructor.apply(context, args);
		// 如果返回结果是对象，就直接返回，否则返回context对象
		return (typeof result === 'object' && result != null) ? result : context;
	}
	
	// 实例
	var actor = _new(Person, '张三', 28);
    
    new.target: 函数内部使用new.target属性;如果当前函数是new命令调用,new.target指向当前函数;否则undefined;进而判断函数调用是否使用new命令
    Object.create()创建实例对象:使用现有对象作为模版，生成新的实例对象

_this关键字_
    this可以用在构造函数中，表示实例对象;总是代表一个对象
    JavaScript语言中，一切皆为对象，运行环境也是对象，所以函数都是在某个对象之中运行，this就是函数运行所在对象(环境)
    this设计的目的就是在函数体内部，指代函数当前的运行环境
    this使用场合:
        1. 全局变量this指的是顶层对象window 
        2. 构造函数this指的是实例对象
        3. 对象方法：指向方法运行时所在的对象
    避免多层this结构,因为this的指向是不确定的
    严格模式下, this一旦指向顶层对象就会报错
    避免回调函数中的this
    JavaScript提供call,apply,bind三个方法，切换/固定this的指向
    Function.prototype.call(): 可以指定函数内部this的指向;call方法参数如果为空、null、undefined则默认传入全局对象;如果参数是原始值，会自动转成对应的包装对象
    Function.prototype.apply(): 改变this指向，参数接受数组作为函数的参数
    > var a = [10, 2, 4, 15, 9]  // JavaScript不提供数组最大元素的函数
    undefined
    > Math.max.apply(null, a)
    15
    > Array.apply(null, ['a', ,'b']) // 利用Array构造函数将数组的空元素变成undefined
    [ 'a', undefined, 'b' ]
    Function.prototype.bind(): 将函数体内的this绑定到某个对象，然后返回一个新函数

_对象的继承_
    大部分面向对象的编程语言，都是通过"类"class实现对象的继承，传统上，JavaScript语言的继承不通过class,而是通过"原型对象prototype"实现
    JavaScript继承机制的设计思想：原型对象的所有属性和方法，原型对象的作用就是定义所有实例对象的属性和方法，实例对象作为视为从原型对象衍生出来的字对象
    JavaScript所有对象的原型最终上溯到Object.prototype. Object.prototype的原型是null,null咩有任何属性和方法，也没有自己的原型，因此，原型链的尽头就是null。
    prototype.constructor: 指向prototype对象所在的构造函数;由于constructor属性定义在prototype对象上面,因此可以被所有实例对象继承 
    instanceof运算符: 表示对象是否为某个构造函数的实例;任意对象(除了null)都是Object的实例，所以instanceof运算符可以判断一个值是否为null的对象
    JavaScript不提供多重继承功能，不允许一个对象同时继承多个对象
        > function M1() {this.hello = 'hello';}
        undefined
        > function M2() {this.world = 'world';}
        undefined
        > function S() {M1.call(this); M2.call(this);}
        undefined
        > S.prototype = Object.create(M1.prototype); // 继承 M1 
        M1 {}
        > Object.assign(S.prototype, M2.prototype);  // 继承链加上M2 
        M1 {}
        > S.prototype.constructor = S;  // 指定构造函数 
        [Function: S]
        > var s = new S(); // 子类S 同时继承父类M1和M2,这种模式称为Mixin(混入)
        undefined
        > s.hello
        'hello'
        > s.world
        'world'
    JavaScript 不是一种模块化编程语言，ES6才开始支持“类”和“模块”
        模块是实现特定功能的一组属性和方法的封装
            1. 简单的做法是把模块写成一种对象,所有的模块成员都放到这个对象里面;这样的写法曝露所有模块成员、内部状态可以被外部改写
            2. 封装私有变量：构造函数的写法:双重作用，用来塑造实例对象、用来保存实例对象的数据，违背构造函数与实例对象在数据上相分离的原则(实例对象的数据、不应该保存在实例对象以外)
            3. 封装私有变量：立即执行函数的写法
                立即执行函数Immediately Invoked Function Expression IIFE: 将相关属性和方法封装在一个函数作用域里面，可以达到不曝露私有成员的目的
_Object对象的相关方法_
    Object.getPrototypeOf(): 返回参数对象的原型
    > Object.getPrototypeOf({}) === Object.prototype  // 空对象的原型是Object.prototype 
    true
    > Object.getPrototypeOf(Object.prototype) === null;  // Object.prototype 的原型是null 
    true
    > function f() {};  // 函数的原型是Function.prototype 
    undefined
    > Object.getPrototypeOf(f) === Function.prototype
    true
    Object.setPrototypeOf(): 为参数对象设置原型
    Object.create(): 将一个对象作为参数，然后以它为原型，返回一个实例对象,该实例完全继承原型对象的属性 
    Object.prototype.isPrototypeOf(): 判断该对象是否为参数对象的原型
    Object.prototype.__proto__: 返回对象的原型,双线划线表明是一个内部属性，等于构造函数prototype属性 
    Object.getOwnPropertyNames(): 返回一个数组，成员是参数对象本身的所有属性的键名

_严格模式_
    严格模式strict mode: 采用严格的JavaScript语法
    严格模式是从ES5进入标准，主要目的：
        1.明确禁止一些不合理、不严谨的语法，减少JavaScript语言的一些怪异行为
        2.增加更多报错的场合，消除代码运行的一些不安全之处，保证代码运行的安全 
        3.提高编译器效率，增加运行速度 
        4.为未来新版本的JavaScript
    严格模式使得JavaScript语法变得严格，更多的操作会显式报错，其中有些操作，在正常模式下只会默默失败，不会报错
```

异步操作
--------
```
# 单线程模型
    JavaScript只在线程上运行,同时只能执行一个任务,实际上,JavaScript引擎有多个线程，单个脚本只能在一个线程上运行(称为主线程),其他线程都是在后台配合;JavaScript核心特征：单线程，这种模式实现起来简单，执行环境相对单纯,劣势一个任务耗时太长，后面任务都必须排队等候，会拖累整个程序的执行；JavaScript语言本身并不慢，慢的是读写外部数据，等待Ajax请求返回结果，
    JavaScript内部采用“事件循环Event Loop”

# 同步任务(synchronous)和异步任务(asynchronous)
    同步任务:那些没有被引擎挂起，在主线程上排队执行的任务，只有前一个任务执行完毕，才能执行后一个任务
    异步任务:那些被引擎放在一边，不进入主线程，而进入任务队列的任务，只有引擎认为某个异步任务可以执行，该任务采用回调函数的形式进入主线程执行，排在异步任务后面的代码不用等待异步任务结束马上运行，异步任务不具备“堵塞”效应 

# 任务队列和事件循环
    JavaScript运行时除了一个正在运行的主线程，引擎还提供一个任务队列(task queue).里面是各种需要当前程序处理的异步任务。
    异步任务通常是回调函数，一旦异步任务重新进入主线程，就会执行对应的回调函数，如果一个异步任务没有回调函数，就不会进入任务队列.
    JavaScript引擎只要同步任务执行完，引擎就会去检查那些刮起的异步任务，是不是可以进入主线程；这种循环检查的机制就叫事件循环Event Loop.

# 异步操作的模式
    1. 回调函数:是异步操作最基本的方法
        回调函数的优点是简单、容易理解和实现、缺点是不利于代码的阅读和维护，各种部分之间高度耦合coupling使得程序结构混乱、流程难以追踪，每个任务只能指定一个回调函数
    2. 事件监听:事件驱动模式异步任务的执行不取决于代码的顺序，而取决于某个事件是否发生
        事件监听优点是比较容易理解，可以绑定多个事件，每个事件可以指定多个回调函数而且可以"去耦合decoupling",有利于事件模块化，缺点是整个程序都要变成事件驱动型，运行流程会变得很不清晰，阅读代码的时候，很难看出主流程 
    3. 发布public 订阅subscribe(publish-subscribe pattern)发布订阅模式又称为观察者模式 observer pattern 
        明显优于“事件监听”，因为可以通过查看"消息中心"了解存在多少信号、每个信号有多少订阅者，从而监控程序的运行 

# 异步操作的流程控制
    串行执行: 
    并行执行: 流程控制函数可以并行执行，所有异步任务同时执行
    并行与串行结合：设置一个门槛，每次最多只能并行执行n个异步任务，这样就避免过分占用系统资源

# 定时器
    JavaScript提供定时执行代码的功能，定时器timer:向任务队列添加定时任务
        setTimeout(): 多少毫秒后执行,返回一个整数表示定时器的编号，以后可以取消定时器;更多的参数，依次传入回调函数
        setInterval():每个一段时间就执行一次，也就是无限次的定时执行;常见用途是实现轮询;指定“开始执行”之间的间隔，并不考虑每次执行任务本身所消耗的时间,因此两次执行之间的间隔会小于指定的时间
    setTimeout和setInterval函数返回一个整数值，表示计数器编号
        clearTimeout():
        clearInterval():
        debounce:防抖动

        setTimeout和setInterval运行机制是将制定的代码移出本轮时间循环，等到下一轮时间循环，在检查是否到指定时间，意味着setTimeout,setInterval指定的回调函数必须等到本轮时间循环的所有同步任务都执行完，才会开始执行，由于前面的任务到底需要多少时间执行完，

# Promise对象
    Promise对象是JavaScript的异步操作解决方案，为异步操作提供统一接口，起到代理的作用proxy.充当异步操作与回调函数之间的中介，使得异步操作具备同步操作的接口，
    传统的回调函数写法使得代码混成一团，变得横向发展而不是向下发展.Promise就是解决这个问题，使得异步流程可以写成同步流程.
    Promise原本只是社区提出的一个构想，一些函数库率先实现这个功能，ECMAScript 6将其写入语言标准，目前JavaScript原生支持Promise对象
    
    Promise实例三种状态:
        1. 异步操作未完成   pending 
        2. 异步操作成功     fulfilled 
        3. 异步操作失败     rejected 
        fulfilled和rejected合在一起称为resolved已定型
    Promise.prototype.then() 添加回调函数 
    Promise优点在于让回调函数变成规范链式写法，Promise回调函数不是正常的异步任务，而是微任务microtask.正常任务追加到下一轮事件循环，微任务追加到本轮事件循环执行
```

DOM
---
```
DOM(Document Object Model文档对象模型)是JavaScript操作网页的接口,将网页转为一个JavaScript对象，从而可以使用脚本进行各种操作
DOM只是一个接口规范，可以使用各种语言实现，所以严格地说,DOM不是JavaScript语法的一部分，但是DOM操作是JavaScript最常见的任务，离开DOM，JavaScript就无法控制网页，

DOM最小组成单位叫做节点(node)
    Document: 整个文档树的顶层节点
    DocumentType:doctype标签 
    Element:网页的各种HTML标签 <body> <a>
    Attribute:网页元素的属性 class="right"
    Text:标签之间或标签包含的文本 
    Comment:注释
    DocumentFragment:文档的片段 
        parentNode: 父节点
        childNode: 子节点
        sibling: 同级节点
        firstChild: 第一个子节点 
        lastChild:最后一个子节点
        nextSibling:紧邻同级别后节点
        previousSibling:紧邻同级别前节点
所有DOM节点对象都继承Node接口，拥有一些共同的属性和方法
    Node.prototype.nodeType: 返回整数，表示节点类型 
        Node.DOCUMENT_NODE: 9 
        Node.ELEMENT_NODE: 1 
        Node.ATTRIBUTE_NODE: 2 
        Node.TEXT_NODE: 3 
        Node.DOCUMENT_FRAGMENT_NODE: 11 
        Node.DOCUMENT_TYPE_NODE: 10 
        Node.COMMENT_NODE: 8 
    Node.prototype.nodeName: 返回节点名称 
        文档节点document: #document 
        元素节点element: 大写标签名 
        属性节点attr: 属性的名称 
        文本节点text: #text 
        文档片段节点DocumentFragment: #document-fragment 
        文档类型节点DocumentType:文档的类型 
        注释节点Comment: #comment 
    Node.prototype.nodeValue:返回一个字符串，表示当前节点本身的文本值
        只有文本节点text,注释节点comment属性节点attr有文本值
    Node.prototype.textContent:返回当前节点和所有后代节点的文本内容
    Node.prototype.baseURI:返回一个字符串，表示当前网页的绝对路径
    Node.prototype.ownerDocument: 返回当前节点所在的顶层文档对象即document对象
    Node.prototype.nextSibling: 返回紧跟在当前节点后面的第一个同级节点
    Node.prototype.previousSibling:返回当前节点前面的距离最近的一个同级节点
    Node.prototype.parentNode:返回当前节点的父节点
    Node.prototype.parentElement:返回当前节点的父节点
    Node.prototype.firstChild|lastChild:返回当前节点的第一个子节点｜最后一个子节点
    Node.prototype.childNodes:返回一个类似数组的对象(NodeList集合)所有子节点
    Node.prototype.isConnected:返回一个布尔值，表示当前节点是否在文档之中 

    Node.prototype.appendChild(): 接受一个节点对象作为参数，将其作为最后一个子节点
    Node.prototype.hasChildNodes(): 返回布尔值，表示当前节点是否有子节点 
    Node.prototype.cloneNode(): 克隆一个节点，接受一个布尔值表示是否同时克隆子节点
    Node.prototype.insertBefore():将某个节点插入父节点内部的指定位置
    Node.prototype.removeChild():将当前节点移除该子节点
    Node.ptototype.replaceChild():将一个新节点替换当前节点的某个子节点
    Node.prototype.contains():布尔值
    Node.prototype.compareDocumentPosition():表示参数节点与当前节点的关系 
    Node.prototype.isEqualNode()|isSameNode():返回布尔值，检查两个节点是否相等
    Node.prototype.normalize():清理当前节点内部的所有文本节点text,去除空的文本节点，并且将毗邻的文本节点合并成一个，也就是说
    Node.prototype.getRootNode(): 返回当前节点所在文档的跟节点

# NodeList接口，HTMLCollection接口 
    NodeList : 可以包含各种类型的节点 
        NodeList实例是一个类似数组的对象，成员是节点对象
            Node.childNodes : 动态集合
            document.querySelectorAll()
        
    HTMLCollection : 只能包含HTML元素节点 
        HTMLCollection是一个节点对象的集合，只能包含元素节点element,不能包含其他类型的节点;HTMLCollection没有forEach方法，只能使用for循环遍历
        HTMLCollection实例都是动态集合，节点的变化会实时反映在集合中 

# ParentNode接口，ChildNode接口
    ParentNode接口表示当前节点是一个父节点，提供一些处理子节点的方法
        children: 返回一个HTMLCollection实例,成员是当前节点的所有元素子节点
    ChildNode接口表示当前节点是子节点，提供一些相关方法

```

JavaScript: The Keyword "This" for Beginners
--------------------------------------------
```
#1 Global Object: 
(mac: Cmd + Option + J) 
in the global scope, this refers to the global object.


#2 Declared Object 
When the keyword this is used inside of a declared object, the value of this is set to the closest parent object the method is called on. 

#3 The New Keyword
When the new keyword is used (a constructor), this is bound to the new object being created.

#4 Call, Bind, Apply 
we can actually set the value of this explicitly with call(), bind(), and apply(). 
Call takes any number of paramters: this, followed by the additional arguments 
Apply takes only two parameters: this, followed by an array of the additional arguments 

#Conclusion
    1. The value of this is usually determined by a function execution context. 
    2. In the global scope, this refers to the global object (the window object).
    3. When the new keyboard is used (a constructor), this is bound to the new object being created.
    4. We can set the value of this explicitly with call(), bind(), and apply() 
    5. Arrow Functions don't bind this -- instead this is bound lexically (i.e. based on the original context)
```

JavaScript: Arrow Functions for Beginners
-----------------------------------------
```
arrow function: 

#Benefit #1: Shorter Syntax 
    
regular function:
    function funcName(params) {
        return params + 2; 
    }

    funcName(2); 
    // 4

arrow function 
    var funcName = (params) => params + 2 
    funcName(2);
    // 4

# syntax of arrow functions 
(parameters) => { statements }

# If have no parameters, express an array function like this:
() => { statements }

# If have one parameter, the opening parenthesis are optional:
parameters => { statements }

# if returning an expression, you remove the brackets 
parameters => expression 

// is equivalent to:

function (parameters) {
    return expressions;
}

#Benefit#2: No binding of this 
Unlike a regualr function, an arrow function does not bind this. Instead, this is bound lexically(i.e. this keeps its meaning from its original context)

#Conclusion 
    1. Shorter Syntax 
    2. No binding of this
```

HOW TO START A NODE.JS PROJECT
------------------------------
```
$ node --version                                                                                                
v12.10.0
$ npm --version             
6.11.3

# npm: Node开发包管理器,主要职责是安装开发包和管理依赖项
# nvm: Node Version Manager - POSIX-compliant bash script to manager multiple active node.js versions
    
    1.Install nvm via Homebrew 
        $ brew install nvm 
    2.Add following line to your profile (.profile or .zshrc or .zprofile)
        # NVM 
        export NVM_DIR=~/.nvm 
        source $(brew --prefix nvm)/nvm.sh
    3. Reload Profile 
        $ source ~/.zshrc 
    4. Verify nvm is installed 
        $ nvm --version 
    5. Check all avaliable version by this command 
        $ nvm ls-remote 
    6. Install NodeJS(Recommended to install LTS version.)
        $ nvm instal --lts
    7. Check installed NodeJS in your machine 
        $ nvm ls 
    8. Set Global nodejs version to environment 
        $ nvm use default 

1. First, use npm to generate initial project
$ npm init  # builds a package.json file 
OR
$ npx license mit > LICENSE     # use the license package to download a license of choice, in this case the MIT license.
$ npx gitignore node            # uses the gitignore package to automatically download the relevant .gitignore file from GitHub's repo
$ npx covgen YOUR_EMAL_ADDRESS  # uses the covgen package to generate the Contributor Covenant and give your project a code of conduct that will be welcoming to all contributors
$ npm init -y                   # accepts all of the default options that npm init asks you about

2. CUSTOMISING npm init
$ npm config list   # check current npm config 
# author name, author email, author url, the license, and the version
$ npm set init.author.name "ChyiYaqing"
$ npm set init.author.email "ChyiYaqing@gamil.com"
$ npm set init.author.url "https://chyidl.com"
$ npm set init.license "MIT"
$ npm set init.version "0.0.1"

3. BUILDING YOUR OWN INIT SCRIPT 
    function node-project {
        git init 
        npx license $(npm get init.licese) -o "$(npm get init.author.name)" > LICENSE
        npx gitignore node 
        npx covgen "$(npm get init.author.email)"
        npm init -y
        git add -A 
        git commit -m "Initial commit"
    }
    You can take this function and add it to your ~/.zshrc OR ~/.bash_profile. or open a new command line window and run node-project.
```

Douglas Crockford: Why I removed comments from JSON 
---------------------------------------------------
```

```

Gulp
----
```
# Install the gulp command line utility 
$ npm install --global gulp-cli 

# Create a project directory and navigate into it 
$ npx mkdirp my-project 
$ cd my-project 

# Create a package.json file in your project directory 
$ npm init 

# Install the gulp package in your devDependencies  
$ npm install --save-dev gulp 

# Verify your gulp versions 
$ gulp --version 

# Create a gulpfile.js in your project root with these contents. 
$ vim gulpfile.js 
    function defaultTask(cb) {
        // place code for your default task here 
        cb();
    }

    exports.default = defaultTask 

# Test it 
$ gulp

# Result 
$ gulp
[15:29:47] Using gulpfile /Volumes/Time Capsule SD/Downloads/my-project/gulpfile.js                            
[15:29:47] Starting 'default'...                                                                                
[15:29:47] Finished 'default' after 67 ms
```

TypeScript vs JavaScript
------------------------
```
JavaScript: 动态类型语言：一个对象的类型在最终运行的时候才会决定和进行检测
TypeScript:允许在书写和编译代码时，对代码中对象的类型和使用进行规范和约束，以降低因类型错误而导致的bug;TypeScript最大特点就是静态类型，一般一个TypeScript项目发布时会编译成JavaScript,同时会发布一个d.ts文件，这个文件记录发布的这个JavaScript文件里的对象类型.

VS Code 使用下面几种方式寻找d.ts文件:
    1. 首先查看npm包本身有没有d.ts文件,使用TypeScript书写项目一般都会有d.ts文件，很多JavaScript框架虽然不是使用TypeScript维护，也提供d.ts文件 
    2. VS Code查看当前文件夹中是否有d.ts文件，如果使用某种npm包没有d.ts文件，可以自行书写
    3. 社区书写的d.ts文件，并且发布到npm @types 
    Auto Type Acquisition: 自动类型采集 
```
* JSDoc
> JSDoc:是一个文档规范工具通过在代码中写注释，然后可以生成相应的API文档，同时可以注释里标记对象的JavaScript类型，这样在阅读和使用代码时比较方便.
根据JSDoc注释提供的类型信息对类型进行检查和建议
```

```

Node.js Tutorial
----------------
> Node.js runs single-threaded, non-blocking, asynchronously programming, whichi is very memory efficient.
```
Include Modules: use the require() function with the name of the module;
    var http = require('http');
    exports keyword to make properties and methods available outside the module file.
```

* Built-in HTTP Module
```
Node.js has a built-in module called HTTP, which allows Node.js to transfer data over the Hyper Text Transfer Protocol (HTTP).
```

* Built-in File System Module 
```
The Node.js file system module allows you to work with the file system on your computer.
```

* Node.js - module.exports vs exports 
```
# Let's first take a look at what the module object is all about
$ vim run.js 
    exports.a = 'A';
    exports.b = 'B';
    console.log(module);
    console.log(exportss === module.exports);
    console.log(module.exports);
$ node run.js 
Module {
  id: '.',
  exports: { a: 'A', b: 'B' },      // exports is a reference to module.exports.
  parent: null,
  filename:
   '/Users/chyiyaqing/Dropbox/chyidlTutorial/root/javaScript/javaScriptTutorial/learn-node/run.js',
  loaded: false,
  children: [],
  paths:
   [ '/Users/chyiyaqing/Dropbox/chyidlTutorial/root/javaScript/javaScriptTutorial/learn-node/node_modules',
     '/Users/chyiyaqing/Dropbox/chyidlTutorial/root/javaScript/javaScriptTutorial/node_modules',
     '/Users/chyiyaqing/Dropbox/chyidlTutorial/root/javaScript/node_modules',
     '/Users/chyiyaqing/Dropbox/chyidlTutorial/root/node_modules',
     '/Users/chyiyaqing/Dropbox/chyidlTutorial/node_modules',
     '/Users/chyiyaqing/Dropbox/node_modules',
     '/Users/chyiyaqing/node_modules',
     '/Users/node_modules',
     '/node_modules' ] }

So, now exports is shortcut fro referencing module.exports, if your module is to export an object. It is a pretty much usless object if you module exports any other or you have assigned anything to module.exports.

// -- exports hello.js 
exports.anything = function() {
    console.log('I'm anything.');
};

// -- module.exports hello.js 
module.exports.anything = function() {
    console.log('I'm anything.');
};

// -- hello-runner.js 
const hello = require('./hello');

// let's see what's there in hello veriable 
console.log(hello); // {anything: Function}

hello.anything();   // I am anything.

Exports is just module.exports little helper, If there's something attached to module.exports already, everything on exports is ignored.
```

* Requireing modules in Node.js 
> Node uses two core modules for managing module dependencies
```
> const config = require('/path/to/file');
# When Node invokes that require() function with a local file path as the function's only argument. Node goes through the following sequence of steps:
    1. Resolving: To find the absolute path of the file 
    2. Loading: To determine the type of the file content.
    3. Wrapping: To give the file its private scope. This is what makes both the require and module objects local to every file we require.
    4. Evaluating: This is what the VM eventually does with the loaded code. 
    5. Caching: So that when we require this file again, we don't go over all the steps anthoer time. 

# Resolving a local path 
$ node 
> module 
Module {
  id: '<repl>',
  exports: {},
  parent: undefined,
  filename: null,
  loaded: false,
  children: [],
  paths:
   [  ] }
> module.paths 

# Requiring a folder
Modules don't have to be files, we can create a find-me folder under node_modules and place an index.js file in there. The same require('find-me') line will use that folder's index.js file 

An index.js file will be used by default When we require a folder.but we can control what file name to start with under the folder using the main property in package.json.
$ echo "console.log('I rule');" > node_modules/find-me/start.js 
$ echo '{"name": "find-me-folder", "main": "start.js"}' > node_modules/find-me/package.json 
$ node 
> require('find-me');

# require.resolve 
If you want to only resolve the module and not execute it, you can use the require.resolve function. it will not load the file, still throw an error if the file does not exist and it will return the full path to the file when found.
$ node 
> require.resolve('find-me')
'/Users/chyiyaqing/Dropbox/chyidlTutorial/root/javaScript/javaScriptTutorial/learn-node/node_modules/find-me.js'

# Relative and absolute paths 
relative paths(./ and ../)
absolute paths starting with /.

# Parent-child relation between files 
$ mkdir lib 
$ echo "console.log('In util', module);" > lib/util.js 

# exports, module.exports, and synchronous loading of modules 
In any module, exports is a special object.
the exports variable inside each module is just a reference to module.exports which manages the exported properties.

The module.exports object in every module is what the require function returns when we require that module.

The exports object becomes complete when Node finishes loading the module. The whole process of requireing/loading a module is synchronous.

# Circular module dependency - 

# JSON and C/C++ addons 
    .js > .json > .node(binary file). 
    However, to remove ambiguity, you should probably specify a file extension when requiring anything other than .js files.
$ node 
> require.extensions 
[Object: null prototype] { '.js': [Function], '.json': [Function], '.node': [Function] }
> require.extensions['.js'].toString()
'function(module, filename) {\n  var content = fs.readFileSync(filename, \'utf8\');\n  module._compile(stripBOM(content), filename);\n}'
> require.extensions['.json'].toString()
'function(module, filename) {\n  var content = fs.readFileSync(filename, \'utf8\');\n  try {\n    module.exports = JSON.parse(stripBOM(content));\n  } catch (err) {\n    err.message = filename + \': \' + err.message;\n 
   throw err;\n  }\n}'
> require.extensions['.node'].toString()
'function(module, filename) {\n  return process.dlopen(module, path.toNamespacedPath(filename));\n}'

# All code you write in Node will be wrapped in functions 
$ node 
>> require('module').wrapper
Proxy [ [ '(function (exports, require, module, __filename, __dirname) { ',
    '\n});' ],
  { set: [Function: set],
    defineProperty: [Function: defineProperty] } ]
// exports is defined as a reference to module.exports 
// require and module are both specifc to the function to be executed 
// __filename/__dirname variables will contain the wrapped module's absolute filename and directory path. 
$ echo "console.log(arguments)" > index.js 
$ node index.js 
[Arguments] {
  '0': {},  // exports 
  '1':      // require 
   { [Function: require]
     resolve: { [Function: resolve] paths: [Function: paths] },
     main:
      Module {
        id: '.',
        exports: {},
        parent: null,
        filename:
         '/Users/chyiyaqing/Dropbox/chyidlTutorial/root/javaScript/javaScriptTutorial/learn-node/index.js',
        loaded: false,
        children: [],
        paths: [Array] },
     extensions:
      [Object: null prototype] { '.js': [Function], '.json': [Function], '.node': [Function] },
     cache:
      [Object: null prototype] {
        '/Users/chyiyaqing/Dropbox/chyidlTutorial/root/javaScript/javaScriptTutorial/learn-node/index.js': [Module] } },
  '2':      // module 
   Module {
     id: '.',
     exports: {},
     parent: null,
     filename:
      '/Users/chyiyaqing/Dropbox/chyidlTutorial/root/javaScript/javaScriptTutorial/learn-node/index.js',
     loaded: false,
     children: [],
     paths:
      [ ' ] },
  '3':      // file path 
   '/Users/chyiyaqing/Dropbox/chyidlTutorial/root/javaScript/javaScriptTutorial/learn-node/index.js',
  '4':      // directory path 
   '/Users/chyiyaqing/Dropbox/chyidlTutorial/root/javaScript/javaScriptTutorial/learn-node' }

The wrapping function return value is module.exports. Inside the wrapped function, we can use the exports object to change the properties of module.exports, but we can't reassign exports itself because it's just a reference. 
    function (require, module, __filename, __dirname) {
        let exports = module.exports;
        // Your Code... 
        return module.exports
    }

# The require object 
$ vim print-in-frame.js 
const printInFrame = (size, header) => {
    console.log('*'.repeat(size));
    console.log(header);
    console.log('*'.repeat(size));
};

if (require.main === module) {
    // The file is being executed directly (not with require)
    printInFrame(process.argv[2], process.argv[3]);
} else {
    module.exports = printInFrame;
}

# All modules will be cached. 

```