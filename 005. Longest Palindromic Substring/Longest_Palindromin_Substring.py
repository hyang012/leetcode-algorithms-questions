#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 5. Longest Palindromin Substring

Given a string s, find the longest palindromic substring in s. You may
assume that the maximum length of s is 1000.

Example 1:

Input: "babad"

dabab

Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    
    if not s:
        return ''
    elif len(s) == 1:
        return s
    
    max_len = 1
    start = 0
    for i in range(1, len(s)):
        if i - max_len >= 1 and s[(i-max_len-1):(i+1)] == s[(i-max_len-1):(i+1)][::-1]:
            start = i - max_len - 1
            max_len += 2
            continue
        if i - max_len >= 0 and s[(i-max_len):(i+1)] == s[(i-max_len):(i+1)][::-1]:
            start = i - max_len
            max_len += 1
            continue
    
    return s[start:(start+max_len)]


print(longestPalindrome('cecbaa'))
print(longestPalindrome('cbbd'))

        
    
    
