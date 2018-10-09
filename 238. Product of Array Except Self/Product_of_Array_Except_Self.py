#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 238. Product of Array Except Self

Given an array nums of n integers where n > 1,  return an array output such
that output[i] is equal to the product of all the elements of nums except
nums[i].

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not
count as extra space for the purpose of space complexity analysis.)
"""

def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    p = 1
    output = []
    
    for i in range(len(nums)):
        output.append(p)
        p = p * nums[i]
    
    p = 1
    for i in range(len(nums)-1, -1, -1):
        output[i] *= p
        p = p * nums[i]
        
    return output

print(productExceptSelf([1, 2, 3, 4]))