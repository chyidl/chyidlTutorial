//
//  stack.h
//  MasterAlgorithmsWithC
//  Descripted -- Header for the Stack Abstract Datatype.
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#ifndef stack_h
#define stack_h

#include <stdlib.h>

#include "list.h"

/**
 * Implement stacks as linked lists.
 */
typedef List Stack;

/*******************************************************************
* Public Interface
*******************************************************************/

/**
 * Initializes the Stack specified by stack.
 *
 * @Complexity O(1)
 *
 * @param stack
 * @param destroy 成员析构函数 (free...)
 *
 * @return None
 * */
#define stack_init list_init 


/**
 * Destroys the stack specified by stack.
 *
 * @Complexity O(n), where n is the number of elements in the linked list.
 *
 * @param stack 栈
 *
 * @return None 
 * */
#define stack_destroy list_destroy

/**
 *  Pushes an element onto the stack specified by stack.
 *
 * @Complexity O(1)
 *
 * @param stack 
 * @param data 元素数据
 *
 * @return 0 if pushing the element is successful, or -1 otherwise.
 * */
int stack_push(Stack *stack, const void *data);

/**
 *  Pops an element off the stack specified by stack.
 *
 * @Complexity O(1)
 *
 * @param stack 
 * @param data 元素数据
 *
 * @return 0 if popping the element is successful, or -1 otherwise.
 * */
int stack_pop(Stack *stack, void **data);

/**
 * Macro that evaluates to the data stored in the element at the top of the stack specified by stack
 * @Complexity O(1)
 *
 * @param stack 
 *
 * @return Data stored in the element at the top of the stack, or NULL if the stack is empty
 * */
#define stack_peek(stack) ((stack)->head == NULL ? NULL : (stack)->head->data)

/* *
 * Macro that evaluates to the number of elements in the stack specified by stack
 * @Complexity O(1)
 *
 * @param stack 
 *
 * @return Number of elements in the stack
 * */
#define stack_size list_size 


#endif /* stack_h */
