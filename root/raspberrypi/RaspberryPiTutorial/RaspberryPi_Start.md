树莓派
======

> 2006年,剑桥大学助教Eben Upton,树莓派基金会致力于计算机教育项目. ARM 是 “Acorn RISC Machine”的简称， RISC 是指ARM处理器对精简指令集的支持。 Intel采用的是CISC, 复杂指令集。 Intel处理器提供比ARM处理器多得多的指令。RISC支持的指令虽然基础，但总可以通过基础的组合来实现CISC处理器的功能。

> 1990年，Acorn Computer Company艾康电脑公司和Apple Computer Company苹果电脑公司联合成立ARM公司。

> Linux操作系统是林纳斯托瓦兹 Linus Torvalds 

```
显示CPU信息
$ lscpu  - display information about the CPU architecture 

显示内存使用情况
$ free -h - Display amount of free and used memory in the system 

显示磁盘信息
$ sudo fdisk -l - manipulate disk partition table 

显示所有USB外设
$ lsusb - list USB devices 

显示操作系统信息
$ uname -a 

显示网络连接信息
$ sudo  ifconfig - configure a network interface 

显示CPU+GPU温度
$ vcgencmd measure_temp

显示CPU核心电压
$ vcgencmd measure_volts core 

UNIX/Linux体统提供的文本交互界面
$ bash - GNU Bourne-Again SHell

确定命令对应的可执行文件
$ which date

定义别名
$ alias ll="ls -l"

了解命令类型
$ type pwd

查看当前Shell类型
$ echo $SHELL 

提供简短介绍
$ whatis  - display one-line manual page descriptions

帮助手册
$ man  - an interface to the on-line reference manuals 

帮助信息
$ info - read info documents

历史命令
$ history - GNU History Library 

终止停止 暂停
$ Ctrl+C Ctrl+Z

命令行配置工具
$ sudo raspi-config 

配置密码
$ sudo passwd pi 

配置Locale 修改/etc/default/locale手动添加
LANG=en_GB.UTF-8
LC_ALL=en_GB.UTF-8
LANGUAGE=en_GB.UTF-8 

配置Keyboard 修改/etc/default/keyboard 
XKBLAYOUT=us 

配置Wi-Fi 修改/etc/wpa_supplicant/wpa_supplicant.conf 

network={
ssid="xxx"
psk="xxx"
key_mgmt=WPA-PSK
}

更新固件 - 树莓派有许多硬件，比如Wi-Fi适配器，Bluetooth适配器,这些硬件都有特定的固件支持
$ sudo rpi-update 

软件升级与安装
$ sudo apt-get update  -- 获取最新的软件列表
$ sudo apt-get upgrade -- 升级已安装的软件 
$ sudo apt-get install mysql -- 安装软件 
$ sudo apt-get remove mysql -- 删除已安装的软件(不会删除配置文件)
$ sudo apt-get purge mysql  -- 彻底删除软件 

修改软件源服务器 /etc/apt/sources.list 

SSH登陆
$ ssh pi@ip_addr  -- 需要直到Raspberry pi IP地址, ifconfig 可以查看IP地址

局域网扫描工具查找局域网下所有的IP地址和MAC地址
$ arp -- manipulate the system ARP cache 

Bonjour 用于自动发现网络上的设备，可以实现局域网上的自动域名解析，在同一个局域网下可以用主机名.local形式找到对应的IP地址。

NAT端口映射 - 利用公网IP和端口号能对应唯一的私网IP和端口号，这种情况下，就能从外网连接到局域网中的树莓派了。

SSH反向隧道(Reverse Tunneling)技术，可以从外网远程登陆树莓派，首先让树莓派主动向公网服务器的某个端口发起SSH连接，形成一个SSH隧道，了解原理之后，我们可以自行实现一个类似的中继服务器，可以使用Amazon弹性云架设中继服务器，需要在云控制台中开放反向连接端口9527.从树莓派上用SSH命令建立反向隧道
$ SSH -R 9527 user@public_ip

文件传输
$ scp local.file pi@ip_addr:/home/  -- 将本地文件上传到raspberry 
$ scp pi@ip_addr:/home/ .  -- 将raspberry下载到本地文件

NTP服务 -- Network Time Protocol 用于网络时间同步,NTP通信分为服务端和客户端两方，客户端发出的数据包包含发出时的客户端的时间，服务器收到数据包并回复，在回复的数据包中，附加了服务器收到和发出数据包的时间，客户端收到回复后就可以获得网络延迟时间，以及自己和服务器的时间差，客户端依据此调整时钟，就可以与服务器时间保持同步.
$ sudo ntpq -np  -- 查看当前NTP服务器 
$ sudo service ntp status|start|stop 

时区设置
地球以15度的经度划分时区，一个时区使用统一的时间，向东跨过一个时区时间就要+1小时。

实时时钟 RTC Real time Colock
...

date
$ date +"%Y year %m month %d day" +号后面表示时间显示格式，%开头的标识符会用时间信息填充。
%a - 显示星期几的缩写Thu 
%A - 显示星期几的全程Thursday 
%b - 显示月份的缩写 Feb
%B - 显示月份的全程 February 
%d - 显示那一天 30 
%D - 显示日期，月/日/年 03/30/2019
%F - 显示日期, 年-月-日 2019-03-30 
%H - 显示24小时制的小时 14 
%I - 显示12小时制的小时 2
%j - 显示一年中的天数 89
%m - 显示月份，比如03
%M - 显示分钟, 比如14
%S - 显示秒, 47 
%N - 显示纳秒, 
%T - 显示24小时制的时间
%u - 显示一周中的那一天，周一是1
%U - 显示一年中的周数, 
%Y - 显示年份
%Z - 显示时区缩写

cron 规划任务
$ ps aux | egrep "[c]ron"  -- 获取cron守护进程
$ crontab -e 编辑规划记录，每一行为一条记录，以#开始的是注解，每一行记录分为6列,空格分隔，分别表示分钟(m, 0-59), 小时(h, 0-23), 天(dom, 1-31), 月(mon, 1-12), 星期几(dow, 0-6), 以及要执行的命令 
每个用户都有一个自己的crontab，当cron要执行规划时，会以相应的用户身份执行，
$ sudo crontab -e -u pi|root 
@reboot touch /home/pi/reboot.log -- 实现开机启动 

/etc/init.d 实现开机启动
Linux 系统中运行级别 0 - 关机，1 - 单用户,无网络连接，不运行守护进程，不允许非root用户登陆; 2 - 多用户无网络连接，不运行守护进程; 3 - 多用户，正常启动; 4 - 用户自定义; 5 - 多用户，带图形界面; 6 - 重启

Hard link 硬链接
$ unlink file.txt 
$ ln file.txt /home/pi/another_file.txt  # 创建硬链接 

Soft link软链接 
$ ln -s file.txt /home/pi/another_file.txt # 创建软链接 
$ file /home/pi/another_file.txt # 获知文件类型 

$ touch empty.txt # 新建一个空的普通文件 
$ mkdir good # 创建新目录 
$ rmdir good # 删除一个空目录

root 用户创建 
$ su - 切换root用户
$ sudo adduser tommy  # 创建新用户
$ su tommy 
$ sudo deluser --remove-home tommy # 删除用户
$ sudo groupdel genius # 删除用户组

用户信息文件(/etc/passwd)每一行代表一个用户，每一行用冒号分为7个部分
用户名:密码:UID:GID:描述:用户目录:登陆Shell 
pi:x:1000:1000:,,,:/home/pi:/usr/bin/zsh  密码"x"表示密码用密文形式保存在文件/etc/shadow. nologin表示拒绝登陆 
用户组的信息保存在(/etc/group)文件中.这个文件每一行代表一个组，每一行用冒号分割成4段信息
组名:组密码:GID:用户列表

文件权限管理
$ sudo chown pi:root file.txt  # 改变文件的拥有者和用户组
$ sudo chmod 755 file.txt # 改变文件的权限标志

文件搜索
$ find -- 递归遍历文件，搜索符合条件的文件
$ find / -name "*.c"  打印硬盘上所有文件后缀名为.c的文件
$ find . -not -name "*.c" 取反
$ locate grep 根据文件名寻找文件

Text Stream 文本流 
Byte字节 8bit Unix设计哲学中万物皆是文件 Everything is a file. 
Standard Input标准输入 Standard Output标准输出 Standard Error标准错误
Redirect重定向 
$ ls &> output_error.log  &>可以把标准输出和标准错误指向同一个文件
pipe 管道 借用管道可以把一个进程的输出变为另一个进程的输入

$ who am i 查看最近一次登陆时间和用户名
$ who 返回所有的已经登陆的用户 
$ groups 查找用户所属的组 
$ id 
```

