#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 95. Unique Binary Search Trees II

Given an integer n, generate all structurally unique BST's (binary search
trees) that store values 1 ... n.
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def generateTrees(n):
    """
    :type n: int
    :rtype: List[TreeNode]
    """
    
    if n == 0:
        return []
    
    return dfs(1, n+1)

def dfs(start, end):
    if start == end:
        return None
    
    res = []
    for cur_root in range(start, end):
        for left in dfs(start, cur_root) or [None]:
            for right in dfs(cur_root+1, end) or [None]:
                node = TreeNode(cur_root)
                node.left, node.right = left, right
                res.append(node)
    return res


        

