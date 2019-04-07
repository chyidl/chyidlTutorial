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

共享内存Shared Memory 
共享内存是效率最高的IPC方式，共享内存特被适用于大数据量的情况

套接字socket:一种常见的IPC方式，互联网上常用的网络协议都可以通过套接字的方式连接，从而连接分别位于两台计算机上的两个进程
```

多任务与同步
-------------
```
Linux系统是一个支持并发Concurrency操作系统，并发系统可以同时执行多个任务，并发系统必须解决同步的问题。

单核CPU计算机的并发通过分时Time-Sharing来实现，进程切换的工作是由操作系统负责，

多进程加上IPC就可以提供丰富的多任务协作方式，在一个进程中运行多线程Multi-Threading.多线程允许在一个进程中同时执行多个子任务。

进程描述符需要记录每个线程的相关信息，特别是他们的状态和进度
操作系统需要把适当的计算时间分配给进程，内核调度器在分配计算时间时，必须把各个线程考虑在内。
进程空间中必须有多个栈。栈中记录着函数调用的顺序，最下方的帧时唯一一个激活函数，既然多线程是多任务并发，那就意味着会有多个函数处于激活状态，并同时运行。
当程序创建一个新的线程时，必须为这个线程构建一个新的栈，每个栈对应一个线程，当某个栈执行到全部弹出时，对应的线程完成任务，因此多线程在进程中有多个栈，多个栈以一定的空白区域隔开，以备栈的增长，对于多线程来讲，由于同一个进程空间中存在多个栈，任何一个空白区域被填满都会导致栈溢出的问题。

进程空间中需要调整栈的部分，一个线程与其他线程共享内存中的程序段、堆和全局数据，由于多线程共享很多内存区域，他们都可以直接读写堆上的内容，线程间的数据共享变得很简单，因此多闲成数据交流成本要比多进程低很多

多进程和多线程都实现了并发，并发系统实现了多任务协作，但是很容易产生竞态条件Race Condition: 并发情况下，指令执行的先后顺序由内核决定，同一个线程内部，指令按照先后顺序执行，但不同线程之间的指令很难说清哪一个先执行。在并发系统中，如果运行的结果依赖于不同线程执行的先后顺序，则会造成竞争状态。

Synchronization同步：是指在一定时间内只允许某一个任务访问某一个资源，同步可以解决竞争态条件，多线程中可以通过互斥锁Mutex,条件变量Condition Variable，读写锁Reader-Writer Lock.来同步资源
    互斥锁Mutex: 是一个特殊的变量，有两种状态上锁，去锁，互斥锁一般被设定为全局变量，每个线程必须遵守互斥锁的上述规则，才能保证互斥锁发挥作用，如果某个线程不尝试获得锁而直接修改变量i那么互斥锁就失去保存资源的意义，互斥锁本身并不能硬性的阻止线程对i的修改 
    条件变量:
    读写锁:如果一个共享资源只有读取而没有写入操作，那么多个任务可以同时读取而不用担心竞态条件的发生，一旦有一个进程开始写入，那么其他读取和写入的进程必须等待该进程完成写入，才能继续操作，因此，读写锁包含两把锁，读锁R，写锁W，应用程序用R锁控制读取操作，如果一个线程获得R锁，读写锁允许其他线程继续获得R锁，而不必等待线程释放R锁，W锁用来控制写入操作，同一时间只能有一个线程获得W锁，获得W锁之前，线程必须等到所有持有共享读取锁释放掉各自的R锁，以免写入锁干扰其他线程的读取。
```

进程调度
--------
```
内核中安排进程执行的模块称为调度器Scheduler.
调度器可以切换进程状态Process State
    进程三种状态：
        就绪Ready: 进程已经获得CPU以外的所有必要的资源，进程空间、网络连接、 
        执行Running：进程获得CPU
        阻塞：进程由于等待某个事件而无法执行时，放弃CPU，进入阻塞状态

