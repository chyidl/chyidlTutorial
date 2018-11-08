//
//  set.h
//  MasterAlgorithmsWithC
//  Descripted -- Header for the Set Abstract Datatype.
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#ifndef set_h
#define set_h

#include <stdlib.h>

#include "list.h"

/**
 * Implement sets as linked lists.
 */
typedef List Set;

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
void set_init(Set *set, int (*match)(const void *key1, const void *key2), void (*destroy)(void *data));


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
int set_insert(Set *set, const void *data);

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
int set_remove(Set *set, void **data);

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
int set_union(Set *setu, const Set *set1, const Set *set2);

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
int set_intersection(Set *seti, const Set *set1, const Set *set2);

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
int set_difference(Set *setd, const Set *set1, const Set *set2);

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
int set_is_member(const Set *set, const void *data);

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
int set_is_subset(const Set *set1, const Set *set2);

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
int set_is_equal(const Set *set1, const Set *set2);

/**
 * Macro that evaluates to the number of members in the set specified by set.
 *
 * @Complexity O(1)
 * 
 * @param set
 *
 * @return Number of members in the set. 
 * **/
#define set_size(set) ((set)->size)

#endif /* set_h */
