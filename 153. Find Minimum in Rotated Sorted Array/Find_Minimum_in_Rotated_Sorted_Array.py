#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 153. Find Minimum in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown
to you beforehand.

Find the minimum element.

You may assume no duplicate exists in the array.
"""

def findMin(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    if not nums:
        return []
    
    left, right = 0, len(nums)-1
    
    while left < right:
        mid = (right + left) // 2
        
        if nums[left] <= nums[mid] and nums[mid] < nums[right]:
            return nums[left]
        elif nums[left] > nums[mid]:
            right = mid 
        else:
            left = mid + 1
    return nums[left]

print(findMin([3, 4, 5, 1, 2]))
print(findMin([4, 5, 6, 7, 0, 1, 2]))