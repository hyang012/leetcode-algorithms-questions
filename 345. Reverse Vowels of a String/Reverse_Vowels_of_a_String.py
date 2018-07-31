#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 345. Reverse Vowels of a String

Write a function that takes a string as input and reverse only the vowels of
a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
"""

def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    
    if not s or len(s) == 1:
        return s
    
    res = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if res[i] not in ['a', 'e', 'i', 'o', 'u']:
            i += 1
            continue
        if res[j] not in ['a', 'e', 'i' , 'o', 'u']:
            j -= 1
            continue
        
        res[i], res[j] = res[j], res[i]
        i += 1
        j -= 1
    
    return ''.join(res)

print(reverseVowels('hello'))
print(reverseVowels('leetcode'))    