#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# queue_array_implement.py
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

Operations on Queue:
    Enqueue: Adds an item to the queue. If the queue is full, then it is said
        to be an Overflow condition.
    Dequeue: Removes an item from the queue. The items are popped in the same
        order in which they are pushed. If the queue is empty, then it is said
        to be an Underflow condition.
    Front: Get the front item from queue
    Rear: Get the last item from queue

Array implementation of Queue:
For implementing queue, we need to keep track of two indices, front and rear.
We en-queue an item at the rear and dequeue an item from front.
"""


# Class Queue to represent a queue
class Queue:

    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        self.Q = [None]*capacity
        self.capacity = capacity

    # Queue is full when size become equal to the capacity
    def isFull(self):
        return self.size == self.capacity

    # Queue is empty when size is 0
    def isEmpty(self):
        return self.size == 0

    # Function to add an item to the queue, It changes rear and size
    def EnQueue(self, item):
        if self.isFull():
            print("Full")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.Q[self.rear] = item
        self.size += 1
        print("{} enqueued to queue".format(item))

    # Function to remove an item from queue. It changes front and size
    def DeQueue(self):
        if self.isEmpty():
            print("Empty")
            return

        print("{} dequeued from queue".format(self.Q[self.front]))
        self.front = (self.front + 1) % (self.capacity)
        self.size -= 1

    # Function to get front of queue
    def que_front(self):
        if self.isEmpty():
            print("Queue is empty")
        print("Front item is {}".format(self.Q[self.front]))

    # Function to get rear of queue
    def que_rear(self):
        if self.isEmpty():
            print("Queue is empty")
        print("Rear item is {}".format(self.Q[self.rear]))


# Driver Code
if __name__ == '__main__':
    queue = Queue(4)
    queue.EnQueue(10)
    queue.EnQueue(20)
    queue.EnQueue(30)
    queue.EnQueue(40)
    queue.DeQueue()
    queue.que_front()
    queue.que_rear()
