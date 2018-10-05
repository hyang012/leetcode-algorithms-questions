#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 216. Combination Sum III

Find all possible combinations of k numbers that add up to a number n, given
that only numbers from 1 to 9 can be used and each combination should be a
unique set of numbers.

Note:
    All numbers will be postivie integers
    The solution set must not contain duplicate combinations.
    
"""

def combinationsSum3(k, n):
    """
    :type k: int
    :type n: int
    :rtype List[List[int]]
    """
    res = []   
    
    helper(list(range(1, 10)), k, n, 0, [], res)
    return res
    
def helper(nums, k, n, index, path, res):
    if k == 0 and n == 0:
        res.append(path)
    elif k < 0 or n < 0:
        return
    for i in range(index, len(nums)):
        helper(nums, k-1, n-nums[i], i+1, path+[nums[i]], res)
    
print(combinationsSum3(3, 7))
