#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 90. Subsets II

Given a collection of integers that might contain duplicates, nums,
return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
"""

## Iterative
#def subsetsWithDup(nums):
#    """
#    :type nums: List[int]
#    :rtype: List[List[int]]
#    """
#    
#    if not nums:
#        return []
#    
#    nums.sort()
#    res = [[]]
#    size = 0
#    cur = nums[0]
#    for num in nums:
#        if num == cur:
#            j = size
#        else:
#            j = 0
#            cur = num
#        tmp = []
#        size = len(res)
#        for i in range(j, len(res)):
#            tmp.append(res[i] + [num])
#        res += tmp
#    return res


# DFS
def subsetsWithDup(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    
    if not nums:
        return []
    
    res = []
    nums.sort()
    dfs(nums, 0, [], res)
    return res

def dfs(nums, index, path, res):
    res.append(path)
    for i in range(index, len(nums)):
        if i > index and nums[i] == nums[i-1]:
            continue
        dfs(nums, i+1, path+[nums[i]], res)

print(subsetsWithDup([1, 2, 2]))