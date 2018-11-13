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
* Define a structure for binary tree nodes. 
*******************************************************************/

typedef struct BiTreeNode_ {
    
    void                *data;
    struct BiTreeNode_  *left;
    struct BiTreeNode_  *right;

} BiTreeNode;

/**
 * Define a structure for binary trees.
 */
typedef struct BiTree_ {

    int         size;

    int         (*compare)(const void *key1, const void *key2);
    void        (*destroy)(void *data);

    BiTreeNode  *root;
} BiTree;

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
void bitree_init(BiTree *tree, void (*destroy)(void *data));


/**
 * Destroys the binary tree specified by tree.
 *
 * @Complexity O(n), where n is the number of nodes in the binary tree.
 *
 * @param tree 树
 *
 * @return None 
 * */
void bitree_destroy(BiTree *tree);


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
int bitree_ins_left(BiTree *tree, BiTreeNode *node, const void *data);


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
int bitree_ins_right(BiTree *tree, BiTreeNode *node, const void *data);


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
int bitree_rem_left(BiTree *tree, BiTreeNode *node);


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
int bitree_rem_right(BiTree *tree, BiTreeNode *node);

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
int bitree_merge(BiTree *merge, BiTree *left, BiTree *right, const void *data);


/**
 * Macro that evaluates to the number of nodes in the binary tree specified by tree
 *
 * @Complexity O(1)
 *
 * @return Number of nodes in the tree
 * */
#define bitree_size(tree) ((tree)->size)


/**
 * Macro that evaluates to the node at the root of binary the tree specified by tree.
 *
 * @Complexity O(1)
 *
 * @return Element at the root of the tree
 * */
#define bitree_root(tree) ((tree)->root)


/**
 * Macro that determines whether the node specified as node marks the end of a branch in a binary tree.
 *
 * @Complexity O(1)
 *
 * @return  1 if the node marks the end of a branch, or 0 otherwise. 
 * */
#define bitree_is_eob(node) ((node) == NULL)


/**
 * Macro that determines whether the node specified as node is a leaf node in a binary tree.
 *
 * @Complexity O(1)
 *
 * @return 1 if the node is a leaf node, or 0 otherwise.
 * */
#define bitree_is_leaf(node) ((node)->left == NULL && (node)->right == NULL)


/**
 * Macro that evaluates to the data stored in the node of a binary tree specified by node.
 *
 * @Complexity O(1)
 *
 * @return Data stored in the node.
 * */
#define bitree_data(node) ((node)->data)


/**
 * Macro that evaluates to the node of a binary tree that is the left child of the node specifed by node.
 *
 * @Complexity O(1)
 *
 * @return Left child of the specified node.
 * */
#define bitree_left(node) ((node)->left)


/**
 * Macro that evaluates to the node of a binary tree that is the right child of the node specifed by node.
 *
 * @Complexity O(1)
 *
 * @return Right child of the specified node.
 * */
#define bitree_right(node) ((node)->right)

#endif /* bitree_h */
