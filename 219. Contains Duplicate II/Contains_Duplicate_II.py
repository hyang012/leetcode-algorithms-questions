#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 219. Contains Duplicate II

Given an array of integers and an integer k, find out whether there are 
two distinct indices i and j in the array such that nums[i] = nums[j] and
 the absolute difference between i and j is at most k.
"""

def containsNearbyDuplicate(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    
    if nums is None or len(nums) <= 1 or k == 0:
        return False
    
    dic = {}
    
    for i, num in enumerate(nums):
        if num in dic and i - dic[num] <= k:
            return True
        dic[num] = i
    return False

print(containsNearbyDuplicate([1,0,1,1], 1))

    
    
    
    

    

