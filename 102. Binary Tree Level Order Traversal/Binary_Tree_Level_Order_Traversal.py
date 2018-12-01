#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).
"""

 Definition for a binary tree node.
 class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

import collections

# BFS
def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    res = []
    if not root:
        return res

    queue = collections.deque([(root, 1)])

    cur_lvl = 1
    cur_lvl_list = []

    while queue:
        node, node_level = queue.popleft()
        if  node_level != cur_lvl:
            res.append(cur_lvl_list)
            cur_lvl += 1  # Update number of current level in the Tree
            cur_lvl_list = []  # Reset current level list
        
        if node:
            cur_lvl_list.append(node.val)

            if node.left:
                queue.append((node.left, node_level + 1))

            if node.right:
                queue.append((node.right, node_level + 1))
    res.append(cur_lvl_list)
    return res
                

            
                
            
            
            

            
            
    

