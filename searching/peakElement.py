a = [1, 2, 3, 4, 5]

def solve(A):
    n = len(A)
    if n == 1 or A[0] > A[1]:
        return A[0]
    if A[n - 1] >= A[n - 2]:
        return A[n - 1]
    l = 1
    h = n - 2
    while l <= h:
        m = (l + h) // 2
        if A[m - 1] < A[m] > A[m + 1]:
            return A[m]
        if A[m] < A[m + 1]:
            l = m + 1
        else:
            h = m - 1

print(solve(a))

# Given an array of integers A, find and return the peak element in it.
# An array element is peak if it is NOT smaller than its neighbors.
# For corner elements, we need to consider only one neighbor. We ensure that answer will be unique.
