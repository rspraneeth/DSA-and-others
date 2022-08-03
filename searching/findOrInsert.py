a = [1, 3, 5, 6]
b = 5

def searchInsert(A, B):
    n = len(A)
    l = 0
    h = n - 1
    while l <= h:
        m = (l + h) // 2
        if A[m] == B:
            return m
        elif A[m] > B:
            h = m - 1
        else:
            l = m + 1
    return l

print(searchInsert(a, b))

# Given a sorted array A of size N and a target value B, return the index (0-based indexing) if the target is found.
# If not, return the index where it would be if it were inserted in order.
# NOTE: You may assume no duplicates in the array.
