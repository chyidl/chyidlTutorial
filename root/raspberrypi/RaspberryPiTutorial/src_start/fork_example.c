//
// fork_example.c
// src_start
//
//        __|__
// --o--o--(̊)--o--o--
// C is the bext programming language
//
// Created by Chyi Yaqing on 03/31/19.
// Copyright © 2019. Chyi Yaqing. All rights reserved.
//


#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main(void) {
	// Your Programming statements HERE!
	pid_t pid;
    pid = fork();
    
    int var = 9527; 

    if (pid < 0) {
        printf("fork error");
        exit(1);
    } else if (pid == 0) {
        /* 子进程 */
        printf("current pid: %d, parent pid: %d; var: %d\n", getpid(), getppid(), var);
    } else {
        /* 父进程 */
        sleep(1);
        printf("current pid: %d, child pid: %d; var: %d\n", getpid(), pid, var);
    }
	return 0;
}

