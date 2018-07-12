#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 14. Longest Common Prefix

Write a function to find the longest common prefix string amongst
an array of strings.

If there is no common prefix, return an empty string "".

Note:
All given inputs are in lowercase letters a-z.
"""

# Horizontal scanning
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    
    if strs is None or len(strs) == 0:
        return ''
    
    res = strs[0]
    
    for word in strs:
        while word.find(res) != 0:
            res = res[:-1]
            if res is '':
                return res
    return res

# Vertical scanning
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    
    if strs is None or len(strs) == 0:
        return ''
    
    res = ''
    for i in range(0, len(strs[0])):
        for word in strs:
            if i >= len(word) or strs[0][i] != word[i]:
                return res
        res += strs[0][i]
        
        
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    
    
print(longestCommonPrefix(["flower","flow","flight"]))
    
