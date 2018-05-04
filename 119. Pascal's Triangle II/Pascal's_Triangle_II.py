#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 119. Pascal's Triangle II

Given a non-negative index k where k ≤ 33, return the kth index row
of the Pascal's triangle.

Note that the row index starts from 0.

"""

def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """

    prev = [1]
    
    if rowIndex < 0:
        return []
    elif rowIndex == 0:
        return prev
    
    for i in range(1, rowIndex + 1):
        tmp1 = [0] + prev
        tmp2 = prev + [0]
        new_line = []
        for i in range(0, len(tmp1)):
            new_line.append(tmp1[i] + tmp2[i])
        
        prev = new_line
    
    return prev



    