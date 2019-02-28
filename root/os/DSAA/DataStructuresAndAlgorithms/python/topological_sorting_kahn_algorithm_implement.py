#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# topological_sorting_kahn_algorithm_implement.py
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
# Created by Chyi Yaqing on 02/28/19 09:30.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Kahn's algorithm for Topological Sorting: Topological sorting for
Directed Acyclic Graph(DAG) is a linear ordering of vertices such that for
every directed edge uv, vertex u comes before v in the ordering.

Algorithm:
    1) Compute in-degree(number of incoming edges) for each of the vertex
    present in the DAG and initialize the count of visited nodes as 0.

    2) Pick all the vertices with in-degree as 0 and add them into a queue
    (Enqueue operation)

    3) Remove a vertex from the queue (Dequeue operation) and then:
        a) Increment count of visited nodes by 1
        b) Decrease in-degree by 1 for all its neighbording nodes
        c) if in-degree of a neighbording nodes is reduced to zero, then add it
        to the queue

    4) Repeat Step 3 until the queue is empty

    5) If count of visited nodes is not equal to the number of nodes in the
    graph then the topological sort is not possible for the given graph

Kahn 算法时间复杂度O(V+E) V: 顶点数 E:表示边数
"""
# A Python program to print topological sorting of a graph using indegrees
from collections import defaultdict


# class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency list
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # The function to do Topological Sort
    def topologicalSortByKahn(self):
        # Create a vector to store indegrees of all vertices.
        # Initialize all indegrees as 0.
        in_degree = [0]*(self.V)

        # Traverse adjacency lists to fill indegrees of vertices.
        # This step takes O(V+E) time
        for i in self.graph:
            for j in self.graph[i]:
                in_degree[j] += 1

        # Create an queue and enqueue all vertices with indegree 0
        queue = []
        for i in range(self.V):
            if in_degree[i] == 0:
                queue.append(i)

        # Initialize count of visited vertices
        cnt = 0

        # Create a vector to store result (A topological ordering of the
        # vertices)
        top_order = []

        # One by one dequeue vertices from queue and enqueue adjacents if
        # indegree of adjacent becomes 0
        while queue:
            # Extract front of queue (or perform dequeue) and add it
            # to topological order
            u = queue.pop(0)
            top_order.append(u)

            # Iterate through all neighbouring nodes of dequeued node u and
            # decrese their in-degree by 1
            for i in self.graph[u]:
                in_degree[i] -= 1
                # If in-degree becomes zero, add it to queue
                if in_degree[i] == 0:
                    queue.append(i)

            cnt += 1

        # Check if there was a cycle
        if cnt != self.V:
            print("There exists a cycle in the graph")
        else:
            print(top_order)


if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)

    print("Following is a Topological Sort of the given graph")
    g.topologicalSortByKahn()
