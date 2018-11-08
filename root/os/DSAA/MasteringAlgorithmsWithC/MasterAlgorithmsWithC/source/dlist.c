//
//  dlist.c
//  MasterAlgorithmsWithC
//  Descripted -- Header for the Doubly-Linked List Abstract Datatype.
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#include <stdlib.h>
#include <string.h>

#include "dlist.h"

/**
 * Initializes the doubly linked list specified by list.
 *
 * @Complexity O(1)
 *
 * @param list 链表
 * @param destroy 成员析构函数 (free...)
 *
 * @return None
 * */
void dlist_init(DList *list, void (*destroy)(void *data)) {
    // Initialize the list.
    
    list->size = 0;
    list->destroy = destroy;

    list->head = NULL;
    list->tail = NULL;

    return; 
}


/**
 * Destroys the Doubly linked list specified by list.
 *
 * @Complexity O(n), where n is the number of elements in the linked list.
 *
 * @param list 链表
 *
 * @return None 
 * */
void dlist_destroy(DList *list) {
    void *data;

    // Remove each element.
    while (dlist_size(list) > 0) {
        if (dlist_remove(list, dlist_tail(list), (void **)&data) == 0 && list->destroy != NULL) {
            // Call a user-defined function to free dynamically allocated data.
            list->destroy(data);
        }
    }

    // No operations are allowed now, but clear the structure as a precaution.
    memset(list, 0, sizeof(DList));

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
int dlist_ins_next(DList *list, DListElmt *element, const void *data) {
    DListElmt    *new_element;

    // Do not allow a NULL element unless the list is empty
    if (element == NULL && dlist_size(list) != 0)
        return -1;

    // Allocate storage for the element.
    if ((new_element = (DListElmt *)malloc(sizeof(DListElmt))) == NULL)
        return -1;

    // Insert the element into the list. 
    new_element->data = (void *)data;
    
    if (dlist_size(list) == 0) {
        // Handle insertion when the list is empty.
        list->head = new_element;
        list->head->prev = NULL;
        list->head->next = NULL;
        list->tail = new_element;
    }
    else {
        // Handle insertion when the list is not empty.
        new_element->next = element->next;
        new_element->prev = element;

        if (element->next == NULL)
            list->tail = new_element;
        else 
            element->next->prev = new_element; 

        element->next = new_element;
    }

    // Adjust the size of the list to account for the inserted element.
    list->size++;

    return 0;
}

/**
 * Inserts an element just before element in the linked list specified by list. If element is NULL, the new element is inserted at the head of the list 
 *
 * @Complexity O(1)
 *
 * @param list 链表
 * @param element 待插入元素的前元素
 * @param data 元素数据
 *
 * @return 0 if inserting the element is successful, or -1 otherwise.
 * */
int dlist_ins_prev(DList *list, DListElmt *element, const void *data) {
    DListElmt    *new_element;

    // Do not allow a NULL element unless the list is empty
    if (element == NULL && dlist_size(list) != 0)
        return -1;

    // Allocate storage to be managed by the abstract datatype.
    if ((new_element = (DListElmt *)malloc(sizeof(DListElmt))) == NULL)
        return -1;

    // Insert the element into the list. 
    new_element->data = (void *)data;
    
    if (dlist_size(list) == 0) {
        // Handle insertion when the list is empty.
        list->head = new_element;
        list->head->prev = NULL;
        list->head->next = NULL;
        list->tail = new_element;
    }
    else {
        // Handle insertion when the list is not empty.
        new_element->next = element;
        new_element->prev = element->prev;

        if (element->prev == NULL)
            list->head = new_element;
        else 
            element->prev->next = new_element; 

        element->prev = new_element;
    }

    // Adjust the size of the list to account for the inserted element.
    list->size++;

    return 0;
}
/**
 * Removes the element just element from the linked list specified by list. If element is NULL, the element at the head of the list is removed. 
 *
 * @Complexity O(1)
 *
 * @param list 链表
 * @param element 待移除元素的前元素
 * @param data 已移除元素的存储数据
 *
 * @return 0 if removing the element is successful, or -1 otherwise.
 * */
int dlist_remove(DList *list, DListElmt *element, void **data) {

    // Do not allow a NULL element or removal from an empty list.
    if (element == NULL || dlist_size(list) == 0)
        return -1;

    // Remove the element from the list.
    *data = element->data; 

    if (element == list->head) {
        // Handle removal from the head of the list.
        list->head = element->next;
        
        if (list->head == NULL)
            list->tail = NULL;
        else 
            element->next->prev = NULL;
    }
    else {
       // Handle removal from somewhere other than the head of the list. 
        element->prev->next = element->next;

        if (element->next == NULL)
            list->tail = element->prev;
        else
            element->next->prev = element->prev;
    }

    // Free the storage allocated by the abstract datatype.
    free(element);

    // Adjust the size of the list to account for the removed element.
    list->size--;

    return 0;
}
