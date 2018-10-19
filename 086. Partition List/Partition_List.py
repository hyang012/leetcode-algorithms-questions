#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 86. Partition List

Given a linked list and a value x, partition it such that all nodes less than
x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two
partitions.
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



def partition(head, x):
    """
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """
    if not head or not head.next:
        return head
    
    end = head  # Create a pointer at the end of the list
    n = 1
    while end.next:
        n += 1
        end = end.next    
    dummy = ListNode(0)  # create a dummy head
    dummy.next = head
    cur, node = dummy, dummy.next
    
    i = 1
    while i <= n:
        if node.val >= x and node.next:
            cur.next = cur.next.next
            node.next = None
            end.next = node
            
            end = end.next
        else:
            cur = cur.next
        node = cur.next
        i += 1
    
    return dummy.next

l1 = createLinkedList([1, 4, 3, 2, 5, 2])
l2 = createLinkedList([1, 2])

printLinkedList(partition(l1, 3))
printLinkedList(partition(l2, 0))

