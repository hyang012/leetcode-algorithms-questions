#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 71. Simplify Path

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:

Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together,
such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".

"""

def simplifyPath(path):
    """
    :type path: str
    :rtype: str`
    """
    
    if not path or len(path) == 1:
        return path
    
    res = []
    
    for folder in path.split('/'):
        if folder == '..' and len(res) > 0:
            res.pop(-1)
        elif folder not in ['', '.', '..']:
            res.append(folder)
    
    return '/' + '/'.join(res)
    
    
print(simplifyPath('/home/'))
print(simplifyPath('/a/./b/../../c/'))
print(simplifyPath('/../'))

