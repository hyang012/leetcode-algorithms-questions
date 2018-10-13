#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 160. Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked
lists begins.

Notes:
    If the two linked lists have no intersection at all, return null.
    The linked lists must retain their original structure after the function returns.
    You may assume there are no cycles anywhere in the entire linked structure.
    Your code should preferably run in O(n) time and use only O(1) memory.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    
    if not headA or not headB:
        return None
    
    cur_a, cur_b = headA, headB
    
    while cur_a is not cur_b:
        if cur_a is None:
            cur_a = headB
        else:
            cur_a = cur_a.next
            
        if cur_b is None:
            cur_b = headA
        else:
            cur_b = cur_b.next
        
    return cur_a


        
    
    
    