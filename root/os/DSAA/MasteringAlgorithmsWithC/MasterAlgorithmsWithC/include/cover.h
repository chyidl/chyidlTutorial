//
//  cover.h
//  MasterAlgorithmsWithC
//  Descripted -- Header for the Set Covering.
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#ifndef cover_h
#define cover_h

#include "set.h"

/**
 * Define a structure for subsets identified by a key.
 */
typedef struct KSet_ {
    
    void    *key;
    Set     set;

} KSet;

/*******************************************************************
* Public Interface
*******************************************************************/

/**
 * Initializes the Set specified by cover.
 *
 * @Complexity O(1)
 *
 * @param members is the set S to be covered 
 * @param subsets is the set of subsets in P 
 * #param covering is the set S to be covered 
 *
 * @return 0 if it finds a covering, 1 if a covering is not possible, or -1 otherwise.
 * */
int cover(Set *members, Set *subsets, Set *covering);

#endif /* cover_h */
