Offline Download
================

Aria2
-----
> Aria2是一款轻量级的命令行下载工具，支持包括HTTP，BT在内常见的下载协议
```
$ aria2c http://google.com 
$ aria2c http://xxxtorrent # 通过BT下载文件 
$ aria2c 'magent:?' # 使用磁力链接下载文件 

$ sudo apt-get install screen
$ screen # 新建会话 
$ aria2c http://  # 在新建的会话中，输入下载命令开始下载 
$ Ctrl+A+D #  卸载当前会话 
$ screen -r # 重新加载会话 
```
