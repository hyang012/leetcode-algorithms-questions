#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 20. Valid Parentheses

Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

"""


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    
    if s is None:
        return True
    
    stack = []
    look_up = {')':'(', '}':'{', ']':'['}
    for character in s:
        if character in ['(', '{', '[']:
            stack.append(character)
        elif not stack or stack.pop() != look_up[character]:
            return False
    
    return True


# Test cases
print(isValid('()') == True)  
print(isValid('()[]{}') == True)
print(isValid('(]') == False)
print(isValid('{[]}') == True)




        
