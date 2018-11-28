#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 98. Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# O(n) space
def isValidBST(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
    
    res = []
    isValidBSTHelper(root, res)
    for i in range(1, len(res)):
        if res[i] <= res[i-1]:
            return False
    return True

def isValidBSTHelper(root, res):
    if root is None:
        return 
    
    isValidBSTHelper(root.left, res)
    res.append(root)
    isValidBSTHelper(root.right, res)

    
# O(1) space 
def isValidBST(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    return isValidBSTHelper(root, -float('inf'), float('inf'))

def isValidBSTHelper(node, lower_bound, upper_bound):
    if not node:
        return True
    
    if node.val >= upper_bound or node.val <= lower_bound:
        return False
    
    left = isValidBSTHelper(node.left, lower_bound, node.val)
    right = isValidBSTHelper(node.right, node.val, upper_bound)
    return left and right

    
            
        

