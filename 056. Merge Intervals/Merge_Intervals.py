#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.
"""

def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """

    if len(intervals) <= 1:
        return intervals
    
    res = []
    
    

   
