//
//  main.c
//  MasterAlgorithmsWithC
//  Description: Illustrates sorting algorithms (see Chapter 12).
//
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#include <stdio.h>
#include <string.h>

#include "frames.h"
#include "list.h"

static void print_list(const List *list) {
    ListElmt    *element;
    int         *data, i=0;

    fprintf(stdout, "-> List size is %d\n", list_size(list));
    element = list_head(list);

    while (1) {
        data = list_data(element);
        fprintf(stdout, "--> List[%03d]=%03d\n", i, *data);
        i++;

        if (list_is_tail(element)) {
            break;
        } else {
            element = list_next(element);
        }
    }

    return;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    List        frames;
    ListElmt    *element;
    int         *data, i;

    // 初始化Frames
    list_init(&frames, free);

    // 链表操作
    element = list_head(&frames);

    for (i = 10; i > 0; i--) {
        if ((data = (int *)malloc(sizeof(int))) == NULL) return 1;
        
        *data = 0;
        
        if (list_ins_next(&frames, NULL, data) != 0) return 1;
    }
    printf("The Frames Linked List:\n");
    print_list(&frames); 

    // How to use Frame, I need some example using frames

    printf("Hello, World!\n");
    return 0;
}
