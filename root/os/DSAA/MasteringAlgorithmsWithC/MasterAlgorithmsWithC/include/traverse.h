//
//  traverse.h
//  MasterAlgorithmsWithC
//  Descripted -- implementation of Functions for Traversing a Binary Tree.
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#ifndef traverse_h
#define traverse_h

#include "bitree.h"
#include "list.h"


/*******************************************************************
* Public Interface
*******************************************************************/

/**
 * 前序方式遍历表达式树
 *
 * @param node 根节点
 * @param list 链表
 *
 * @return 操作成功返回0;否则返回-1
 * */
int bitree_preorder(const BiTreeNode *node, List *list);


/**
 * 中序式遍历表达式树
 *
 * @param node 根节点
 * @param list 链表
 *
 * @return 操作成功返回0;否则返回-1
 * */
int bitree_inorder(const BiTreeNode *node, List *list);


/**
 * 后序方式遍历表达式树
 *
 * @param node 根节点
 * @param list 链表
 *
 * @return 操作成功返回0;否则返回-1
 * */
int bitree_postorder(const BiTreeNode *node, List *list);

#endif /* traverse_h */
