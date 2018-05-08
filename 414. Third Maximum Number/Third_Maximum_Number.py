#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 414. Third Maximum Number

Given a non-empty array of integers, return the third maximum number
in this array. If it does not exist, return the maximum number. The time
complexity must be in O(n).

"""

def thirdMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    max_three = [float('-inf'), float('-inf'), float('-inf')]
    
    for num in nums:
        if num not in max_three:
            if num > max_three[0]:
                max_three = [num] + max_three[0:2]
            elif num > max_three[1]:
                max_three = [max_three[0], num, max_three[1]]
            elif num > max_three[2]:
                max_three = max_three[0:2] + [num]
    
    if float('-inf') not in max_three:
        return max_three[2]
    else:
        return max(max_three)
        
        