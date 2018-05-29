#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 48. Rotate Image
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to
modify the input 2D matrix directly. DO NOT allocate another 2D
matrix and do the rotation.

"""

def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    if matrix is None or len(matrix) == 0:
        return
    
    for i in range(0, len(matrix)):
        for j in range(i, len(matrix[0])):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])//2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][-(j+1)]
            matrix[i][-(j+1)] = temp