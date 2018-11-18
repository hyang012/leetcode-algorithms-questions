#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 404. Sum of Left Leaves
Find the sum of all left leaves in a given binary tree.
"""
import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
# Recursive
def sumOfLeftLeaves(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    
    if root.left and not root.left.left and not root.left.right:
        return root.left.val + sumOfLeftLeaves(root.right)
    else:
        return sum(sumOfLeftLeaves(root.left)) + sum(sumOfLeftLeaves(root.right))
    
    
# DFS
def sumOfLeftLeaves(root):
    """
    :type root: TreeNode
    :rtype: int
    """

    stack = [root]
    res = 0
    
    while stack:
        node = stack.pop()
        if node:
            if node.left and not node.left.left and not node.left.right:
                res += node.left.val
            else:
                stack.append(node.left)
            stack.append(node.right)
    return res


# BFS
def sumOfLeftLeaves(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    queue = collections.deque(root)
    res = 0
    
    while queue:
        node = queue.popleft()
        if node:
            if node.left and not node.left.left and not node.left.right:
                res += node.left.val
            else:
                queue.append(node.left)
            queue.append(node.right)
    return res
