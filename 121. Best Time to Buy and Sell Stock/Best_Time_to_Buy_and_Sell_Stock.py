#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 121. Best Time to Buy and Sell Stock

Say you have an array for which the ith element is the price of 
a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy
one and sell one share of the stock), design an algorithm to find the 
maximum profit.

Note that you cannot sell a stock before you buy one.
"""

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """

    max_profit = 0
    
    if prices is None or len(prices) <= 1:
        return max_profit
    
    buy = prices[0]
    for i in range(1, len(prices)):
        if prices[i] < buy:
            buy = prices[i]
        else:
            max_profit = max(max_profit, prices[i] - buy)
        
    return max_profit

