//
//  cover.c
//  MasterAlgorithmsWithC
//  Descripted -- Implementation of a Function for Set Covering
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#include <stdlib.h>

#include "list.h"
#include "cover.h"
#include "set.h"

/*******************************************************************
* Public Interface
*******************************************************************/

/**
 * Initializes the Set specified by cover.
 *
 * @Complexity O(m3), where m is the initial number of members in memebers
 *
 * @param members is the set S to be covered 
 * @param subsets is the set of subsets in P 
 * @param covering is the set C returned as the covering
 *
 * @return The function cover 0 if it finds a covering, 1 if a covering is not possible, or -1 otherwise.
 * */
int cover (Set *members, Set *subsets, Set *covering) {
    Set         intersection;
    KSet        *subset;
    ListElmt    *member, *max_member;
    void        *data;
    int         max_size; 

    // Initialize the covering 
    set_init(covering, subsets->match, NULL);

    // Continue while there are noncovered members and candidate subsets
    while (set_size(members) > 0 && set_size(subsets) > 0) {
        
        // Find the subsets that covers the most members. 
        max_size = 0;
        // Inside this loop, during each iteration, it finds the set in subsets that produces the largest intersection with members.
        for (member = list_head(subsets); member != NULL; member = list_next(member)) {
            
            if (set_intersection(&intersection, &((KSet *)list_data(member))->set, members) != 0) {
                return -1;
            }
            
            if (set_size(&intersection) > max_size) {
                max_member = member;
                max_size = set_size(&intersection);
            }
            
            set_destroy(&intersection);
        }
        
        // A covering is not possible if there was no intersection. 
        if (max_size == 0)
            return -1;
        
        // Insert the selected subset into the covering.
        subset = (KSet *)list_data(max_member);
        
        // adds this set to the covering 
        if (set_insert(covering, subset)!=0)
            return -1;
        
        // Remove each covered member from the set of noncovered members.
        for (member = list_head(&((KSet *)list_data(max_member))->set); member != NULL; member = list_next(member)) {
            data = list_data(member);
            if (set_remove(members, (void**)&data) == 0 && members->destroy != NULL)
                members->destroy(data);
        }
        
        // Remove the subset from the set of candidate subsets 
        if (set_remove(subsets, (void **)&subset) != 0)
            return -1;

    }
    
    // No covering is possible if there are still noncovered members 
    // if the outermost loop terminates with members not empty,
    if (set_size(members) > 0)
        return -1;

    return 0;
}
