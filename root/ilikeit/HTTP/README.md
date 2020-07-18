HTTP - Hyper Text Transfer Protocol
===================================
> 超文本传输协议
```
WEB: World wide web 
URI: 统一自阿远标识符，互联网资源唯一身份 
HTML: 超文本标记语言，描述超文本文档 
HTTP: 超文本传输协议，用来传输超文本
  HTTP/0.9: 纯文本格式 
    GET: 请求/响应 断开连接
  
  HTTP/1.0: 
    1. 增加HEAD，POST 方法。 
    2. 增加响应状态码，
    3. 协议版本号概念
    4. HTTP Header(头部)
    5. 传输数据不再仅限于文本

  HTTP/1.1:
    1. 增加PUT，DELETE新防范 
    2. 增加缓存管理和控制 
    3. 连接管理 允许持久连接 
    4. 允许响应数据分块chunked 可以传输大文件
    5. 强制要求Host头

  HTTP/2: (SPDY协议)
    1. 二进制协议
    2. 可以发起多个请求，废弃1.1里管道 
    3. 使用专门算法压缩头部，减少数据传输量 
    4. 允许服务器主动向客户端推送数据
    5. 增加安全性 

  HTTP/3: (QUIC协议)
    
HTTP 是一个用在计算机世界里的协议，使用计算机能够理解的语言确立了一种计算机之间交流通信的规范，以及相关的各种控制和错误处理方式
HTTP 协议是一个"双向协议"
HTTP 是一个在计算机世界里专门用来在两点之间传输数据的约定和规范
HTTP是一个在计算机世界里专门在两点之间传输文字、图片、音频、视频等超文本数据的约定和规范

HTTP 
  TCP/IP协议栈 
    IP协议实现寻址和路由
    TCP协议实现可靠数据传输
  DNS协议实现域名查找 
  SSL/TLS协议实现安全通信 

TCP/IP 网络分层模型
  application layer HTTP 
    传输单位则是消息或报文
  transport Layer   TCP/UDP -- 传输层 保证数据在IP地址标记两点之间“可靠传输”
    TCP: 有状态协议 需要先建立连接然后才能发送数据，而且保证数据不丢失不重复
    UDP: 无状态协议 不需要事先建立连接就可以任意发送数据，但不保证数据一定发送到对方
    TCP 数据是连续的字节流，有先后顺序 
    UDP分散的小数据包，是顺序发 乱序收
    TCP层传输单位是段segment 
  internet layer    IP  -- 网络层 -- 
    传输单位是包 packet
  link layer        MAC -- 链路层 -- 负责以太网/WiFi底层网络上发送原始数据包 工作在网卡
    传输单位是帧 Frame
```

