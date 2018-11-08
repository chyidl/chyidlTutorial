//
//  queue.c
//  MasterAlgorithmsWithC
//  Descripted -- Implementation of the Queue Abstract Datatype.
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#include <stdlib.h>

#include "list.h"
#include "queue.h"

/**
 * The queue_enqueue operation enqueues an element at the tail of a queue by call-ing list_ins_next to insert an element pointing to data at the tail of the list.
 *
 * @Complexity O(1)
 *
 * @param queue
 *
 * */
int queue_enqueue(Queue *queue, const void *data) {
    // Enqueue the data
    return list_ins_next(queue, list_tail(queue), data);
}


/**
 * The queue_dequeue operation dequeues an element from the head of a queue by calling list_rem_next to remove the element at the head of the list
 *
 * @Complexity O(1)
 *
 * @param queue
 *
 * */
int queue_dequeue(Queue *queue, void **data) {
    // Dequeue the data.
    return list_rem_next(queue, NULL, data);
}
