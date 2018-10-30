#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.

Note: A leaf is a node with no children.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

# Recursive
def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0    
    return max(1+maxDepth(root.left), 1+maxDepth(root.right))



t1 = TreeNode(3)
t1.left = TreeNode(9)
t1.right = TreeNode(20)
t1.right.left = TreeNode(15)
t1.right.right = TreeNode(7)

print(maxDepth(t1))
    

