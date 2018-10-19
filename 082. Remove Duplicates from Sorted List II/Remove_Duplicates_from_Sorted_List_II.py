#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 82. Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list.
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



def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
        return head
    
    dummy = ListNode(head.val-1)  # Create a dummy head 
    dummy.next = head
    slow, fast = dummy, dummy.next.next
    
    while fast:
        if slow.next.val == fast.val:
            if not fast.next:
                slow.next = None                
        else:
            if slow.next.next == fast:
                slow = slow.next
            else:
                slow.next = fast
        fast = fast.next
    return dummy.next

l1 = createLinkedList([1, 2, 3, 3, 4, 4, 5])
l2 = createLinkedList([1, 1, 1, 2, 3])

printLinkedList(deleteDuplicates(l1))
printLinkedList(deleteDuplicates(l2))


        
        
        
        
        
        
        
        
        
        