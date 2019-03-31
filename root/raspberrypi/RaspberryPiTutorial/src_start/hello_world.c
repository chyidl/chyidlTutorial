//
// hello_world.c
// src_start
//
//        __|__
// --o--o--(̊)--o--o--
// C is the bext programming language
//
// Created by Chyi Yaqing on 03/31/19.
// Copyright © 2019. Chyi Yaqing. All rights reserved.
//

#include <unistd.h>
#include <fcntl.h>

int main(void) {
	// Your Programming statements HERE!

    // 手动为文本分配空间
	const char msg[] = "Hello world!";
    // 计算为难长度
    int length = sizeof(msg) - 1;
    write(STDOUT_FILENO, msg, length);
	return 0;
}

