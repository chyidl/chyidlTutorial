//
//  hashpjw.h
//  MasterAlgorithmsWithC
//  Descripted -- A Hash Function That Performs Well for Strings.
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#ifndef hashpjw_h
#define hashpjw_h

// 定义桶数量 表大小
#define     PRIME_TBLSIZ    1699 

/**
 * 处理字符串的哈希函数
 *
 * @param key 
 *
 * @return hash 
 *
 * */
int hashpjw(const void *key);

#endif /* cover_h */
