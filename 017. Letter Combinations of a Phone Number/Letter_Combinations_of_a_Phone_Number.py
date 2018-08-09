#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible
letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given
below. Note that 1 does not map to any letters.

Note:

Although the above answer is in lexicographical order, your answer could be
in any order you want.
"""

def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    phone_pad = {'1': [],
                 '2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'i'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
    
    if not digits or len(digits) == 0:
        return []
    elif len(digits) == 1:
        return phone_pad[digits]
    
    prev = letterCombinations(digits[:-1])
    additional = phone_pad[digits[-1]]
    
    return [p + a for p in prev for a in additional]


# Backtracking
def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    
    phone_pad = {'1': [],
                 '2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'i'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
    res = []
    def letterCombinationsHelper(phone_pad, digits, idx, path, res):
        if idx == len(digits):
            res.append(path)
            return
        for i in phone_pad[digits[idx]]:
            letterCombinationsHelper(phone_pad, digits, idx+1, path+i, res)
    
    letterCombinationsHelper(phone_pad, digits, 0, '', res)
    return res
print(letterCombinations('23'))

    





    
    
    
