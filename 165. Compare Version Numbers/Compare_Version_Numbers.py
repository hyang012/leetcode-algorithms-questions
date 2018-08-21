#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 165. Compare Version Numbers

Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1; otherwise
return 0.

You may assume that the version strings are non-empty and contain only digits
and the '.' character.
The . character does not represent a decimal point and is used to separate
number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it
is the fifth second-level revision of the second first-level revision.
"""

def compareVersion(version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    version1 = version1.split('.')
    version2 = version2.split('.')
    
    for i in range(max(len(version1), len(version2))):
        if i < len(version1) and i < len(version2):
            if int(version1[i]) < int(version2[i]):
                return -1
            elif int(version1[i]) > int(version2[i]):
                return 1
        elif i >= len(version1):
            if 0 != int(version2[i]):
                return -1
        else:
            if 0 != int(version1[i]):
                return 1
    
    return 0
    
        
print(compareVersion('0.1', '1.1'))
print(compareVersion('1.0.1', '1'))
print(compareVersion('0.1', '1.1'))
print(compareVersion('01', '1'))
print(compareVersion('1.0.0', '1'))