Linux调度器负责两件事情：一件事选择某些就绪的进程来执行;另一件事打断某些执行中的进程，变回就绪状态。并不是所有的调度器都有第二种功能，支持双向状态切换的调度器被称为抢占式PreEmptive调度器。

上下文切换Context Switch: 进程在CPU中切换执行的过程，内核承担上下为切换的任务，负责存储和重建进程被切换之前的CPU状态。从而让进程感觉不到自己的执行被中断，应用程序的开发者在编写计算机程序时就不用专门写代码处理上下文切换。

进程优先级：
    实时进程 Real-Time Process: 优先级高、需要尽快被执行的进程， 
    普通进程 Normal Process: 优先级底，更长的执行时间进程；普通进程根据行为的不同分为：互动进程Interactive Process,批处理进程Batch Process.

实时进程由Linux操作系统创建；普通用户只能创建普通进程，进程的优先级是一个0到139的整数，数字越小，优先级越高。0-99属于实时进程，100-139属于普通进程。
 
$nice -n -20 ./app # nice修改进程的默认优先级,默认优先级会被变成执行时的静态优先级Static Priority.调度器最终使用的优先级根据的是进程的动态优先级

动态优先级 = 静态优先级 - Bonus + 5 

Linux调度策略：
     最原始的调度策略是按照优先级排序，等运行完在运行优先级底的一个，这种策略完全无法发挥多任务系统的优势
    Linux2.4内核推出O(n)调度器，n表示操作系统中活跃进程数，o(n)表示这个调度器的时间复杂度和获取进程的数量成正比。O(n)调度器吧时间分成大量的微小时间片Epoch。每个时间片开始的时候，调度器会检查所有处在就绪状态的进程，调度器计算每个进程的优先级，然后选择最高优先级的进程执行。一旦被调度器切换到执行，进程可以不被打扰地用尽这个是时间片，如果进程没有用尽时间片，那么该时间片的剩余时间会增加到下一个时间片中。

    Linux2.6内核开始使用O(1)调度器，调度器每次选择要执行的时间都是1个单元的常熟，和系统的进程数无关，O(1)调度器的创新之处在于它会把进程按照优先级排好，放入特定的数据结构中，选择下一个要执行的进程时，调度器不用遍历进程，就可以直接选择优先级最高的进程。O(1)时间分配给优先级120一下的进程时间为(140-priority)x20毫秒;
    优先级120及以上的进程时间为(140-priority)x5毫秒.O(1)调度器会用两个队列存放进程，一个队列称为活跃队列，用于存储那些待分配是金啊片的进程，另一个队列称为过期队列，用于存放那些已经享用过时间片的进程。
    CFS完全公正调度器Completely Fair Scheduler取代O(1)调度器。CFS增加一个虚拟运行时的记录，在每次选择要执行的进程时，不是选择优先级最高的进程，而是选择虚拟运行时最少的进程。红黑树的数据结构可以高效的找到虚拟时间最少的进程，本质上将，虚拟运行时间代表了该进程已经消耗的多少CPU时间
