//
//  stack.c
//  MasterAlgorithmsWithC
//  Descripted -- Implementation of the Stack Abstract Datatype.
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#include <stdlib.h>

#include "list.h"
#include "stack.h"

/**
 * The stack_push operation pushes an element onto the top of a stack calling list_ins_next to insert an element point to data all the head of the list
 *
 * @Complexity O(1)
 *
 * @param stack
 *
 * */
int stack_push(Stack *stack, const void *data) {
    // Push the data onto the stack 
    return list_ins_next(stack, NULL, data);
}


/**
 * The stack_pop operation pops an element off the top of a stack by calling list_rem_next to remove the element at the head of the list.The list_rem_next operation sets data to point to the data from the element removed.
 *
 * @Complexity O(1)
 *
 * @param stack
 *
 * */
int stack_pop(Stack *stack, void **data) {
    // Pop the data off the stack 
    return list_rem_next(stack, NULL, data);
}
