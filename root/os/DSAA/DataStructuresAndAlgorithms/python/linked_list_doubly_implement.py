#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# linked_list_doubly_implement.py
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
# Created by Chyi Yaqing on 02/15/19 14:13.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
A Doubly Linked List (DLL) contains an extra pointer, typically called previous
pointer, together with next pointer and data which are there in singly linked
list.

Advantages over singly linked list
    1) A DLL can be traversed in both forward and backward direction
    2) The delete operation in DLL is more efficient if pointer to the node to
    be deleted is given
    3) can quickly insert a new node before a given node

Disadvantages over singly linked list
    1) Every node of DLL Require extra space for an previous pointer.
    2) All operations require an extra pointer previous to be maintained

Insertion : A node can be added in four ways
    1) At the front of the DLL
    2) After a given node
    3) At the end of the DLL
    4) Before a given node

Delete a node in a Doubly Linked List
    1) If node to be deleted is head node, then change the head pointer to
    next current head.
    2) Set next of previous to del, if previous to del exists.
    3) Set prev of next to del, if next to del exists.

Reverse a Doubly Linked List
    All we need to do is swap prev and next pointers for all nodes,change prev
    of the head (or start) and change the head pointer in the end
"""
import gc   # For Garbage collection


# Node of a doubly linked list
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None  # reference to next node in DLL
        self.prev = None  # reference to previous node in DLL


class DoublyLinkedList:

    # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head = None

    # Adding a node at the front of the Doubly Linked List
    def push(self, new_data):
        # 1 & 2: Allocate the Node & Put in the data
        new_node = Node(data=new_data)

        # 3. Make next of new node as head and previous as NULL
        new_node.next = self.head
        new_node.prev = None

        # 4. change prev of head node to new node
        if self.head is not None:
            self.head.prev = new_node

        # 5. move the head to point to the new node
        self.head = new_node

    # Given a node as prev_node, insert a new node after the given node
    def insertAfter(self, prev_node, new_data):
        # 1. check if the given prev_node is NULL
        if prev_node is None:
            print("This node doesn't exist in DLL")
            return

        # 2. allocate node & 3. put in the data
        new_node = Node(data=new_data)

        # 4. Make next of new node as next of prev_node
        new_node.next = prev_node.next

        # 5. Make the next of prev_node as new_node
        prev_node.next = new_node

        # 6. Make prev_node as previous of new_node
        new_node.prev = prev_node

        # 7. Change previous of new_node's next node
        if new_node.next is not None:
            new_node.next.prev = new_node

    # Given a node as next_node, insert a new node before the given node
    def insertBefore(self, next_node, new_data):
        # 1. check if the given prev_node is NULL
        if next_node is None:
            print("This node doesn't exist in DLL")
            return

        # 2. allocate node & 3. put in the data
        new_node = Node(data=new_data)

        # 4. Make prev of new node as prev of next_node
        new_node.prev = next_node.prev

        # 5. Make the prev of next_node as new_node
        next_node.prev = new_node

        # 6. Make next_node as next of new_node
        new_node.next = next_node

        # 7. Change next of new_node's previous node
        if new_node.prev is not None:
            new_node.prev.next = new_node
        # 8. If the prev of new_node is NULL, it will be the new head node
        else:
            self.head = new_node

    # Add a node at the end of the DLL
    def append(self, new_data):
        # 1. allocate node 2. put in the data
        new_node = Node(data=new_data)
        last = self.head

        # 3. This new node is going to be the last node, so make next of
        # it as NULL
        new_node.next = None

        # 4. If the Linked List is empty, then make the new node as head
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        # 5. Else traverse till the last node
        while (last.next is not None):
            last = last.next

        # 6. Change the next of last node
        last.next = new_node

        # 7. Make last node as previous of new node
        new_node.prev = last

    # Function to delete a node in a Doubly Linked List.
    def deleteNode(self, dele):
        # Base Case
        if self.head is None or dele is None:
            return

        # If node to be deleted is head node
        if self.head == dele:
            self.head = dele.next

        # Change next only if node to be deleted is NOT the last node
        if dele.next is not None:
            dele.next.prev = dele.prev

        # Change prev only if node to be deleted is NOT the first node
        if dele.prev is not None:
            dele.prev.next = dele.next

        # Finally, free the memory occupied by dele Call python
        # garbage collector
        gc.collect()  # run a full collection.

    # This function prints contents of linked list starting from the given node
    def printList(self):
        print("\nTraversal in forward direction")
        temp = self.head
        print("HEADER", end="")
        while temp:
            print(' -> ', temp.data, end='')
            last = temp
            temp = temp.next
        print(" NULL ", end='')

        print("\nTraversal in reverse direction")
        print(" TAIL ", end="")
        while last:
            print(' <- ', last.data, end='')
            last = last.prev

    # Function reverse a Doubly Linked List
    def reverse(self):
        temp = None
        current = self.head

        # Swap next and prev for all nodes of doubly linked list
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp

            current = current.prev

        # Before changing head, check for the cases like empty list and
        # list with only one node
        if temp is not None:
            self.head = temp.prev


# Dirver program to test above functions
if __name__ == '__main__':
    # Start with empty list
    llist = DoublyLinkedList()

    # Insert 6. So the list becomes 6-> None
    llist.append(6)

    # Insert 7 at the begining. so linked list become 7->6->None
    llist.push(7)

    # Insert 1 at the beginning so Linked list becomes 1->7->6->None
    llist.push(1)

    # Insert 4 at the end So linked list becomes 1->7->6->4->None
    llist.append(4)

    # Insert 8, after 7. So Linked List become 1->7->8->6->4->None
    llist.insertAfter(llist.head.next, 8)

    # Insert 5, before 7. So Linked List becomes 1->5->7->8->6->4->None
    llist.insertBefore(llist.head.next, 5)

    print("Created DLL is: ")
    llist.printList()

    # Reverse doubly linked list
    llist.reverse()
    print("\n\n Reversed Linked List")
    llist.printList()

    # delete nodes from doubly linked list
    llist.deleteNode(llist.head.next)
    print("\n Modified Linked List")
    llist.printList()
