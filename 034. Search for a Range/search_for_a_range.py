"""
Leetcode 34. Search for a Range

Given an array of integers sorted in ascending order, find the starting
 and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Time Complexity: O(log(n))
Space Complexity: O(1)
"""

def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    if nums is None or len(nums) == 0:
        return [-1, -1]
    
    left_position = find_extreme_position(nums, target, True)
    
    if nums[left_position] != target:
        return [-1, -1]
    
    right_position = find_extreme_position(nums, target, False)
    
    if nums[right_position] == target:
        return [left_position, right_position]
    else: 
        return [left_position, right_position-1]
    
        
def find_extreme_position(nums, target, find_start):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        mid = (right - left) // 2 + left
        if (find_start and nums[mid] == target) or nums[mid] > target:
            right = mid
        else:
            left = mid + 1

    return left

print(searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4])
print(searchRange(None, 8) == [-1, -1])
print(searchRange([], 8) == [-1, -1])
print(searchRange([5, 7, 7, 8, 8, 10], 10) == [5, 5])
print(searchRange([5, 7, 7, 8, 8, 10], 3) == [-1, -1])

            