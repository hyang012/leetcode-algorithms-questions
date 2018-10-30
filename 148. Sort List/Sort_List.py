#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 148. Sort List

Sort a linked list in O(nlogn) time using constant space complexity.
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


def sortList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next:
        return head
    
    # Find the middle of the list
    fast, slow = head.next, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    second_half = slow.next
    
    # Split linked list
    slow.next = None
    left = sortList(head)
    right = sortList(second_half)
    
    return merge(left, right)

def merge(left, right):
    if not left or not right:
        return left or right
    
    if left.val > right.val:
        left, right = right, left
    
    head = prev = left
    left = left.next
    
    while left and right:
        if left.val < right.val:
            left = left.next
        else:
            prev.next = right
            right = right.next
            prev.next.next = left
        prev = prev.next
    prev.next = left or right
    return head

l1 = createLinkedList([4,2,1,3])
l2 = createLinkedList([-1,5,3,4,0])

printLinkedList(sortList(l1))
printLinkedList(sortList(l2))




    
    
    


