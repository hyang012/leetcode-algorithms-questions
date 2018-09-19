#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 80. Remove Duplicates from Sorted Array II

Given a sorted array nums, remove the duplicates in-place such that duplicates
appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification
to the input array will be known to the caller as well.
"""

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    if not nums or len(nums) <= 2:
        return len(nums)
    
    cur, point = 0, 0
    while point < len(nums):
        if point < len(nums)-2 and nums[point] == nums[point+1] and nums[point] == nums[point+2]:
            point += 1
        else:
            nums[cur] = nums[point]
            point += 1
            cur += 1
    return cur
    

print(removeDuplicates([1, 1, 1, 2, 2, 3]))
print(removeDuplicates([0,0,1,1,1,1,2,3,3]))
print(removeDuplicates([1,1,1,1]))

        


