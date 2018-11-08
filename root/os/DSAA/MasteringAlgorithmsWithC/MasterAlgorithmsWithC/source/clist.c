//
//  clist.c
//  MasterAlgorithmsWithC
//  Descripted -- Header for the Circular List Abstract Datatype.
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#include <stdlib.h>
#include <string.h>

#include "clist.h"

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
void clist_init(CList *list, void (*destroy)(void *data)) {
    // 初始化链表
    
    list->size = 0;
    list->destroy = destroy;
    list->head = NULL;

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
void clist_destroy(CList *list) {
    void *data;

    // Remove each element.
    while (clist_size(list) > 0) {
        if (clist_rem_next(list, list->head, (void **)&data) == 0 && list->destroy != NULL) {
            // Call a user-defined function to free dynamically allocated data.
            list->destroy(data);
        }
    }

    // No operations are allowed now, but clear the structure as a precaution.
    memset(list, 0, sizeof(CList));

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
int clist_ins_next(CList *list, CListElmt *element, const void *data) {
    CListElmt    *new_element;

    // Allocate storage for the element.
    if ((new_element = (CListElmt *)malloc(sizeof(CListElmt))) == NULL)
        return -1;

    // Insert the element into the list. 
    new_element->data = (void *)data;
    
    if (clist_size(list) == 0) {
        // Handle insertion when the list is empty.
        new_element->next = new_element;
        list->head = new_element;
    }
    else {
        // Handle insertion when the list is not empty
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
int clist_rem_next(CList *list, CListElmt *element, void **data) {
    CListElmt    *old_element;

    // Do not allow removal from an empty list.
    if (clist_size(list) == 0)
        return -1;

    // Remove the element from the list.
    *data = element->next->data; 
    
    if (element->next == element) {
        // Handle removal the last element.
        old_element = element->next;
        list->head = NULL;
    }
    else {
       // Handle removing other than the last element. 
       old_element = element->next;
       element->next = element->next->next;

       if (old_element == clist_head(list))
           list->head = old_element->next;
    }

    // Free the storage allocated by the abstract datatype.
    free(old_element);

    // Adjust the size of the list to account for the removed element.
    list->size--;

    return 0;
}
