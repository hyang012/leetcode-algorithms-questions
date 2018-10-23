#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.
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


def reverseBetween(head, m, n):
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """
    if not head or not head.next or m == n:
        return head
    
    # Create a dummy head node
    dummy = ListNode(0)
    dummy.next = head
    
    # Two cursors that point at the mth node and the n+1 th node
    # to be reversed
    m_node = dummy
    n_node = dummy.next
    
    for _ in range(m-1):
        m_node = m_node.next
        n_node = n_node.next
    
    for _ in range(n-m):
        tmp = n_node.next
        n_node.next = tmp.next
        tmp.next = m_node.next
        m_node.next = tmp
    
    return dummy.next

l1 = createLinkedList([1, 2, 3, 4, 5])

printLinkedList(reverseBetween(l1, 2, 4))
                
        
        
        
    