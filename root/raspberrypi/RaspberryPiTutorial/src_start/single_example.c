//
// single_example.c
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
#include <signal.h>
#include <unistd.h>

void sigint_handler()
{
    printf("Received SIGINT\n");
}

int main() {
    // signal函数两个参数，第一个参数：信号标识，第二个参数：回调函数
	signal(SIGINT, sigint_handler);
    while (1) {
	    // Printf() displays the string inside quotation
	    printf("Hello, World!");
        sleep(1);
    }
    return 0;
}

