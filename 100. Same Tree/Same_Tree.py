#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 100. Same Tree

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical
and the nodes have the same value.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursive
def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if not p and not q:
        return True
    elif p and q:
        return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    else:
        return False
 
    
# DFS with stack
def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    
    stack = [(p, q)]
    while stack:
        node_1, node_2 = stack.pop()
        
        if not node_1 and not node_2:
            continue
        elif node_1 and node_2:
            if node_1.val != node_2.val:
                return False
            stack.append((node_1.left, node_2.left))
            stack.append((node_1.right, node_2.right))
        else:
            return False
    return True

t1 = TreeNode(1)
t1.left = TreeNode(2)

t2 = TreeNode(1)
t2.right = TreeNode(2)

print(isSameTree(t1, t2))


t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(3)

t2 = TreeNode(1)
t2.left = TreeNode(2)
t2.right = TreeNode(3)


