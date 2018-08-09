#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations
of well-formed parentheses.
"""

def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    res = []
    generateParenthesisHelper(2*n, res, n, 0, 0, '')
    return res
    
def generateParenthesisHelper(n, res, count, open, close, prefix):
    if n == 0:
        print(prefix)
        res.append(prefix)
    else:
        if open < count:
            generateParenthesisHelper(n-1, res, count, open+1, close, prefix+'(')
        
        if close < open:
            generateParenthesisHelper(n-1, res, count, open, close+1, prefix+')')
        
    
generateParenthesis(3)
