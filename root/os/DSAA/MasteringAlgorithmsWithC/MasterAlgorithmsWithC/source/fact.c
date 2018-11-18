//
//  fact.c
//  MasterAlgorithmsWithC
//  Description - Implementation of a Function for Computing Factorials Recursively
//
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#include "fact.h"

/***************************************************************
 *                                                              *
 * -------------------------- fact -----------------------------*
 *                                                              *
 ***************************************************************/

int fact(int n) {
    // Compute a factorial recursively. 
    if (n < 0)
        return 0;
    else if (n == 0 || n == 1)
        return 1;
    else
        return n * fact(n - 1);
}
