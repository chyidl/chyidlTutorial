#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# sort_quick_doubly_linked_list_implement.py
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
# Created by Chyi Yaqing on 02/20/19 15:56.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
QuickSort on Doubly Linked List
"""


# Node of a doubly linked list
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None  # Reference to next node in DLL
        self.prev = None  # Reference to prev node in DLL


class DoublyLinkedList:

    # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head = None
        self.tail = None

    # Adding a node at the begining of the Doubly linked List
    def push(self, new_data):
        # allocate the Node put in the data
        new_node = Node(data=new_data)

        # Make next of new node as head and previous as NULL
        new_node.next = self.head
        new_node.prev = None

        # change prev of head node to new node
        if self.head is not None:
            self.head.prev = new_node
        else:
            self.tail = new_node

        # move the head to point to the node
        self.head = new_node

    # Add a node at the end of the DLL
    def append(self, new_data):
        # allocate node put in the data
        new_node = Node(data=new_data)
        last = self.head

        # This new node is going to be the last node, so make next of
        # it as NULL
        new_node.next = None
        self.tail = new_node

        # If the Linked List is empty, then make the new node as head
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        # Else traverse till the last node
        while (last.next is not None):
            last = last.next

        # Change the next of last node
        last.next = new_node

        # Make last node as previous of new node
        new_node.prev = last

    # This function prints contains of Linked list starting from the given node
    def printList(self):
        print("Traveral in forward direction")
        temp = self.head
        print("HEADER", end="")
        while temp:
            print(' -> ', temp.data, end='')
            temp = temp.next
        print(" None", end="")


# Considers last element as pivot, places the pivot element at its correct
# position in sorted array, and places all smaller (smaller than pivot) to
# left of pivot and all greater elements to right of pivot
def partition(head, tail):
    # set pivot as tail element
    pivot = tail
    current = head
    switcher = current
    while current != tail:
        if current.data < pivot.data:
            switcher.data, current.data = current.data, switcher.data
            switcher = switcher.next
        current = current.next
    switcher.data, pivot.data = pivot.data, switcher.data
    return switcher


# The main function to sort a linked list.
def quickSort(head, tail):
    if (head is not None and tail != head and tail != head.next):
        pivot = partition(head, tail)
        quickSort(head, pivot.prev)
        quickSort(pivot.next, tail)


# Driver program to test above function
if __name__ == '__main__':
    dlist = DoublyLinkedList()
    dlist.push(5)
    dlist.push(20)
    dlist.push(4)
    dlist.push(3)
    dlist.push(30)
    print("Original Doubly Linked List is \n")
    dlist.printList()
    print()
    quickSort(dlist.head, dlist.tail)
    print("Sorted Doubly Linked List is \n")
    dlist.printList()
