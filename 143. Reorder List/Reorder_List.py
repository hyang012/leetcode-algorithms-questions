#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 143. Reorder List

Given a singly linked list L: L0 -> L1 -> ... -> Ln
reorder it to: L0 -> Ln -> L1 -> Ln-1 -> L2 -> ...

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


def _splitList(head):
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    right_half = slow.next
    slow.next = None
    return head, right_half

def _reverseList(head):
    if not head or not head.next:
        return head
    prev = None
    while head:
        cur = head
        head = head.next
        cur.next = prev
        prev = cur
    return prev

def _mergeLists(l1, l2):
    tail = head = l1
    l1 = l1.next
    while l2:
        tail.next = l2
        tail = tail.next
        l2 = l2.next
        if l1:
            l1, l2 = l2, l1
    return head

def reorderList(head):
    """
    :type head: ListNode
    :rtype: void Do not return anythin, modify head in-place instead.
    """
    if not head or not head.next:
        return
    head, right_half = _splitList(head)
    right_half = _reverseList(right_half)
    head = _mergeLists(head, right_half)
    return head
    


l1 = createLinkedList([1, 2, 3, 4])
l2 = createLinkedList([1, 2, 3, 4, 5])

printLinkedList(reorderList(l1))
printLinkedList(reorderList(l2))


