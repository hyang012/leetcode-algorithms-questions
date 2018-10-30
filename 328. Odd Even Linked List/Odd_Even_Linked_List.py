#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 328. Odd Even Linked List

Given a singly linked list, group all odd nodes together followed by the even
nodes. Please note here we are talking about the node number and not the value
in the nodes.

You should try to do it in place. The program should run in O(1) space
complexity and O(nodes) time complexity.

Note:
The relative order inside both the even and odd groups should remain as it was
in the input.

The first node is considered odd, the second node even and so on ...
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


def oddEvenList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next:
        return head
    
    odd, even = head, head.next
    head = head.next.next
    odd_cur, even_cur = odd, even
    i = 3
    
    while head:
        if i % 2 != 0:  # odd node
            odd_cur.next = head
            odd_cur = odd_cur.next
        else:
            even_cur.next = head
            even_cur = even_cur.next
        head = head.next
        i += 1
    
    even_cur.next = None
    odd_cur.next = even
    
    return odd
    
l1 = createLinkedList([1,2,3,4,5])
l2 = createLinkedList([2,1,3,5,6,4,7])

printLinkedList(oddEvenList(l1))
printLinkedList(oddEvenList(l2))
