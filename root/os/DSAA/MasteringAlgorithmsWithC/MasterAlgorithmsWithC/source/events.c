//
//  events.c
//  MasterAlgorithmsWithC
//  Descripted -- Implementation of Functions for Handling Events.
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#include <stdlib.h>
#include <string.h>

#include "event.h"
#include "events.h"
#include "queue.h"

/**
 * The queue_enqueue operation enqueues an element at the tail of a queue by call-ing list_ins_next to insert an element pointing to data at the tail of the list.
 *
 * @Complexity O(1)
 *
 * @param queue
 *
 * */
int receive_event(Queue *events, const Event *event) {
    Event       *new_event;

    // Allocate space for the event 
    if ((new_event = (Event *)malloc(sizeof(Event))) == NULL)
        return -1;

    // Make a copy of the event and enqueue it, 
    memcpy(new_event, event, sizeof(Event));

    if (queue_enqueue(events, new_event) != 0)
        return -1; 
    
    return 0;
}


/**
 * The queue_dequeue operation dequeues an element from the head of a queue by calling list_rem_next to remove the element at the head of the list
 *
 * @Complexity O(1)
 *
 * @param queue
 *
 * */
int process_event(Queue *events, int (*dispatch)(Event *event)) {
    Event   *event;

    if (queue_size(events) == 0)
        // Return that there are no events to dispatch 
        return -1;
    else {
        if (queue_dequeue(events, (void **)&event) != 0)
            // Return that an event could not be retrieved 
            return -1;
        else {
            // Call a user-defined function to dispatch the event.
            dispatch(event);
            free(event);
        }
    }
    return 0;
}
