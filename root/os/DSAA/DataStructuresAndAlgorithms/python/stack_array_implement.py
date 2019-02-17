#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:encoding=utf-8
#
# stack_array_implement.py
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

Implementing Stack using Arrays
    Pros: Easy to implement. Memory is saved as pointers are not involved.
    Cons: It is not dynamic. It doesn't grow and shrink depending on needs
    at runtime.

Infix expression: The expression of the form a op b.When an operator is in
    between every pair of operands.

Postfix expression: The expression of the form a b op. When an operator is
    followed for every pair of operands.

The corresponding expression in postfix form is: abc*+d+. The postfix
expressions can be evaluated easily using a stack. We will cover postfix
expression evaluation in a separate post.

Algorithm:
    1) Scan the infix expression from left to right
    2) if the scanned character is an operand, output it.
    3) Else
        a) if the precendence of the scanned operator is greater than the
        precedence of the operator in the stack(or the stack is empty or the
        stack contains a'('), push it.
        b) Else, Pop all the operators from the stack which are greater than
        or equal to in precendence than that of the scanned operator. After
        doing that Push the scanned operator to the stack
"""
# Python program for implementation of Stack
# import maxsize from sys module
# Used to return -infinite when stack is empty
import sys


# Function to create a stack. It initializes size of stack as 0
class Stack:
    def __init__(self):
        self.data = []

    # Stack is empty when stack size is 0
    def isEmpty(self):
        return len(self.data) == 0

    # Function to add an item to stack. It increase size by 1
    def push(self, item):
        self.data.append(item)
        print("pushed {} to stack".format(item))

    # Function to remove an item from stack. It decreases size by 1
    def pop(self):
        if self.isEmpty():
            return str(-sys.maxsize - 1)  # return minus infinite

        return self.data.pop()


if __name__ == '__main__':
    # Driver program to test above class
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("popped {} from stack".format(stack.pop()))
