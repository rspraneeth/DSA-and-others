nums1 = [5, 7, 7, 8, 8, 10]
target1 = 8


def searchRange(nums, target):
    f, l = -1, -1
    if target not in nums:
        return [f, l]
    f = nums.index(target)
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == target:
            l = i
            break
    return [f, l]

print(searchRange(nums1, target1))

# 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position
# of a given target value. If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.
