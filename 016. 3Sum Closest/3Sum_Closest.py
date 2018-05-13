#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 16. 3Sum Closest

Given an array nums of n integers and an integer target, find three
integers in nums such that the sum is closest to target. Return the
sum of the three integers. You may assume that each input would have
exactly one solution.
"""

def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) <= 3:
        return sum(nums)
    
    nums.sort()
    res = nums[0] + nums[1] + nums[2]
    for i in range(0, len(nums) - 2):
        low, high = i + 1, len(nums) - 1
        while low < high:
            cur_sum = nums[i] + nums[low] + nums[high]
            
            if cur_sum == target:
                return cur_sum
            
            if abs(target - cur_sum) < abs(target - res):
                res = cur_sum
            
            if cur_sum < target:
                low += 1
            else:
                high -= 1
    
    return res    
        

