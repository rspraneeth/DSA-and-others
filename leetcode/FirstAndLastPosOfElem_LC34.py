nums1 = [5, 7, 7, 8, 8, 10]
target1 = 8


def searchRange1(nums, target):
    f, l = -1, -1
    if target not in nums:
        return [f, l]
    f = nums.index(target)
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == target:
            l = i
            break
    return [f, l]

def searchRange(nums, target):
    """Approach: Binary search for first and last position of element.
       For first position(f) of element binary search over array and find the index.
       For last position, take start as 'f' and binary search. Binary search finds the element but
       not necessarily the first_occurrence/last_occurrence of element. There might be duplicates on left.
       So while finding the first position, whenever we find target we move to left of mid and continue search.
       Similarly, when we are finding last position, whenever we find target we move to right of mid"""
    s = 0
    ind = [-1, -1]  # Taking an array ind[], to store first and last position of element.
    f_found = False  # to track if we found first position
    for i in range(2):  # loops 2 times for first and last position
        e = len(nums) - 1
        while s <= e:
            m = (s+e)//2
            if nums[m] == target:
                ind[i] = m  # we store value
                if not f_found:
                    e = m-1  # since we are still searching for first position, move left.
                else:
                    s = m+1  # we are searching for second position, move right.
            elif nums[m] > target:
                e = m-1
            else:
                s = m+1
        if ind[0] == -1:
            return ind
        f_found = True
        s = ind[0]  # to search second position we start binary search from first position

    return ind


print(searchRange1(nums1, target1))
print(searchRange(nums1, target1))

# leet code 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position
# of a given target value. If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.
