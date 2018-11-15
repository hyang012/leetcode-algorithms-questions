#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 112. Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def hasPathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: bool
    """
    if not root:
        return False
    else:
        if not root.left and not root.right:
            if sum == root.val:
                return True
            else:
                return False
        else:
            return hasPathSum(root.left, sum-root.val) or hasPathSum(root.right, sum-root.val)
        
t1 = TreeNode(1)
t1.left = TreeNode(2)

print(hasPathSum(t1, 1))