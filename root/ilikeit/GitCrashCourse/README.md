Git Crash Course
================
> Git is distributed version-control system for tacking changes in source code during software development. It is designed for coordinating work among programmer, but it can be used to track changes in any set of files. it goals include speed, data integrity, and support for distributed, non-linear workflows.

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
# git checkout  .其实是版本库的版本替换工作区的版本，无论工作区是修改还是删除，都可以"一键还原"

# GitHub：本地Git仓库和GitHub仓库之间传输是通过SSH加密, Git支持SSH协议
$ git remote add origin git@github.com:xxx/xxx.git  # 远程仓库的名字就是origin,这时Git默认的名称 
$ git push -u origin master  # 将本地库的内容推送到远程，第一次推送加上-u参数,并关联本地库和远程库
$ git push origin master # 以后每次推送

# Git支持多种协议，默认git://使用ssh协议,https://支持https协议,使用https除了速度慢，还有每次推送都必须输入口令，但是某些只开放http端口的公司内部无法使用ssh协议，而只能使用https。
$ git clone git@github.com:xxx/xxx.git 

# master分支, HEAD指向当前分支,master指向提交.最开始情况下，master分支是一条线，Git用master指向最新的提交，在用HEAD指向master,就能确定当前的分支，以及当前分支的提交点

# 当我们创建新的分支，例如dev,Git新建一个指针dev,指向master相同的提交，再把HEAD指向dev,就表示当前分支在dev上。

# git checkout -b <分支名称> -b参数表示创建并切换 
$ git checkout -b chyi-dev == git branch chyi-dev && git checkout chyi-dev 

# git branch # 查看当前分支,会列出所有分支，当前分支前面会标记*号
$ git branch 

# git checkout master # 切换分支
# git merge chyi-dev #  合并指定分支到当前分支，(Fast-forward)
# git branch -d chyi-dev # 删除chyi-dev分支 

# 因为创建、合并和删除分支非常快，所以Git孤立你使用分支完成某个任务，合并后再删除分支，这和直接在master分支上工作效果是一样的，但过程更加安全

# git checkout -b chyi-feature 

# 
$ git merge chyi-feature  
Auto-merging readme.txt
CONFLICT (content): Merge conflict in readme.txt
Automatic merge failed; fix conflicts and then commit the result.

# 手动解决冲突后再提交

# git log --graph --pretty=oneline --abbrev-commit 查看分支合并图情况
$ git log --graph --pretty=oneline --abbrev-commit

*   be1e806 (HEAD -> master) conflict fixed
|\
| * e8abdb1 (chyi-feature) AND simple
* | ad767b8 & simple
|/
* eda6297 branch test
* a6e4f35 remove test.txt
* 24a6bc8 add test.txt
* 79c5a9f git tracks two changed
* 49e95f2 git tracks changed
* 5b96797 understand how stage works
* b3a7bcc append GPL
* aa489b0 add distributed
* 451c00b wrote a readme file
(END)

$ git branch -b chyi-feature  # 删除chyi-feature分支

# 合并分支时，Git会用Fast forward模式，但这种模式下，删除分支后，会丢失分支信息.如果要强制禁止Fast forward模式，Git会在merge时生成一个新的commit，这样，从分支历史上就可以看出分支信息. 
# 准备合并dev分支，--no-ff参数，表示禁止Fast forward,
$ git merge --no-ff -m "merge with no-ff" dev 

# 分支管理规则，master分支非常稳定,工作修改在dev分支上,工作同事之间在的 v分支上工作，并合并

# 合并分支时，加上--no-ff参数就可以用普通模式合并，合并的历史由分支，可以看出曾经做过合并，而fast forward合并看不出曾经做过合并.

# Git 提供stash功能,把当前工作现场“储藏"起来等以后恢复现场后继续工作.
$ git stash 

# git stash list 查看 
# git stash apply stash@{0} 恢复指定的工作区，git stash drop删除stash内容
# git stash pop  恢复工作区并stash内容删除 

# 修复bug时，通常会创建新的bug分支进行修复，然后合并，最后删除.当手头工作还没有完成时，先把工作现场git stash存储，然后修复bug，后在git stash pop回到工作现场

# git branch -D <name> 丢弃一个没有被合并的分支
# git remote  查看远程库的信息 fetch抓取, push推送的权限
$ git remote -v  #查看远程库信息
origin  ssh://xx@xxx/home/xx/GitRepository/chutils (fetch)  # 抓取
origin  ssh://xx@xxx/home/xx/GitRepository/chutils (push)   # 推送 

# 并不是一定要把本地分支推送到远程
# master 分支是主分支，因此要时刻与远程同步
# dev 分支是开发分支，团队所有成员需要在上面工作,所以需要远程同步
# bug分支只用于本地修复bug,没必要推送到远程
# feature是否推动到远程，取决于你是否合作开发 
$ git push origin master # 将本地提交推送到远程库 

