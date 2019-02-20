#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# sort_quick_singly_linked_list_implement.py
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
# Created by Chyi Yaqing on 02/19/19 09:24.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
QuickSort on Singly Linked List
The important things aboyt implementation are, it changes pointers rather
swapping data and time complexity is same as the implementation for Doubly
Linked List.
"""


# Node class
class Node:
    # Function to initialize the ndoe object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Singly Linked list class contains a Node object
class SinglyLinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None  # Initialize head as None
        self.tail = None  # Initialize tail as None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        # 1 & 2: Allocate the Node & Put in the data
        new_node = Node(new_data)
        # 3. Make next of new Node as head
        new_node.next = self.head

        if self.getCount() == 0:
            self.tail = new_node

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

    # This Function checks whether the value x present in the linked list
    def search(self, x):
        # Initialize current to head
        current = self.head

        # loop till current not equal to None
        while current is not None:
            if current.data == x:
                return True  # data found

            current = current.next

        return False  # Data Not found

    # Function to reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def detectLoop(self):
        s = set()
        temp = self.head
        while (temp):
            # If we have already has this node in hashmap it means their is
            # cycle (Because you we encountering the node second time).
            if (temp in s):
                return True

            # If we are seeing the node for the first time, insert it in
            # hash
            s.add(temp)

            temp = temp.next

    # Implementation of Floyd's Cycle-Finding Algorithm
    def detectLoopFloyd(self):
        slow_p = self.head
        fast_p = self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                print("Found Loop")
                return

    # This function counts number of nodes in Linked List iterative,
    # given 'node' as starting node.
    def getCount(self):
        temp = self.head  # Initialise temp
        count = 0  # Initialise count

        # Loop while end of linked list is not reached
        while (temp):
            count += 1
            temp = temp.next
        return count

    # Function to get the middle of the linked list
    def middle(self):
        slow_p = self.head
        fast_p = self.head

        if self.head is not None:
            while fast_p is not None and fast_p.next is not None:
                fast_p = fast_p.next.next
                slow_p = slow_p.next
            print("The middle element is [{}]\n".format(slow_p.data))
        else:
            print("the linked list is None, so no middle node")

    # Utility function to print the linked Linked List
    def printList(self):
        temp = self.head
        print("HEADER", end='')
        while temp:
            print(' -> ', temp.data, end='')
            temp = temp.next
        print(" None", end='')


# Find the before
def find_before(first, last, search_node):
    current = first
    while current is not last.next:
        if current.next == search_node:
            return current
        current = current.next
    return None


def swap(A, B):
    '''swaps the data '''
    temp = A.data
    A.data = B.data
    B.data = temp


def partition(head, end):
    # Partitions the list taking the last element as the pivot
    pivot = end
    switcher, current = head, head

    # During partition, both the head and end of the list might change
    # which is updated in the newHead and newEnd variables
    while (current is not pivot):
        if current.data < pivot.data:
            swap(switcher, current)
            switcher = switcher.next
        current = current.next
    swap(pivot, switcher)
    return switcher


def quickSort(head, tail):
    if head.next is not tail:
        m = partition(head, tail)
        quickSort(m.next, tail)
        mprev = find_before(head, tail, m)
        quickSort(head, mprev)


# Driver program to test above functions
if __name__ == '__main__':
    slist = SinglyLinkedList()
    slist.push(5)
    slist.push(20)
    slist.push(4)
    slist.push(3)
    slist.push(30)
    print("Original Singly Linked List")
    slist.printList()
    quickSort(slist.head, slist.tail)
    print("\n\nSorted Singly Linked List")
    slist.printList()
