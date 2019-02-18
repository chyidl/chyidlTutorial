#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:encoding=utf-8
#
# stack_linked_list_implement.py
# python
#
# 🎂"Here's to the crazy ones. The misfits. The rebels.
# The troublemakers. The round pegs in the square holes.
# The ones who see things differently. They're not found
# of rules. And they have no respect for the status quo.
# You can quote them, disagree with them, glority or vilify
# them. About the only thing you can't do is ignore them.
# Because they change things. They push the human race forward.
# And while some may see them as the creazy ones, we see genius.
# Because the poeple who are crazy enough to think thay can change
# the world, are the ones who do."
#
# Created by Chyi Yaqing on 02/17/19 21:06.
# Copyright © 2019. Chyi Yaqing. All rights reserved.
#
# Distributed under terms of the MIT
"""
Stack Data Structure
Stack is a linear data structure. The order may be LIFO(Last in First Out)
of FILO(First In Last Out).

Mainly the following three basic operations are performed in the stack:
    Push: Adds an item in the stack. If the stack is full, then it is said to
        be Overflow condition
    Pop: Removes an item from the stack. The items are popped in the reversed
        order in which they are pushed. If the stack is empty, the it is said
        to be an Underflow condition
    Peek or Top: Returns top element of stack
    isEmpty: Returns true if stack is empty, elese false.

Stack Insertion and Deletion happen on same end.
Time Complexities of operations on stack:
    push(),pop(),isEmpty() and peek() all take O(1) time.

Implementing Stack using Linked List
    Pros:The linked list implementation of stack can grow and shrink according
        to needs at runtime.
    Cons: Requires extra memory due to involvement of points

Using a stack to evaluate postfix
    1) Starting at the beginning of the expression, get one term (operator or
    operand) at a time.
        a) If the term is an operand, push it on the stack.
        b) If the term is an operator, pop two operands off the stack, perform
        the operation on them, and push the result back on the stack
    2) When you get to the end of the expression, there should be exactly one
    operand left on the stack. That operand is the result.
"""
# Python program for linked list implementation of Stack


# Class to represent a node
class StackNode:
    # Constructor to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    # Constructor to initialize the root of linked list
    def __init__(self):
        self.root = None

    # Check whether the stack is empty
    def isEmpty(self):
        return True if self.root is None else False

    # Add a new item to the stack
    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.root
        self.root = newNode
        print("pushed {} to stack".format(data))

    # Remove the return an item from the stack. The item that is returned is
    # always the last one that was added.
    def pop(self):
        if (self.isEmpty()):
            return float("-inf")
        temp = self.root
        self.root = self.root.next
        popped = temp.data
        return popped

    def peek(self):
        if self.isEmpty():
            return float("-inf")
        return self.root.data


if __name__ == '__main__':
    # Driver program to test above class
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("{} popped from stack".format(stack.pop()))
    print("Top element is {}".format(stack.peek()))
