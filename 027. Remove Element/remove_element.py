"""
Leetcode 27. Remove Element

Given an array and a value, remove all instances of that value in-place 
and return the new length.

Do not allocate extra space for another array, you must do this by 
modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave 
beyond the new length.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
   
    if nums is None or len(nums) == 0:
        return 0
    
    i, j = 0, len(nums) - 1
    
    while i <= j:
        if nums[i] == val:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
        else:
            i += 1
            
    return i

print(removeElement([], 5) == 0)
print(removeElement([1, 1, 1, 1], 1) == 0)
print(removeElement([1, 2, 2, 1], 2) == 2)
print(removeElement([1, 2, 2, 1], 3) == 4)
