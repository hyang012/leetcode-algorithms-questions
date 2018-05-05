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

    row = [1]
    
    if rowIndex < 0:
        return []
    elif rowIndex == 0:
        return row
    
    for i in range(1, rowIndex + 1):
        tmp1 = [0] + row
        tmp2 = row + [0]
        row = [sum(i) for i in zip(tmp1, tmp2)]
    
    return row