蓝牙
---

> 蓝牙是一个使用广泛的无线通信协议，蓝牙的无线通信的频率是2.4GHz,和Wi-Fi一样，都属于特高频，相对于低频信号，高频信号的传输速度快，穿透能力强，但是传输距离受限制，使用低频的433MHz的对讲机设备，通信距离很容易超过百米。因此蓝牙常用与短距离无线设备。

> 蓝牙工作流程 广播/扫描 -> 连接 -> 数据通信 
```
广播/扫描: 通信一方向外广播自己的信息，另一方通过扫描知道自己周边的设备地址，以及是否可以连接.

连接: 通信一方向另一方发起连接请求，双方通过一系列的数据交换建立连接

数据通信: 蓝牙通信分为经典蓝牙(Class Bluetooth)、低功耗蓝牙(Bluetooth Low Energy)
    Class Bluetooth: 传输协议是串型仿真协议 RFCOOM,缺点是比较耗电
    BLE Bluetooth Low Energy: BLE把通信双方分为非对称的双方，尽量让其中的一方承担主要开销，减轻另一方的负担，
    Peripheral外设: 主动发起广播的设备
    Central中心设备：扫描设备
    BLE的数据传输协议是ATT协议和GATT协议，ATT是GATT的基础，ATT协议把通信双方分为服务端Server和客户端Client.客户端主动向服务器发起读写请求操作，ATT协议以属性Attribute为单位进行该数据传输，一个属性的格式有一下四部分:
    handle  |   type    |   value   |   permission 
    handle: 句柄，包含属性的唯一编号，长度为16位
    type: 属性类型，每中类型用一个UUID编号
    value: 属性值
    permission: 属性权限，无、可读、可写、可读写 
    ATT还提供通知Notification的工作方式，当服务器改变某个属性值时，可以主动通知订阅该属性值的客户端。

GATT协议构建在ATT协议之上，为属性提供组织形式，GATT协议最小组织单元是Characteristic特征.可以由数条属性组成，Service服务，服务和特征都是属性的组织形式，客户端可以向服务器请求服务和特征列表，然后对其进行操作

BlueZ是Linux官方的蓝牙协议栈
$ bluetoothd -v  # 检查BlueZ版本
$ sudo systemctl status bluetooth # 检查BlueZ运行状态
$ sudo systemctl start|stop bluetooth # 启动蓝牙
$ sudo systemctl enable bluetooth # 蓝牙跟随系统启动
$ bluetoothctl  # 进入BlueZ提供的shell 
[bluetooth]# list   -- 显示树莓派上可用的蓝牙模块
[bluetooth]# scan on -- 开启扫描
[bluetooth]# exit -- 推出bluetoothctl 
$ sudo hciconfig hci0 up -- 启动蓝牙模块
$ sudo hciconfig hci0 down -- 关闭蓝牙模块

Apple公司在BLE基础上推出iBeacon协议，iBeacon使用BLE的广播部分但不建立连接，一个遵从iBeacon协议的外设称为Beacon. Beacon会广播自己的身份信息和发射信号的强度。中心设备接收到广播后，除了可以获取Beacon的身份外，还能通过信号的衰减算出自己与Beacon的距离。

将RaspberryPi改造成Beacon，Beacon只使用蓝牙中的广播功能，应该关闭树莓派的扫描，打开广播，并且不接受蓝牙连接
$ sudo hciconfig hci0 noscan  -- 关闭扫描
$ sudo hciconfig hci0 leadv 3 -- 开始广播，并且不接受连接
将广播信息改为符合iBeacon协议的内容
0x08 - 说明整条信息是蓝牙命令
0x0008 - 说明后面的内容作为广播信息
1E - 广播信息开始的标志,广播信息最多31个字节，后面的广播信息分为两组：
    第一组: 02 01 1A : 02 表示改组信息的长度为2, 01: 表示改组信息是蓝牙控制标志, 
    第二组: 1A FF 4C 00 02 15 63 6F 3F 8F 64 91 4B EE 95 F7 D8 CC 64 A8 63 B5 00 01 00 02 C5 : 1A 表示该组信息长度26字节，FF: 表示蓝牙制造商的相关信息, 4C 00 : 制造商信息 Apple. 02 15: iBeacon协议标识，63 6F 3F 8F 64 91 4B EE 95 F7 D8 CC 64 A8 63 B5: 是设备的UUID 00 01: 主编号, 00 02: 次编号 C5: 说明蓝牙信号强度，即在1米处测得该Beacon的RSSI值
$ sudo hcitool -i hci0 cmd 0x08 0x0008 1E 02 01 1A 1A FF 4C 00 02 15 63 6F 3F 8F 64 91 4B EE 95 F7 D8 CC 64 A8 63 B5 00 01 00 02 C5 
$ sudo hciconfig hci0 noleadv 停止广播
$ sudo hciconfig hci0 piscan 恢复扫描
```

