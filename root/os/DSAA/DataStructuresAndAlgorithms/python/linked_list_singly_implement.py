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

Find Length of a Linked List
count number of nodes in a given singly linked list
    1) Initialize count as 0
    2) Initialize a node pointer, current = head
    3) Do following while current is not NULL
        a) current = current -> next
        b) count++
    4) Return count
Recursive Solution int getCount(head)
    1) If head is NULL, return 0
    2) Else return 1 + getCount(head->next)

Search an element in a Linked List
    1) Initialize a node pointer, current = head.
    2) Do following while current is not NULL
        a) current->key is equal to the key being searched return true
        b) current = current->next
    3) Return false

Reverse a Linked List
    1) Initialize three pointers prev as NULL, curr as head and next as NULL
    2) Iterate trough the linked list. In loop, do following.
        // Before changing next of current store next node
        next = curr->next
        // Now change next of current, This is where actual reversing happens
        curr->next = prev
        // Move prev and curr one step forward
        prev = curr
        curr = next

Detect loop in a linked list Following are different ways of doing this:
    1) Use Hashing
        Traverse the list one by one and keep putting the node addresses in a
        Hash Table. At any point, if NULL is reached then return false and if
        next of current node points to any of the previously stored nodes in
        Hash then return true.
    2) Mark Visited Nodes:
        This solution requires modifications to basic linked list data
        structure. Have a visited flag with each node. Traverse the linked list
        and keep marking visited nodes. If you see a visited node again then
        there is a loop. This solution works in O(n) but requires additional
        information with each node.

Floyd's Cycle-Finding Algorithm
    This is the fastest method, Traverse linked list using two pointers. Move
    one pointer by one and other pointer by two. If these pointers meet at same
    node then there is a loop. if pointers do not meet then linked list doesn't
    have loop

Find the middle of a given linked list
    1) Traverse the whole linked list and count the no. of nodes. Now traverse
    the list again till count/2 and return the node at count/2

    2) Traverse linked list using two pointers. Move one pointer by one and
    other pointer by two. When the fast pointer reaches and slow pointer will
    reach middle of the linked list.

Merge two sorted lists (in-place)

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
        self.head = None  # Initialize head as None

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
            print("the linked list is NULL, so no middle node")

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
    llist.reverse()
    print("\nReversed Linked List")
    llist.printList()
    llist.deleteNode(7)
    print("\nLinked List after Deletion of 1:")
    llist.printList()

    if llist.search(1):
        print("\nYes")
    else:
        print("\nNo")

    if (llist.detectLoop()):
        print("Loop found")
    else:
        print("No Loop")

    llist.detectLoopFloyd()
    llist.printList()
    print("\nCount of nodes is :", llist.getCount())
    llist.middle()
