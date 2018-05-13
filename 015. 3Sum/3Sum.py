#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 15. 3Sum

Given an array nums of n integers, are there elements a, b, c
in nums such that a + b + c = 0? Find all unique triplets in 
the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.
"""

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    
    if nums is None or len(nums) <= 2:
        return []
    elif len(nums) == 3:
        return [] if sum(nums) != 0 else nums
    
    res = []
    nums.sort()
    for i in range(0, len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        low, high, target = i + 1, len(nums) - 1, 0 - nums[i]
        while low < high:
            if nums[low] + nums[high] == target:
                res.append([nums[i], nums[low], nums[high]])
                while low < high and nums[low] == nums[low + 1]:
                    low += 1
                while low < high and nums[high] == nums[high - 1]:
                    high -= 1
                low += 1
                high -= 1
            elif nums[low] + nums[high] < target:
                low += 1
            else:
                high -= 1
    
    return res                
                                
         
        
