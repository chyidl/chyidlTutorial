//
//  chtbl.h
//  MasterAlgorithmsWithC
//  Descripted -- Header for the Chained Hash Table Abstract Datatype
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#ifndef chtbl_h
#define chtbl_h

#include <stdlib.h>

#include "list.h"

/*************************************************
 * Define a structure for chained hash tables.
 * **********************************************/
typedef struct CHTbl_ {

    int         buckets;

    int         (*h) (const void *key);
    int         (*match) (const void *key1, const void *key2);
    void        (*destroy) (void *data);

    int         size;
    List        *table;

} CHTbl;

/************************************************
 * Public Interface 
 * *********************************************/


/**
 * Initializes the chained hash table specified by htbl.
 *
 * @complexity O(m), where m is the number of buckets in the hash table.
 *
 * @param htbl 哈希表
 * @param buckets The number of buckets allocated in the hash table 
 * @param h user-defined hash function for hashing keys.
 * @param match user-defined function to determine whether two keys match, return 1 if key1 is equal to key2, and 0 otherwise
 * @param destroy free dunamically allocated data 
 *
 * @return 0 if initializing the hash table is successful, or -1 otherwise.
 *
 * */
int chtbl_init(CHTbl *htbl, int buckets, 
        int (*h)(const void *key), 
        int (*match)(const void *key1, const void *key2), 
        void (*destroy)(void *data));


/*
 * Destroys the chained hash table specified by htbl.
 *
 * @Complexity O(m), where m is the number of buckets in the hash table
 *
 * @param htbl 
 *
 * */
void chtbl_destroy(CHTbl *htbl); 


/**
 * Inserts an element into the chained hash table specified by htbl.
 *
 * @Complexity O(1)
 *
 * @param htbl
 * @param data 
 * 
 * @return 0 if inserting the element is successful, 1 if the element is already in the hash table, or -1 otherwise.
 *
 * */
 int chtbl_insert(CHTbl *htbl, const void *data);


/**
 * Removes the element matching data from the chained hash table specified by htbl.
 *
 * @Complexity O(1)
 *
 * @param htbl
 * @param data 
 * 
 * @return 0 if removing the element is successful, or -1 otherwise.
 *
 * */
 int chtbl_remove(CHTbl *htbl, void **data);


/**
 * Determines whether an element matches data in the chained hash table specified by htbl.
 *
 * @Complexity O(1)
 *
 * @param htbl
 * @param data 
 * 
 * @return 0 if the element is found in the hash table, or -1 otherwise.
 *
 * */
 int chtbl_lookup(const CHTbl *htbl, void **data);


/**
 * Macro that evaluates to the number of elements in the chained hash table specified by htbl.
 *
 * @Complexity O(1)
 *
 * @param htbl
 * 
 * @return Number of elements in the hash table
 *
 * */
#define chtbl_size(htbl) ((htbl)->size)


#endif /* chtbl_h */
