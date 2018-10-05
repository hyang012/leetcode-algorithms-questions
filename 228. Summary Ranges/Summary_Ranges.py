#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 228. Summary Ranges

Given a sorted integer array without duplicates, return the summary of its
ranges.
"""

def summaryRanges(nums):
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    if not nums:
        return []
    elif len(nums) == 1:
        return [str(nums[0])]
    
    res = []
    cur, next = 0, 1
    
    while cur < len(nums):
        if next == len(nums):
            if cur < len(nums) - 1:
                # x -> y at the end
                res.append(str(nums[cur]) + '->' + str(nums[-1]))
            else:
                # x by itself at the end
                res.append(str(nums[cur]))
            cur = next
                
        elif nums[next-1] + 1 != nums[next]:
            if cur + 1 != next:
                res.append(str(nums[cur]) + '->' + str(nums[next-1]))
            else:
                res.append(str(nums[cur]))
            cur = next
        next += 1
    return res
      
print(summaryRanges([0, 1, 2, 4, 5, 7]))
print(summaryRanges([0, 2, 3, 4, 6, 8, 9]))