```

内存
----
```
内存时计算机的主存储器，内存为进程开辟进程空间，让进程保存数据;内存的最小存储单位字节，内存地址Memory Address;线性地址：Linear Address: 地址空间的范围和地址总线Address Bus的位数相关，CPU通过地址总线来向内存说明想要存取数据的地址。内存的存储单元采用随机读取存储器RAM:Random Access
Memory.随机存取表示存储器的读取时间和数据所在的位置无关，进程需要调用内润中不同位置的数据，如果数据读取时间和位置相关，那么计算机很难控制进程的运行时间，因此随机存取特性时内存称为主存储器的关键因素。内存的缺点是不能持久地保存数据，一旦断电，内存中的数据就会消失，因此，计算机即使有内存这样一个主存储器也需要SD卡这样的外部存储器来提供持久存储空间。
    虚拟内存：进程不能直接访问内存，在Linux下，进程不能直接读写内存中的地址，进程只能访的地址只能是虚拟内存地址Virtual Memory Address,操作系统会把虚拟内存地址翻译成真实的内存地址，这种内存管理方式，叫做虚拟内存Virtual
    Memory.进程的虚拟内存地址相互独立。因此，两个进程空间可以有相同的虚拟内存地址。应用程序对无力内存地址一无所知，只知道通过虚拟内存地址来进行数据读写，程序中表达的内存地址也都是虚拟内存地址，程序中表达的内存地址都是虚拟内存地址。虚拟内存地址的存在，内存共享变得简单，操作系统可以把同一个物理内存区域对应到多个进程空间，这样不需要任何数据赋值，多个进程就可以看到相同的数据，
    内存分页：记录虚拟内存和物理内存对应的关系最简单的办法就是把对应关系记录在一张表中，为了让翻译速度足够快，这个表必须加载到内存中，Linux采用分页Paging的方式记录对应的关系，所谓的分页就是以更大尺寸的单位页Page来管理内存，通常没页大小为4KB,Linux把物理内存和进程空间都分割成页。无论是虚拟页还是物理页，一页之内的地址都是连续的，这样一个虚拟页和一个物理页对应起来页内的数据就可以按顺序一一对应起来。偏移量Offset,偏移量实际上表达该字节在业内的位置，地址的前一部分则是页编号，操作系统只需要记录页编号；
    内存分页制度的关键在于管理进程空间和物理页的对应关系，操作系统把对应关系记录在分页表Page table，Linux采用多层的数据结构，多层的分页表能够减少多需的空间，单层分页表必须存在于连续的内存空间，多层分页表可以散布在内存的不同位置。这样操作系统可以利用零碎的空间存储分页表，
$ getconf PAGE_SIZE # 获取内存页的大小
```
磁盘
----
```
外部存储设备的容量一般比较大,可以持久地保存数据，存储的数据不会随着断电而消失，外部存储器的读写速度要比内存慢，传统的机械式批判进行随机读写时，效率比连续读写更低，机械式磁盘由多个盘片和磁头组成，每个盘片上有多个可以存储数据的磁道，如果读写的区域不连续，磁盘需要改变磁头位置来切换磁道。因为SD卡没有类似的机械结构，所以随机读写和连续读写的速度差距不想磁盘那马达。

Linux下常见的ext2fs, ext3fs, ext4fs,Windows采用FAT文件系统和NTFS，每种文件系统都有自己一套数据管理策略：
    通过名字和层级来组织文件，比如文件名和路径
    提供操作文件的接口，比如查找，新建，删除，读取和写入文件 
    提供权限功能：比如文件保护和文件共享 
    同一个外部存储区可以划分为一个或多个分区 Partition,每个分区可以用一种文件系统格式来管理，RaspberrySD烧录Rasbian系统后SD上的存储空间就会划分为两个分区，一个空间时启动分区，采用FAT32形式的文件系统，启动分区主要用于开机启动，空间较小，剩下的空间是主分区，采用ext4fs形式的文件系统。
    挂在Mounting: 文件树上的某个目录在存储器的物理分区对应起来，这个目录称为挂载点Mounting Point.从挂载点开始向下的子文件树，实际上对应挂载的物理分区

Linux系统的挂载信息保存在/etc/fstab中
$ cat /etc/fstab 
    /boot下的数据存放启动分区，其他分区存放在主分区/ 

一个外部存储器必须经过挂载，才能加入操作系统的文件树，
$ sudo fdisk -l 
$ sudo umount /dev/sda1 # 卸载挂载点 
设置设备的默认挂载点,配置文件在/etc/fstab 
    设备名称: 一般是/dev/xxx 
    挂载点: 一般是/media/ 
    文件系统格式: ext4 
    设备参数: defaults,noatime 
    一个不再使用的参数: 0 
    磁盘检测设置: 1为根文件系统,2为永久挂载磁盘,0为可插拔移动设备
