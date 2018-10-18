#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.
"""

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



def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    
    if not head:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    
    slow, fast = dummy, dummy.next
    
    while slow.next and fast.next:
        slow.next = slow.next.next
        fast.next = fast.next.next
        slow.next.next = fast
        
        slow = slow.next.next
        fast = slow.next
    return dummy.next

l1 = createLinkedList([1, 2, 3, 4])
printLinkedList(swapPairs(l1))