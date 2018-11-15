#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 257. Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.
"""
import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursive
def binaryTreePaths(root):
    """
    :type root: TreeNode
    :rtype: List[str]
    """
    if not root:
        return []

    res = []
    self.binaryTreePathsHelper(root, res, str(root.val))
    return res

def binaryTreePathsHelper(self, node, res, path):
    if not node.left and not node.right:
        res.append(path)
    else:
        path += '->'
        if node.left:
            self.binaryTreePathsHelper(node.left, res, path+str(node.left.val))
        if node.right:
            self.binaryTreePathsHelper(node.right, res, path+str(node.right.val))


# DFS
def binaryTreePaths(root):
    """
    :type root: TreeNode
    :rtype: List[str]
    """
    if not root:
        return []
    
    res = []
    stack = [(root, '')]
    
    while stack:
        node, path = stack.pop()
        if not node.left and not node.right:
            res.append(path+str(node.val))
        else:
            path = path + str(node.val) + '->'
            if node.left:
                stack.append((node.left, path))
            if node.right:
                stack.append((node.right, path))
            
# BFS
def binaryTreePaths(root):
    """
    :type root: TreeNode
    :rtype: List[str]
    """
    if not root:
        return []
    
    res = []
    queue = collections.deque((root, ''))
    while queue:
        node, path = queue.popleft()
        if not node.left and not node.right:
            res.append(path+str(node.val))
        else:
            path = path + str(node.val) + '->'
            if node.left:
                queue.append((node.left, path))
            if node.right:
                queue.append((node.right, path))

    
            
            