$ sudo df # 查看文件系统的挂载情况 

存储器开始部分块会有一个总的分区表Partition Table.记录存储器的基本信息，比如Block大小，存储器的编号，可用空间，块是存储器的读写单元，

ext文件系统：ext4称为第四代拓展文件系统Fourth Extended File System.
    引导块Boot Block: 引导块有引导加载程序Boot Loader.帮助计算机在开机时加载Linux内核，引导加载程序存储有内核的相关信息，比如内核名称和内核所在位置
    Super Block:超级快：超级快记录文件组织的信息，包括文件系统的类型，inode的数目，快的总数和空闲数量，超级快对于文件系统来说至关重要，如果超级快损坏，会导致整个分区的文件系统损坏 
    Inodes表和数据块Data Block: 一个inode表中有多个inode,是描述文件存储信息的数据结构，

$ stat example.txt  # 查看文件的inode编号

FAT 文件系统: 引导块+文件分配表FAT:File Allocation Table,FAT文件洗头膏中还有一个区域专门记录FAT根目录的信息，其他的子目录则以文件的形式保持，目录中每条记录对应一个文件，除了文件名和文件属性，还记录了文件的起始数据块的位置。

文件描述符: File Descriptor: 进程描述符中有一个文件描述符表，记录该进程所有已经打开的文件，文件描述符说明目标文件在文件描述表中的位置，文件表File Table.

/boot挂载FAT32格式化的启动分区，里面的文件用于树莓派的开机启动，计算机一般会从主办BIOS上读取存储的程序，BIOS知道主办上的硬件，从默认存储设备中读取最开始的512字节的数据，MBR Master Boot Record.
通过MBR，计算机知道要从该存储器设备的那个分区找引导加载程序，引导加载程序存储有操作系统的相关信息，比如操作系统名称，内核所在位置，随后引导加载程序加载内核，操作系统开始工作。树莓派的开机方式有别于普通计算机，树莓派没有BIOS，树莓派电路板上携带启动程序，板载启动程序会挂载FAT32的启动分区，并运行引导程序bootcode.bin，负责下一阶段的启动工作，会从SD卡上找到GPU固件start.elf，将固件写入GPU，GPU在start.elf的指挥下，会读取系统配置文件config.txt和内核配置文件cmdline.txt,并启动内核文件kernel.img.该内核加载成功后，处理器开始工作，系统启动正式开始

引用程序相关：应用程序都编译成二进制的可执行文件，位于名为bin的目录下，/sbin保存了系统启动、修复、恢复所必须的应用程序。/usr/local/bin和/usr/local/sbin用来保存应用程序的地方，保存自己编写或手动编译安装的应用程序。

/etc: 保存关键的操作系统配置文件，这些配置文件可以改变操作系统级别的行为，
    /etc/default/locale : 本地设置
    /etc/default/keyboard: 键盘设置
    /etc/localtime: 时间与时区配置
    /etc/modules: 可加载模块配置 
    /etc/init.d: 初始化相关文件
    /etc/rc.local: 初始化脚本 
    /etc/passwd: 用户列表，用户密码 
    /etc/group:用户组列表 
    /etc/motion/motion.conf: Motion的配置文件
    /etc/apt/sources.list: apt-get软件源配置
    /etc/wpa_supplication/wpa_supplicant.conf: Wi-Fi设置 
    /etc/virc: vi初始化设置

/proc 虚拟文件系统，直接对应内存上的内核空间，
    /proc/cpuinfo: 保存CPU信息 
    /proc/meminfo: 保存内存使用信息

/dev 保存设备文件,每个设备文件对应一个设备，
/mnt: 用于挂载额外的文件系统
/media:挂载可插拔设备
/var:保存系统中会动态增长的数据
    /var/log: 系统日志和应用程序日志
/tmp: 下的文件会自动清空，因此/tmp下的文件基本不需要维护，不同版本的Linux系统会选择不同的时间清空临时文件，Raspbian会在开机后清空/tmp,

