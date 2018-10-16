#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.
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



def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    
    if not l1 or not l2:
        return l1 or l2
    
    carry_over = 0
        
    res = ListNode(0)
    cur_r = res
    
    while l1 or l2 or carry_over != 0:
        v1, v2 = 0, 0
        
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        
        num = (v1 + v2 + carry_over) % 10
        carry_over = (v1 + v2 + carry_over) // 10

        cur_r.next = ListNode(num)
        cur_r = cur_r.next
    return res.next

num1 = createLinkedList([2, 4, 3])
num2 = createLinkedList([5, 6, 4])

printLinkedList(addTwoNumbers(num1, num2))