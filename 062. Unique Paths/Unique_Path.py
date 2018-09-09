#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 62. Unique Paths

A robot is located at the top-left corner of a m*n grid.

The robot can only move either down or right at any point in time. The
robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?

Note: m and n will be at most 100.
"""

# Recursive
def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    return uniquePathsHelper(m, n)

def uniquePathsHelper(i, j):
    if i == 1 and j == 1:
        return 1
    else:
        if i > 1 and j > 1:
            return uniquePathsHelper(i-1, j-1) + uniquePathsHelper(i, j-1)
        elif i == 1:
            return uniquePathsHelper(i, j-1)
        else:
            return uniquePathsHelper(i-1, j)


# Recursive with Memoization
def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    memo = [[-1 for _ in range(n)] for _ in range(m)]
    return uniquePathsHelper(m-1, n-1, 0, 0, memo)

def uniquePathsHelper(m, n, i, j, memo):
    if memo[i][j] != -1:
        return memo[i][j]
    
    if i == m and j == n:
        tmp = 1
    else:
        if i < m and j < n:
            tmp = uniquePathsHelper(m, n, i+1, j, memo) + uniquePathsHelper(m, n, i, j+1, memo)
        elif i == m:
            tmp = uniquePathsHelper(m, n, i, j+1, memo)
        else:
            tmp = uniquePathsHelper(m, n, i+1, j, memo)
    memo[i][j] = tmp
    return tmp


# DP
def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    memo = [[1 for _ in range(n)] for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            memo[i][j] = memo[i][j-1] + memo[i-1][j]
    return memo[-1][-1]
            

print(uniquePaths(3,7))
print(uniquePaths(23,12))
