#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating
characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the
answer must be a substring, "pwke" is a subsequence and not a substring.
"""

# Slicing Window
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """

    if s is None:
        return 0
    elif len(s) == 1:
        return 1
        
    i, j, res = 0, 1, 1
    
    while j < len(s):
        if s[j] not in s[i:j]:
            j += 1
            res = max(res, len(s[i:j]))
        else:
            if i != j:
                i += 1
            else:
                j += 1
    
    return res

# Slicing Window Optimized
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """

    if s is None:
        return 0
    elif len(s) == 1:
        return 1
        
    i, j, res = 0, 0, 0
    look_up = {}
    
    while j < len(s):
        if look_up.get(s[j]) is not None:
            i = max(look_up[s[j]] + 1, i)            
        look_up[s[j]] = j
        res = max(res, j - i + 1)
        j += 1
            
    
    return res

print(lengthOfLongestSubstring('abcabcbb'))
print(lengthOfLongestSubstring('bbbbb'))
print(lengthOfLongestSubstring('pwwkew'))

            
    