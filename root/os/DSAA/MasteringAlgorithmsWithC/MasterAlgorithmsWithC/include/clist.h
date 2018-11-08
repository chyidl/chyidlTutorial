//
//  clist.h
//  MasterAlgorithmsWithC
//  Descripted -- Header for the Circular List Abstract Datatype.
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#ifndef clist_h
#define clist_h

#include <stdlib.h>

/*******************************************************************
* Define a structure for circular list elements. 
*******************************************************************/

/**
 * As with a singly-linked list, each element of a circular list consists of two parts: a data member and a pointer to the next element.
 * circular link list nodea 环链表节点
 */
typedef struct CListElmt_ {
    
    void    *data;
    struct  CListElmt_   *next;

} CListElmt;

/**
 * Define a structure for circular lists. 环链表
 */
typedef struct CList_ {

    int         size;

    int         (*match)(const void *key1, const void *key2);
    void        (*destroy)(void *data);

    CListElmt    *head;

} CList;

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
void clist_init(CList *list, void (*destroy)(void *data));


/**
 * Destroys the linked list specified by list.
 *
 * @Complexity O(n), where n is the number of elements in the linked list.
 *
 * @param list 链表
 *
 * @return None 
 * */
void clist_destroy(CList *list);

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
int clist_ins_next(CList *list, CListElmt *element, const void *data);

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
int clist_rem_next(CList *list, CListElmt *element, void **data);

/**
 * Macro that evaluates to the number of elements in the linked list specified by list
 *
 * @Complexity O(1)
 *
 * @return Number of elements in the list
 * */
#define clist_size(list) ((list)->size)

/**
 * Macro that evaluates to the element at the head of the linked list specified by list.
 *
 * @Complexity O(1)
 *
 * @return Element at the head of the list
 * */
#define clist_head(list) ((list)->head)

/**
 * Macro that evaluates to the data stored in the element of a linked list specified by element.
 *
 * @Complexity O(1)
 *
 * @return Data stored in the element.
 * */
#define clist_data(element) ((element)->data)


/**
 * Macro that evaluates to the element of a linked list following the element specified by element.
 *
 * @Complexity O(1)
 *
 * @return Element following the specified element.
 * */
#define clist_next(element) ((element)->next)


#endif /* clist_h */
