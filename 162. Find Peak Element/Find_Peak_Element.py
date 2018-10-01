#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 162. Find Peak Element

A peak element is an element that is greater than its neighbors

Given an input array nums, where nums[i] != nums[i+1], find a peak element
and return its index.

The array may contain multiple peaks, in that case return the index to any one
of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -Inf.

Note:
    You solution should be in logarithmic complexity.
"""

def findPeakElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    left, right = 0, len(nums)-1
    while left < right:
        mid = (right + left) // 2
        
        if 0 < mid and mid < len(nums) and nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
            return mid
        elif nums[mid] < nums[mid+1]:
            left = mid + 1
        else:
            right = mid - 1            

    return left

print(findPeakElement([1, 2, 3, 1]))
print(findPeakElement([1, 2, 1, 3, 5, 6, 4]))