//
// linux_namespace.c
// docker_base
//
//        __|__
// --o--o--(̊)--o--o--
// C is the bext programming language
//
// Created by Chyi Yaqing on 03/30/19.
// Copyright © 2019. Chyi Yaqing. All rights reserved.
//
/*
 * Linux Namespace 是Linux提供的一种内核级别环境隔离方法{UTS、IPC、mount、PID、network、User}
 * 
 * Linux Namespace有一下几种
 *  分类                系统调用参数      
 *  Mount namespaces    CLONE_NEWNS
 *  UTS namespaces      CLONE_NEWUTS
 *  IPC namespaces      CLONE_NEWIPC  -- $ ipcmk -Q 创建一个IPC Queue $ ipcs -q 
 *  PID namespaces      CLONE_NEWPID
 *  Network namespaces  CLONE_NEWNET
 *  User namespaces     CLONE_NEWNET
 *  User namespaces     CLONE_NEWUSER
 *
 * clone() - 实现线程的系统调用，用来创建一个新进程，并可以通过涉及上述参数达到隔离
 * unshare() - 使某个进程脱离某个namespace
 * setns() - 把某个进程加入到某个namespace
 * 
 * */

#define _GNU_SOURCE 
#include <sys/types.h>
#include <sys/wait.h>
#include <sys/mount.h>
#include <stdio.h>
#include <stdlib.h>
#include <sched.h>
#include <signal.h>
#include <unistd.h>

/* 定义一个给 clone 用的栈， 栈大小1M */
#define STACK_SIZE (1024 * 1024) 
static char container_stack[STACK_SIZE];

char* const container_args[] = {
    "/bin/bash",
    NULL
};

int container_main(void* arg)
{   
    /* 查看子进程的PID，我们可以看到其输出子进程的 pid为 1 */
    printf("Container [%5d] - inside the container!\n", getpid());
    sethostname("container", 10); /* 设置hostname */
    /* 重新mount proc文件系统到 /proc下 */
    // system("mount -t proc proc /proc");
    /* 容器以tmpfs 内存盘 格式，重新挂载/tmp目录 */
    mount("none", "/tmp", "tmpfs", 0, "");
    /* 直接执行一个shell, 以便我们观察这个进程空间里的资源是否被隔离 */
    execv(container_args[0], container_args);
    printf("Something's wrong!\n");
    return 1;
}

int main() {
    printf("Parent [%5d] - start a container!\n", getpid());
    /* 调用clone函数, 其中传出一个函数，还有一个栈空间 (为什么传尾指针，因为栈增长的方向是自上向下) */
    /* 启用CLONE_NEWUTS Namespace隔离 */
    /* 启用CLONE_NEWIPC Namespace隔离 - IPC隔离 */
    /* 启用CLONE_NEWPID Namespace隔离 - PID隔离 */
    /* 启用Mount Namespace - 增加CLONE_NEWNS参数*/
    int container_pid = clone(\
            container_main, \
            container_stack+STACK_SIZE, \
            CLONE_NEWUTS | CLONE_NEWIPC | CLONE_NEWPID | CLONE_NEWNS | SIGCHLD, \
            NULL);
    /* 等待子进程结束 */
    waitpid(container_pid, NULL, 0);
    printf("Parent - container stopped!\n");
	return 0;
}

