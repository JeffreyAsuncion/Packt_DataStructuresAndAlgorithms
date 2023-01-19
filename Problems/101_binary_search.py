"""
704. Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""



def binary_search(nums, target):
    
    low = 0
    high = len(nums)-1

    while low <= high:
        mid_point = (low+high)//2

        if nums[mid_point] == target:
            return mid_point
        elif nums[mid_point] > target:
            high = mid_point - 1
        else:
            low = mid_point + 1

    return -1


nums = [-1,0,3,5,9,12]
target = 9
# Output: 4
print(binary_search(nums,target))