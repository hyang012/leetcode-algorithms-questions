#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 229. Majority Element II

Given an integer array of size n, find all elements that appear more than
⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.
"""

def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    candidate_1, candidate_2, count_1, count_2 = nums[0], nums[0], 0, 0
    
    if not nums or len(nums) == 1:
        return nums
    
    for num in nums:
        # if is candidate, count ++
        if num == candidate_1:
            count_1 +=1
            continue
        
        if num == candidate_2:
            count_2 += 1
            continue
        
        # if not candidate, if candidate has count == 0 set the num to be new candidate
        if num != candidate_1 and num != candidate_2:
            if count_1 == 0:
                candidate_1 = num
                count_1 += 1
                continue
            
            if count_2 == 0:
                candidate_2 = num
                count_2 += 1
                continue
        
        # if not candidate and all counts != 0, subtract all
        count_1 -= 1
        count_2 -= 1
    
    count_1, count_2 = 0, 0
    for num in nums:
        if num == candidate_1:
            count_1 += 1
        elif num == candidate_2:
            count_2 += 1
    
    res = []
    if count_1 > len(nums) // 3:
        res.append(candidate_1)
    if count_2 > len(nums) //3:
        res.append(candidate_2)
    return res

print(majorityElement([3, 2, 3]))
print(majorityElement([1, 1, 1, 3, 3, 2, 2, 2]))

    
    
