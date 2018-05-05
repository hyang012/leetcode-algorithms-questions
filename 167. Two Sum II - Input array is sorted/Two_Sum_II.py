#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 167. Two Sum II - Input array is sorted

Given an array of integers that is already sorted in ascending order, 
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that
they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you 
may not use the same element twice.

"""

def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    if numbers is None or len(numbers) == 0:
        return [-1, -1]
    
    left, right = 0, len(numbers) - 1
    
    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left + 1, right + 1]
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            right -= 1
    
    return [-1, -1]

twoSum([2, 7, 11, 15], 9)