摄像头
-----
```
更新Rasbian 系统的软件源并更新
$ sudo apt-get update && sudo apt-get upgrade -y 

设置启动摄像头
$ sudo raspi-config 

摄像头拍照
$ raspistill -o image.jpeg 

摄像头录视频
$ raspivid -o video.h264 -t 10000  # 10s 视频

播放视频
omxplayer video.h264 
```

Linux 
-----
> Linux系统可以简单区分为内核程序和应用程序两部分，内核程序在Linux启动后就一直运行,内核程序有权调用配置计算机资源。内核之外就是应用程序。应用程序只有内核启动后才会运行。Linux Kernel接口按照POSIX(Portable Operating System Interface)标准制作，由于其他UNIX系统同样遵从POSIX标准，所以Linux可以很容易的和其他UNIX系统互通。

> GNU "GNU's Not UNIX"

> Linux 发行版 Debain/Ubuntu 

Bash 
----
```
变量赋值 
$ var='Hello World' 变量赋值,根据bash语法，赋值符号左右不留空格
$ now=`date`  # 把一个命令输出的文本直接赋值给变量 
$ another=$var # 将一个变量中的数据赋值给另一个变量
$ read name  # 用户可以直接向bash输入数据，使用read命令
$ echo $name # 打印变量name检查 

引用变量 ${} 
bash中把一段包含空格的文本当作单一参数需要用到单引号或双引号,可以在双引号中使用变量

数学运算
$ echo $((2 + (5*2)))  # bash会对其中内容进行数值运算

返回代码
$ echo $? 获知返回码

bash 脚本 -- 是一种复用代码的方式
bash脚本可以在行首用"#"符号来表示改行注释
$./test_arg.bash hello world $0 $1 $2 $3 方式获得bash脚本运行的参数, $0 是命令的一部分，$1代表参数hello, $2代表参数world. 
exit 命令设置脚本的返回代码,一个脚本正常运行完最后依据会自动返回代码0.脚本运行后，可以通过$?变量查询脚本的返回代码。

函数
定义函数my_info 
function my_info(){
    lscpu >> $1
    uname -a >> $1 
    free -h >> $1
}
调用函数
my_info output.file 

跨脚本调用
source命令的作用是在同一个进程中执行另一个文件中的bash脚本。

逻辑判断
$ test 3 -gt 2; echo $?  # gt greater than 
$ test 3 -lt 2; echo $?  # lt less than; eq equal than; -ne not equal 
$ test abc = abx; echo $? # 文本相同判断 
$ test abc != abx; echo $? # 文本不同
$ test -e a.out; echo $? # 检查文件是否存在
$ test -f file.txt; echo $? # 检查文件是否存在并且是否是普通文件
$ test -d myfiles; echo $? # 检查文件是否存在并且是否是目录文件
$ test -L a.out; echo $? # 检查文件是否存在并且是否是软连接文件
$ test -r file.txt; echo $? # 检查文件是否可读
$ test -w file.txt; echo $? # 检查文件是否可写 
$ test -x file.txt; echo $? # 检查文件是否可执行
$ test ! expression # 逻辑判断非
$ test expression1 -a expression2 # 逻辑判断与 
$ test expression1 -o expression2 # 逻辑判断或 

选择结构 
#!/bin/bash 
var=`whoami`
# 
if [ $var = "root" ]
then
    echo "You are root"
    echo "You are my God."
else
    echo "You are normal user."
fi
echo "The End"

在bash下，可以用case语法实现多程序块的选择执行
#!/bin/bash 
var=`whoami`
echo "You are $var"
case $var in 
root)
    echo "You are God."
;;
pi)
    echo "You are a happy user."
;;
*)
    echo "You are the Others."
;;
esac

循环结构
#!/bin/bash 
now=`date +'%Y%m%d%H%M'`
deadline=`date --date='1 hour' +'%Y%m%d%H%M'`
while [ $now -lt $deadline ]
do
    date
    echo "not yet"
    sleep 10 
    now=`date +'%Y%m%d%H%M'`
done
echo "now, deadline reached"

#!/bin/bash 
for user in pi root
do 
    echo $user
done 
$ seq 用于生成一个等差的整数序列,后面跟三个参数，第一个参数表示整数序列开始数字，第二个参数表示每次增加多少，第三个参数表示序列终点 

#!/bin/bash 
total=0
number=1
while :
do 
    if [ $number -gt 100 ]
        then
        break 
    fi
    total=$(($total + $number))
    number=$(($number + 1))
done
echo $total 
```

