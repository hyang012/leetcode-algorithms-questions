#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the
following mapping:
    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26

Given a non-empty string containing only digits, determine the total number
of ways to decode it.
"""

# Recursive
def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    
    
    if s == '':
        return 1
    elif s[0] == '0':
        return 0
    else:
        if len(s) >= 2 and int(s[:2]) <= 26:
            return numDecodings(s[1:]) + numDecodings(s[2:])
        else:
            return numDecodings(s[1:])


# Recursive with Memoisation
def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    memo = {}
    res = numDecodingsHelper(s, memo)
    print(memo)
    return res
    
def numDecodingsHelper(s, memo):
    if memo.get(s) is not None:
        return memo[s]
    
    if s == '':
        return 1
    elif s[0] == 0:
        return 0
    else:
        if len(s) >= 2 and int(s[:2]) <= 26:
            tmp = numDecodingsHelper(s[1:], memo) + numDecodingsHelper(s[2:], memo)
            memo[s] = tmp
        else:
            tmp = numDecodingsHelper(s[1:], memo)
            memo[s] = tmp
        return tmp
    
    
# Bottom Up DP
def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    memo = {}
    for k in range(len(s)-1, -1, -1):
        if s[k:][0] == '0':
            memo[s[k:]] = 0
            continue
        
        if k == len(s) - 1:
            tmp = 1
        elif k == len(s) - 2 and int(s[k:]) <= 26:
            if s[k+1] != '0':
                tmp = 2
            else:
                tmp = 1
        else:
            if int(s[k:k+2]) <= 26:
                tmp = memo[s[k+1:]] + memo[s[k+2:]]
            else:
                tmp = memo[s[k+1:]]
        memo[s[k:]] = tmp
    return memo[s]



print(numDecodings('12'))
print(numDecodings('226'))
print(numDecodings('1020'))




