#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# shortest_path_algorithm_Dijkstra_implement.py
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
# Created by Chyi Yaqing on 02/28/19 10:32.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Dijkstra's algorithm is an algorithm for finding the shortest paths between
nodes in a graph, which may represent, for example, road networks.

The algorithm exists in many variants; Dijkstra's original variant found the
shortest path between two nodes, but a more common variant fixes a single nodes
as the "source" nodes and finds shortest paths from the source to all other
nodes in the graph, producing a shortest-path tree.

Below are the detailed steps used in Dijkstra's algorithm to find the shortest
path from a single source vertex to all other vertices in the given graph.
    1) Create a set sptSet(shortest path tree set) that keeps track of vertices
    included in shortest path tree.

    2) Assign a distance value to all vertices in the input graph. Initialize
    all distance values as INFINITE. Assign distance value as 0 for the source
    vertex so that it is picked first.

    3) While sptSet doesn't include all vertices
        a) Pick a vertex u which is not there in sptSet and has minimum
        distance value.

        b) Include u to sptSet

        c) Update distance value of all adjacent vertices of u. To update the
        distance values, iterate through all adjacent vertices. For every
        adjacent vertex v, if sum of distance value of u(from source) and
        weight of edge u-v, is less than the distance value of v, then update
        the distance value of v.
"""
# Python program for Dijkstra's single source shortest path algorithm. The
# program is for adjacency matrix representation of the graph


# 有向有权图的邻接表表示
class Graph:
    def __init__(self, vertices):
        self.V = vertices  # 顶点数
        self.graph = [[0 for column in range(
            vertices)]for row in range(vertices)]
    
    def addEdge(self, u, v, w):
        # u: 起始顶点编号 v: 终止顶点编号 w: 权重
        if u >= self.V or v >= self.V:
            print("Out of operating range")
            return
        self.graph[u][v] = w
    
    def printSolution(self, dist):
        print("Vertex Distance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    # A utility function to find the vertex with minimum distance value, from
    # the set of vertices not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
        # Initialize minimum distance for next node
        min = float("inf")

        # Search not nearest vertex not in the shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] is False:
                min = dist[v]
                min_index = v
        return min_index

    # Function that implements Dijkstra's single source shortest path algorithm
    # for a graph represented using adjacency matrix representation
    def dijkstra(self, src):
        # 从起始顶点到这个顶点的距离
        dist = [float("inf")] * self.V
        dist[src] = 0
        sptSet = [False] * self.V  # Shorts path tree set

        for cout in range(self.V):
            # Pick the minimum distance vertex from the set of vertices not
            # yet processed. u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the shotest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices of the picked vertex
            # only if the current distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                if self.graph[u][v] > 0 and (
                        sptSet[v] is False) and (
                        dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)


if __name__ == '__main__':
    g = Graph(9)
    g.graph = [
            [0, 4, 0, 0, 0, 0, 0, 8, 0],
            [4, 0, 8, 0, 0, 0, 0, 11, 0],
            [0, 8, 0, 7, 0, 4, 0, 0, 2],
            [0, 0, 7, 0, 9, 14, 0, 0, 0],
            [0, 0, 0, 9, 0, 10, 0, 0, 0],
            [0, 0, 4, 14, 10, 0, 2, 0, 0],
            [0, 0, 0, 0, 0, 2, 0, 1, 6],
            [8, 11, 0, 0, 0, 0, 1, 0, 7],
            [0, 0, 2, 0, 0, 0, 6, 7, 0]]
    g.dijkstra(0)
