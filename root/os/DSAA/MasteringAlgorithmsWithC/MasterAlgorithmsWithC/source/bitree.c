//
//  bitree.c
//  MasterAlgorithmsWithC
//  Descripted -- Header for the Binary Tree Abstract Datatype.
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#include <stdlib.h>
#include <string.h>

#include "bitree.h"

/*******************************************************************
* Public Interface
*******************************************************************/

/**
 * Initializes the binary tree specified by tree.
 *
 * @Complexity O(1)
 *
 * @param tree 树
 * @param destroy 成员析构函数 (free...)
 *
 * @return None
 * */
void bitree_init(BiTree *tree, void (*destroy)(void *data)){
    // Initialize the binary tree.
    tree->size = 0;
    tree->destroy = destroy;
    tree->root = NULL;

    return ;
}


/**
 * Destroys the binary tree specified by tree.
 *
 * @Complexity O(n), where n is the number of nodes in the binary tree.
 *
 * @param tree 树
 *
 * @return None 
 * */
void bitree_destroy(BiTree *tree) {
    // Remove all the nodes from the tree.
    bitree_rem_left(tree, NULL);

    // No operations are allowed now, but clear the structure as a precaution.
    memset(tree, 0, sizeof(BiTree));
    
    return ;
}


/**
 * Inserts a node as the left child of node in the binary tree specified by tree.
 *
 * @Complexity O(1)
 *
 * @param tree 树
 * @param node 指定的节点
 * @param data 节点数据
 *
 * @return 0 if inserting the element is successful, or -1 otherwise.
 * */
int bitree_ins_left(BiTree *tree, BiTreeNode *node, const void *data){
    BiTreeNode *new_node, **position;

    // Determine where to insert the node.
    if (node == NULL) {
        // Allow insertion at the root only in an empty tree.
        if (bitree_size(tree) > 0)
            return -1;

        position = &tree->root;
    }
    else {
        // Normally allow insertion only at the end of a branch,
        if (bitree_left(node) != NULL)
            return -1;

        position = &node->left;
    }

    // Allocate storage for the node.
    if ((new_node = (BiTreeNode *)malloc(sizeof(BiTreeNode))) == NULL)
        return -1;

    // Insert the node into the tree 
    new_node->data = (void *)data;
    new_node->left = NULL;
    new_node->right = NULL;
    *position = new_node;

    // Adjust the size of the tree to account for the inserted node. 
    tree->size++;
    
    return 0;
}


/**
 * Inserts a node as the right child of node in the binary tree specified by tree.
 *
 * @Complexity O(1)
 *
 * @param tree 树
 * @param node 指定的节点
 * @param data 节点数据
 *
 * @return 0 if inserting the element is successful, or -1 otherwise.
 * */
int bitree_ins_right(BiTree *tree, BiTreeNode *node, const void *data){
    BiTreeNode *new_node, **position;

    // Determine where to insert the node 
    if (node == NULL) {
        // Allow insertion at the root only in an empty tree.
        if(bitree_size(tree) > 0)
            return -1;

        position = &tree->root;

    }
    else {
        // Normally allow insertion only at the end of a branch 
        if (bitree_right(node) != NULL)
            return -1;
        
        position = &node->right;

    }
    // Allocate storage for the node.
    if ((new_node = (BiTreeNode *)malloc(sizeof(BiTreeNode))) == NULL)
        return -1;

    // Insert the node into the tree.
    new_node->data = (void *)data;
    new_node->left = NULL;
    new_node->right = NULL;
    *position = new_node;

    // Adjust the size of the tree to account for the inserted node. 
    tree->size++;

    return 0;
}


/**
 * Removes the subtree rooted at the left child of node from the binary tree specified by tree.
 *
 * @Complexity O(n), where n is the number of nodes in the subtree.
 *
 * @param tree 树
 * @param node 指定结点
 *
 * @return None
 * */
void bitree_rem_left(BiTree *tree, BiTreeNode *node){
    BiTreeNode **position;

    // Do not allow removal from an empty tree.
    if (bitree_size(tree) == 0)
        return;

    // Determine where to remove nodes.
    if (node == NULL)
        position = &tree->root;
    else
        position = &node->left;

    // Remove the nodes
    if (*position != NULL) {
        bitree_rem_left(tree, *position);
        bitree_rem_right(tree, *position);

        if (tree->destroy != NULL) {
            // Call a user-defined function to free dynamically allocated data. 
            tree->destroy((*position)->data);
        }
        
        free(*position);
        *position = NULL;
        
        // Adjust the size of the tree to account for the removed node. 
        tree->size--;
    }
    return ;
}


/**
 * Removes the subtree rooted at the right child of node from the binary tree specified by tree.
 *
 * @Complexity O(n), where n is the number of nodes in the subtree.
 *
 * @param tree 树
 * @param node 指定结点
 *
 * @return None
 * */
void bitree_rem_right(BiTree *tree, BiTreeNode *node){
    BiTreeNode **position;

    // Do not allow removal from an empty tree.
    if (bitree_size(tree) == 0)
        return;

    // Determine where to remove nodes.
    if (node == NULL)
        position = &tree->root;
    else
        position = &node->right;

    // Remove the nodes 
    if (*position != NULL) {
        bitree_rem_left(tree, *position);
        bitree_rem_right(tree, *position);

        if (tree->destroy != NULL) {
            // Call a user-defined function to free dynamically allocated data. 
            tree->destroy((*position)->data);
        }
        free(*position);
        *position = NULL;

        // Adjust the size of the tree to account for the removed node. 
        tree->size--;

    }
    return;
}

/**
 * Merges the two binary trees specified by left and right into the single binary tree merge.
 *
 * @Complexity O(1) 
 *
 * @param merge 合并后的树
 * @param left  合并后左子树
 * @param right 合并后右子树
 * @param data  新树的根节点数据
 *
 * @return 0 if merging the trees is successful, or -1 otherwise
 * */
int bitree_merge(BiTree *merge, BiTree *left, BiTree *right, const void *data){
    // Initialize the merged tree.
    bitree_init(merge, left->destroy);

    // Insert the data for the root node of the merged tree.
    if (bitree_ins_left(merge, NULL, data) != 0) {
        bitree_destroy(merge);
        return -1;
    }

    // Merge the two binary trees into a single binary tree. 
    bitree_root(merge)->left = bitree_root(left);
    bitree_root(merge)->right = bitree_root(right);

    // Adjust the size of the new binary tree. 
    merge->size = merge->size + bitree_size(left) + bitree_size(right);

    // Do not let the original trees access the merged nodes. 
    left->root = NULL;
    left->size = 0;
    right->root = NULL;
    right->size = 0;

    return 0;
}
