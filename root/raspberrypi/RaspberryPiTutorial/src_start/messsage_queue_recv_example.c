//
// messsage_queue_recv_example.c
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
#include <sys/ipc.h>
#include <sys/msg.h>

struct msg_struct {
    int type;
    char content[100];
} message;

int main() {
	// Your Programming statements HERE!
	// 生成IPC Key 
    key_t key = ftok("path", 65);

    // 创建一个Message Queue,获得Message Queue ID 
    int mqid = msgget(key, 0666 | IPC_CREAT);

    // 接收数据 
    msgrcv(mqid, &message, sizeof(message), 1, 0);
    printf("收到的数据: %s", message.content);

    // 销毁Message Queue 
    msgctl(mqid, IPC_RMID, NULL);
	return 0;
}

