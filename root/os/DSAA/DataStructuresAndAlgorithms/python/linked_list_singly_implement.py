#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# linked_list_singly_implement.py
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
# Created by Chyi Yaqing on 02/15/19 11:29.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Implementing a Singly Linked List in Python

Linked list elements are not stored at contiguous location, the elements are
linked using pointers.

Linked list Advantages over Arrays:
    1) Dynamic size
    2) Ease of insertion/deletion

Linked list Drawbacks over Arrays:
    1) Random access is not allowed.
    2) Extra memory space for a pointers is required with each element of the
    list.
    3) Not cache friendly. Since array elements are contiguous locations, there
    is locality of reference which is not there in case of linked list.

Linked list Representation:
    Each node in a list consists of at least two parts
        1) data
        2) Pointer (Or Reference) to the next node

Linked list Insert a New Node
    1) At the front of the linked list
    2) After a given node.
    3) At the end of the linked list

To delete a node from linked list
    1) Find previous node of the node to be deleted
    2) Change the next of previous node
    3) Free memory for the node to be deleted
"""


# A simple Python program to introduce a linked list

# Node class
class Node:
    # Function to initialize the ndoe object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Singly Linked list class contains a Node object
class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        # 1 & 2: Allocate the Node & Put in the data
        new_node = Node(new_data)
        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node

    # Inserts a new node after the given prev_node.
    def insertAfter(self, prev_node, new_data):
        # 1. check if the given prev_node exists
        if prev_node is None:
            print("The given previous node must in LinkedList.")
            return
        # 2. Create new node & 3. Put in the data
        new_node = Node(new_data)

        # 4. Make next of new Node as next of prev_node
        new_node.next = prev_node.next

        # 5. make next of prev_node as new node
        prev_node.next = new_node

    # Appends a new node at the end. This method is defined inside
    # LinkedList class shown above.
    def append(self, new_data):
        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as Node
        new_node = Node(new_data)

        # 4. If the Linked List is empty, then make the new node as head
        if self.head is None:
            self.head = new_node
            return

        # 5. Else traverse till the last node
        last = self.head
        while last.next:
            last = last.next

        # 6. Change the next of last node
        last.next = new_node

    # Delete the first occurence of key in linked list
    def deleteNode(self, key):
        # Store head node
        temp = self.head

        # If head node itself holds the key to be deleted
        if (temp is not None and temp.data == key):
            self.head = temp.next
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
        if (temp is None):
            return

        # Unlink the node from linked list
        prev.next = temp.next
        temp = None

    # Utility function to print the linked Linked List
    def printList(self):
        temp = self.head
        print("HEADER", end='')
        while temp:
            print(' -> ', temp.data, end='')
            temp = temp.next
        print(" NULL", end='')


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()

    # Insert 6. So linked list becomes 6->None
    llist.append(6)

    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.push(7)

    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.push(1)

    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.append(4)

    # Insert 8, after 7. So linked list becomes 1->7->8->6->4->None
    llist.insertAfter(llist.head.next, 8)

    print("Created Linked list is:")
    llist.printList()
    llist.deleteNode(7)
    print("\nLinked List after Deletion of 1:")
    llist.printList()
