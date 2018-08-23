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

## Recursive
#def uniquePaths(m, n):
#    """
#    :type m: int
#    :type n: int
#    :rtype: int
#    """
#    return uniquePathsHelper(m, n)
#
#def uniquePathsHelper(i, j):
#    if i == 1 and j == 1:
#        return 1
#    else:
#        if i > 1 and j > 1:
#            return uniquePathsHelper(i-1, j) + uniquePathsHelper(i, j-1)
#        elif i == 1:
#            return uniquePathsHelper(i, j-1)
#        else:
#            return uniquePathsHelper(i-1, j)


# Recursive with Memoization
def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    memo = {}
    return uniquePathsHelper(1, 1, m, n, memo)

def uniquePathsHelper(i, j, m, n, memo):
    key = str(i) + str(j)
    if memo.get(key) is not None:
        return memo.get(key)
    
    if i == m and j == n:
        return 1
    else:
        if i < m and j < n:
            tmp = uniquePathsHelper(i+1, j, m, n, memo) + uniquePathsHelper(i, j+1, m, n, memo)
        elif i == m:
            tmp = uniquePathsHelper(i, j+1, m, n, memo)
        else:
            tmp = uniquePathsHelper(i+1, j, m, n, memo)
        memo[key] = tmp
        return tmp

print(uniquePaths(4,7))
print(uniquePaths(23,12))