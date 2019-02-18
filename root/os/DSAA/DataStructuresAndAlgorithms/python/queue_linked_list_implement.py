#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# queue_linked_list_implement.py
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
# Created by Chyi Yaqing on 02/18/19 10:57.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Like Stack, Queue is a linear structure which follows a particular order in
which the operations are performed. The order is First In First Out(FIFO).

In Queue data structure, we maintain two pointers, front and rear. The front
points the first item of queue and rear points to last item.

enQueue() : This operation adds a new node after rear and moves rear to the
    next node.
deQueue() : This operation removes the front node and moves front to the next
    node.
"""
# Python3 program to demonstrator linked list based implementation of queue


# A linked list (LL) node to store a queue entry
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# A class to represent a queue, The queue, front stores the front node or LL
# and rear stores the last node of LL
class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        return self.front is None

    # Method to add an item to the queue
    def EnQueue(self, item):
        temp = Node(item)

        if self.rear is None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    # Method to remove an item from queue
    def DeQueue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next

        if (self.front is None):
            self.rear = None
        return str(temp.data)


# Driver Code
if __name__ == '__main__':
    queue = Queue()
    queue.EnQueue(10)
    queue.EnQueue(20)
    queue.DeQueue()
    queue.DeQueue()
    queue.EnQueue(30)
    queue.EnQueue(40)
    queue.EnQueue(50)

    print("Dequeued item is {}".format(queue.DeQueue()))
