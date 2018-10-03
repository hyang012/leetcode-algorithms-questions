#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given an array of n positive integers and a positive integer s, find the
minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
one, return 0 instead.

Follow up:
If you have figured out the O(n) solution, try coding another solution of
which the time complexity is O(n log n). 
"""

# O(n)
def minSubArrayLen(s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    total, left, res = 0, 0, len(nums)+1
    for right, num in enumerate(nums):
        total += num
        while total >= s:
            res = min(res, right-left+1)
            total -= nums[left]
            left += 1
    
    return res if res <= len(nums) else 0

# O(nlogn)
def minSubArrayLen(s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    
    result = len(nums) + 1
    for idx, n in enumerate(nums[1:], 1):
        nums[idx] = nums[idx - 1] + n
    left = 0
    for right, n in enumerate(nums):
        if n >= s:
            left = find_left(left, right, nums, s, n)
            result = min(result, right - left + 1)
    return result if result <= len(nums) else 0

def find_left(left, right, nums, s, n):
    while left < right:
        mid = (left + right) // 2
        if n - nums[mid] >= s:
            left = mid + 1
        else:
            right = mid
    return left
print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(minSubArrayLen(15, [1, 2, 3, 4, 5]))
