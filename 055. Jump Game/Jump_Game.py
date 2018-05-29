#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 55. Jump Game

Given an array of non-negative integers, you are initially positioned
at the first index of the array.

Each element in the array represents your maximum jump length at that
position.

Determine if you are able to reach the last index.
"""

def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    memo = ['Unkown'] * (len(nums) - 1) + [True]
    return jumpHelper(nums, 0, memo)
    
def jumpHelper(nums, cur, memo):
    if memo[cur] != 'Unkown':
        return memo[cur]
    else:
        max_step = min(cur + nums[cur], len(nums) - 1)
        for i in range(max_step, cur, -1):
            if jumpHelper(nums, i, memo):
                memo[cur] = True
                return True
        memo[cur] = False
        return False
    
        
def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    memo = ['Unkown'] * (len(nums) - 1) + [True]
    
    for i in range(len(nums)-2, -1, -1):
        max_step = min(i + nums[i], len(nums) - 1)
        for j in range(max_step, i, -1):
            if memo[j] == True:
                memo[i] = True
                break
    
    return memo[0] == True



print(canJump([3, 2, 1, 0, 4]))