Linux 架构
----------
> 计算机启动之后，Linux的内核程序启动成为一个单一的内核进程，内核进程有权调用所有的计算机资源，当应用程序启动时，内核会分配给该应用程序一定的计算机资源，应用程序与硬件之间的互动，也必须经由内核进行。因此即使是一个应用程序，他的运行也离不开内核，内核程序工作在内核模式Kernel Mode, 应用程序工作在用户模式User Mode.
> 应用程序可以通过特定的接口调用内核功能，用户单次的内核调用，可以称为一次系统调用System Call.
```
接口的系统调用大约两百多种，每种系统调用都有特定的名称和调用方式
$ man 2 syscalls - Linux system calls 

常见的系统调用如下
read, 文件读取
write,文件写入
fork, 复制当前进程
wait, 等待当前进程完成
chdir, 改变工作目录 

库函数 
系统调用提供的功能很基础，使用起来很麻烦，一个给变量分配内存空间的简单操作就需要动用多个系统调用，为了方便，可以使用封装好的库函数Library Function.
函数是面向过程语言中复用代码功能的一种方式，所谓的库是一个文件，包含多个常用函数。在C语言中我们可以跨文件的调用库中的函数，
$ man 3 printf 查看printf的帮助文档 

Linux系统除了C语言标准库，还用POSIX标准库，目录/lib, /lib64 存放着Linux系统自带的库.用户可以在目录/usr/lib下安装额外的库.

应用程序是二进制可执行文件，在/bin, /usr/bin中 bin是指binary,即二进制,在linux中,应用程序位于整个架构的顶层，应用程序的进程会获得一块独立的内存空间，即进程空间.

进程空间: 程序段TEXT->全局变量Global Variable->堆Heap->未使用空间->栈Stack  
程序段TEST区域,进程启动后，会先把程序文件加载到进程空间的程序段中，程序文件是编译后的指令式程序，加载到程序段后，每个指令占据一个存储单元，并可以通过内存地址定位，随后，计算机会按照指令顺序依次执行每一条指令. 为了记录函数调用的可变信息，进程开辟的另一个栈Stack的内存空间.帧中存储的本地变量Local
Variable.当函数被调用，该函数的本地变量才在对应的帧中出现，当函数调用结束时，帧被清空，其中存储的本地变量自然会被清空。因此本地变量只能用来存储函数调用相关的数据.
帧中内容：返回地址，本地变量，参数
进程空间中还有全局变量和动态变量Global
Data，在C语言中，函数之外声明的变量就是全局变量，通常讲，全局变量只用于存储不变的常量。堆Heap用于存放动态变量，全局变量和动态变量的区别：全局变量的个数和类型在程序一开始就是确定的，全局变量区域的大小也是确定的，而动态变量可以在进程中产生和消失，当进程创建动态变量时，堆的空间就会增长，占据更多的内存空间，堆和栈是相互独立的区域，堆的空间不随着函数调用自动增长，或清空，每个函数都可以使用malloc系统调用在堆上创建动态变量，这个系统调用返回的是动态变量的内存地址。函数之间可以通过参数或者返回值来交换该地址，而从跨函数地共享数据，本地变量无法实现上述功能。当不再需要某个动态变量时，可以通过free系统调用释放动态变量占据的内存空间。
C语言中常见错误是内存泄漏Memory Leakage.就是没有释放不再使用的动态变量，导致进程空间可用内存不足。

信号是一种进程传递信息的方式
Ctrl+C 中断运行的进程 SIGINT (中断Interrupt)前台进程 
Ctrl+Z 中止进程 SIGTSTP (暂停 Stop) 前台进程
Ctrl+\ 退出进程 SIGQUIT (Quit) 前台进程
每个Shell最多有一个前台程序，前台程序会阻塞Block Shell,Shell 可以有很多个后台程序，后台程序不会阻塞Shell命令.

$ ps aux | grep '[p]'ing  # 找到ping命令对应进程的PID
pi 10939  0.0  0.2   5056  2036 pts/3    S+   11:22   0:00 ping localhost
$ kill 10939  # kill 命令中断程序 Kill命令可以向系统中任意个进程发信号， 
$ kill -s SIGTSTP 11153 
$ kill -l # 查看完整的信号列表

信号机制
信号是Linux系统的重要机制，信号的本质就是内核传递给进程的一个整数，每个整数代表一种信号,信号最终都是由内核写入目标进程，信号保存在内核空间，进程执行系统调用正处于内核模式，查看内核空间的代价最小，如果有信号，那么进程会执行对应信号操作，这称为信号处理Signal Disposition.从信号生成到信号处理这段时间，信号处于等待Pending状态。
进程的信号处理有一下三种情况:
    无视信号: Ignore Signal: 信号被清除，进程本身不采用任何特殊的操作
    默认操作: Default Action: 每个信号对应有一定的默认操作，
    捕获信号：Catch Signal: 根据信号，执行程序中自定义的操作 

#!/bin/bash 
WANNA_QUIT=false 
function handle_exit {
    if [ "$WANNA_QUIT" = true ]; then
        echo "Bye."
        exit 0
    else
        WANNA_QUIT=true
        echo "Press Ctrl+C again to quit."
    fi
}
# trap命令捕获信号, drop 工作方式是异步Asynchronous
trap "handle_exit;" SIGNINT 
while true
    do
        echo hello
        sleep 1
done

Synchronous 同步, Asynchronous 异步，异步编程用于处理像信号这样出现时机不确定的事件 
```

