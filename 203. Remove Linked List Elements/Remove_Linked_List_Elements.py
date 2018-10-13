#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 203. Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.
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


def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    if not head:
        return head
    
    cur = head
    
    while cur and cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
            continue
        cur = cur.next
    
    # Remove head if head.val == val
    if head.val == val:
        head = head.next
    
    return head



l1 = createLinkedList([1, 2, 6, 3, 4, 5, 6])
l2 = createLinkedList([6, 6, 6])

printLinkedList(removeElements(l1, 6))
printLinkedList(removeElements(l2, 6))


