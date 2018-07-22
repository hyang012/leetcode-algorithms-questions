#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 67. Add Binary

Given two binary strings, return their sum (also a binary string)

The input strings are both non-empty and contains only characters 1 or 0

"""

# Recursive
def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    if not a:
        return b
    elif not b:
        return a
    
    if a[-1] == '1' and b[-1] == '1':
        return addBinary(addBinary(a[0:-1], b[0:-1]), '1') + '0'
    elif a[-1] == '0' and b[-1] == '0':
        return addBinary(a[0:-1], b[0:-1]) + '0'
    else:
        return addBinary(a[0:-1], b[0:-1]) + '1'
    
    
def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    res = ''
    index = 0
    carry = '0'
    
    while index < max(len(a), len(b)) or carry == '1':
        num_a = a[-1-index] if index < len(a) else '0'
        num_b = b[-1-index] if index < len(b) else '0'
        
        val = int(num_a) + int(num_b) + int(carry)
        res = str(val % 2) + res
        
        carry = '1' if val > 1 else '0'
        index += 1
    
    return res
    

# Test cases
print(addBinary('11', '1'))
print(addBinary('1010', '1011'))