进程
----
```
计算机开机时，Linux内核只创建一个名为init的进程，在Linux运行期间，会有很多其他新进程，Linux内核不直接创建其他新进程，除了init进程之外，都是通过fork机制创建的。

fork分叉，就是从老进程中复制处一个新进程,老进程继续运行成为新进程的父进程Parent Process, 新进程成为老进程的子进程Child Process.
$ ps -o pid, ppid,cmd  # 查看当前Shell下进程 
从任何一个进程出发，循着PPID不断向上追溯，总会发现源头是init进程，因此Linux的所有进程构成一个树状结构.，这个树状结构以init为根，
$ pstree  # 显示树莓派整个进程树 
$ ll /sbin/init -> /lib/systemd/systemd 

Linux 应用程序可以通过fork系统调用来创建新进程，两者的进程空间完全相同，fork系统调用一次会返回两次，一次返回到父进程，把子进程的PID作为返回值交给父进程，如果fork失败，就会返回一个负值给父进程。另一个返回到子进程，用0作为返回值，通过检查fork调用的返回值是否为0，进程就可以知道自己是否是子进程。
父进程可以通过fork返回值知道子进程的PID，进程可以通过PPID知道父进程是谁。
进程空间记录进程的数据和状态，当进程fork时，Linux需要在内存中分配新的进程空间给新的进程。原有进程空间中的所有内容，如程序段、全局数据、栈、堆都要复制到新的进程空间中。而且fork还会复制进程描述符Process Descriptor.之前提到的PID，PPID和信号当前工作目录，环境变量，已经打开文件的相关信息，信号mask和disposition都存在与进程描述符中，
父进程和子进程描述符有很多信息不同
    PID，PPID
    进程运行时的相关信息在子进程中重置为0
    父进程的文件锁在子进程中被清空
    父进程的未处理信号在子进程中被清空
当某个进程终结时，父进程会获得通知，进程空间随即被清空，然而，进程附加信息会保留在内核空间，即使一个进程终结，他还会在内核中留下痕迹，删除进程对应内核信息的重任就落在父进程身上。
孤儿进程Orphand Process: 孤儿进程会过继给init进程，进程init是所有的孤儿进程的父进程。而对孤儿进程调用wait责任就转交给init进程.
僵尸进程Zombie Process: 

进程间通信IPC Inter-process Communication 
  一种原始的IPC方式就是进程间通过文件来交换信息，即一个进程往文件里写数据，另一个进程从文件中读出数据,这种文件读写效率低，此外多进程同时写入一个文件很容易造成文件混乱
    信号也算是一种IPC,一个进程发出信号，放入目标进程的描述符，另一个进程进程进行系统调用，在自己描述符中看到该信号，两个进程通过信号进行简单的数据交换。信号无法大量交换数据。
    管道，直接把一个进程的输出和另一个进程的输入连接起来，基于管道的进程间数据交换发生在内核空间，与信号类似，也是通过内核空间绕开进程空间的独立性限制。Linux创建管道的方式是通过fork机制，管道基于文本流，打开和操作方式类似与Linux中文件。管道遵循“先进先出”的队列数据结构。从而保证信息的有序传输。
$mknod {文件名} p  # 创建命名管道 
$mknod /tmp/named-pipe p  # 在临时文件夹创建一个命名管道 
$tail -f /tmp/named-pipe # 
$echo hello >> /tmp/named-pipe 
消息队列 Message Queue :可以有多个进程往队列中放入消息，也可以有多个进程从队列中取出消息。消息队列一旦创建，会一直留在内核空间中，直到某个进程删除该队列，在使用消息队列时，要注意及时删除队列，以免造成内核空间的浪费.

```

