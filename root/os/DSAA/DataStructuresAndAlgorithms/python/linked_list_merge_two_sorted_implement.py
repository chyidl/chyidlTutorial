#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# linked_list_merge_two_sorted_implement.py
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
# Created by Chyi Yaqing on 02/28/19 17:39.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Merge two sorted Linked lists

Method 1 (Using Dummy Nodes)
    The Strategy here uses a temporary dummy node as the start of the result.
    The pointer Tail always points to the last node in the result list,
    so appending new nodes is easy.
    
    The dummy node gives tail something to point to initially when the result
    list is empty. This dummy node is efficient, since it is only temporary,
    and it is allocated in the stack. The loop proceeds, removing one node from
    'a' or 'b', and adding it to tail.

Method 2 (Using Recursion)
    Merge is one of those nice recursive problems where the recursive solution
    code is much cleanerthan the iterative code. You probably wouldn't want to
    use the recursive version for production code however, because it will use
    stack space which is proporional to the length of the lists.
"""
# Python3 program merge two sorted linked in third linked list using recursive


# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Constructor to initialize the node object
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Method to print Linked List
    def printList(self):
        temp = self.head
        print("HEADER", end="->")
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("TAIL")

    # Function to add of node at the end
    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


# Takes two lists sorted in incresing order, and splices their nodes together
# to make one big sorted list which is returned.
def sortedMerge1(headA, headB):
    # a dummy first node to hang the result on
    dummy_node = Node('dummy')

    # tail points to the last result node
    tail = dummy_node

    while True:
        # if either list runs out, use the other list
        if headA is None:
            tail.next = headB
            break
        if headB is None:
            tail.next = headA
            break

        # Compare the data of the two lists whichever lists data is smaller,
        # append it into tail and advance the head to the next Node.
        if headA.data <= headB.data:
            tail.next = headA
            headA = headA.next
        else:
            tail.next = headB
            headB = headB.next

        # Advance the tail
        tail = tail.next

    return dummy_node.next


# Function to merge two sorted linked list.
def sortedMerge2(headA, headB):
    # create a temp node NULL
    temp = None

    # List1 is empty then return List2
    if headA is None:
        return headB

    # if List2 is empty then return List1
    if headB is None:
        return headA

    # If List1, data is smaller or equal to List2 data
    if headA.data <= headB.data:
        # assign temp to List1 data
        temp = headA

        # Again check List1 data is smaller or equal list2 data and call sortedMerge2 function
        temp.next = sortedMerge2(headA.next, headB)
    else:
        # If List2 data is greater then or equal List1 data assign temp to head2
        temp = headB

        # Again check List2 data is greater or equal List data and call sortedMerge2 function
        temp.next = sortedMerge2(headA, headB.next)

    # Return the temp list
    return temp


# Driver Function
if __name__ == "__main__":
    # Create Linked list 1:
    # 10->20->30->40->50
    list1 = LinkedList()
    list1.append(10)
    list1.append(20)
    list1.append(30)
    list1.append(40)
    list1.append(50)

    # Create linked list 2:
    # 5->15->25->35->60
    list2 = LinkedList()
    list2.append(5)
    list2.append(15)
    list2.append(25)
    list2.append(35)
    list2.append(60)

    # Method 1:
    # Create listMethod1
    #listMethod1 = LinkedList()
    #listMethod1.head = sortedMerge1(list1.head, list2.head)
    #print("Method 1:")
    #listMethod1.printList()

    # Method 2:
    # Create listMethod2
    listMethod2 = LinkedList()
    listMethod2.head = sortedMerge2(list1.head, list2.head)
    print("Method 2:")
    listMethod2.printList()
