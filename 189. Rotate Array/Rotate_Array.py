#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 189. Rotate Array

Given an array, rotate the array to the right by k steps, where
k is non-negative.

Note:

Try to come up as many solutions as you can, there are at least 3
different ways to solve this problem.

Could you do it in-place with O(1) extra space?

"""

def rotate1(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    
    k %= len(nums)
    
    if k!= 0: 
        tmp = nums[-k:] + nums[:-k]
        for i in range(0, len(nums)):
            nums[i] = tmp[i]


def rotate2(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    
    k %= len(nums)
    
    i, start, cur, count = 0, 0, nums[0], 0
    
    while count < len(nums):
        i = (i + k) % len(nums)
        tmp = nums[i]
        nums[i] = cur
        
        if i == start:
            start += 1
            i = start
            cur = nums[i]
        else:
            cur = tmp
        
        count += 1            
        
    