树莓派上的三种电子元件都有存储数据的功能
    CPU缓存:一级缓存32KB,二级缓存512KB
    内存：1GB 
    SD卡存储:大于4GB
分级存储的设计，兼顾了读取速度、储存容量和计算机的稳定性
缓存记录Cache Entry
缓存命中Cache Hit
缓存缺失Cache Miss 
缓存替换策略：
    最少使用LFU,Least Frequently Used 
    最久没有使用 LRU,Least Recently Used: CPU为每一个缓存记录增加一个计数，当CPU读缓存时，LRU会把命中记录的计数清零，而其他记录的计数增加1，如果一条记录长期没有被读取，那么他的计数就会越来越大，在选择牺牲者时，CPU缓存会选择计数最大的记录作为牺牲者。
    最早被缓存FIFO,First In First Out 
    随机替换:Random Replacement 

页交换Page Swap
虚拟内存可以把一部分的外部存储器空间转换成内存空间，让应用程序可以虚拟地增加内存大小，页交换Page Swap就是进程空间和外部存储空间以页为单位交换数据，虚拟内存是一套管理数据和数据地址的方法，也可以用于外部存储空间的管理，操作系统可以把一部分外部存储空间换分为页，成为交换空间Swap

Space.操作系统按照管理内存的方式管理交换空间，物理内存和交换空间，外部存储器的读写速度慢，为了保证读写效率，应用程序只用在物理内存中的虚拟内存，当程序访问的数据恰好位于交换空间时，内核会启动页交换，把交换空间的页转移到物理内存中，随后内核把分页对应到物理内存位置，并通知应用程序继续进行数据操作。

交换空间：交换分区和交换文件两种形式
    交换分区就是一个独立的存储器分区作为交换空间，没有文件系统完全以页的方式进行管理
    交换文件时文件系统中的特殊文件，占据的空间以页的方式进行管理
$ sudo swapon -s # 查看交换空间
$ sudo mkswap /dev/hdb1 # 将/dev/hdb1编程交换分区 
$ sudo swapon /dev/hdb1 # 用swapon命令激活交换分区 
$ sudo dd if=/dev/zero of=/var/swapfile bs=2014 count=1048576 # 使用dd创建一个1GB的文件 
$ mkswap /var/swapfile 调用交换文件
$ swapon /var/swapfile 激活交换文件，方交换文件成为可以使用的交换空间

页缓存Page Cache
$ free # 查看内存页缓存空间的大小
内存为进程打开文件保留缓冲区Buffer,用于收集待写入文件的文本，缓冲区采用先进先出的策略，先写入的字符会被先取出，刷新Flush缓冲区，操作系统的内核提供缓冲区，因此，很多时候用write()系统写一个字符到文件，字符并没有真正存入文件，计算机会在多个条件下刷新缓冲区:
    缓冲区填满了数据
    文件关闭
    进程终结
    文本中出现换行符
    该文件出现数据读取
Linux内核内置了缓冲读写功能，不过，鉴于缓冲时一种简单而有效的策略，应用程序也可以自己在进程空间中安排缓冲区，来把多次操作合并成一次操作，实际上，C标准库中的标准IO函数，就负责在读写过程中管理进程空间的缓冲区，IPC和网络通信也经常用到相似的缓冲策略，以提高通信效率。
```

网络协议
--------
```
协议Protocol: 
    点报使用莫尔斯码通信，求救信息SOS，短短短 长长长 短短短

