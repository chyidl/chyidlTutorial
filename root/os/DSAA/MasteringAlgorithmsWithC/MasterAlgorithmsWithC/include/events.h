//
//  events.h
//  MasterAlgorithmsWithC
//  Descripted -- Header for the Queue Abstract Datatype.
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#ifndef events_h
#define events_h

#include "event.h"
#include "queue.h"

/*******************************************************************
* Public Interface
*******************************************************************/

/**
 * 将要处理的事件入队 
 *
 * @Complexity O(1)
 *
 * @param events 事件队列
 * @param event  事件
 *
 * @return 0 if pushing the element is successful, or -1 otherwise.
 * */
int receive_event(Queue *events, const Event *event);

/**
 * 事件从队列中出队 
 *
 * @Complexity O(1)
 *
 * @param events 事件队列
 * @param dispatch 调度函数
 *
 * @return 0 if popping the element is successful, or -1 otherwise.
 * */
int process_event(Queue *events, int (*dispath)(Event *event));


#endif /* events_h */
