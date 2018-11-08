//
//  page.h
//  MasterAlgorithmsWithC
//
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#ifndef page_h
#define page_h

/**
 Define a structure for information about pages. 
 */
typedef struct Page_ {
    int     number;
    int     reference;
} Page;

/****************************************************
 * ----------------Public Interface -------------*
 * ************************************************/


/**
 *  第二次机会置换法 (时钟算法) LRU 
 *
 *  @param current 当前元素
 *  @return 页位置
 * */
int replace_page(CListElmt **current);

#endif /* page_h */
