//
// multi_threading.c
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
#include <pthread.h>
#include <unistd.h>  // for sleep 

void *func1(void){
    int i;
    for (i=0; i<5; i++){
        printf("func1 is running %d \n", i);
        sleep(1);
    }
    return NULL;
}

void *func2(void){
    int i;
    for (i=0; i < 5; i++){
        printf("func2 os running %d \n", i);
        sleep(1);
    }
    return NULL;
}

void *func3(void){
    int i;
    for(i = 0; i < 3; i++){
        printf("func3 is running %d \n", i);
        sleep(1);
    }
    return NULL;
}

int main() {
	// Your Programming statements HERE!
	int i=0, ret=0;
    pthread_t func1_id, func2_id, func3_id;

    ret = pthread_create(&func1_id, NULL, (void *)func1, NULL);
    if(ret){
        printf("Cannot create func1./n");
        return 1;
    }
    
    ret = pthread_create(&func2_id, NULL, (void *)func2, NULL);
    if(ret){
        printf("Cannot create func2./n");
        return 1;
    }
    
    ret = pthread_create(&func3_id, NULL, (void *)func3, NULL);
    if(ret){
        printf("Cannot create func3./n");
        return 1;
    }
    
    // Wait for func3.
    pthread_join(func3_id, NULL);

    printf("Math thread exists.\n");

	return 0;
}

