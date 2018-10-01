#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 81. Search in Rotate Sorted Array II
Suppose an array sorted in ascending order is rotated at some pivot unknown
to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true,
otherwise return false.

Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums
may contain duplicates.
Would this affect the run-time complexity? How and why?
"""

def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: bool
    """
    
    if not nums or len(nums) == 0:
        return False
    
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2   
        
        if nums[mid] == target:
            return True
        
        while left < mid and nums[left] == nums[mid]:
            left += 1
        
        if nums[left] <= nums[mid]:
            if nums[mid] < target or target < nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if nums[mid] < target and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
            
    return False

print(search([2, 5, 6, 0, 0, 1, 2], 0))
print(search([2, 5, 6, 0, 0, 1, 2], 3))
print(search([1, 3, 1, 1, 1], 3))
print(search([3, 1], 1))
print(search([1, 3, 5], 1))

