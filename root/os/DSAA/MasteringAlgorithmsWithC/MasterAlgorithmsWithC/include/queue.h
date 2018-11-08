//
//  queue.h
//  MasterAlgorithmsWithC
//  Descripted -- Header for the Queue Abstract Datatype.
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#ifndef queue_h
#define queue_h

#include <stdlib.h>

#include "list.h"

/**
 * Implement queues as linked lists.
 */
typedef List Queue;

/*******************************************************************
* Public Interface
*******************************************************************/

/**
 * Initializes the Queue specified by queue.
 *
 * @Complexity O(1)
 *
 * @param queue
 * @param destroy 成员析构函数 (free...)
 *
 * @return None
 * */
#define queue_init list_init 


/**
 * Destroys the queue specified by queue.
 *
 * @Complexity O(n), where n is the number of elements in the linked list.
 *
 * @param queue 栈
 *
 * @return None 
 * */
#define queue_destroy list_destroy

/**
 *  Enqueues an element at the tail of the queue specified by queue.
 *
 * @Complexity O(1)
 *
 * @param queue 
 * @param data 元素数据
 *
 * @return 0 if pushing the element is successful, or -1 otherwise.
 * */
int queue_enqueue(Queue *queue, const void *data);

/**
 *  Dequeues an element from the head of the queue specified by queue.
 *
 * @Complexity O(1)
 *
 * @param queue 
 * @param data 元素数据
 *
 * @return 0 if popping the element is successful, or -1 otherwise.
 * */
int queue_dequeue(Queue *queue, void **data);

/**
 * Macro that evaluates to the data stored in the element at the head of the queue specified by queue
 * @Complexity O(1)
 *
 * @param queue 
 *
 * @return Data stored in the element at the head of the queue, or NULL if the queue is empty
 * */
#define queue_peek(queue) ((queue)->head == NULL ? NULL : (queue)->head->data)

/* *
 * Macro that evaluates to the number of elements in the queue specified by queue
 * @Complexity O(1)
 *
 * @param queue 
 *
 * @return Number of elements in the queue
 * */
#define queue_size list_size 


#endif /* queue_h */
