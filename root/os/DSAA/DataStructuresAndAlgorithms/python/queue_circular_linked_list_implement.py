#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# queue_circular_linked_list_implement.py
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
# Created by Chyi Yaqing on 03/03/19 11:00.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Circular Queue is a linear data structure in which the operations are performed
based on FIFO(First In First Out) principle and the last position is connected
back to the first position to make a circle. It is also called "Ring Buffer"

Operations on Circular Queue:
    Front: Get the front item from queue.
    Rear: Get the last item from queue.
    enQueue(value): This function is used to insert an element into the
        circular queue. In a circular queue. the new element is always inserted
        at Rear position.

        Steps:
            1. Check whether queue is Full - Check (
                (rear == SIZE-1 && front == 0)||(rear == front-1))
            2. If it is full then display Queue is full. If queue is not full
                then, check if (rear == SIZE-1 && font != 0) if it is true
                then set rear=0 and insert element.
    deQueue(): This function is used to delete an element from the circular
        queue.In a circular queue, the element is always deleted from front
        position.

        Steps:
            1. Check whether queue is Empty means check (front == -1).
            2. if it is empty then display Queue is empty, If queue is not
                empty then step3
            3. Check if (front == rear) if it is true then set front=rear=-1
                else check if (front==size-1), if it is true then set front 0
                and return the element.

Time Complexity: Time complexity of enqueue(), dequeue() operation is O(1) as
there is no loop in any of the operation.

Applications:
    1. Memory Management: The unused memory locations in the case of ordinary
        queues can be utilized in circular queues.
    2. traffic system: In computer controlled traffic system, circular queue
        are used to switch on the traffic lights one by one repeatedly as per
        the time set.
    3. CPU Scheduling: Operating systems often maintain a queue of process-es
        that are ready to execute or that are waiting for a particular envent
        to occur
"""


class CircularQueue():

    # constructor
    def __init__(self, size):  # initializing the class
        self.size = size

        # initializing queue with none
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def enqueue(self, data):
        # condition if queue is full
        if ((self.rear + 1) % self.size == self.front):
            print("Queue is Full\n")

        # condition if queue is empty
        elif (self.front == -1):
            self.rear = self.front = 0
            self.queue[self.rear] = data
        else:
            # next position of rear
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if (self.front == -1):  # condition for empty queue
            print("Queue is Empty\n")

        # condition for only one element
        elif (self.front == self.rear):
            temp = self.queue[self.front]
            self.front = self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    def display(self):

        # condition for empty queue
        if (self.front == -1):
            print("Queue is Empty")

        elif (self.rear >= self.front):
            print("Elements in the circular queue are:", end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

        else:
            print("Elements in Circular Queue are:", end=" ")
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

        if ((self.rear + 1) % self.size == self.front):
            print("Queue is Full")


if __name__ == '__main__':
    circularq = CircularQueue(5)
    circularq.enqueue(14)
    circularq.enqueue(22)
    circularq.enqueue(13)
    circularq.enqueue(-6)
    circularq.display()
    print("Deleted value = ", circularq.dequeue())
    print("Deleted value = ", circularq.dequeue())
    circularq.display()
    circularq.enqueue(9)
    circularq.enqueue(20)
    circularq.enqueue(5)
    circularq.display()
