#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 287. Find the Duplicate Number

Given an array nums containing n + 1 integers where each integer is between 1
and n (inclusive), prove that at least one duplicate number must exist. Assume
that there is only one duplicate number, find the duplicate one.

Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n^2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""

# nlog(n)
def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    left, right = 0, len(nums)-1

    while left < right:
        mid = (right + left) // 2

        count = 0
        for k in nums:
            if mid < k <= right:
                count += 1
        if count > right - mid:
            left = mid + 1
        else:
            right = mid

    return left

print(findDuplicate([1, 3, 4, 2, 2]))
print(findDuplicate([3, 1, 3, 4, 2]))
    
