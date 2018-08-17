#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 151. Reverse Words in a String

Given an input string, reverse the string word by word.

Note:

A word is defined as a sequence of non-space characters.

Input string may contain leading or trailing spaces. However, your reversed
string should not contain leading or trailing spaces.

You need to reduce multiple spaces between two words to a single space in the
reversed string.
"""

def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    
    res = []
    cur_word = ''
    
    for char in s:
        if char == ' ':
            if cur_word:
                res = [cur_word] + res
                cur_word = ''
            continue        
        else:
            cur_word += char
    
    if cur_word:
        res = [cur_word] + res
    
    return ' '.join(res)

print(reverseWords('the sky is blue'))
print(reverseWords('     '))
print(reverseWords('t'))



