#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 28. implement strStr()

Implement strStr()

Return the index of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack

Clarification:
What should we return when needle is an empty string?

For the purpose of this problem, we will return 0 when needle is an empty string.
"""


# Brute-Force approach
def strStr(haystack, needle):
    """
    :type hyastack: str
    :type needle: str
    :rtype: int
    """
    
    if not needle:
        return 0
    elif not haystack:
        return -1
    
    start = 0
    while start <= len(haystack) - len(needle):
        if haystack[start:(start+len(needle))] == needle:
            return start
        else:
            start += 1
    
    return -1


# KMP approach
def get_next(needle):
    next = [-1]
    length = len(needle)
    
    i, j = 0, -1
    while i < length - 1:
        if j == -1 or needle[i] == needle[j]:
            i += 1
            j += 1
            next.append(j)
        else:
            j = next[j]
    return next
    
def strStr(haystack, needle):
    """
    :type hyastack: str
    :type needle: str
    :rtype: int
    """
    
    if not needle:
        return 0
    elif not haystack:
        return -1
    
    i, j = 0, 0
    next = get_next(needle)
    while i < len(haystack):
        if j == -1 or needle[j] == haystack[i]:
            i += 1
            j += 1
            if j == len(needle):
                return i - j 
        else:
            j = next[j]
    
    return -1

        
# Test cases
print(strStr('hello', 'll'))
print(strStr('aaaa', 'bba'))
print(strStr('aaaa', ''))
