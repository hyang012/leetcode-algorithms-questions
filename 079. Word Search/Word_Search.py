#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same
letter cell may not be used more than once.
"""

def exist(board, word):
    """
    :type board: list[List[str]]
    :type word: str
    :rtype:bool
    """
    if not board:
        return False
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, i, j, word):
                return True
    return False
    
def dfs(board, i, j, word):
    if len(word) == 0:
        return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
        return False
    tmp = board[i][j]
    board[i][j] = '#'
    res = dfs(board, i+1, j, word[1:]) or dfs(board, i, j+1, word[1:]) \
        or dfs(board, i-1, j, word[1:]) or dfs(board, i, j-1, word[1:])
    board[i][j] = tmp
    return res


board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
print(exist(board, 'ABCCED'))
print(exist(board, 'SEE'))
print(exist(board, 'ABCB'))



