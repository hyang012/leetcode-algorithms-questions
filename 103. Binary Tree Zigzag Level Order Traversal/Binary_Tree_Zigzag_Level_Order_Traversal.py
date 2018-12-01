#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes'
values. (ie, from left to right, then right to left for the next level and
alternate between).
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def zigzagLevelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return []
    
    res, level = [], [root]
    reverse = False  # Whether to go the opposite order
    
    while level:
        if reverse is False:
            res.append([node.val for node in level])
        else:
            tmp = []
            for node in level:
                tmp = [node.val] + tmp
            res.append(tmp)
            
        reverse = not reverse  # To change the order for next level
        tmp = []
        for node in level:
            tmp.extend([node.left, node.right])
        level = [child for child in tmp if child]
    return res
        
        
        