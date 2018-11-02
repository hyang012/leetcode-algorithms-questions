#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 110. Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never
differ by more than 1.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Recursive
def isBalanced(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    return isBalancedHelper(root) != -1

def isBalancedHelper(root):
    if not root:
        return 0
    left = isBalancedHelper(root.left)
    right = isBalancedHelper(root.right)
    
    if left == -1 or right == -1 or abs(left - right) > 1:
        return -1
    return 1 + max(left, right)


# Iterative
def isBalanced(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    stack, node, last, depths = [], root, None, {}
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack[-1]
            if not node.right or last == node.right:
                node = stack.pop()
                left, right = depths.get(node.left, 0), depths.get(node.right, 0)
                if abs(left - right) > 1:
                    return False
                depths[node] = 1 + max(left, right)
                last = node
                node = None
            else:
                node = node.right
    return True

