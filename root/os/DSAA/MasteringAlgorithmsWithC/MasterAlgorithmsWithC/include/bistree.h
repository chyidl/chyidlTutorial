//
//  bistree.h
//  MasterAlgorithmsWithC
//  Descripted -- Header for the Binary Tree Abstract Datatype.
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#ifndef bisree_h
#define bistree_h

#include "bitree.h"


// Binary Search Trees 
typedef BiTree BisTree;

/*******************************************************************
* Interface for Binary Search Trees 
********************************************************************/

/**
 * Initializes the binary search tree specified by tree.
 *
 * @Complexity O(1)
 *
 * @param tree 
 * @compare user-defined function to compare elements.This function should return 1 if key1 > key2, 0 if key1 = key2, and -1 if key1 < key2
 * @param destroy argument provides a way to free dynamically allocated data
 *
 * @return None
 * */
void bistree_init(BisTree *tree, int (*compare)(const void *key1, const void *key2), void (*destroy)(void *data));


/**
 * Destroys the binary search tree specified by tree.
 *
 * @Complexity O(n), where n is the number of nodes in the binary search tree.
 *
 * @param tree
 *
 * @return None 
 * */
void bistree_destroy(BisTree *tree);


/**
 * Inserts a node into the binary search tree specified by tree.
 * 
 * @Complexity O(log n), where n is the number of nodes in the binary search tree.
 *
 * @param tree 树
 * @param data 节点数据
 *
 * @return 0 if inserting the element is successful, 1 if the node is already in the tree, or -1 otherwise.
 * */
int bistree_insert(BisTree *tree, const void *data);


/**
 * Removes the node matching data from the binary search tree specified by tree. 
 * 
 * @Complexity O(log n), where n is the number of nodes in the binary search tree.
 *
 * @param tree 
 * @param data
 *
 * @return 0 if removing the node is successful, or -1 otherwise.
 * */
int bistree_remove(BisTree *tree, const void *data);


/**
 * Determines whether a node matches data in the binary search tree specified as tree.
 * 
 * @Complexity O(log n), where n is the number of nodes in the binary search tree.
 *
 * @param tree 
 * @param data
 *
 * @return 0 if the data is found in the binary search tree, or -1 otherwise.
 * */
int bistree_lookup(const BisTree *tree, void **data);


/**
 * Macro that evaluates to the number of nodes in the binary search tree specified by tree
 *
 * @Complexity O(1)
 *
 * @return Number of nodes in the tree
 * */
#define bistree_size(tree) ((tree)->size)

#endif /* bistree_h */
