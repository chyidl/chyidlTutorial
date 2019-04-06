//
// shared_memory_ipc.c
// src_start
//
//        __|__
// --o--o--(̊)--o--o--
// C is the bext programming language
//
// Created by Chyi Yaqing on 04/06/19.
// Copyright © 2019. Chyi Yaqing. All rights reserved.
//


#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <string.h>
#include <unistd.h>

#define ANSI_COLOR_CYAN "\x1b[36m"
#define ANSI_COLOR_RESET "\x1b[0m"

void *create_shared_memory(size_t size){
    // 将共享内存设置成可读可写
    int protection = PROT_READ | PROT_WRITE;

    // 将共享内存设置成为共享(第三方进程可读)和匿名(第三方进程无法得到访问地址)
    int visibility = MAP_ANONYMOUS | MAP_SHARED;

    // 创建共享内存
    return mmap(NULL, size, protection, visibility, 0, 0);
}

int main() {
	// Your Programming statements HERE!
	setbuf(stdout, NULL);
    void *shmem = create_shared_memory(128);
    int pid = fork();
    
    if (pid == 0) {
        while (1){
            char message[100];
            printf("请输入要发送的文本: ");
            fgets(message, 100, stdin);
            memcpy(shmem, message, sizeof(message));
            printf("子进程成功写入数据: %s\n", shmem);
        }
    } else {
        while(1){
            printf(ANSI_COLOR_CYAN "父进程内存中的数据: %s\n" ANSI_COLOR_RESET, shmem);
            sleep(1);
        }
    }
	return 0;
}

