//
//  hashpjw.c
//  MasterAlgorithmsWithC
//  Descripted -- A Hash Function That Performs Well for Strings
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#include "hashpjw.h"

/*******************************************************************
* Public Interface
*******************************************************************/

/**
 * */
int hashpjw(const void *key) {
    const char  *ptr;
    unsigned int val; 

    // Has the key by performing a number of bit operations on it 
    val = 0;
    ptr = key;
    
    while (*ptr != '\0') {
        unsigned int tmp;
        
        val = (val << 4) + (*ptr);
        
        if (tmp = (val & 0xf0000000)) {
            val = val ^ (tmp >> 24);
            val = val ^ tmp;
        }
        ptr++;
    }
    // Inpractice, replace PRIME_TBLSIZ with the actual table size. 
    return val % PRIME_TBLSIZ;
}
