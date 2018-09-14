#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 74. Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous
row.
"""

def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    
    if not matrix or not matrix[0]:
        return False

    row = len(matrix)
    col = len(matrix[0])
    
    low = 0
    high = row * col - 1
        
    while low <= high:
        mid = (high + low) // 2
        
        if matrix[mid//col][mid%col]  == target:
            return True
        else:
            if target < matrix[mid//col][mid%col]:
                high = mid - 1
            else:
                low = mid + 1
    return False


print(searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 3))
                
print(searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 13)) 

print(searchMatrix([[1, 3]], 1))         