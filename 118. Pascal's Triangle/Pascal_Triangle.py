#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 118. Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of 
Pascal's triangle.

"""

def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    
    res = [[1]]
    
    if numRows <= 0:
        return []
    elif numRows == 1:
        return res
    
    for i in range(1, numRows):
        tmp1 = [0] + res[i - 1]
        tmp2 = res[i - 1] + [0]
        new_line = []
        for i in range(0, len(tmp1)):
            new_line.append(tmp1[i] + tmp2[i])
        
        res.append(new_line)
    
    return res




    