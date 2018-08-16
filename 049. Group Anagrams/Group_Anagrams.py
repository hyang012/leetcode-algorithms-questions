#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Leetcode 49. Group Anagrams

Given an array of strings, group anagrams together.

Note:
All inputs will be in lowercase.
The order of your output does not matter.
"""

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    if not strs:
        return []
    elif len(strs) == 1:
        return [strs]
    
    res = []
    look_up = {}
    
    for word in strs:
        key = ''.join(list(set(word)))
        if key not in look_up:
            look_up[key] = len(res)
            res.append([word])
        else:
            res[look_up[key]].append(word)
        
    return res

print(groupAnagrams(["cab","pug","pei","nay","ron","rae","ems","ida","mes"]))
