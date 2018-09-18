#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 78. Subsets

Given a set of distinct integers, nums, return all possible subsets
(the power set).

Note: The solution set must not contain duplicate subsets.
"""

## Backtracking
#def subsets(nums):
#    """
#    :type nums: List[int]
#    :rtype: List[List[int]]
#    """
#    if not nums:
#        return []
#    elif len(nums) == 1:
#        return [[], nums]
#    
#    chosen = []
#    res = []
#    subsetsHelper(nums, chosen, res)
#    return res
#
#def subsetsHelper(nums, chosen, res):
#    if len(nums) == 0:
#        res.append(chosen.copy())
#    else:
#        first = nums.pop(0)
#        chosen.append(first)
#        subsetsHelper(nums, chosen, res)
#
#        chosen.remove(first)
#        subsetsHelper(nums, chosen, res)    
#        nums.insert(0, first)    
        

# DP
def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
        return []
    
    res = [[]]
    for num in nums:
        tmp = res.copy()
        for item in tmp:
            res.append(item + [num])
    return res    
    res = []
    
print(subsets([1,2,3]))                     
    


