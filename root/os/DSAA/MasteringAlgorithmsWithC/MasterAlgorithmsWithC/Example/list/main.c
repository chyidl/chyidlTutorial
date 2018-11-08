//
//  main.c
//  MasterAlgorithmsWithC
//  Description: Illustrates sorting algorithms (see Chapter 5).
//
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#include <stdio.h>
#include <string.h>

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
    List        list;
    ListElmt    *element;
    int         *data, i;

    // 初始化链表
    list_init(&list, free);

    // 链表操作
    element = list_head(&list);

    for (i = 10; i > 0; i--) {
        if ((data = (int *)malloc(sizeof(int))) == NULL) return 1; 

        *data = i;

        if (list_ins_next(&list, NULL, data) != 0) return 1;

    }

    print_list(&list);

    element = list_head(&list);

    for (i = 0; i < 7; i++) {
        element = list_next(element);
    }

    data = list_data(element);
    fprintf(stdout, "Removing an element after the one containing %03d\n", *data);

    if (list_rem_next(&list, element, (void **)&data) != 0) return 1;

    print_list(&list);

    fprintf(stdout, "Inserting 011 at the tail of the list\n");

    *data = 11;
    if (list_ins_next(&list, list_tail(&list), data) != 0) return 1;

    print_list(&list);

    fprintf(stdout, "Removing an element after the first element\n");

    element = list_head(&list);
    if (list_rem_next(&list, element, (void **)&data) != 0) return 1;

    print_list(&list);

    fprintf(stdout, "Inserting 012 at the head of the list\n");
    
    *data = 12;
    if(list_ins_next(&list, NULL, data) != 0) return 1;

    print_list(&list);

    fprintf(stdout, "Iterating and removing the fourth element\n");

    element = list_head(&list);
    element = list_next(element);
    element = list_next(element);

    if (list_rem_next(&list, element, (void **)&data) != 0) return 1;

    print_list(&list);

    fprintf(stdout, "Inserting -13 after the first element\n");

    *data = 13;
    if (list_ins_next(&list, list_head(&list), data) != 0) return 1;

    print_list(&list);

    i = list_is_head(&list, list_head(&list));
    fprintf(stdout, "Testing list_is_head...Value=%d (1=OK)\n", i);
    i = list_is_head(&list, list_tail(&list));
    fprintf(stdout, "Testing list_is_head...Value=%d (0=OK)\n", i);
    i = list_is_tail(list_tail(&list));
    fprintf(stdout, "Testing list_is_tail...Value=%d (1=OK)\n", i);
    i = list_is_tail(list_head(&list));
    fprintf(stdout, "Testing list_is_tail...Value=%d (0=OK)\n", i);

    // 销毁链表
    fprintf(stdout, "Destroying the list\n");
    list_destroy(&list);

    return 0;
}
