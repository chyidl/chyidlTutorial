//
// wait_example.c
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
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
	// Your Programming statements HERE!
	pid_t pid = fork(); 
    if (pid < 0) {
        // 创建子进程失败
        printf("fork error.");
    } else if (pid == 0) {
        // child process 
        int sum = 0;
        for (int i = 0; i < 1000000; i++) {
            for (int j = 0; j < 100; j++) {
                sum += i;
            }
        }
        exit(0);
    } else {
        // parent process 
        int status;
        printf("child pid: %d...\n", pid);
        // await 
        do {
            waitpid(pid, &status, WUNTRACED);
        } while(!WIFEXITED(status) && !WIFSIGNALED(status));

        // status is child process reurn value 
        printf("child process return value: %d", status);
    }
	return 0;
}

