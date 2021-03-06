#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 385. Mini Parser

Given a nested list of integers represented as a string, implement a parser to deserialize it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Note: You may assume that the string is well-formed:

String is non-empty.
String does not contain white spaces.
String contains only digits 0-9, [, - ,, ].
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

def deserialize(s):
    """
    :type s: str
    :rtype: NestedInteger
    """
    
    if s[0] != '[':
        return NestedInteger(int(s))
    
    nested = NestedInteger()
    numP, start = 0, 1
    for i in range(1, len(s)):
        if (numP == 0 and s[i] == ',') or i == len(s) - 1:
            if start < i:
                nested.add(deserialize(s[start:i]))
            start = i + 1
        elif s[i] == '[':
            numP += 1
        elif s[i] == ']':
            numP -= 1
    return nested


# Stack solution
def deserialize(s):
    """
    :type s: str
    :rtype: NestedInteger
    """
    stack = []
    start = -1
    for i, char in enumerate(s):
        if  char == '[':
            stack.append(NestedInteger())
        elif char == ']':
            if len(stack) > 1:
                t = stack.pop()
                stack[-1].add(t)
        elif char.isdigit() or c == '-':
            if start == -1:
                start = i
            if i == len(s) - 1 or not s[i+1].isdigit():
                if stack:
                    stack[-1]. add(NestedInteger(int(s[start:i+1])))
                else:
                    stack.append(NestedInteger(int(s[start:i+1])))
                start = -1
    return stack.pop()
    
        
    
    


