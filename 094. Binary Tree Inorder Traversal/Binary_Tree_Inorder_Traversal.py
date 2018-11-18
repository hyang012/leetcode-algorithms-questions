#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 94. Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.

Follow up:
    Recursive solution is trival, could you do it iteratively?
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
# Recursive
def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    res = []
    inorderTraversalHelper(root, res)
    return res

def inorderTraversalHelper(node, res):
    if not node:
        return
    inorderTraversalHelper(node.left, res)
    res.append(node.val)
    inorderTraversalHelper(node.right, res)


# Iterative
def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    stack = []
    res = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack:
            return res
        node = stack.pop()
        res.append(node.val)
        root = node.right
    
    
    
