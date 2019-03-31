//
// messsage_queue_send_example.c
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

struct msg_struct{
    int type;
    char content[100];
} message;

int main() {
	// Your Programming statements HERE!
	//生成IPC key 
    key_t key = ftok("path", 65);

    // 创建一个Message Queue,获得Message Queue ID 
    int mqid = msgget(key, 0666 | IPC_CREAT);

    // 输入文本
    printf("请输入要发送的文本: ");
    fgets(message.content, 100, stdin);
    message.type = 1; 

    // 发送数据 
    msgsnd(mqid, &message, sizeof(message), 0);
    printf("发送的数据: %s", message.content);
	return 0;
}

