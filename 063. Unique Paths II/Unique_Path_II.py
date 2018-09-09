#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 63. Unique Paths II

A robot is located at the top-left corner of a m*n grid.

The robot can only move either down or right at any point in time. The
robot is trying to reach the bottom-right corner of the grid.

Now consider if some obstacles are added to the grids. How many possible
unique paths would there be?

An obstacle empty sapce is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.
"""

# Backtracking
def uniquePathsWithObstacles(obstalceGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    if not obstalceGrid:
        return 0
    
    m, n = len(obstalceGrid), len(obstalceGrid[0])
    return uniquePathsWithObstaclesHelper(m-1, n-1, 0, 0, obstalceGrid)
    
def uniquePathsWithObstaclesHelper(m, n, i, j, obstaleGrid):
    if i > m or j > n or obstaleGrid[i][j] == 1:
        return 0
    
    if i == m and j == n:
        return 1
    
    return uniquePathsWithObstaclesHelper(m, n, i+1, j, obstaleGrid) + uniquePathsWithObstaclesHelper(m, n, i, j+1, obstaleGrid)


# Recursive with Memoization
def uniquePathsWithObstacles(obstalceGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    if not obstalceGrid:
        return 0
    
    m, n = len(obstalceGrid), len(obstalceGrid[0])
    memo = [[-1 for _ in range(n)] for _ in range(m)]
    return uniquePathsWithObstaclesHelper(m-1, n-1, 0, 0, obstalceGrid, memo)
    
def uniquePathsWithObstaclesHelper(m, n, i, j, obstaleGrid, memo):
    if i > m or j > n or obstaleGrid[i][j] == 1:
        return 0
    
    if i == m and j == n:
        return 1
    
    if memo[i][j] != -1:
        return memo[i][j]
    
    memo[i][j] = uniquePathsWithObstaclesHelper(m, n, i+1, j, obstaleGrid, memo) + uniquePathsWithObstaclesHelper(m, n, i, j+1, obstaleGrid, memo)
    return memo[i][j]


# DP
def uniquePathsWithObstacles(obstalceGrid):
    """
    :type obstacleGrid: List[List[int]]
    :rtype: int
    """
    if not obstalceGrid:
        return 0
    
    m, n = len(obstalceGrid), len(obstalceGrid[0])
    memo = [[-1 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if obstalceGrid[i][j] == 1:
                memo[i][j] = 0
                continue
            
            if i == 0 and j == 0:
                memo[i][j] = 1
            elif i > 0 and j == 0:
                memo[i][j] = memo[i-1][j]
            elif i == 0 and j > 0:
                memo[i][j] = memo[i][j-1]
            else:
                memo[i][j] = memo[i-1][j] + memo[i][j-1]
    return memo[-1][-1]
    
#print(uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(uniquePathsWithObstacles([[1, 0]]))