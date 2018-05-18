#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 39. Combination Sum

Given a set of candidate numbers (candidates) (without duplicates)
and a target number (target), find all unique combinations in candidates
where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number
of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

"""


def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    res = []
    if candidates is None or len(candidates) == 0:
        return res
    helper(res, [], candidates, target, 0)
    return res

def helper(res, path, candidates, target, start):
    if target < 0:
        return
    if target == 0:
        if path not in res:
            res.append(path)
        return 
    for i in range(start, len(candidates)):
        helper(res, path+[candidates[i]], candidates, target - candidates[i], i)