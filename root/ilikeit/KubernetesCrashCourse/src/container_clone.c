//
// container_clone.c
// src
//
//        __|__
// --o--o--(̊)--o--o--
// C is the bext programming language
//
// Created by Chyi Yaqing on 05/04/19.
// Copyright © 2019. Chyi Yaqing. All rights reserved.
//
#define _GNU_SOURCE 
#include <sys/mount.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>
#include <sched.h>
#include <signal.h>
#include <unistd.h>

/* 定一个给 clone 用的栈, 栈的大小1M */
#define STACK_SIZE (1024 * 1024)
static char container_stack[STACK_SIZE];

char* const container_args[] = {
    "/bin/bash",
    NULL
};

int container_main(void* arg)
{
    printf("Container - inside the container!\n");
    // 如果你的机器的根目录的挂载类型是shared, 那必须重新挂载根目录
    // mount("", "/", NULL, MS_PRIVATE, "");
    mount("none", "/tmp", "tmpfs", 0, "");
    /* 直接执行一个shell, 以便我们观察这个进程空间里的资源是否被隔离了 */
    execv(container_args[0], container_args);
    printf("Something's wrong!\n");
    return 1;
}

int main() {
	// Your Programming statements HERE!
	printf("Parent - start a container!\n");
    /* 调用clone函数,其中传出一个函数,还有一个栈空间的 (为什么传尾指针，因为栈是反着的) */
    int container_pid = clone(container_main, container_stack+STACK_SIZE, CLONE_NEWNS | SIGCHLD, NULL);
    /* 等待子进程结束 */
    waitpid(container_pid, NULL, 0);
    printf("Parent - container stopped!\n");
	// Printf() displays the string inside quotation
	return 0;
}

