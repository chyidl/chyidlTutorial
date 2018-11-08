//
//  dlist.h
//  MasterAlgorithmsWithC
//  Descripted -- Header for the Doubly-Linked List Abstract Datatype.
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#ifndef dlist_h
#define dlist_h

#include <stdlib.h>

/*******************************************************************
* Define a structure for doubly-linked list elements. 
*******************************************************************/

/**
 * Double-link list node 双向链表节点
 */
typedef struct DListElmt_ {
    
    void                *data;

    struct  DListElmt_  *prev;
    struct  DListElmt_  *next;

} DListElmt;

/**
 * Define a structure for doubly-linked lists. 双向链表
 */
typedef struct DList_ {

    int         size;

    int         (*match)(const void *key1, const void *key2);
    void        (*destroy)(void *data);

    DListElmt    *head;
    DListElmt    *tail;

} DList;

/*******************************************************************
* Public Interface
*******************************************************************/

/**
 * Initializes the Doubly-linked list specified by list.
 *
 * @Complexity O(1)
 *
 * @param list 双向链表
 * @param destroy 成员析构函数 (free...)
 *
 * @return None
 * */
void dlist_init(DList *list, void (*destroy)(void *data));


/**
 * Destroys the doubly-linked list specified by list.
 *
 * @Complexity O(n), where n is the number of elements in the linked list.
 *
 * @param list 双向链表
 *
 * @return None 
 * */
void dlist_destroy(DList *list);

/**
 * Inserts an element just after element in the doubly-linked list specified by list. If element is NULL, the new element is inserted at the head of the list 
 *
 * @Complexity O(1)
 *
 * @param list 双向链表
 * @param element 待插入元素的前元素
 * @param data 元素数据
 *
 * @return 0 if inserting the element is successful, or -1 otherwise.
 * */
int dlist_ins_next(DList *list, DListElmt *element, const void *data);

/**
 * Inserts an element just before element in the doubly-linked list specified by list. If element is NULL, the new element is inserted at the head of the list 
 *
 * @Complexity O(1)
 *
 * @param list 双向链表
 * @param element 待插入元素的后元素
 * @param data 元素数据
 *
 * @return 0 if inserting the element is successful, or -1 otherwise.
 * */
int dlist_ins_prev(DList *list, DListElmt *element, const void *data);

/**
 * Removes the element just after element from the linked list specified by list. If element is NULL, the element at the head of the list is removed. 
 *
 * @Complexity O(1)
 *
 * @param list 双向链表
 * @param element 待移除元素存储元素
 * @param data 已移除元素的存储数据
 *
 * @return 0 if removing the element is successful, or -1 otherwise.
 * */
int dlist_remove(DList *list, DListElmt *element, void **data);

/**
 * Macro that evaluates to the number of elements in the linked list specified by doubly-list
 *
 * @Complexity O(1)
 *
 * @return Number of elements in the doubly-list
 * */
#define dlist_size(list) ((list)->size)

/**
 * Macro that evaluates to the element at the head of the linked list specified by doubly-list.
 *
 * @Complexity O(1)
 *
 * @return Element at the head of the list
 * */
#define dlist_head(list) ((list)->head)

/**
 * Macro that evaluates to the element at the tail of the linked list specified by list.
 *
 * @Complexity O(1)
 *
 * @return Element at the tail of the list
 * */
#define dlist_tail(list) ((list)->tail)

/**
 * Macro that determines whether the element specified as element is at the head of a linked list.
 *
 * @Complexity O(1)
 *
 * @param element 待判断的元素
 *
 * @return 1 if the element is at the head of the list, or 0 otherwise.
 * */
#define dlist_is_head(element) ((element)->prev == NULL ? 1 : 0)

/**
 * Macro that determines whether the element specified as element is at the tail of a linked list.
 *
 * @Complexity O(1)
 *
 * @return 1 if the element is at the tail of the list, or 0 otherwise.
 * */
#define dlist_is_tail(element) ((element)->next == NULL ? 1 : 0)

/**
 * Macro that evaluates to the data stored in the element of a linked list specified by element.
 *
 * @Complexity O(1)
 *
 * @return Data stored in the element.
 * */
#define dlist_data(element) ((element)->data)


/**
 * Macro that evaluates to the element of a linked list following the element specified by element.
 *
 * @Complexity O(1)
 *
 * @return Element following the specified element.
 * */
#define dlist_next(element) ((element)->next)


/**
 * Macro that evaluates to the element of a linked list following the element specified by element.
 *
 * @Complexity O(1)
 *
 * @return Element following the specified element.
 * */
#define dlist_prev(element) ((element)->prev)

#endif /* dlist_h */
