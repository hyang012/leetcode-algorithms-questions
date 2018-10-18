#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 61. Rotate List

Given a linked list, rotate the list to the right by k places, where k is
non-negative.
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


def rotateRight(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if not head or not head.next:
        return head
    
    n = 0
    cur = head
    while cur:
        n += 1
        cur = cur.next
    
    k = k % n
    slow, fast = head, head
    for _ in range(k):
        fast = fast.next
    
    while fast.next:
        slow = slow.next
        fast = fast.next
    
    fast.next = head
    head = slow.next
    slow.next = None
    return head

l1 = createLinkedList([1, 2 ,3 ,4 ,5])
l2 = createLinkedList([0, 1, 2])

printLinkedList(rotateRight(l1, 2))
printLinkedList(rotateRight(l2, 4))
