#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 122. Best Time to Buy and Sell Stock ii

Say you have an array for which the ith element is the price of a
given stock on day i.

Design an algorithm to find the maximum profit. You may complete as
many transactions as you like (i.e., buy one and sell one share of 
the stock multiple times).

Note: You may not engage in multiple transactions at the same time
(i.e., you must sell the stock before you buy again).
"""

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    profit = 0
    
    if prices is None or len(prices) <= 1:
        return profit
    
    buy = prices[0]
    for i in range(1, len(prices)):
        if prices[i] > buy:
            profit += prices[i] - buy
        buy = prices[i]
        
    return profit
