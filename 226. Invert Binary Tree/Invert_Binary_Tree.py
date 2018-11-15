#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 226. Invert Binary Tree

Invert a binary tree.
"""
import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Recursive
def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root:
        return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root

# DFS
def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack.append(node.left)
            stack.append(node.right)
    return root

# BFS
def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    queue = collections.deque([(root)])
    while queue:
        node = queue.popleft()
        if node:
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)
    return root
    
    
