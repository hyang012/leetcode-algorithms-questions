#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 169. Majority Element

Given an array of size n, find the majority element. The majority
element is the element that appears more than [n/2] times.

You may assume that the array is non-empty and the majority element
always exist in the array.


"""

def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    dic = {}
    
    for num in nums:
        if num not in dic:
            dic[num] = 1
        else:
            dic[num] += 1
            if dic[num] > len(nums) / 2:
                return num
