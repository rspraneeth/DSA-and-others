from sortedcontainers import SortedList
a = [5, 3, 1, 1, 2, 4]

def countSmaller(nums):
    """Approach: Take a new list(A[]) of sorted elements. The index of a value/element in A[] tells how many
    elements are lesser than the value. We remove the element that is iterated, from A[]. So that element
    will not be counted in next iteration."""
    counts = []
    A = SortedList(nums)
    for i in nums:
        ind = A.index(i)
        counts.append(ind)
        A.remove(i)
    return counts

print(countSmaller(a))

# we used sortedlist instead of sorted considering there will be upto 10**4 values in given array
# to reduce time complexity

# 315. Count of Smaller Numbers After Self
# You are given an integer array nums, and you have to return a new counts array.
# The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
