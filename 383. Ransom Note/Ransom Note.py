#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 383. Ransom Note

Given an arbitrary ransom note string and another string containing
letters from all the magazines, write a function that will return true
if the ransom note can be constructed from the magazines ; otherwise, it
will return false.

Each letter in the magazine string can only be used once in your ransom
note.

Note:
You may assume that both strings contain only lowercase letters.
"""

import collections

def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    
    if not ransomNote:
        return True
    elif len(ransomNote) > len(magazine):
        return False
    
    r, m = list(ransomNote), list(magazine)
    r.sort()
    m.sort()
    
    i, j = 0, 0
    while i < len(r) and j < len(m):
        if r[i] == m[j]:
            i += 1
            j += 1
        else:
            j += 1
    
    if i < len(r):
        return False
    else:
        return True

# Pythonic
def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    cr = collections.Counter(ransomNote)
    cm = collections.Counter(magazine)
    
    for letter in cr:
        if cr[letter] > cm[letter]:
            return False
    return True

print(canConstruct('a', 'b'))
print(canConstruct('aa', 'ab'))
print(canConstruct('aa', 'aab'))
