#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 147. Insertion Sort List

Sort a linked list using insertion sort.
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


def insertionSortList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next:
        return head
    
    cur = dummy = ListNode(0)
    while head:
        if cur and cur.val > head.val:
            cur = dummy
        while cur.next and cur.next.val < head.val:
            cur = cur.next
        cur.next ,cur.next.next, head = head, cur.next, head.next
        
    return dummy.next

l1 = createLinkedList([4, 2 ,1 ,3])
l2 = createLinkedList([-1, 5, 3, 4, 0])

printLinkedList(insertionSortList(l1))
printLinkedList(insertionSortList(l2))
