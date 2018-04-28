"""
Leetcode 35. Search Insert Positions

Given a sorted array and a target value, return the index if the target 
is found. If not, return the index where it would be if it were inserted
in order.

You may assume no duplicates in the array.

Time Complexity: O(log(n))
Space Complexity: O(1)
"""

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if nums is None or nums[0] > target:
        return 0
    elif nums[-1] < target:
        return len(nums)

    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        
    return left
                
