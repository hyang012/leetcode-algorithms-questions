#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 380. Insert Delete GetRandom O(1)

Design a data structure that supports all following operations in average O(1) time.
    1. insert(val): Inserts an item val to the set if not already present.
    2. remove(val): Removes an item val from the set if present.
    3. getRandom: Returns a random element from current set of elements. Each
       element must have the same probability of being returned.

"""
import random

class RandomizedSet(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.dic = {}
    
    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already
        contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.dic:
            self.list.append(val)
            self.dic[val] = len(self.list) - 1
            return True
        else:
            return False
    
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the
        specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            idx = self.dic[val]
            new_val = self.list[-1]
            self.list[idx] = new_val
            self.dic[new_val] = idx
            self.list.pop()
            del self.dic[val]
            return True
        else:
            return False
        
    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.list)
        
random_set = RandomizedSet()
print(random_set.insert(1))
print(random_set.remove(2))
print(random_set.insert(2))
print(random_set.getRandom())
print(random_set.remove(1))
print(random_set.getRandom())

