//
//  list.h
//  MasterAlgorithmsWithC
//  Descripted -- Header for the Linked List Abstract Datatype.
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#ifndef list_h
#define list_h

#include <stdlib.h>

/*******************************************************************
* Define a structure for linked list elements. 
*******************************************************************/

/**
 * link list nodea 链表节点
 */
typedef struct ListElmt_ {
    
    void    *data;
    struct  ListElmt_   *next;

} ListElmt;

/**
 * Define a structure for linked lists. 链表
 */
typedef struct List_ {

    int         size;

    int         (*match)(const void *key1, const void *key2);
    void        (*destroy)(void *data);

    ListElmt    *head;
    ListElmt    *tail;

} List;

/*******************************************************************
* Public Interface
*******************************************************************/

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
void list_init(List *list, void (*destroy)(void *data));


/**
 * Destroys the linked list specified by list.
 *
 * @Complexity O(n), where n is the number of elements in the linked list.
 *
 * @param list 链表
 *
 * @return None 
 * */
void list_destroy(List *list);

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
int list_ins_next(List *list, ListElmt *element, const void *data);

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
int list_rem_next(List *list, ListElmt *element, void **data);

/**
 * Macro that evaluates to the number of elements in the linked list specified by list
 *
 * @Complexity O(1)
 *
 * @return Number of elements in the list
 * */
#define list_size(list) ((list)->size)

/**
 * Macro that evaluates to the element at the head of the linked list specified by list.
 *
 * @Complexity O(1)
 *
 * @return Element at the head of the list
 * */
#define list_head(list) ((list)->head)

/**
 * Macro that evaluates to the element at the tail of the linked list specified by list.
 *
 * @Complexity O(1)
 *
 * @return Element at the tail of the list
 * */
#define list_tail(list) ((list)->tail)

/**
 * Macro that determines whether the element specified as element is at the head of a linked list.
 *
 * @Complexity O(1)
 *
 * @return 1 if the element is at the head of the list, or 0 otherwise.
 * */
#define list_is_head(list, element) ((element) == (list)->head ? 1 : 0)

/**
 * Macro that determines whether the element specified as element is at the tail of a linked list.
 *
 * @Complexity O(1)
 *
 * @return 1 if the element is at the tail of the list, or 0 otherwise.
 * */
#define list_is_tail(element) ((element)->next == NULL ? 1 : 0)

/**
 * Macro that evaluates to the data stored in the element of a linked list specified by element.
 *
 * @Complexity O(1)
 *
 * @return Data stored in the element.
 * */
#define list_data(element) ((element)->data)


/**
 * Macro that evaluates to the element of a linked list following the element specified by element.
 *
 * @Complexity O(1)
 *
 * @return Element following the specified element.
 * */
#define list_next(element) ((element)->next)


#endif /* list_h */
