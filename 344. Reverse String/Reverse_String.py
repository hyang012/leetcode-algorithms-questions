#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 344. Reverse String

Write a function that takes a string as input and returns the string reversed

"""

# Classic
def reverseString(s):
    """
    :type s: str
    :rtype: str
    """
    
    if not s or len(s) == 1:
        return s
    
    res = list(s)
    i, j = 0, len(s) - 1
    
    while i < j:
        res[i], res[j] = res[j], res[i]
        i += 1
        j -= 1
    return ''.join(res)

# Recurssive
def reverseString(s):
    """
    :type s: str
    :rtype: str
    """
    
    if not s or len(s) == 1:
        return s
    
    n = len(s)
    return reverseString(s[n//2:]) + reverseString(s[:n//2])

print(reverseString('hello'))
print(reverseString('     '))
