#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 234. Palindrome Linked List

Given a singly linked list, determine if it is a palidrome.

Follow up:
Could you do it in O(n) time and O(1) space?
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


# Reverse the second half of the input list
# O(n) time, O(1) space
def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if not head or not head.next:
        return True
    
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    reverse = None
    
    while slow:
        current_node = slow
        slow = slow.next
        current_node.next = reverse
        reverse = current_node
    
    cur = head
    while reverse:
        if cur.val != reverse.val:
            return False
        cur = cur.next
        reverse = reverse.next
    return True

l1 = createLinkedList([1, 2])
l2 = createLinkedList([1, 1, 2, 1])

print(isPalindrome(l1))
print(isPalindrome(l2))
