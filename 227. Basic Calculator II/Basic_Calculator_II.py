#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 227. Basic Calculator II

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, /
operators and empty spaces . The integer division should truncate toward
zero.

Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""

def calculate(s):
    """
    :type s: str
    :rtype: int
    """
    
    stack = []
    num = 0
    sign = '+'
    
    for i, char in enumerate(s):
        if ord('0') <= ord(char) <= ord('9'):
            num = num * 10 + int(char)
        if (char != ' ' and (ord(char) < ord('0') or ord(char) > ord('9'))) or i == len(s) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop()*num)
            else:
                stack.append(int(stack.pop()/num))
            sign = char
            num = 0
     
    return sum(stack)

print(calculate('3+2*2'))
print(calculate('3/2'))
print(calculate('3+5/2'))
print(calculate('14-3/2'))


