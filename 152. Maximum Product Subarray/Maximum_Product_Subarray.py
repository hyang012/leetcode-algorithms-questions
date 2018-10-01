#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 152. Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.
"""

## DFS
#def maxProduct(nums):
#    """
#    :type nums: List[int]
#    :rtype: int
#    """
#    res = float('-inf')
#    for i in range(0, len(nums)):
#        res = max(res, dfs(nums, i, 1, res))
#    return res
#
#def dfs(nums, index, chosen, res):
#    res = max(res, nums[index]*chosen)    
#    if index < len(nums) - 1:
#        res = max(dfs(nums, index+1, nums[index]*chosen, res), res)
#    return res

# DP 
def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    small, large, res = nums[0], nums[0], nums[0]
    for i in range(1, len(nums)):
        large, small = max(nums[i], nums[i]*large, nums[i]*small), min(nums[i], nums[i]*large, nums[i]*small)
        res = max(res, large)
    return res
print(maxProduct([2, 3, -2, 4]))
print(maxProduct([-2, 0, -1]))