HTTP 协议工作的全过程
--------------------
```
“三次握手”建立与Web服务器的连接
  [SYN]
  [SYN, ACK]
  [ACK]
GET / HTTP/1.1 
TCP 协议层面确认，刚才的报文收到
"HTTP/1.1 200 OK "
HTTP/1.1 长连接特性: 默认不会立即关闭连接
1. 浏览器从地址栏输入中获得服务器的IP地址和端口号
2. 浏览器用TCP的三次握手与服务器建立连接 
3. 浏览器想服务器发送拼好的报文 
4. 服务器收到报文后处理请求，同样拼好报文再发给浏览器 
5. 浏览器解析报文，渲染输出页面

域名解析会有多级缓存
  浏览器缓存
  操作系统缓存 
  本地域名解析文件/etc/hosts 
  根DNS
  顶级DNS
  权威DNS层解析

CDN 缓存网站大部分静态资源
动态资源 CDN无法缓存 
负载均衡设备先访问系统里缓存服务器 通常有memory缓存 Redis 

1. HTTP 协议基于底层的TCP/IP协议，所以必须要用IP地址建立连接 
2. 如果不知道IP地址，就要用DNS协议去解析得到IP地址，否则就会连接失败 
3. 建立TCP连接后会顺序收发数据，请求方和应答方都必须依据HTTP规范构建和解析报文 
4. 为了减少响应时间，整个过程中的每一个环节都会有缓存，能够实现短路操作 
5. 虽然现实中HTTP传输过程非常复杂，但理论上仍然可以简化成实验里的

报文结构:
  1. TCP 报文实际传输的数据之前附加20字节的头部数据[发送方的端口号、接收方的端口号、包序号、标志位、窗口大小]数据部分一般1460字节
  2. HTTP 请求报文和响应报文结构基本相同
    1. 起始行 start line: 描述请求或响应的基本信息 -- request line : 描述客户端想要如何操作服务器端资源
      GET / HTTP/1.1\r\n 
      1. 请求方法: GET/POST 
      2. 请求目标: URI 标记请求方法要操作的资源
      3. 版本号: 标示报文使用的HTTP协议版本
      4. CRLF 换行
    2. 头部字段集合 header: 使用key-value 形式更详细地说明报文
    3. 消息正文 entity: 实际传输的数据
  HTTP 协议规定报文必须有header 但可以没有body 0D0A header 和 body之间有一个空行

  HTTP协议对header大小没有限制，但是各个浏览齐都不允许过大的请求头，因为头部太大可能会占用大量的服务器资源，影响运行效率
  
  服务器响应状态:
    1. 版本号: 标示报文使用的HTTP协议版本 
    2. 状态码: 
    3. 原因: 作为数字状态码的补充

  头部字段: key-value形式 HTTP头字段非常灵活，不仅可以使用标准的Host,Connection也可以任意添加自定义头，这就给HTTP协议带来无限的扩展可
    1. 字段名不区分大小写，
    2. 字段名不允许出现空格，可以使用连字符"-"不能使用下划线
    3. 字段名后面紧接着":"不能有空格

  常用头字段:
    1. 通用字段: 在请求头和响应头里都可以出现 
      Date: HTTP报文创建时间
    2. 请求字段: 仅能出现在请求头里，进一步说明请求信息或额外的附加条件
      Host: HTTP/1.1 要求出现的字段 ：请求应该由那个主机处理
      User-Agent: 描述发起HTTP请求的客户端,服务器可以依据它返回合适此浏览器显示的页面
    3. 响应字段: 仅能出现在响应头里,补充说明响应报文信息
      Server: 表述当前正在提供Web服务的软件名称和版本号
      X-Powered-By: 非标准字段， 表示服务器使用的编程语言
    4. 实体字段: 实际上属于通用字段，专门描述body额外信息
      Content-Length: 表示报文里body的长度, 如果没有字段 就是不定长，需要使用chunked方式分段传输

  Nginx 默认的请求头大小不能超过8K, 可以使用large_client_header_buffers 修改

HTTP/1.1:
  1. GET: 从服务器获取资源 
    URI后面使用"#" 可以在获取页面后直接定位到某个标签所在的位置
  2. HEAD: 获取资源的元信息
    HEAD的响应头与GET完全相同
    检查文件是否存在 
  3. POST: 向资源提交数据 新建 create 含义
  4. PUT: 修改 update含义 (资源对一个删除标记)
  5. DELETE: 删除资源
  6. CONNECT:要求服务器为客户端和另一台远程服务器建立一条特殊的连接隧道, 这时web服务器充当代理的角色
  7. OPTIONS: 列出可对资源实行的方法
  8. TRACE: 追踪请求 - 响应的传输路径 多对于HTTP链路的测试或诊断

安全: HTTP协议请求方法不会破坏服务器上资源，不会对服务器上资源造成实质的修改 
  GET/HEAD : 是安全的 只读操作 
  POST/PUT/DELETE: 会修改服务器上资源 增加或者删除数据 
幂等: 多次执行相同的操作，结果都是相同的 
  GET/HEAD: 幂等 
  DELETE: 幂等 
  POST: 新增或提交数据 多次提交数据会创建多个资源 所以不是幂等 
  PUT: 替换或更新数据 幂等

URI: Uniform Resource Identifier: 统一资源标识符
  URI = URL + URN 
  URI = scheme + host:port + path + query + fragment 
  scheme://host:port/path?query
  scheme: 协议名 - 资源应该使用那种协议
  :// authority: 资源所在的主机名 
  URI 真正的完整形态
    scheme://user:passwd@host:port/path?query#fragment 
      user:passwd@ : 身份信息 
      fragment: 片段标识符 -- 片段标识符仅能由浏览器这样的客户端使用，服务器看不到 
URL: Uniform Resource Locator: 统一资源定位符
URI转义规则直接把非ASCII码或特殊字符转换成十六进制字节值，然后前面加上% 
查询参数query也可以不使用"key=value"的形式，只是单纯的"key" 这样"value"就是空字符串

URI编码转义使用的是"%",而HTML转义使用的&# 

状态行:
  Version SP Status Code SP Reason CRLF 

RFC标准 -- 状态码 
  1xx: 提示信息 表示目前协议处理的中间状态，还需要后续操作 
    101 Switching Protocols: 客户端使用Upgrade头字段，要求HTTP协议的基础上改成其它协议继续通信
  2xx: 成功 报文已经收到并被正确处理 
    200 OK 
    204 No Content 响应头后没有body数据
    206 Partial Content: HTTP分块下载或断点续传的基础
  3xx: 重定向 资源位置发生变动 需要客户端重新发送请求
    301 Moved Permanently: 永久重定向 此次请求的资源已经不存在，需要该用新的URI再次访问 
      浏览器看到301优化更新历史记录、更新书签、直接使用新的URI访问 省去再次跳转的成本
    302 Found: 描述Moved Temporarily 临时重定向
    303 See Other: 重定向后请求改为GET方法，访问一个结果页面 避免POST/PUT重复操作
    location 指明后续跳转的URI
    304 Not Modified: 资源未修改，用于缓存控制 
    307 Temporary Redirect: 类似302， 重定向后请求的方法和实体不允许变动
  4xx: 客户端错误 请求报文错误 服务器无法处理 
    400 Bad Request: 请求报文有错误
    403 Forbidden: 服务器禁止访问资源
    404 Not Found: 
    406: Not Acceptable: 资源无法满足客户端请求的条件 
    408: Request Timeout: 请求超时 
    409: Conflict: 多个请求发生冲突，可以理解为多线程并发竞态 
    413: Request Entity Too Large: 请求报文里的body太大 
    414: Request-URI Too Long: 请求行里的URI太大 
    429: Too Many Requests : 客户端发送了太多的请求
    431: Request Header Fields Too Large: 请求头某个字段总体太大
  5xx: 服务器错误 服务器处理请求时内部发生错误
    500: Internal Server Error 
    501: Not Implemented: 标示客户端请求的功能还不支持
    502: Bad Gateway: 服务器作为网关或者代理时返回的错误码，表示服务器自身工作正常，访问后端服务器时发生错误
    503: Service Unavailable: 服务器当前很忙暂时无法响应服务器

HTTP  协议:
  1. HTTP 协议是一个“灵活可扩展” 的传输协议
  2. HTTP 协议是一个“可靠”的传输协议 "可靠传输是指网络基本正常的情况下数据收发必定成功"
  3. HTTP 协议是一个应用层协议
  4. HTTP 协议使用的是请求-应答通信模式
    请求-应答模式完全符合RPC(Remote Procedure Call) 工作模式 可以把HTTP请求处理封装成远程函数调用，导致WebService, RESETFUL gRPC等出现
  5. HTTP 协议是无状态
    状态就是客户端或者服务器里保存一些数据或者标志，记录通信过程中一些变化信息
    TCP 协议是有状态的：一开始CLOSED状态，连接成功后是ESTABLISHED状态，断开连接后是FIN_WAIT状态最后又是CLOSED状态
    UDP 无连接 无状态: 顺序发包乱序收包
    HTTP 有连接无状态: 顺序发包 顺序收包 
    以前的HTTP协议属于“无连接”特点，协议不保证连接状态，每次请求应答后都会关闭连接 HTTP/1.1改为默认启动keepalive长连接机制

MIME: Multipurpose Internet Mail Extensions 多用途互联网邮件扩展
1. text: 文本格式的可读数据
  text/html : 超文本文档 
  text/plain : 纯文本 
  text/css: 样式表
2. image: 图像文件
  image/gif: 
  image/jpeg: 
  image/png: 
3. audio/video: 音频/视频数据 
  audio/mpeg 
  video/mp4 
4. application: 数据格式不固定
  application/json 
  application/javascript 
  application/pdf 
  application/octet-stream: 不透明的二进制数据
5. Encoding type:
  gzip: GNU zip 压缩格式
  deflate: zlib 压缩格式 
  br: 专门为HTTP优化的新压缩算法

消息中间件MQ: RabbotMQ, ZeroMQ, Kafka 

HTTP 协议 Accept请求头字段 和 Content实体头字段
  客户端用Accept头告诉服务器希望接收的数据 
    Accept: 字段标记客户端可理解的MIME type
    Accept-Encoding: 标记客户端支持的压缩格式
    Accept-Language: 标记客户端可理解自然语言
    Accept-Charset: 字符集
    如果请求报文中没有Accept-Encoding 字段：表示客户端不支持压缩数据
  服务器用Content头告诉客户端实际发送的数据
    Content-Type: charset=
    Content-Encoding:
    Content-Language: 实际语言类型
    响应报文中没有Content-Encoding字段: 表示响应数据没有被压缩

语言类型和字符集:
  en-US: 美式英语
  en-GB: 英式英语
  zh-CN: 汉语

quality factor: 内容协商质量值

gzip 压缩算法通常指对文本文件有较好的压缩率，图片视频多媒体数据本身已经是高度压缩 -- Nginx gzip on 启动text/html 压缩 : 压缩率通常超过60%，
HTTP 协议中chunked 分块传输编码
  响应报文Transfer-Encoding: chunked 
  Transfer-Encoding: chunked  VS Content-Length: 两个字段不能同时出现

分块传输的编码规则:
  1. 每个分块包含两个部分 长度头和数据块
  2. 长度头是以CRLF (\r\n) 结尾的一行明文 16进制数字表示长度
  3. 数据块紧跟在长度头后，最后CRLF结尾 数据不包含CRLF
  4. 最后长度为0的块表示结束 0\r\n\r\n

HTTP协议 范围请求 range requests:
  Range: bytes=x-y  字节为单位的数据范围
    0-: 标示起点到终点 整个文件
    -1: 标示文档的最后一个字节
    -10:文档末尾倒数10哥字节
  Accept-Ranges: bytes 范围请求

下载工具中多段下载、断点续传基于HTTP范围查询
  1. 先发送HEAD 查询服务器是否支持范围请求 同时获取文件大小 
  2. 开N个线程 每个线程使用Range字段划分负责下载的片段 发请求传输数据 

多段数据:
  multipart/byteranges: 特殊的MIME类型

HTTP 连接管理
  HTTP 协议 0.9/1.0 通信过程采用简单的"请求-应答"方式 short-lived connections 
  HTTP 协议 1.1 通信过程采用长连接 持久连接 persistent connections keep alive connection reuse 
  HTTP/1.1 中连接都会默认启用长连接
    Connection: keep-alive 

TCP连接长时间不关闭，服务器必须在内存里保存状态，占用服务器的资源
keepalive_requests: 设置长连接可发送最大请求次数 
  客户端: Connection:close 
  服务端通常不会主动关闭连接 但是可以使用策略 
  Nginx:
    keepalive_timeout -- 设置长连接超时时间 如果一段时间内连接没有任何数据收发就主动断开连接 避免空闲连接占用系统资源
    keepalive_requests: 设置长连接可发送最大请求次数 

TCP 建立连接三次握手：
  发送3个数据包 - 需要1个RTT 
TCP 关闭连接四次挥手：
  发送4个数据包 需要2个RTT

RTT: round-trip time which is the time it takes for a small packet to travel from client to server and back to the client 

队头堵塞: Head-of-line blocking 
  队头阻塞与短连接和长连接无关，是由HTTP基本的“请求-应答”模型所导致 
    
性能优化:
  并发连接 concurrent connections: 同时队一个域名发起多个长连接 用数量解决质量问题
  HTTP 协议建议客户端使用并发，众多浏览器并发上线提高6～8 

域名分片 domain sharding: 

利用HTTP的长连接特性队服务器发起大量请求，导致服务器最终耗尽资源“拒绝服务” DDOS 

Connection: Upgrade 配合状态码101 标示协议升级，从HTTP切换WebSocket 

浏览器使用者主动发起“主动跳转” 
  

服务器“被动跳转”
  重定向 Redirection 
  Location:/index.html  location 属于响应字段 必须出现响应报文 
  站内跳转 可以放心使用相对URI,跳转站外 必须使用绝对URI 
  
重定向“性能损耗” "循环跳转"
HTTP 协议规定 浏览器具有检测“循环跳转”的能力

Cookie:
  响应头字段 Set-Cookie  : 身份标识
    服务器会在响应头添加多个Set-Cookie 存储多个
  请求头字段 Cookie 

Cookie 是由浏览器负责存储 不是操作系统 所以"浏览器绑定"

Cookie 就是服务器委托浏览器存储在客户端里的一些数据，这些数据通常都会记录用户的关键识别信息
  Cookie 有效期: 
    Expires: 过期时间 deadline 
    Max-Age: 相对时间 (浏览器优先使用Max-Age)
  Cookie 作用域:
    Domain 和 Path 指定Cookie所属域名和路径
  HttpOnly: 此Cookie只能通过浏览器HTTP协议传输
  SameSite: 防范“跨站请求伪造XSRF攻击” 
  Secure: 表示Cookie仅能用HTTPS协议加密传输 

Cookie 最基本的用途就是身份识别 保存用户的登录信息 实现会话事务

Local Web Storage: 能比Cookie存储更多的数据 但是Cookie仍然是最通用，兼容性最强的客户端数据存储手段

Magic Cookie: 不透明的数据
Cookie基本使用数据库记录的形式存放Sqlite 
浏览器队Cookie的数量和大小有限制， 不允许无限存储，一般总大小不能超过4K 
如果不指定Expires 或 Max-Age 属性 Cookie尽在浏览器运行时有效 浏览器关闭就会失去效果 [会话Cookie、内存Cookie]

HTTP 传输的每个环节基本都会有缓存 
  客户端缓存 
    Cache-Control: max-age  标记资源的有效期
      max-age: Time-To-Live TTL: 时间的计算起点是响应报文的创建时刻，而不是客户端收到报文的时刻
      no_store: 不允许缓存 
      no_cache: 可以缓存，但是在使用之前必须要去服务器验证是否过期，是否有最新的版本 
      must-revalidate: 如果缓存不过期就可以继续使用 但过期需要到服务器验证 
    
    Cache-Control: max-age=0 刷新按钮 

  服务端缓存 

条件请求:
  if-Modified-Since 
    Last-modified 文件最后的修改时间
    ETag Entity Tag: 实体标签 --精确识别资源的变动情况 让浏览器能够更有效利用缓存
  if-None-Match 
  if-Unmodified-Since: 
  If-Match 
  If-Range 

“没有消息就是好消息，没有请求的请求 才是最快的请求”

HTTP代理:
  代理服务本身不产生内容，而是处于中间位置转发上下游的请求和响应，具有双重身份
  反向代理: 在传输链路中更靠近源服务器，为源服务器提供代理服务
  "计算机科学领域的任何问题，都可以通过引入一个中间层来解决, 如果一个中间层解决不了问题，那就在一个中间层"
  代理中负载均衡算法:
    轮训:
    一致性哈希:
  代理服务器可以执行：
    健康检查: 使用心跳机制监控后端服务器 
    安全防护: 保护被代理的后端服务器 限制IP地址或流量
    加密卸载: 对外网使用SSL/TLS加密通信认证，在安全的内网不加密，消除加解密成本 
    数据过滤: 拦截上下行的数据 ，任意制定策略修改请求或响应。
    内容缓存: 

  Via: 标示代理身份 解决客户端和源服务器判断是否存在代理的问题 
    服务器IP地址应该保密，关系到企业的内网安全
    客户端的真实IP地址 方便访问控制 用户画像 统计分析
    X-Forwarded-For: 为谁而转发, 追加请求方的IP地址 最左边IP地址就是客户端的地址 
    X-Real-IP: 

  代理协议:
    The Proxy Protocol: 
    HAProxy:定义的代理协议
      v1: 明文 PROXY TCP4 请求方IP 应答方IP 请求方端口 应答方端口 \r\n 
      v2: 二进制格式

代理软件：
  HAProxy
  Squid 
  Varnish 

缓存代理:
  RPS: Request per second: 
  HTTP 服务器缓存功能主要由代理服务器来实现 源服务器系统内部虽然
  缓存代理身份特殊，即是客户端、又是服务器 可以使用客户端缓存控制策略也可以用服务器端的缓存控制策略
  区分客户端缓存和代理缓存 
    private: 标示缓存只能在客户端保存 
    public: 标示缓存完全开放
    s-maxage: share maxage 限定代理上缓存多久
    no-transform: 代理会对缓存下来的数据做优化

max-stale:代理缓存过期也可以接收，但不能过期太多
min-fresh:缓存必须有效 必须在x秒

HTTP 天生明文特点，整个传输过程完全透明 任何人都能够在链路中截获 修改 或者伪造请求/响应报文 数据不具有可信性
通信过程：
  机密性: Secrecy/Confidentiality 
    encrypt:加密
      key: 密钥
      plain text/clear text 明文 
      cipher text: 密文 
      decrupt: 解密 
    对称加密:
      加密和解密时使用的密钥都是同一个 
      RC4、DES、3DES、AES、ChaCha20 
      AES: Advanced Encryption Standard 高级加密标准 
      加密分组模式: 算法使用固定长度的密钥加密任意长度的明文 
      AEAD Autenticated Encryption with Associated Data: 
      密钥交换问题: 只用对称加密算法 无法解决密钥交换的问题
      分为块加密算法: block cipher : DES AES 块加密
      流加密算法:stream cipher : RC4 Chacha20
    非对称加密:
      公钥：Public key 
      私钥：Private key 
      公钥和私钥单向性，都可以用来加密解密，但公钥加密后只能用私钥解密 反过来 私钥加密后只能用公钥解密
      RSA - 推荐2048 bit -- 安全性基于“整数分解” 使用两个超大素数的乘积作为生成密钥的材料 
      ECC (Elliptic Curve Cryptography) 是非对称加密的 基于“椭圆曲线离散对数”
        ECC 在安全强度和性能上都有明显的优势 160位的ECC相当于1024位的RSA 224位的ECC相当于2048位的RSA
    混合加密方式:
      通信开始使用非对称加密：解决密钥交换的问题 
      然后使用随机数产生对称算法使用"会话密钥 session key" 在用公钥加密，对方拿到密文后用私钥解密 取出会话密钥 然后双方实现对称加密的安全交换，后续就不再使用非对称加密，全都使用对称加密
  $ openssl speed aes 
  $ openssl speed rsa2048 

  完整性: Integrity 数据在传输过程中没有被篡改 
  身份认证: Authentication 
  不可否认: Non-repudiation/Undeniable 

HTTPS: HTTP over SSL/TLS 
  HTTP运行在安全的SSL/TLS协议上 收发报文不在使用Socket API 而是调用专门的安全接口

SSL/TLS: 
  SSL: Secure Socket Layer 安全套接层 -- 会话层 
  TLS: Transport Layer Security 传输层安全 
    1. 记录协议 
    2. 握手协议 
    3. 警告协议 
    4. 变更密码协议 
    5. 扩展协议 
  cipher suite: 加密套件 
  OpenSSL:著名的开源密码学程序库和工具包 是SSL/TLS的具体实现
  除了HTTP，SSL/TLS承载其它应用协议 FTP->FTPS LADP->LDAPS 

实现完整性的手段是摘要算法Digest Algorothm:
  > 能够把任意长度的数据“压缩”成固定长度 而且独一无二的“摘要”字符串
  > 摘要算法理解成特殊的“单向”加密算法，只有算法，没有密钥 加密后的数据无法解密 不能从摘要逆推出原文
  散列函数
  哈希函数hash Function 
  MD5 (Message-Digest 5)
  SHA-1(Secure Hash Algo)
  SHA-2: 是一系列摘要算法的统称：常用SHA224， SHA256， SHA384 

摘要算法保证“数字摘要”和原文的完全等价，只需要在原文后附上摘要算法，就能保证数据的完整性 
> 散列表、数据校验、大文件比较 

哈希消息认证码(HMAC):

私钥+摘要算法=能够实现数字签名 
数字签名原理就是把公钥 私钥用法反过来，之前的公钥加密 私钥解密 转变为私钥加密 公钥解密；由于非对称加密效率太低，私钥只加密原文的摘要，这样运算量就小得多，而且得到的数字签名也很小，方便保管和传输 

CA (Certificate Authority 证书认证机构):
  DV: 域名级别可信 

TLS 协议:
  1. 记录协议: Record Protocol 所有的其它子协议都需要通过记录协议发出 记录数据可以在一个TCP包里一次性发出
  2. 警报协议: Alert Protocol 
  3. 握手协议: Handshake Protocl: 浏览器和服务器会在握手过程中协商TLS版本号，随机数，密码套件等信息，然后交换证书和密钥参数，最终双方协商得到会话密钥，用于后续的混合加密系统
  4. 变更密码规范协议: Change Cipher Spec Protocol: 

HTTPS:
  1. 连接时的非对称加密握手 
  2. 握手后的对称加密报文传输

在TCP建立之后，正式数据传输之前，HTTPS比HTTP增加一个TLS握手的步骤，最长可以花费两个消息往返2-RTT 

HTTPS连接是计算密集型 而不是IO密集型

会话复用TLS session resumption:
  Session ID 
```


