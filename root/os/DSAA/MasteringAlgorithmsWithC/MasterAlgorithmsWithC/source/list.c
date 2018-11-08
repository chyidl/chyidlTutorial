//
//  list.c
//  MasterAlgorithmsWithC
//  Descripted -- Header for the Linked List Abstract Datatype.
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#include <stdlib.h>
#include <string.h>

#include "list.h"

/**
 * Initializes the linked list specified by list.
 *
 * @Complexity O(1)
 *
 * @param list 链表
 * @param destroy 成员析构函数 (free...)
 *
 * @return None
 * */
void list_init(List *list, void (*destroy)(void *data)) {
    // 初始化链表
    
    list->size = 0;
    list->destroy = destroy;

    list->head = NULL;
    list->tail = NULL;

    return; 
}


/**
 * Destroys the linked list specified by list.
 *
 * @Complexity O(n), where n is the number of elements in the linked list.
 *
 * @param list 链表
 *
 * @return None 
 * */
void list_destroy(List *list) {
    void *data;

    // Remove each element.
    while (list_size(list) > 0) {
        if (list_rem_next(list, NULL, (void **)&data) == 0 && list->destroy != NULL) {
            // Call a user-defined function to free dynamically allocated data.
            list->destroy(data);
        }
    }

    // No operations are allowed now, but clear the structure as a precaution.
    memset(list, 0, sizeof(List));

    return;
}

/**
 * Inserts an element just after element in the linked list specified by list. If element is NULL, the new element is inserted at the head of the list 
 *
 * @Complexity O(1)
 *
 * @param list 链表
 * @param element 待插入元素的前元素
 * @param data 元素数据
 *
 * @return 0 if inserting the element is successful, or -1 otherwise.
 * */
int list_ins_next(List *list, ListElmt *element, const void *data) {
    ListElmt    *new_element;

    // Allocate storage for the element.
    if ((new_element = (ListElmt *)malloc(sizeof(ListElmt))) == NULL)
        return -1;

    // Insert the element into the list. 
    new_element->data = (void *)data;
    
    if (element == NULL) {
        // Handle insertion at the head of the list.
        if (list_size(list) == 0)
            list->tail = new_element;

        new_element->next = list->head;
        list->head = new_element;
    }
    else {
        // Handle insertion somewhere other than at the head.
        if (element->next == NULL)
            list->tail = new_element;
        new_element->next = element->next;
        element->next = new_element;
    }

    // Adjust the size of the list to account for the inserted element.
    list->size++;

    return 0;
}

/**
 * Removes the element just after element from the linked list specified by list. If element is NULL, the element at the head of the list is removed. 
 *
 * @Complexity O(1)
 *
 * @param list 链表
 * @param element 待移除元素的前元素
 * @param data 已移除元素的存储数据
 *
 * @return 0 if removing the element is successful, or -1 otherwise.
 * */
int list_rem_next(List *list, ListElmt *element, void **data) {
    ListElmt    *old_element;

    // Do not allow removal from an empty list.
    if (list_size(list) == 0)
        return -1;

    // Remove the element from the list.
    if (element == NULL) {
        // Handle removal from the head of the list.
        *data = list->head->data;
        old_element = list->head;
        list->head = list->head->next;

        if (list_size(list) == 1)
            list->tail = NULL;
    }
    else {
       // Handle removal from somewhere other than the head. 
       if (element->next == NULL)
           return -1;

       *data = element->next->data;
       old_element = element->next;
       element->next = element->next->next;

       if (element->next == NULL)
           list->tail = element;
    }

    // Free the storage allocated by the abstract datatype.
    free(old_element);

    // Adjust the size of the list to account for the removed element.
    list->size--;

    return 0;
}
