#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# greedy_algorithms_activity_selection_implement.py
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
# Created by Chyi Yaqing on 02/27/19 12:40.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
A greedy algorithm is an algorithmic paradigm that follows the problem solving
heuristic of making the locally optimal choice at each stage with the intent of
finding a global optimum.In many problems, a greedy strategy does not usually
produce an optimal solution, but nonetheless a greedy heuristic may yield
locally optimal solutions that approximate a globally optimal solution in a
reasonable amount of time.

Activity Selection problem as our first example of Greedy algorithms.
    you are given n activities with their start and finish times. Select the
    maximum number of activities that can be performed by a single person,
    assuming that a person can only work on a single activity at a time.
"""
# The foloowing implementation assume that the activities are laredy sorted
# according to their finished time


# Prints a maximum set of activities that can be done by a single person, one
# at a time
# n             --> Total number of activities
# start[]       --> An array that contains start time of all activities
# finish[]      --> An array that contains finished time of all activities
def printMaxActivities(start, finish):
    print("The following activities are selected")
    # The first activity is always selected
    i = 0
    print(i, end="->")
    # Consider reset of the activities
    for j in range(len(finish)):
        # If this activity has start time greater than or equal to the finish
        # time of previously selected activity, then select it.
        if start[j] >= finish[i]:
            print(j, end="->")
            i = j


# Driver program to test above function
start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
printMaxActivities(start, finish)
