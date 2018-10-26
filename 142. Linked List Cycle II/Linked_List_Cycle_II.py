#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 142. Linked List Cycyle II

Given a linked list, return the node where the cycle begins. If there is no
cycle return null.

Note: Do not modified the linked list

Follow up: Can you solve it without using extra space.
"""

def detectCycle(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    
    if not head or not head.next:
        return None
    
    slow = fast = start = head
    while fast and fast.next:
        fast = fast.next.next
        shlow = slow.next
        
        if slow == fast:
            while slow != start:
                start.next
                slow.next
    
            return start
    return null
    
    
