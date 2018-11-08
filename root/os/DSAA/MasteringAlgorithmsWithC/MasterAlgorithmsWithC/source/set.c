//
//  set.c
//  MasterAlgorithmsWithC
//  Descripted -- Header for the Set Abstract Datatype.
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#include <stdlib.h>
#include <string.h>

#include "list.h"
#include "set.h"

/*******************************************************************
* Public Interface
*******************************************************************/

/**
 * Initializes the Set specified by set.
 *
 * @Complexity O(1)
 *
 * @param set
 * @param match is a function used by various set operations to determine if two members match 
 * @param destroy 成员析构函数 (free...)
 *
 * @return None
 * */
void set_init(Set *set, int (*match)(const void *key1, const void *key2), void (*destroy)(void *data)) {
    // Initialize the set.
    list_init(set, destroy);
    set->match = match; 

    return; 
}

/**
 * Destroys the set specified by set.
 *
 * @Complexity O(n), where n is the number of elements in the linked list.
 *
 * @param set 栈
 *
 * @return None 
 * */
#define set_destroy list_destroy

/**
 *  Insert a member into the set specified by set.
 *
 * @Complexity O(n), where n is the number of members in the set.
 *
 * @param set 
 * @param data 元素数据
 *
 * @return 0 if inserting the element is successful,1 if the member is already in the set, or -1 otherwise.
 * */
int set_insert(Set *set, const void *data) {
    // Do not allow the insertion of duplicates 
    if (set_is_member(set, data))
        return 1;

    // Insert the data
    return list_ins_next(set, list_tail(set), data);
}

/**
 *  Removes the member matching data from the the set specified by set.
 *
 * @Complexity O(n), where n is the number of members in the set.
 *
 * @param set 
 * @param data 元素数据
 *
 * @return 0 if popping the element is successful, or -1 otherwise.
 * */
int set_remove(Set *set, void **data) {
    ListElmt        *member, *prev;
    
    // Find the member to remove 
    prev = NULL;
    for (member = list_head(set); member != NULL; member = list_next(member)) {
        if (set->match(*data, list_data(member)))
            break;

        prev = member;
    }

    // Return if the member was not found.
    if (member == NULL)
        return -1;

    // Remove the member.
    return list_rem_next(set, prev, data);
}

/**
 * Builds a set that is the union of set1 and set2
 *
 * @Complexity O(mn), where m and n are the number of members in set1 and set2
 *
 * @param setu
 * @param set1
 * @param set2 
 *
 * @return 0 if computing the union is successful, or -1 otherwise.
 * */
int set_union(Set *setu, const Set *set1, const Set *set2) {
    ListElmt    *member;
    void        *data;

    // Initialize the set for the union.
    set_init(setu, set1->match, NULL);

    // Insert the members of the first set. 
    for (member = list_head(set1); member != NULL; member = list_next(member)) {
        data = list_data(member);
        if (list_ins_next(setu, list_tail(setu), data) != 0) {
            set_destroy(setu);
            return -1; 
        }
    }

    // Insert the members of the second set. 
    for (member = list_head(set2); member != NULL; member = list_next(member)) {
        if (set_is_member(set1, list_data(member))) {
            // Do not allow the insertion of duplicates 
            continue;
        } else {
            data = list_data(member);
            if (list_ins_next(setu, list_tail(setu), data) != 0) {
                set_destroy(setu);
                return -1; 
            }
        }
    }
    return 0;
}

/**
 * Builds a set that is the intersection of set1 and set2
 *
 * @Complexity O(mn), where m and n are the number of members in set1 and set2
 *
 * @param seti contains the intersection 
 * @param set1
 * @param set2 
 *
 * @return 0 if computing the union is successful, or -1 otherwise.
 * */
int set_intersection(Set *seti, const Set *set1, const Set *set2) {
    ListElmt    *member;
    void        *data; 

    // Initialize the set for the intersection. 
    set_init(seti, set1->match, NULL);

    // Insert the members present in both sets 
    for (member = list_head(set1); member != NULL; member = list_next(member)) {
        if (set_is_member(set2, list_data(member))) {
            data = list_data(member);

            if (list_ins_next(seti, list_tail(seti), data) != 0) {
                set_destroy(seti);
                return -1;
            }
        }
    }
    return 0;
}

/**
 * Builds a set that is the difference of set1 and set2
 *
 * @Complexity O(mn), where m and n are the number of members in set1 and set2
 *
 * @param setd contains the intersection 
 * @param set1
 * @param set2 
 *
 * @return 0 if computing the union is successful, or -1 otherwise.
 * */
int set_difference(Set *setd, const Set *set1, const Set *set2) {
    ListElmt    *member;
    void        *data; 

    // Initialize the set for the difference 
    set_init(setd, set1->match, NULL); 

    // Insert the members from set1 not in set2 
    for (member = list_head(set1); member != NULL; member = list_next(member)) {
        if (!set_is_member(set2, list_data(member))) {
            data = list_data(member);
            if (list_ins_next(setd, list_tail(setd), data) != 0) {
                set_destroy(setd);
                return -1;
            }
        }
    }
    return 0;
}

/**
 * Determines whether the data specified by data matches that of a member in the set specified by set.
 *
 * @Complexity O(n), where n is the number of members in the set.
 * 
 * @param set
 * @param data 
 *
 * @return 1 if the member is found, or 0 otherwise. 
 * * */
int set_is_member(const Set *set, const void *data) {
    ListElmt    *member;
    // Determine if the data is a member of the set 
    for (member = list_head(set); member != NULL; member = list_next(member)) {
        if (set->match(data, list_data(member)))
            return -1; 
    }
    return 0;
}

/**
 * Determines whether the set specified by set1 is a subset of the set specified by set2
 *
 * @Complexity O(mn), where m and n are the number of members in set1 and set2, respectively
 * 
 * @param set1
 * @param set2 
 *
 * @return 1 if the set is a subset, or 0 otherwise.  
 * **/
int set_is_subset(const Set *set1, const Set *set2) {
    ListElmt        *member;
    // Do a quick test to rule out some cases 
    if (set_size(set1) > set_size(set2))
        return 0; 

    // Determine if set1 is a subset of set2 
    for (member = list_head(set1); member != NULL; member = list_next(member)) {
        if (!set_is_member(set2, list_data(member)))
            return 0;
    }
    return 1;
}

/**
 * Determines whether the set specified by set1 is a equal to the set specified by set2
 *
 * @Complexity O(mn), where m and n are the number of members in set1 and set2, respectively
 * 
 * @param set1
 * @param set2 
 *
 * @return 1 if the set is a equal, or 0 otherwise.  
 * **/
int set_is_equal(const Set *set1, const Set *set2) {
    // Do a quick test to rule our some cases.
    if (set_size(set1) != set_size(set2))
        return 0; 

    // Sets of the same size are equal if they are subsets 
    return set_is_subset(set1, set2);
}
