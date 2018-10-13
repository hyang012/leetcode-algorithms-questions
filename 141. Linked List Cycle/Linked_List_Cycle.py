#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def printLinkedList(l):
    res = ''
    if l is None:
        return 'Input is None'
    
    while l.next is not None:
        res = res + str(l.val) + '->'
        l = l.next
    res += str(l.val)
    return res

def createLinkedList(nums):
    res = cur = ListNode(nums[0])
    for num in nums[1:]:
        cur.next = ListNode(num)
        cur = cur.next
    return res
        

def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    
    if not head:
        return False
    
    slow = fast = head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


