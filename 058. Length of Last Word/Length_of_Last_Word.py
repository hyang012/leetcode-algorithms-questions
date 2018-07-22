#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 58. Length of Last Word

Given a string s consisits of upper/lower-case alphabets and empty space 
characters ' ', return the length of last word in the string. If the last
word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space
characters only
"""

def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    
    if s is None:
        return 0
    
    count = 0
    for i in range(len(s)-1, -1, -1):
        if s[i] == ' ' and count == 0:
            continue
        elif s[i] == ' ' and count != 0:
            return count
        else:
            count += 1
    return count
        


print(lengthOfLastWord('Hellow World'))  # ==> 5
print(lengthOfLastWord('  World'))  # ==> 5
print(lengthOfLastWord('Hellow  '))  # ==> 6
print(lengthOfLastWord('   ')) # ==> 0