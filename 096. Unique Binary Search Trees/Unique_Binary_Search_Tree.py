#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 95. Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store
values 1 ... n?
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def numTrees(n):
    """
    :type n: int
    :rtype: int
    """
    # root -> 1: left: 0, right: 2, f(0) * f(2)
    # root -> 2: left: 1, right: 1, f(1) * f(1)
    # root -> 3: left: 2, right: 0, f(2) * f(0)
    
    res = [0] * (n+1)
    res[0] = 1
    for i in range(1, n+1):
        for j in range(i):
            res[i] += res[j] + res[i-j-1]
    return res[n]