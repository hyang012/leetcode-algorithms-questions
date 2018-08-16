#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to
integer directly.
"""

def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    
    if num1 == '0' or num2 == '0':
        return '0'
    elif num1 == '1':
        return num2
    elif num2 == '1':
        return num1
    
    res = [0] * (len(num1) + len(num2))
    
    for i in range(len(num1)-1, -1, -1):
        for j in range(len(num2)-1, -1, -1):
            mul = int(num1[i]) * int(num2[j])
            p1, p2 = i + j, i + j + 1
            
            total = mul + res[p2]
            res[p1] += total // 10
            res[p2] = total % 10
    
    re = ''
    for i, val in enumerate(res):
        if len(re) == 0 and val == 0:
            continue
        
        re += str(val)
    
    return re


print(multiply('2', '3'))
print(multiply('123', '456'))

    
    
