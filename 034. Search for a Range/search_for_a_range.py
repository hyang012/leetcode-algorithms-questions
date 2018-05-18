#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 34. Search for a Range

Given an array of integers nums sorted in ascending order, find
the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

"""

def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    if nums is None or len(nums) == 0:
        return [-1, -1]
        
    left = find_index(nums, target, True)
    if nums[left] != target:
        return [-1, -1]
    
    right = find_index(nums, target, False)
    if nums[right] != target:
        return [left, find_index(nums, target, False) - 1]
    else:
        return [left, right]
        
def find_index(nums, target, find_left):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (right + left) // 2
        
        if left == right:
            return mid
        else:        
            if target < nums[mid] or (find_left and target == nums[mid]):
                right = mid
            else:
                left = mid + 1
            
        
