#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# graph_implement.py
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
# Created by Chyi Yaqing on 02/26/19 14:16.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Graph and its representations

Graph is a data structure that consists of following two components:
    1) A finite set of vertices also called as nodes.
    2) A finite set of ordered pair of the form(u, v) called as edge. The pair
    is ordered be-cause(u, v) is not same as (v, u) in case of a directed
    graph(di-graph). The pair of the form (u, v) indicates that there is an
    edge from vertex u to vertex v. The edges may contain weight/value/cost.

In Facebook, each person is represented with a vertex(or node). Each node is a
structure and contains information like person id, name, gender and locale.

无向图(undirected graph)
有向图(directed graph)

Following two are the most commonly used representations of a graph.
    1) Adjacency Matrix 邻接矩阵
    2) Adjacency List   邻接表

Adjacency Matrix: 邻接矩阵
    Adjacency Matrix is a 2D array of size V x V where V is the number of
    vertices in a graph.Let the 2D array be adj[i][j],adj[j][i]=1 indicates
    that there is an edge from vertex i to vertex j. Adjacency Matrix is also
    used to represent weighted graphs. If adj[i][j]=w, then there is an edge
    from vertex i to vertex j with weight w.

Adjacency List:
    An array of lists is used, Size of the array is equal to the number of
    vertices.

Breadth-first search: 广度优先搜索
    Breadth-first search (BFS) is an algorithm for traversing or searching
    tree or graph data structures. It starts at a 'search key', and explores
    all of the neighbor nodes at the present depth prior to moving on to the
    nodes at the next depth level.

Depth First Search:


"""
# A Python program to demonstrate the adjacency list representation of the gra


# A class to represent the adjacency list of the node
class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


# A class to represent a graph. A graph is the list of the adjacency lists.
# Size of the array will be the no. of the vertices
class Graph:
    # Constructor
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    # Function to add an edge in an undirected graph
    # 无向图一条边存两次
    def add_edge(self, src, dest):
        # Adding the node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        # Adding the source node to the destination as it is
        # the undirected graph
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    # Function to print a BFS of graph
    def breadth_first_search(self, src):
        # Mark all the virtices as not vistied
        visited = [False] * (len(self.graph))
        # Create a queue for BFS
        queue = []
        # Mark the source node as  visited and enqueue it
        queue.append(src)
        visited[src] = True

        while queue:
            # Dequeue a vertex from queue and print it
            src = queue.pop(0)
            print(src, end=" ")

            # Get all adjacent vertices of the dequeued vertex s. If a adacent
            # has not been visited, then mark it visited and enqueue it
            travl = self.graph[src]
            while travl.next:
                if visited[travl.vertex] is False:
                    queue.append(travl.vertex)
                    visited[travl.vertex] = True
                travl = travl.next

    # A function used by DFS
    def depth_first_searchUtil(self, v, visited):
        # Mark the current node as visited and print it
        visited[v] = True
        print(v, end=" ")

        # Recur for all the vertices adjacent to this vertex
        travl = self.graph[v]
        while travl.next:
            if visited[travl.vertex] is False:
                self.depth_first_searchUtil(travl.vertex, visited)
            travl = travl.next

    # The function to do DFS traversal. It uses recursive DFSUtil
    def depth_first_search(self, v):
        # Mark all the vertices as not visited
        visited = [False]*(len(self.graph))

        # Call the recursive helper function to print DFS traversal
        self.depth_first_searchUtil(v, visited)

    # Function to print the graph
    def printGraph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


# Driver program to the above graph class
if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)

    graph.printGraph()

    print("\nFollowing is Breadth First Traversal (starting from vertex 2)")
    graph.breadth_first_search(2)

    print("\nFollowing is Depth First Travers from (starting from vertex 2)")
    graph.depth_first_search(2)
