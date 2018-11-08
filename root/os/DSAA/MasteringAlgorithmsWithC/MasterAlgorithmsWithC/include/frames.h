//
//  frames.h
//  MasterAlgorithmsWithC
//
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#ifndef frames_h
#define frames_h

#include "list.h"

/**********************************************************
 * -------------------- Public Interface -----------------*
 *  ******************************************************/

/**
 * 从空闲页帧链表中获取空闲页帧号
 *
 * @param frames 帧链表
 *
 * @return 页帧号
 * */
int alloc_frame(List *frames);

/**
 * 释放之前获取的页帧号
 *
 * @param frames 帧链表
 * @param frame_number 页帧号
 *
 * @return 成功返回0，否则返回-1
 * */

int free_frame(List *frames, int frames_number);

#endif /* frames_h */
