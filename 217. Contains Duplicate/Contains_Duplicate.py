#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 217. Contains Duplicate

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice 
in the array, and it should return false if every element is distinct.

"""

def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    dic = {}
    for num in nums:
        if num in dic:
            return True
        else:
            dic[num] = 0
    
    return False

