#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 101. Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric
around its center).

Note: Bonus points if you could solve it both recursively and iteratively.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
        
# Iteration with stack
def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    
    if root is None:
        return True
    
    stack = [(root.left, root.right)]
    
    while len(stack) > 0:
        left, right = stack.pop()
        
        if not left and not right:
            continue
        elif not left or not right:
            return False
        elif left.val == right.val:
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        else:
            return False
    return True


# Recursive
def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    
    if root is None:
        return True
    
    return isSymmetricHelper(root.left, root.right)

def isSymmetricHelper(left, right):
    if not left and not right:
        return True
    elif not left or not right:
        return False
    else:
        return (left.val == right.val and 
                   isSymmetricHelper(left.left, right.right) and 
                   isSymmetricHelper(left.right, right.left))


t1 = TreeNode(1)
t1.left = TreeNode(2)
t1.right = TreeNode(2)
t1.left.left = TreeNode(3)
t1.left.right = TreeNode(4)
t1.right.left = TreeNode(4)
t1.right.right = TreeNode(3)

print(isSymmetric(t1))
    
    
    
    