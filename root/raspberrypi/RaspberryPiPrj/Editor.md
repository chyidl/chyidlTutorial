Editor VS . 
===========

* Eclipse:
    - Eclipse 是最流行的Java IDE之一，插件开发的语言也是Java，但是Eclipse插件运行在主进程中，一旦插件的性能堪忧，就会影响Eclipse本身体验
* Atom VS Code: 
    - 插件开发语言都是JavaScript.
* Emacs:
    - 插件开发语言是Lisp， 
* Vim:
    - 插件开发语言是VimL 
* VS code: Visual Studio Code
    - 免费、开源的跨平台编辑器
    - 2011年，微软从IBM Erich Gamma, <设计模式>作者，2015年，Erich Gamma把Monano Editor移植到桌面平台上-Visual Studio Code.
    - VS Code继承Monaco Editor的设计原则，核心是做一个高性能的轻量级编辑器，个性化的功能交给插件系统完成，同时吸引Eclipse教训，把插件系统在主进程以外，高度可定制但同时可控.
    - VS Code 自带TypeScript和Node.js支持，VS Code为编程语言工作者提供统一的API，Language Server Protocol和Code Debugging Protocol每种语言都能够通过实现两个API和VS Code上得到类似IDE的开发和调试体验 
    - 稳定版Stable, 内部版Insiders
        * 命令面板 Cmd+Shift+P - 可以快速搜索命令并且执行 
            - 安装shell命令，在PATH中安装"Code"命令并执行
            - $ code --help 
            - $ code -r : 窗口重复利用
            - $ code -r -g <file:line[:character]> 打开文件然后滚动到文件中某个特定的行和列
            - $ code -r -d a.txt b.txt : 比较两个文件
            - $ ls | code -r - 接受管道中的数据 
        * 界面概览
            - 文件资源管理器 - Cmd+Shift+E 
            - 跨文件搜索 - Cmd+Shift+F 
            - 源代码管理 - Ctrl+Shift+G 
            - 启动和调试 - Cmd+Shift+D 
            - 管理扩展 - Cmd+Shfit+X 
            - 查看错误和警告 - Cmd+Shift+M
        * 光标移动
            - Option + 方向键: 光标移动单词开始末尾
            - Cmd + 方向键: 光标移动行首行尾
            - Cmd + Shift + \: 代码块的始末快速跳转 
            - Cmd + 上下方向键: 文档第一行、最后一行 
        * 文本选择: 需要按住Shift键，可以在移动光标的同时选中其中的文本 
            - Select to Bracket 
        * 删除操作: 
        * 自定义快捷键:
            - Cmd+Shift+P（打开命令面板） Open Keyboards Shotcuts (打开键盘快捷方法) 
        * Don't Repeat Yourself 
            - Cmd + Shift + K: 当前代码行删除 
            - Cmd + x: 剪切该行代码 
            - Cmd + Enter: 上一行插入 
            - Cmd + Shift + Enter: 下一行插入 
            - Option + 上下方向键: 上下移动整行代码 
            - Cmd + / : 添加注释 
            - Option + Shift + A: 注释整段代码
            - Option + Shift + F: 整个文档进行格式化
            - Cmd + K Cmd + F: 只有选中的代码才会被格式化 
        * 多光标
            - Cmd + D: 选中光标附近的单词，第二次会找到单词第二次出现的位置
            - Option + Shift + i: 选择多行，然后按下Option+Shift+i,每一行的最后都会创建一个新光标 
        * 文件跳转
            - Ctrl + Tab, Ctrl: 打开文件列表(罗列当前打开的所有文件)
            - Cmd + P: 搜索文件,选中文件按下Enter, Cmd + Enter
            - Ctrl + g: 行跳转 
            - Cmd + Shift + O: 文件中符号之间跳转
            - Cmd + T: 搜索多个文件中的符号
            - F12: 跳转definition定义处
            - Cmd + F12: 跳转Implementation实现处 
            - Shift + F12: 跳转Reference引用处
        * VS Code - 🖱️操作
            - 单击左键:移动当前光标到相应的位置
            - 双击鼠标左键:选中当前光标下单词
            - 三次击鼠标左键:选中当前一行代码
            - 四次按下鼠标左键:选中整个文档 
            - 悬停提示窗口: Cmd键-直接显示实现 
        * 代码自动补全、重构
            - VS Code自动补全由语言服务器提供
        * 代码片段 code snippet 
            - 代码片段是对常用代码的一个抽象，保留大部分不变的代码，然后吧需要经常变动的部分，换成变量
            - Tab Stop: 按下Tab键之后，光标移动到的位置
            - 占位符 $1: ${1:label} 代码片段中预先设置好的
        * 代码折叠/展开
            - Cmd + Option + [  // 折叠
            - Cmd + K Cmd + [   // 递归折叠 
            - Cmd + K Cmd + 0   // 当前编辑器所有代码一次性全部折叠
            - Cmd + Option + ]  // 展开 
            - Cmd + K Cmd + ]   // 递归展开
            - Cmd + K Cmd + J   // 当前编辑器所有代码全部展开
        * 小地图 Mini Map 
        * 面包屑 Breadcrumb
        * 单文件搜索
            - Cmd + F: Enter, Shift Enter 该女表存在在搜索框中
            - Cmd + G: 搜索的同时光标保留在编辑器中
            - 大小写敏感: Cmd + Option + C (Case)
            - 全单词匹配: Cmd + Option + W (Word)
            - 正则表达式匹配: Cmd + Option + R (Regex Expression)
            - Cmd + Option + F: 替换窗口
            - Cmd + Shift + F: 多文件搜索视图 
        * 编辑器设置
            - editor.lineNumber: 行号
            - editor.renderWhitespace: all 
            - editor.renderIndentGuides: 缩进参考线
            - editor.rulers:[120] 垂直标尺
            - editor.minimap.enabled: 控制是否显示小地图
            - editor.cursorBlinking 
            - editor.cursorStyle
            - editor.cursorWidth
            - editor.renderLineHighlight: all 
            - editor.tabSize: 制表符对应的空格长度 
            - editor.formatOnType:true 
            - files.defaultLanguage: Markdown
            - editor cursor: 光标渲染、多光标相关设置
            - editor find: 编辑器搜索相关的设置
            - editor font: 与字体相关的设置 
            - editor format: 代码格式化
            - editor suggest: 代码自动补全，建议窗口相关设置 
        * WorkBench: 工作台 
            - Problems Panel: 问题面板 
            - Output Panel: 输出面板 
            - Debug Console: 调试控制台
            - Terminal: 终端 
        * Cmd + Shift + P : Command Panel 
            - ...: Go to File 
            - #:Go to Symbol in WorkSpace 
            - >:Show and Run Commands 
            - debug: Debug Configure 
            - ::Go to Line 
            - edt: show all Open editors 
            - ext: Manager Extensions 
            - task: Run Task 
            - term: Show all open Terminals 
            - view: Open View 
            
            
            