Appendix
--------
```
1. DNS: -- Domain Name System 域名系统
  域名用"."分隔多个单词级别从左到右逐级升高
  根DNS 
  顶级DNS
  权威DNS
  本地DNS
  负载均衡: 因为域名解析可以返回多个IP地址，所以一个域名可以对应多台主机，客户端收到IP地址后，就可以使用轮询
  域名屏蔽: 对请求的域名不解析 
  域名劫持: 域名污染
  域名的总长度限制在253个字符以内，而每一个级域名长度不能超过63个字符
  域名是大小写无关，域名大多是两级或者三级，四级以上很少见

2. 底层协议:
  可靠数据传输 
  四层与七层模型 
  IPv4/IPv6 TCP/IP 
  TCP/IP协议实际上是一系列网络通信协议的统称
    TCP/UDP: 传输层: Transmission Control Protocl: 传输控制协议
      提供字节流形式的通信
    IP : 网络层 Internet Protocol: 解决寻址和路由问题
    ICMP 
    ARP
  UNIX Domain Socket 
  HTTP over TCP/IP 

3. Proxy
  代理Proxy是HTTP协议中请求方和应答方中间的一个环节，可以转发客户端的请求，也可以转发服务器的应答
  匿名代理: 外界只看到代理服务器
  透明代理: 传输过程中是透明开放，外界知道代理也知道客户端
  正向代理: 靠近客户端，代理客户端向服务器发送请求
  反向代理: 靠近服务端,代理服务器响应客户端的请求
  proxy协议-V1 -- HAProxy
  proxy协议-V2 -- HAProxy
  3.1: 负载均衡: 把访问请求均匀分散到多台机器，实现访问集群化
  3.2: 内容缓存,暂存上下行的数据，减轻后端的压力

4. URI/URL:
  URI: Uniform Resource Identifier 统一资源标识符
  协议名://主机名/路径
  URL: Uniform Resource Locator 统一资源定位符
  协议名 
  查询参数 
  编码 

5. HTTP/1.1 
  FRC文档
    RFC2616 
    RFC7230 
  请求/应答
    请求方法: GET HEAD POST 
    请求头+请求体 
    响应头+响应体
    状态码
  无状态 
  长连接机制 
  缓存 
  MIME 

6. HTTPS:
  HTTP over SSL/TLS 运行在SSL/TLS协议上的HTTP
  SSL/TLS 负责加密通信的安全协议
  SSL - Secure Socket Layer: 
  TLS - Transport Layer Security 
  对称加密
    AES
    ChaCha 
  非对称
    RSA 
    DH 
  摘要算法
    SHA-2 
  证书 
    CA 
    X509 
  SSL/TLS 
    SNI 
    OCSP 
    连接优化 

7.HTTP/2
  SPDY 
  HPACK
  Server Push
  gRPC 

8. HTTP/3 
  基于UDP QUIC 

9. 抓包工具 
  Wireshark: 网络抓包工具
  tcpdump: 
  telnet: 虚拟终端 基于TCP协议远程登陆主机, 模拟浏览器行为，连接服务器后手动发送HTTP请求

10. 编码 
  Base64 
  chunked 
  压缩 
    gzip 
    deflate 

11. WebSocket 
  全双工 
  二进制帧
  有状态 

12. 网络 
  局域网 
  广域网
  因特网
    FTP
    IMAP/POP3
    BT 
    Magnet 
  万维网
    www 

13. Web Browser aka: User Agent
  Chrome -- Google : HTTP/1.1 HTTPS. HTTP/2 QUIC 
  Firefox -- Mozila
  Safari  -- Apple 
  IE/Edge  -- Microsoft
  浏览器是一个HTTP协议的请求方
    HTML排版引擎--展示页面 
    JavaScript引擎实现动态效果
    开发者工具调试网页 
  wget, curl command line 

14. Web Server
  Nginx: 
    高性能、高稳定、易扩展
    OpenResty : 是基于Nginx强化包，除了Nginx还有许多功能 不仅支持HTTP/HTTPS还集成脚本语言Lua简化Nginx二次开发，方便快速搭建动态网关，
  Apache:
  Microsoft-IIS 
  Tomcat
    Java 
    Servlet容器 

15. CDN -- Content Delivery Network 内容分发网络
  应用HTTP协议的缓存和代理技术，代替源站响应客户端请求
  CDN: 提供负载均衡，安全防护，边缘计算，跨运营商网络
  扮演透明代理和反向代理
  负载均衡 
  就近访问 
  Squid/Varnish/ATS 

16. 爬虫
  crawler/spider 
  robots.txt -- 协议

17. HTML -- 
  HTML4 
  HTML5 

18. Webservice  -- W3C定义的应用服务开发规范
  RESETFUL JSON 
  SOAP 
  RPC 

19. WAF -- 网络应用防火墙
  应用层防护 
  访问控制 
  审计
  检测HTTP流量，防护Web应用的安全技术
  ModSecurity: 阻止SQL注入，跨站脚本攻击
```
