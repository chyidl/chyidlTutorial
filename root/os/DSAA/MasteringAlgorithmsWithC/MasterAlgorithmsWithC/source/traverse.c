//
//  traverse.h
//  MasterAlgorithmsWithC
//  Descripted -- implementation of Functions for Traversing a Binary Tree.
//  Created by Chyi Yaqing on 2018/10/14.
//  Copyright © 2018 Chyi Yaqing. All rights reserved.
//

#include "list.h"
#include "traverse.h"

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
int bitree_preorder(const BiTreeNode *node, List *list){
    if (!bitree_is_eob(node)) {
        if (list_ins_next(list, list_tail(list), bitree_data(node)) != 0) 
            return -1;

        if (!bitree_is_eob(bitree_left(node))) {
            if (bitree_preorder(bitree_left(node), list) != 0) 
                return -1;
        }

        if (!bitree_is_eob(bitree_right(node))) {
            if (bitree_preorder(bitree_right(node), list) != 0) 
                return -1;
        }
    }

    return 0;
}


/**
 * 中序式遍历表达式树
 *
 * @param node 根节点
 * @param list 链表
 *
 * @return 操作成功返回0;否则返回-1
 * */
int bitree_inorder(const BiTreeNode *node, List *list) {
    if (!bitree_is_eob(node)) {
        if (!bitree_is_eob(bitree_left(node))) {
            if (bitree_inorder(bitree_left(node), list) != 0)
                return -1;
        }
        
        if (list_ins_next(list, list_tail(list), bitree_data(node)) != 0) 
            return -1;
        
        if (!bitree_is_eob(bitree_right(node))) {
            if (bitree_inorder(bitree_right(node), list) != 0) 
                return -1;
        }

    }
    return 0;
}


/**
 * 后序方式遍历表达式树
 *
 * @param node 根节点
 * @param list 链表
 *
 * @return 操作成功返回0;否则返回-1
 * */
int bitree_postorder(const BiTreeNode *node, List *list){
    if (!bitree_is_eob(node)) {
        if (!bitree_is_eob(bitree_left(node))) {
            if (bitree_postorder(bitree_left(node), list) != 0) 
                return -1;
        }

        if (!bitree_is_eob(bitree_right(node))){
            if (bitree_postorder(bitree_right(node), list) != 0)
                return -1;
        }

        if (list_ins_next(list, list_tail(list), bitree_data(node)) != 0)
            return -1;
    }
    return 0;
}

