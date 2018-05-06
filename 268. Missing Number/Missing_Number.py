#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 268. Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, 
find the one that is missing from the array.

Note:
Your algorithm should run in linear runtime complexity. Could you implement
it using only constant extra space complexity?

"""

def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return len(nums) * (len(nums) + 1) // 2 - sum(nums)
