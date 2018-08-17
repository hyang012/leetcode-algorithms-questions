#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 93. Restore IP Addresses

Given a string containing only digits, restore it by returning all possible
valid IP address combinations.
"""

def restoreIpAddresses(s):
    """
    :type s: str
    :rtype: List[str]
    """
    res = []
    restoreIpAddressesHelper(s, 0, '', res)
    return res
    
def restoreIpAddressesHelper(s, idx, path, res):
    if idx == 4:
        if s is '':
            res.append(path[:-1])
        return
    else:
        for i in range(1, 4):
            if i <= len(s):
                if i == 1:
                    restoreIpAddressesHelper(s[i:], idx+1, path+s[:i]+'.', res)
                elif i == 2 and s[0] != '0':
                    restoreIpAddressesHelper(s[i:], idx+1, path+s[:i]+'.', res)
                elif i == 3 and s[0] != '0' and int(s[:i]) <= 255:
                    restoreIpAddressesHelper(s[i:], idx+1, path+s[:i]+'.', res)


print(restoreIpAddresses('25525511135'))