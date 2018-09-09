#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 73. Set Matrix Zerores

Given a m x n matrix, if an element is 0, set its entire row and column to 0.
Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

## O(m+n) space
#def setZeroes(matrix):
#    """
#    :type matrix: List[List[int]]
#    :rtype: void Do not return anything, modify matrix in-place instead.
#    """
#    row_zeros, col_zeros = set(), set()
#    
#    m, n = len(matrix), len(matrix[0])
#    for i in range(m):
#        for j in range(n):
#            if matrix[i][j] == 0:
#                row_zeros.add(i)
#                col_zeros.add(j)
#    
#    for i in row_zeros:
#        matrix[i] = [0] * n
#    
#    for j in col_zeros:
#        for i in range(m):
#            matrix[i][j] = 0
#
#    return matrix   


# O(1) space
def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """   
    col0, rows, cols = 1, len(matrix), len(matrix[0])
    
    for i in range(0, rows):
        if matrix[i][0] == 0:
            col0 = 0
    
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    for i in range(rows-1, -1, -1):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
        if col0 == 0:
            matrix[i][0] = 0
    
    return matrix
                

print(setZeroes([[1,1,1], [1,0,1], [1,1,1]]))
print(setZeroes([[0,1,2,0], [3,4,5,2], [1,3,1,5]]))
