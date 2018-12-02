#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's
sum equals the given sum.

Note: A leaf is a node with no children.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
      
# Recursive
def pathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """
    if not root:
        return []

    res = []
    pathSumHelper(root, sum, res, [])
    return res
    
def pathSumHelper(node, sum, res, tmp_list):
    if node:
        if not node.left and not node.right and sum == node.val:
            res.append(tmp_list + [node.val])
        else:
            pathSumHelper(node.left, sum-node.val, res, tmp_list + [node.val])
            pathSumHelper(node.right, sum-node.val, res, tmp_list + [node.val])


# DFS
def pathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """
    if not root:
        return []
    
    res = []
    stack = [(root, sum-root.val, [root.val])]
    
    while stack:
        node, val, ls = stack.pop()
        if not node.left and not node.right and val == 0:
            res.append(ls)
        if node.right:
            stack.append((node.right, val-node.right.val, ls+[node.right.val]))
    
        if node.left:
            stack.append((node.left, val-node.left.val, ls+[node.left.val]))
    return res

import collections

# BFS
def pathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """
    if not root:
        return []
    
    res = []
    dq = collections.deque([(root, sum-root.val, [root.val])])
    while dq:
        node, val, ls = dq.popleft()
        if not node.left and not node.right and val == 0:
            res.append(ls)
        if node.right:
            dq.append((node.right, val-node.right.val, ls+[node.right.val]))
    
        if node.left:
            dq.append((node.left, val-node.left.val, ls+[node.left.val]))
    return res     
    
    
    
    
    
    
    
    
