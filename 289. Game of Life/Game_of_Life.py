#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 289. Game of Life

According to the Wikipedia's article: 'The Game of Life, also known simply as
Life, is a cellular automaton devised by the British mathematician 
John Horton Conway in 1970.'

Given a board with m by n cells, each cell has an initial state live(1) or
dead(0). Each cell interacts with its eight neighbors (horizontal, vertical,
diagonal) using the following four rules (taken from the above Wikipedia article):
    1. Any live cell with fewer than two live neighbors dies, as if caused by
       under-population
    2. Any live cell with two or three live neighbors lives on to the next generation.
    3. Any live cell with more than three live neighbors dies, as if by over-population.
    4. And dead cell with exactly three live neighbors becomes a live cell, as if by reporduction.
    
Write a function to compute the next state (after one update) of the board given
its current state. The next state is created by applying the above rules
simultaneously to every cell in the current state, where births and deaths occur simultaneously.
"""

def gameOfLife(board):
    """
    :type board: List[List[int]]
    :rtype: void Do not return anythin, modify board in-plae instead.
    """
    if not board or not board[0]:
        return
    
    m, n = len(board), len(board[0])
    for i in range(m):
        for j in range(n):
            update(board, m, n, i, j)
    for i in range(m):
        for j in range(n):
            board[i][j] >>= 1
    return board

def update(board, m, n, i, j):
    live = 0
    for p in range(max(i-1, 0), min(i+2, m)):
        for q in range(max(j-1, 0), min(j+2, n)):
            live += board[p][q] & 1
    if live == 3 or live == board[i][j] + 3:
        board[i][j] += 2

print(gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))