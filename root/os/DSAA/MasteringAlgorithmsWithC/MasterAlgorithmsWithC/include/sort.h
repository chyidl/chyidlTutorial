//
//  sort.h
//  MasterAlgorithmsWithC
//
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#ifndef sort_h
#define sort_h

/**
 Insertion Sort: 利用插入排序将数组data中元素进行排序 -- O(n^2)
 
 @param data    数据数组
 @param size    数组元素个数
 @param esize   数组元素类型大小
 @param compare 函数指针，用于比较两个成员大小 (大于返回 1,小于返回 -1,等于返回 0)
 @return 成功返回 0；否则返回 -1
 */
int issort(void *data, int size, int esize, int (*compare)(const void *key1, const void *ket2));

#endif /* sort_h */
