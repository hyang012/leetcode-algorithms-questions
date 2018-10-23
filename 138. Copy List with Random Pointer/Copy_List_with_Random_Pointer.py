#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random
pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""

class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


# O(n) space, O(2n) time
def copyRandomList(head):
    """
    :type head: RandomListNode
    :rtype: RandomListNode
    """
        
    dic = {}
    m = n = head
    while m:
        dic[m] = RandomListNode(m.label)
        m = m.next
    
    while n:
        dic[n].next = dic.get(n.next)
        dic[n].random = dic.get(n.random)
        n = n.next
    return dic.get[head]

# O(n) time
def copyRandomList(head):
    """
    :type head: RandomListNode
    :rtype: RandomListNode
    """
    dic = collections.defaultdict(lambda: RandomListNode(0))
    dic[None] = None
    n = head
    while n:
        dic[n].label = n.label
        dic[n].next = dic[n.next]
        dic[n].random = dic[n.random]
        n = n.next
    return dic[head]
    