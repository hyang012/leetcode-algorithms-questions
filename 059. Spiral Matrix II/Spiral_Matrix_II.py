#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 59. Spiral Matrix II

Given a positive integer n, generate a square matrix filled with elements
from 1 to n^2 in spiral order
"""

def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    
    res = [[0] * n for _ in range(n)]
    i, j, di, dj = 0, 0, 0, 1
    for k in range(n**2):
        res[i][j] = k + 1
        if res[(i+di)%n][(j+dj)%n] != 0:
            di, dj = dj, -di
        i += di
        j += dj
    return res

print(generateMatrix(3))
        
        