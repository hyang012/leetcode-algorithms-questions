#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 38. Count and Say

The count-and-say sequence is the sequence of integers with the first 
five terms as following:
    1. 1
    2. 11
    3. 21
    4. 1211
    5. 111221
1 is read off as "one 1" or 11
11 is read off as "two 1s" or 21
21 is read off as "one 2, then one 1" or 1211

Given an integer n, generate the nth term of the count-and-say sequence

Note: Each term of the sequence of integers will be represented as a string
"""

def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    term = '1'
    for _ in range(n-1):
        letter, tmp, count = term[0], '', 0
        for character in term:
            if letter == character:
                count += 1
            else:
                tmp = str(count) + letter
                letter = character
                count = 1
        tmp += str(count) + letter
        term = tmp
    return term

print(countAndSay(1))
print(countAndSay(4))
