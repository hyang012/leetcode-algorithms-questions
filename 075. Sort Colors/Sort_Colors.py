#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leetcode 75. Sort Colors

Given an array with n objects colored red, white or blue, sort them in-place
so that objects of the same color are adjacent, with the colors in the order
red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white,
and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Follow up:

A rather straight forward solution is a two-pass algorithm using counting
sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""

## Merge Sort
#def sortColors(nums):
#    """
#    :type nums: List[int]
#    :rtype: void Do not return anything, modify nums in-place instead.
#    """
#    if not nums or len(nums) == 1:
#        return
#    mergeSort(nums)
#    
#def mergeSort(nums):
#    if len(nums) <= 1:
#        return
#    else:
#        left = nums[:len(nums)//2]
#        right = nums[len(nums)//2:]
#        
#        mergeSort(left)
#        mergeSort(right)
#        
#        i, j = 0, 0
#        for k in range(len(nums)):
#            if j >= len(right) or (i < len(left) and left[i] < right[j]):
#                nums[k] = left[i]
#                i += 1
#            else:
#                nums[k] = right[j]
#                j += 1


## Counting Sort - two pass
#def sortColors(nums):
#    """
#    :type nums: List[int]
#    :rtype: void Do not return anything, modify nums in-place instead.
#    """
#    if not nums or len(nums) == 1:
#        return
#    
#    count = [0, 0, 0]
#    for i, num in enumerate(nums):
#        count[num] += 1
#    
#    for i in range(len(nums)):
#        if i < count[0]:
#            nums[i] = 0
#        elif i < count[1] + count[0]:
#            nums[i] = 1
#        else:
#            nums[i] = 2


# Counting Sort - one pass
def sortColors(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    if not nums or len(nums) == 1:
        return
    
    red, white, blue = 0, 0, len(nums)-1
    while white < blue:
        if nums[white] == 0:
            nums[white], nums[red] = nums[red], nums[white]
            red += 1
            white += 1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1
            
nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)
        
        