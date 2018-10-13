#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 83. Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element
appear only once.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    
def printListNode(l):
    res = ''
    if l is None:
        return 'Input is None'
    
    while l.next is not None:
        res = res + str(l.val) + '->'
        l = l.next
    res += str(l.val)
    return res

def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or head.next is None:
        return head
    
    cur = head
    
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head

l = ListNode(1)
l.next = ListNode(1)
l.next.next = ListNode(2)

#l = ListNode(1)
#l.next = ListNode(1)
#l.next.next = ListNode(2)
#l.next.next.next = ListNode(3)
#l.next.next.next.next = ListNode(3)


printListNode(deleteDuplicates(l))