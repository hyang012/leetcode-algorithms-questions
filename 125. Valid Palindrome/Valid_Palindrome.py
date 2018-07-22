#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only
alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid
palindrome.
"""

def isPalindrome(s):
    """
    :type s:str
    :rtype: bool
    """
    
    if not s or len(s) == 1:
        return True
    
    i, j = 0, len(s) - 1
    
    while i < j:
        if not s[i].isalnum():
            i += 1
            continue
        
        if not s[j].isalnum():
            j -= 1
            continue
        
        if s[i].lower() != s[j].lower():
            return False
        else:
            i +=1
            j -=1
    
    return True

print(isPalindrome('A man, a plan, a canal: Panama'))
print(isPalindrome('race a car'))
        
        