# 创建远程origin/dev分支到本地  
$ git checkout -b dev origin/dev

#最新提交从origin/dev抓下来，然后在本地合并，解决冲突 
$ git branch --set-upstream-to=origin/dev dev 
$ git pull  

# 多人协作工作模式
# 1. 首先可以视图git push origin <branch-name> 推送自己修改
# 2. 如果推送失败，则因为远程分支比你的本地更新，需要先用git pull视图合并
# 3. 如果合并冲突，则解决冲突，并在本地提交
# 4. 没有冲突或解决掉冲突后，再用git push origin <branch-name>推送就能成功
#如果git pull提示no tracking information,则说明本地分支和远程分支的连接关系没有创建，用命令git branch --set-upstream-to <branch-name> origin/<branch-name>

# 本地创建和远程分支对应的分支，使用git checkout -b branch-name origin/branch-name, 本地和远程分支的名称最好一致 
# 建立本地分支和远程分支的关联 git branch --set-upstream branch-name origin/branch-name 

# 多人在统一分支上协作时，很容易出现冲突，即使没有冲突，后push不得不先pull，在本地合并，然后才能push成功
$ git rebase  # 将分叉的提交历史“整理”成一条直线，看上去更直观。缺点是本地分支提交已经被修改过

# 标签--版本库的快照,标签不能移动
$ git branch  # 切换需要打标签的分支上
$ git checkout master 

# git tag <name> 就可以打一个新的标签
$ git tag v1.0  

# git tag 查看所有的标签,标签不是按照时间顺序列出，而是按照字母顺序 
# git show <tag name> 查看标签信息 

# 创建带有说明的标签，用-a 指定标签名,-m 指定说明文字, 标签总是指向commit，如果这个commit既出现在master分支，又出现在dev分支，那么这两个分支都可以看到这个标签
$ git tag -a v0.1 -m "version 0.1 released" 1094adb

# git tag -d 删除标签 
$ git tag -d v0.1

# 推送本地某个标签到远程
$ git push origin v1.0 
# 一次性推送全部尚未推送到远程的本地标签
$ git push origin --tags

# 删除一个远程标签 
$ git push origin :refs/tags/v0.9 

# 如何使用GitHub 
# 参与一个开源项目git,你可以访问它的项目主页https://github.com/git/git,点击"Fork"，就在自己账号下克隆一个bootstreap仓库,然后从自己账户下clone： 
# 一定要从自己账户下clone仓库，这样才能推送修改
$ git clone https://github.com/chyidl/git.git  
# 如果修复一个bootstrap的Bug,或者新增一个功能，立刻就可以开始工作，然后网自己仓库推动，如果你希望git的官方库能接受你的修改，你可以在GitHub上发起一个pull request，当然对方是否接受你的pull request就不一定

# GitHub上，可以任意Fork开源仓库，自己拥有Fork后的仓库的读写权限，可以推送pull request给官方仓库来贡献代码.

# 自定义Git 配置文件 
# --global 参数是全局参数，这些命令对于所有的git仓库都有效,如果不加只针对当前仓库起作用，每个仓库的配置文件存放在.git/config文件中
$ cat .git/config
[core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true
[remote "origin"]
        url = https://github.com/chyidl/git.git
        fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
        remote = origin
        merge = refs/heads/master

# 当前用户的Git配置文件存放在用户主目录下的一个隐藏文件.gitconfig中

$ git config --global user.name 
$ git config --global user.email 
$ git config --global color.ui true  Git显示颜色 
$ git config --global alias.st status  配置别名 git status == git st 
$ git config --global alias.co checkout 
$ git config --global alias.ci commit 
$ git config --global alias.br branch 
$ git config --global alias.unstage 'reset HEAD' 
$ git config --global alias.last 'log -l'  配置显示最后一次提交信息
$ git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"  

# 创建特殊文件.gitignore文件，然后然后把忽略的文件名填进去，Git就会自动忽略这些文件
# 忽略文件的原则是:
# 1.忽略操作系统自动生成的文件 
#   Windows 会自动在有图片的目录下生成隐藏的缩略图文件
#   Thumbs.db ehthumbs.db Desktop.ini 
# 2.忽略变异生成的中间文件、可执行文件等
#   Python编译生成的.pyc, pyo, dist文件或目录
# *.py[cod] *.so *.egg *.egg-info dist build 
# 3.忽略自己带有敏感信息的配置文件 

# -f 强制添加到Git 
$ git add -f App.class

# 检查.gitignore是否合理
$ git check-ignore -v App.class 
```

Use vimdiff as git mergetool
----------------------------
```
```
