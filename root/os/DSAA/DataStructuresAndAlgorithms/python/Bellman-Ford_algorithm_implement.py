#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
Given a graph and a source vertex src in graph, find shortest paths from src to all vertices
in the given graph. The graph may contain negative weight edges.

Time complexity of Bellman-Ford is O(VE), which is more than Dijkstra.

Algorithm:
    Input: Graph and a source vertex src
    Output: Shortest distance to all vertices from src. If there is a negative weight cycle, then shortest distances are not calculated, negative weight cycle is reported.
    Step 1: initializes distances from source to all vertices as infinite and distance to source itself as 0. Create an array dist[] of size V with all values as infinite except dist[src] where src is source vertex.
    Step 2: calculates shortest distances.
"""
