#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 387. First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's
index. If it doesn't exist, return -1

"""

def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """
    
    if not s:
        return -1
    elif len(s) == 1:
        return 0
    
    freq = {}
    for char in s:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    
    for i, char in enumerate(s):
        if freq[char] == 1:
            return i
    
    return -1

print(firstUniqChar('leetcode'))
print(firstUniqChar('loveleetcode'))
print(firstUniqChar('aaaddc'))

