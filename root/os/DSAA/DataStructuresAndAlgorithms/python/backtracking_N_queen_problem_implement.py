#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# backtracking_N_queen_problem_implement.py
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
# Created by Chyi Yaqing on 02/27/19 15:05.
# Copyright © 2019. Chyi Yaqing.
# All rights reserved.
#
# Distributed under terms of the
# MIT

"""
Backtracking is an algorithmic-technique for solving problems recursively by
trying to build a solution incrementally, one piece at a time, removing those
solutions that fail to satisfy the constraints of the problem at any point of
time.

Backtracking can be defined as a general algorithmic technique that considers
searching every possible combination in order to solve a computational problem

There are three types of problems in backtracking
    1) Decision Problem -- In this, we search for a feasible solution.
    2) Optimization Problem -- In this, we search for the best solution.
    3) Enumeration Problem -- In this, we find all feasible solution.

The N Queen is the problem of placing N chess queens on an NxN chessboard so
that no two queens attack each other. For example, following is a solution for
8 Queen problem.
    1) Naive Algorithm -- Generate all possible configurations of queens on
    board and print a configuration that satisfies the given constraints.

while there are untried configurations
{
    generate the next configuration
    if queens don't attack in this configuration then
    {
        print this configuration
    }
}

    2) Backtracking Algorithm -- The idea is to place queens one by one in
    different columns, starting from the left-most column. When we place a
    queen in a column, we check for clashes with already placed queens. in
    the current column, if we find a row for which there is no clash, we mark
    this row and column as part of the solution. If we do not find such a row
    due ro clashes then we backtrack and return false.

1. Start in the left most column
2. If all quees are placed
    return true
3. Try all rows in the current column. Do following for every tried row.
    a) If the queen can be placed safely in this row then mark this
    [row,column] as aprt of the solution and recursively check if placing queen
    here leads to a solution.
    b) If placing the queen in [row, column] leads to a solution then return
    true.
    c) If placing queen doesn't lead to a solution then unmark this
    [row, column] (Backtrack) and go to step (a) to try other rows.
4. If all rows have been tried and nothing worked, return false to trigger
    backtracking
"""
# Python program to solve N Queen Problem using backtracking
global N, solNum
N = 8
solNum = 0


def printSolution(board):
    global solNum, N
    solNum += 1
    print("{0}{1}{2}".format("* "*(N//2), solNum, " *"*(N//2)))
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


# A utility function to check if a queen can be placed on board[row][col].
# Note that this function is called when "col" queens are already placed in
# columns from 0 to col - 1. So we need to check only left side for attacking
# queens
def isSafe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solveNQUtil(board, col):
    # base case: If all queens are placed then return true
    if col >= N:
        printSolution(board)
        return True

    # Consider this column and try placing this queen in all rows one by one
    res = False
    for i in range(N):
        if isSafe(board, i, col):
            # Place this queen in board[i][col]
            board[i][col] = 1
          
            # Make result true if any placement is possible
            res = solveNQUtil(board, col+1) or res

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then queen from board[i][col]
            board[i][col] = 0

    # if the queen can not be placed in any row in this column col then return
    # false
    return res


# This function solves the N Queen problem using Backtracking. It mainly uses
# solveNQUtil() to solve the problem. It returns false if queens connot be
# placed, otherwise return true and placement of queens in the form of 1s.
# note that there may be more than one solutions, this function prints one of
# the feasible solutions.
def solveNQ():
    board = [[0]*N for _ in range(N)]
    
    if solveNQUtil(board, 0) is False:
        print("Solution does not exist")
        return False


# driver program to test above function
solveNQ()
