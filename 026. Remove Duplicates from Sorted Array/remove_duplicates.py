"""
Leetcode 26. Remove Duplicates from Sorted Array

Given a sorted array, remove the duplicates in-place such that each element 
appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying 
the input array in-place with O(1) extra memory.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    
    if len(nums) <= 1:
        return len(nums)
    
    i = 0
    
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
            
    return i + 1
    
print(removeDuplicates([]) == 0)
print(removeDuplicates([1, 1, 1]) == 1)
print(removeDuplicates([1, 2, 3]) == 3)
print(removeDuplicates([1, 1, 5]) == 2)
print(removeDuplicates([1, 5, 5]) == 2)


