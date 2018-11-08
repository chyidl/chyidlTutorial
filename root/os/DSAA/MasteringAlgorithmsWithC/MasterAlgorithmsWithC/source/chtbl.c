//
//  chtbl.c
//  MasterAlgorithmsWithC
//  Descripted -- the Chained Hash Table
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#include <stdlib.h>
#include <string.h>

#include "list.h"
#include "chtbl.h"

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
int chtbl_init(CHTbl *htbl, int buckets, int (*h)(const void *key), int (*match)(const void *key1, const void *key2), void (*destroy)(void *data)) {

    int     i;
    
    // Allocate space for the hash table.
    if ((htbl->table = (List *)malloc(buckets * sizeof(List))) == NULL)
        return -1;

    // Initialize the buckets
    htbl->buckets = buckets; 

    for (i = 0; i < htbl->buckets; i++) {
        list_init(&htbl->table[i], destroy);
    }
    
    // encapsulate the h, match, and destroy functions
    htbl->h = h;
    htbl->match = match;
    htbl->destroy = destroy;
    
    // Initialize the number of elements in the table.
    htbl->size = 0;

    return 0;
}

/*
 * Destroys the chained hash table specified by htbl.
 *
 * @Complexity O(m), where m is the number of buckets in the hash table
 *
 * @param htbl 
 *
 * */
void chtbl_destroy(CHTbl *htbl) {
    
    int         i;

    // Destroy each bucket 
    for (i = 0; i < htbl->buckets; i++) {

        list_destroy(&htbl->table[i]);
   
    }
    
    // Free the storage allocated for the hash table 
    free(htbl->table);

    // No operations are allowed now, but clear the structure as a precaution.
    memset(htbl, 0, sizeof(CHTbl));

    return;
}

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
int chtbl_insert(CHTbl *htbl, const void *data) {
    void        *temp;
    int         bucket, retval;

    // Do nothing if the data is already in the table
    temp = (void *)data;

    if (chtbl_lookup(htbl, &temp) == 0) 
        return 1;

    // Hash the key
    bucket = htbl->h(data) % htbl->buckets;

    // Insert the data into the bucket
    if ((retval = list_ins_next(&htbl->table[bucket], NULL, data)) == 0) {
        htbl->size++;
    }
    return retval;
}

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
int chtbl_remove(CHTbl *htbl, void **data) {
    ListElmt    *element, *prev;
    int         bucket;

    // Hash the key.
    bucket = htbl->h(*data) % htbl->buckets;

    // Search for the data in the bucket
    prev = NULL;

    for (element = list_head(&htbl->table[bucket]); element != NULL; element = list_next(element)) {

        if (htbl->match(*data, list_data(element))) {
            
            // Remove the data from the bucket 
            if (list_rem_next(&htbl->table[bucket], prev, data) == 0) {
                htbl->size--;
                return 0;
            } else {
                return -1;
            }

        }
        prev = element;
    }
    // Return that the data was not found.
    return -1;
}

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
int chtbl_lookup(const CHTbl *htbl, void **data) {

    ListElmt    *element;
    int         bucket;

    // Hash the key
    bucket = htbl->h(*data) % htbl->buckets;

    // Search for the data in the bucket
    for (element = list_head(&htbl->table[bucket]); element != NULL; element = list_next(element)) {

        if (htbl->match(*data, list_data(element))) {
            
            // Pass back the data from the table 
            *data = list_data(element);
            return 0;
        }
    }
    // Return that the data was not found.
    return -1;
}
