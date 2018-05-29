#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 54. Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all
elements of the matrix in spiral order.

"""

def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    
    if matrix is None or len(matrix) == 0:
        return []
    
    R, C = len(matrix), len(matrix[0])
    seen = [[False] * C for _ in matrix]
    res = []
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r = c = di = 0
    
    for _ in range(R * C):
        res.append(matrix[r][c])
        seen[r][c] = True
        cr, cc = r + dr[di], c + dc[di]
        
        if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
            r, c = cr, cc
        else:
            di = (di + 1) % 4
            r, c = r + dr[di], c + dc[di]
    return res