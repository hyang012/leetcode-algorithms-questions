#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
    You may assume that duplicates do not exist in the tree.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
def buildTree(preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    if not inorder or not preorder:
        return None
    
    if inorder:
        ind = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[ind])
        root.left = buildTree(preorder, inorder[0:ind])
        root.right = buildTree(preorder, inorder[ind+1:])
        return root
    
