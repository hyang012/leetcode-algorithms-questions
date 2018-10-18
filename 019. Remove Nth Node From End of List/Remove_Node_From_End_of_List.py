#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LeetCode 19. Remove Nth Node From End of List

Given a linked list, remove the n-th node from the end of list and return its head.

Note:
Given n will always be valid.

Follow up:
Could you do this in one pass?
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



# Two Pass
def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    if n == 0:
        return head
    
    length = 0
    cur = head
    while cur:
        length += 1
        cur = cur.next
        
    if length == n:
        return head.next
    
    cur = head
    for _ in range(1, length - n):
        cur = cur.next
    cur.next = cur.next.next
    return head


# One Pass
def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    dummy = ListNode(0)
    slow, fast = dummy, dummy
    dummy.next = head
    
    for _ in range(0, n+1):
        fast = fast.next
    
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next


l1 = createLinkedList([1, 2, 3, 4, 5])
printLinkedList(removeNthFromEnd(l1, 2))

