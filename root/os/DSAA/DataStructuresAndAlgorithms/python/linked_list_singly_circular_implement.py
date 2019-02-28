#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# linked_list_singly_circular_implement.py
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
# Created by Chyi Yaqing on 02/28/19 15:42.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Circular Linked List is a linked list where all nodes are connected to form a
circle. There is no NULL at the ned. A circular linked list can be a singly
circular linked list or doubly circular linked list.

1) Any node can be a starting point.

2) Useful for implementation fo queue.

3) Circular lists are useful in applications to repreatedly go around the list.

4) Circular Doubly Linked Lists are used for implementation of advanced data
structures like Fibonacci Heap.

Implementation:
    To implement a circular singly linked list, we take an external pointer
    that points to the last node of the list. If we have a pointer last
    pointing to the last node, then last->next will point to the first node.
"""
# Python program to demonstrate circular linked list traversal
import gc   # For Garbage collection


# Structure for a Node
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    # Constructor to create a empty circular linked list
    def __init__(self):
        self.head = None
        self.tail = None

    # Function to insert a node at the end of a circular linked list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        new_node.next = self.head
        self.tail.next = new_node
        self.tail = new_node
    
    # Function to delete a node in a Circular Singly Linked List
    def deleteNode(self, dele):
        # Base Case
        if self.head is None or dele is None:
            return

        # If node to be deleted is head
        if dele is self.head:
            self.head = self.head.next
            self.tail.next = self.head
        elif dele is self.tail:
            prev = self._findPre(self.tail)
            self.tail = prev
            prev.next = self.head
        else:
            prev = self._findPre(dele)
            prev.next = dele.next

        gc.collect()  # run a full collection.
    
    def _findPre(self, node):
        prev = self.head
        while True:
            if prev.next == node:
                break
            prev = prev.next
        return prev
    
    # Function to print node in a given circular linked list
    def printList(self):
        temp = self.head
        if self.head is not None:
            print("HEADER", end="->")
            while True:
                print(temp.data, end="->")
                temp = temp.next
                if temp == self.head:
                    print("TAIL", end="")
                    break


# Driver program to test above function
if __name__ == '__main__':
    # Initialize list as empty
    cllist = CircularSinglyLinkedList()
    # Created linked list will be 12->56->2->11
    cllist.append(12)
    cllist.append(56)
    cllist.append(2)
    cllist.append(11)
    cllist.append(33)
    cllist.append(28)
    
    print("Contents of circular Linked List")
    cllist.printList()
    print("\nDelete 56")
    node = cllist.head.next
    cllist.deleteNode(node)
    print("Contents of circular Linked List")
    cllist.printList()
    print("\nDelete 12")
    node = cllist.head
    cllist.deleteNode(node)
    print("Contents of circular Linked List")
    cllist.printList()
