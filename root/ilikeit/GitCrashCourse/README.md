Git Crash Course
================

Git is distributed version-control system for tacking changes in source code during software development. It is designed for coordinating work among programmer, but it can be used to track changes in any set of files. it goals include speed, data integrity, and support for distributed, non-linear workflows.

```
# Mac Install Git 
$ brew install git 

# Git Config --global 参数表示全局有效
$ git config --global user.name "Your Name"
$ git config --global user.email "email@example.com"

# 仓库 repository 
$ git init  # 把当前目录变成Git可以管理的仓库, 并创建.git目录

# 所有版本控制系统,其实只能跟踪文本文件的改动，但是图片、视频这些二进制文件，虽然能够由版本控制系统管理，但没办法跟踪文件的变化，只能把二进制文件每次改动串起来。

# 将文件添加到仓库
$ git add file|. 

# 查看仓库当前的状态
$ git status 

# 把文件提交到仓库 -m: 表示本次提交的说明
$ git commit -m "wrote a readme file"

# 查看difference 文件修改的内容
$ git diff somefile

# 显示提交日志 --pretty=oneline (使用SHA1)
$ git log --pretty=oneline 

# HEAD表示当前版本，上一版本HEAD^,上上版本HEAD^^,往前100版本HEAD-100
$ git reset --hard HEAD^  

# 查看历史命令，以便确定回到未来版本
$ git reflog 

# Working Directory 工作区 chyidlTutorial/  
# Repository 版本库 .git/ 
# 暂存区 .git/index 
# 指向master的指针 .git/HEAD  

# 添加文件到Git版本库需要分为两步执行
# 1. git add 将文件添加进去，实际上就是把文件修改添加到暂存区
# 2. git commit 提交更改，实际上就是把暂存区的所有内容提交到当前分支 

# Git跟踪并管理的是修改，而非文件 
$ git diff HEAD -- readme.txt  # 查看工作区和版本库最新版本的区别

# Discard changes in working directory 撤销文件在工作区的修改
$ git checkout -- <file>  # 回到最近一次git commit 或 git add时的状态 

# git reset HEAD <file> 可以把暂存区的修改撤销掉(unstage),重新放回到工作区 
# git reset 命令可以会退版本，也可以把暂存区的修改回退到工作区，使用HEAD时，表示最新的版本 

# git rm <file> 从版本库中删除文件 
# git checkout 其实是版本库的版本替换工作区的版本，无论工作区是修改还是删除，都可以"一键还原"


```
