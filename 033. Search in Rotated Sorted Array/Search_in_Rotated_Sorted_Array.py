#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some
pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return
its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
"""

def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    if nums is None or len(nums) == 0:
        return -1
    
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (right + left) // 2
        
        if nums[mid] == target:
            return mid
        
        if nums[left] <= nums[mid]:
            if nums[left] <= target and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        
    return -1        