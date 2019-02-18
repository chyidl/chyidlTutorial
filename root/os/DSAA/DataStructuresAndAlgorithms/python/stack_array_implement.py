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

In computer science, a call stack is a stack data structure that stores
information about the active subroutines of a computer program. a call stack
the main reason for having one is to keep track of the point to which each
active subroutine should return control when it finishes executing.

Implementing Stack using Arrays
    Pros: Easy to implement. Memory is saved as pointers are not involved.
    Cons: It is not dynamic. It doesn't grow and shrink depending on needs
    at runtime.

Given a string, reverse it using stack.
    1) Create an empty stack
    2) One by one push all characters of string to stack
    3) One by one pop all characters from stack and put them back to string

Infix expression: The expression of the form a op b.When an operator is in
    between every pair of operands.

Postfix expression: The expression of the form a b op. When an operator is
    followed for every pair of operands.

The repeated scanning makes it very in-efficient. It is better to convert the
expression to postfix(or prefix) form before evaluation. The postfix expression
can be evaluated easily using a stack.

Algorithm
    1) Scan the infix expression from left to right
    2) If the scanned character is an operand, output it.
    3) Else,
        a) If the precedence of the scanned operator is greater than the
            precedence of the operator in the stack(or the stack is empty or
            the stack contains a '('), push it.
        b) Else, Pop all the operators from the stack which are greater than or
        equal to in precedence than that of the scanned operator. After doing
        that Push the scanned operator to the stack. (If you encounter
        parenthesis while poping then stop there and push the scanned operator
        in the stack.)
    4) If the scanned character is an '(', push it to the stack.
    5) if the scanned character is an ')', pop the stack and output it until a
        '(' is en-countered,and discard both the parenthesis.
    6) Repeat steps 2-6 until infix expression is scanned.
    7) Print the output
    8) Pop and output from the stack until it is not empty.

Evaluation of Postfix Expression:
    1) Create a stack to store operands (or values)
    2) Scan the given expression and do following for every scanned element.
        a) If the element is a number, push it into the stack
        b) If the element is a operator, pop operands for the operator from
        stack. Evaluate the operator and push the result back to the stack.
    3) When the expression is ended, the number in the stack is the final

There are following limitations of above implementation.
    1) It supports only 4 binary operators '+','*','-'and'/'.It can be extended
        for more operators by adding more switch cases.
    2) The allowed operands are only single operands. The program can be
        extended for multiple digits by adding a separator like space between
        all elements (operators and operands) of given expression
"""
# Python program for implementation of Stack
# import maxsize from sys module
# Used to return -infinite when stack is empty
import sys


# Function to create a stack. It initializes size of stack as 0
class Stack:
    def __init__(self):
        self.data = []

    # Function to determine the size of the stack
    def size(self):
        return len(self.stack)

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

    def peek(self):
        if self.isEmpty():
            return float('-inf')
        output = self.pop()
        self.push(output)
        return output


# A stack based function to reverse a string
def reverse(string):
    n = len(string)

    # Create a empty stack
    stack = Stack()

    # Push all characters of string to stack
    for i in range(0, n, 1):
        stack.push(string[i])

    # Making the string empty since all characters are saved in stack
    string = ""

    # Pop all characters of string and put them back to string
    for i in range(0, n, 1):
        string += stack.pop()

    return string


# A utility function to check is the given character is operand
def isOperand(ch):
    return ch.isdigit()


# Check is the precedence of operator is strictly less than top of stack or not
def notGreater(stack, i):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    try:
        a = precedence[i]
        b = precedence[stack.peek()]
        return True if a <= b else False
    except KeyError:
        return False


# The function converts given infix expression to postfix expression
def infixToPostfix(exp):
    output = []
    stack = Stack()
    # Iterate over the expression for conversion
    for i in exp:
        # If the character is an operand, add it to output
        if isOperand(i):
            output.append(i)
        # if the character is an '(', push it to stack
        elif i == '(':
            stack.push(i)
        # If the scanned character is an ')', pop and
        # output from the stack until and '(' is found
        elif i == ')':
            while ((not stack.isEmpty()) and stack.peek() is not '('):
                a = stack.pop()
                output.append(a)
            if (not stack.isEmpty() and stack.peek() is not '('):
                return -1
            else:
                stack.pop()
        # An operator is encountered
        else:
            while (not stack.isEmpty() and notGreater(stack, i)):
                output.append(stack.pop())
            stack.push(i)

    # pop all the operator from the stack
    while not stack.isEmpty():
        output.append(stack.pop())

    return output


# evaluete Postfix
def evaluatePostfix(exp):
    stack = Stack()
    # Iterate over the expression for conversion
    for item in exp:
        # If the scanned character is an operand (number here) push it to
        # the stack
        if item.isdigit():
            # push the element in the stack
            stack.push(item)

        # If the scanned character is an operaor, pop two elements from stack
        # and apply it.
        else:
            val1 = stack.pop()
            val2 = stack.pop()
            stack.push(str(eval(val2 + item + val1)))

    return int(stack.pop())


if __name__ == '__main__':
    # Driver program to test above class
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("popped {} from stack".format(stack.pop()))

    string = "Chyi Yaqing"
    print("Original string is {}".format(string))
    string = reverse(string)
    print("Reversed string is {}".format(string))

    exp = "2+(3*1)-9"
    postfix = "".join(infixToPostfix(exp))
    print(postfix)
    print(evaluatePostfix(postfix))
