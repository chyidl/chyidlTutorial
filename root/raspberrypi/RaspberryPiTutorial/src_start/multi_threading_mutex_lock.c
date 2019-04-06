//
// multi_threading_mutex_lock.c
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
#include <unistd.h>
#include <string.h>
#include <pthread.h>

pthread_t tid[2];
int counter;
pthread_mutex_t lock; 

void* trythis(void *args){
    pthread_mutex_lock(&lock); // 获取互斥锁并上锁，如果不能获得就等待
    counter += 1;
    printf("\nJob %d has strated\n", counter);
    sleep(1);
    printf("\nJob %d has finished\n", counter);
    pthread_mutex_unlock(&lock); // 释放互斥锁

    return NULL;
}

int main() {
	// Your Programming statements HERE!
	int i = 0;
    int error;

    if (pthread_mutex_init(&lock, NULL) != 0) {
        printf("\nMutex init has failed\n");
        return 1;
    }
    while(i<2){
        error = pthread_create(&(tid[i]), NULL, &trythis, NULL);
        if (error != 0){
            printf("\nThread can't be created :[%s]", strerror(error));
        }
        i++;
    }

    pthread_join(tid[0], NULL);
    pthread_join(tid[1], NULL);
    pthread_mutex_destroy(&lock);

	return 0;
}

