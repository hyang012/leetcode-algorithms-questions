"""
Leetcode 53. Maximum Subarray

Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum and 
return its sum.

"""

def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    if nums is not None and len(nums) != 0:
        cur_max, cur_sum = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            cur_sum = max(cur_sum + nums[i], nums[i])
            cur_max = max(cur_sum, cur_max)
        
        return cur_max
        