协议分层：
    互联网通信协议以TCP/IP协议为核心，并通过多种多样的协议形式向上下游延伸
    1.物理层： Physical Layer,光纤，电缆，或者电磁波，随后计算机将利用相应的物理层协议，把物理信号解读成二进制序列
    2.连接层:Link Layer,把二进制序列分割成帧Frame,所谓帧是一段有序的二进制序列，连接层协议能帮助计算机识别二进制序列中所包含的帧，规定特殊的01组合作为帧的开始和结束，连接层协议还规定了帧的格式，帧中包含收信地址SRC,source,和送信地址DST Destination,还能够探测错误的校验序列。
        以太网Ethernet和Wi-Fi时现在最常见的连接层协议，分别用于有限网络和无线网络，树莓派上有两个网络接口控制器NIC:Network Interface Controller. 就是所谓的网卡，连接层协议中帧的收信地址只能是本地局域网内，更远距离的通信还需要更高层的网络层实现
    3.网络层:Network Layer
        路由器Router:一个路由器有多个网，因此路由器可以同时接入多个网络，并理解相应的连接层协议。在帧经过路由到达另一个网络的时候，路由会读取帧的信息，并改写发送到另一个网络，由于树莓派上有多个网卡，他也可以充当一个路由器。路由将分离的局域网网络连接成覆盖全球的互联网。
    4.传输层:Transport Layer,TCP 和UDP协议都使用端口号Port Number，TCP和UDP是两种不同的传输层协议
    5. 应用层 Application Layer： HTTP协议，DNS协议 IMAP协议
```

网络诊断
--------
```
$ sudo ip address show # 显示接口名称，接口类型，接口IP地址，硬件MAC地址 
$ sudo arp -a # ARP协议用在局域网内部，借用ARP协议设备可以知道局域网内的IP-MAC对应关系
$ sudo apt-get install arping # 安装arping工具 
$ sudo arping -I wlan0 192.168.31.39 # 经过wlan0接口发送ARP 请求，查询IP地址192.168.31.39设备的MAC地址
$ sudo apt-get install arp-scan工具 
$ sudo arp-scan -l # 查看整个局域网内所有IP地址对应的MAC地址
$ sudo apt-get install tcpdump # 安装tcpdump工具
$ sudo tcpdump -i en0 arp  #监听eth0接口的ARP协议通信 

ping命令是向某个IP地址发送ICMP协议的ECHO_REQUEST请求，收到该请求的设备将返回ICMP回复
$ ping 192.168.31.39 # 如果ping请求到某个IP地址，则说明IP地址的设备可以经过网络层顺利到达,许多网络设备会禁止ICMP
$ sudo dhclient -v -r  #跟新DHCP租约，设备将释放IP地址，再从DHCP服务器重新获得IP地址
$ sudo ifconfig wlan0 192.168.1.106 up # 将接口wlan0的IP地址设置成192.168.1.106
$ sudo nano /etc/hdcpcd.conf # 编辑/etc/dhcpcd.conf文件，在文件末尾加入
    interface eth0 
    static ip_address=192.168.1.106 

$ netstat -nr #显示路由表,从路由表找到网关
$ traceroute 8.8.8.8 # 追踪到达IP目的地址的全程路由 
$ sudo traceroute -I 8.8.8.8 # 通过ICMP协议追踪路由
$ sudo traceroute -T -p 80 chyidl.com # 通过TCP协议，经过80 端口追踪路由，TCP协议的默认端口80很少会被禁用 #跟新DHCP租约，设备将释放IP地址，再从DHCP服务器重新获得IP地址

网络监听：
Linux下，tcpdump是一款网络抓包工具，可以监听网络接口不同层的通信，并过滤出特定的内容，特定协议、特定端口
$ sudo tcpdump -i eth0 # 监听eth0所有的通信 
$ sudo tcpdump -A -i wlan0 # 使用ASCII显示wlan0接口的通信内容
$ sudo tcpdump -i wlan0 'port 8080' # 显示wlan0接口的8080端口的通信
$ sudo tcpdump -i wlan0 src 192.168.31.39 # 显示来自192.168.31.39的通信 
$ sudo tcpdump -i wlan0 dst 192.168.31.39 and port 80 # 显示wlan0接口80端口，目的地为192.168.31.39的通信

域名解析：DNS在域名和IP之间进行翻译，DNS故障会导致用户无法通过域名访问某个网址
```
