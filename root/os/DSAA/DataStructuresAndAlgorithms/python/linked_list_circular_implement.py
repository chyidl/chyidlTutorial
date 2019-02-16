#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# linked_list_circular_implement.py
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
# Created by Chyi Yaqing on 02/15/19 15:55.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Circular Linked List is a linked list where all nodes are connected to form a
circle. There is no NULL at the end. A Circular linked list can be a singly
circular linked list or doubly circular linked list.

Advantages of Circular Linked Lists:
    1) Any node can be a strating point.
    2) Useful for implementation of queue.
    3) Circular lists are useful in applications to repeatedly go around the
    list.
    4) Circular Doubly Linked lists are used for implementation of advanced
    data structures like Fibonacci Heap

Circular Linked List Deletion
    1) Empty list(start = NULL) simply return
    2)
"""


# Structure for a Node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:

    # Constructor to create a empty circular linked list
    def __init__(self):
        self.head = None

    # Function to insert a node at the beginning of a circule linked list
    def push(self, data):
        ptr1 = Node(data)
        temp = self.head
        ptr1.next = self.head

        # If Linked List is not None then set the next of last node
        if self.head is not None:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = ptr1
        else:
            ptr1.next = ptr1  # For the first node

        self.head = ptr1

    def get_node(self, index, start):
        if self.head is None:
            return None
        current = start
        for i in range(index):
            current = current.next
        return current

    # Delete the first occurence of key in Circular list
    def deleteNode(self, key):
        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if (temp is not None and temp.data == key):
            while(temp is not None):
                prev = temp
                temp = temp.next
                if temp == self.head:
                    self.head = temp.next
                    prev.next = self.head
                    temp = None
                    return

        # Search for the key to be deleted, keep track of the previous
        # node as we need to change 'prev.next'
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
            # if key was not present in linked list
            if (temp == self.head):
                return

        # Unlink the node from linked list
        prev.next = temp.next
        temp = None

    # Function to print nodes in a given circular linked list
    def printList(self):
        temp = self.head
        if self.head is not None:
            print("HEADER", end="")
            while(True):
                print(" -> ", temp.data, end='')
                temp = temp.next
                if (temp == self.head):
                    break


# Driver program to test above function
# Initialize list as empty
cllist = CircularLinkedList()

# Created linked list will be 11->2->56->12
cllist.push(12)
cllist.push(56)
cllist.push(2)
cllist.push(11)

print("Contents of circular Linked list")
cllist.printList()
print("\nDelete 11 from circular linked list")
cllist.deleteNode(key=11)
cllist.printList()
print("\nDelete 56 from circular linked list")
cllist.deleteNode(key=56)
cllist.printList()


"""
Josephus Circle using Circular Linked list

Using a circular single linked list to solve the Josephus problem.

"""


# Function to find the only person left after one in every
# k-th node is killed in a circle of n nodes
def getJosephusPosition(n, k):
    # Create a circular linked list of size N
    jPlist = CircularLinkedList()

    # Created linked list will be 11->2->56->12
    for i in reversed(range(n)):
        jPlist.push(i)
    print()

    # I Have no way to solve this problem at the moment
    if jPlist.head is None:
        return None
    start = jPlist.head

    while jPlist.head.next != jPlist.head:
        to_remove = jPlist.get_node(k-1, start)
        start = to_remove.next
        jPlist.deleteNode(to_remove.data)
    return jPlist.head.data


ans = getJosephusPosition(15, 7)
print('The person at position {} won\'t be killed.'.format(ans))
