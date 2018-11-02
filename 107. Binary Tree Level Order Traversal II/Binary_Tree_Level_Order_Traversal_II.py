#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 107. Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its
nodes' values. (ie, from left to right, level by level from leaf to root).
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# DFS recursively
def levelOrderBottom(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    res = []
    dfs(root, 0, res)
    return res
    
def dfs(root, level, res):
    if root:
        if len(res) < level + 1:
            res.insert(0, [])
        res[-(level+1)].append(root.val)
        dfs(root.left, level+1, res)
        dfs(root.right, level+1, res)
        

# DFS with stack
def levelOrderBottom(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """ 
    stack = [(root, 0)]
    res = []
    while stack:
        node, level = stack.pop()
        if node:
            if len(res) < level + 1:
                res.insert(0, [])
            res[-(level+1)].append(node.val)
            stack.append((node.right, level+1))
            stack.append((node.left, level+1))
    return res


# bfs + queue:
def levelOrderBottom(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """ 
    queue = [(root, 0)]
    res = []
    while queue:
        node, level = queue.pop(0)
        if node:
            if len(res) < level+1:
                res.insert(0, [])
            res[-(level+1)].append(node.val)
            queue.append((node.left, level+1))
            queue.append((node.right, level+1))
    return res

    


t1 = TreeNode(3)
t1.left = TreeNode(9)
t1.right = TreeNode(20)
t1.right.left = TreeNode(15)
t1.right.right = TreeNode(7)

print(levelOrderBottom(t1))


    