#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 235. Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two
given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor
is defined between two nodes p and q as the lowest node in T that has both p
and q as descendants (where we allow a node to be a descendant of itself).”

Note:
    All of the nodes' values will be unique.
    p and q are different and both values will exist in the BST.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursive
def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if not root or not p or not q:
        return None
    
    if max(p.val, q.val) < root.val:
        return lowestCommonAncestor(root.left, p, q)
    elif min(p.val, q.val) > root .val:
        return lowestCommonAncestor(root.right, p, q)
    else:
        return root
    
# Iterative
def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            if max(p.val, q.val) < node.val:
                stack.append(node.left)
            elif min(p.val, q.val) > node.val:
                stack.append(node.right)
            else:
                return node
    
    
