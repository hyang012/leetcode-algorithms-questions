#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root
node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Iterative
def minDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    
    stack = [(root, 1)]
    res = float('Inf')
    while stack:
        node, level = stack.pop()
        
        if not node.left and not node.right:
            res = min(res, level)
        else:
            if node.right:
                stack.append((node.right, level+1))
            if node.left:
                stack.append((node.left, level+1))
    return res


# Recursive
def minDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    
    if not root.left and not root.right:
        return 1
    elif root.left and root.right:
        return min(1+minDepth(root.left), 1+minDepth(root.right))
    elif root.left:
        return 1+minDepth(root.left)
    else:
        return 1+minDepth(root.right)                      

t1 = TreeNode(3)
t1.left = TreeNode(9)
t1.right = TreeNode(20)
t1.right.left = TreeNode(15)
t1.right.right = TreeNode(7)

t1 = TreeNode(1)
t1.left = TreeNode(2)

print(minDepth(t1))
    
    