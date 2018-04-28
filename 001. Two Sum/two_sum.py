"""
Leetcode 1. Two Sum

Given an array of integers, return indices of the two numbers such that 
they add up to a specific target.

You may assume that each input would have exactly one solution, and you 
may not use the same element twice.


Time Complexity: O(n)
Space Complexity: O(n)
"""

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    dic = {}
    
    for i, num in enumerate(nums):
        if num not in dic:
            dic[target - num] = i
        else:
            return [dic[num], i]

