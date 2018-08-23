#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 56. Merge Intervals

Given a collection of intervals, merge all overlapping intervals.
"""

# sort
def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    
    if not intervals or len(intervals) == 1:
        return intervals
    
    intervals.sort(key=lambda x: x[0])
    
    res = []
    for interval in intervals:
        if not res or interval[0] > res[-1][1]:
            res.append(interval)
        else:
            res[-1][1] = max(interval[1], res[-1][1])
    return res

print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(merge([[1, 4], [4, 5]]))
print(merge([[1, 6], [2, 3]]))


