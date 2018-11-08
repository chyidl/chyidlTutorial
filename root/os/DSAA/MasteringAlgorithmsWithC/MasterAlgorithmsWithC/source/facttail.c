//
//  facttail.c
//  MasterAlgorithmsWithC
//  Description - Implementation of a Function for Computing Factorials in a Tail-Recursive Manner
//
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#include "facttail.h"

/***************************************************************
 *                                                              *
 * ------------------------ facttail ---------------------------*
 *                                                              *
 ***************************************************************/

int facttail(int n, int a) {
    // Compute a factorial in a tail-recursive manner. 
    if (n < 0)
        return 0;
    else if (n == 0)
        return a;
    else if (n == 1)
        return a;
    else
        return facttail(n - 1, n * a);
}
