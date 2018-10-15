#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 206. Reverse Linked List

Reverse a singly linked list.

Follow up:

A linked list can be reversed either iteratively or recursively. Could you
implement both?
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


# Iteratively
def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    
    if not head or not head.next:
        return head
    
    prev = None
    while head:
        cur = head
        head = head.next
        cur.next = prev
        prev = cur
    return cur

# Recursively
def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    return reverseListHelper(head)

def reverseListHelper(node, prev=None):
    if not node:
        return prev
    
    n = node.next
    node.next = prev
    return reverseListHelper(n, node)
    
    
l = createLinkedList([1, 2, 3, 4, 5])
printLinkedList(reverseList(l))

    