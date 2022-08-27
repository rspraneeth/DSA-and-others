from bisect import bisect_right as count
a = [[1, 3, 5],
     [2, 6, 9],
     [3, 6, 9]]

def findMedian(A):
    mn = A[0][0]
    mx = 0
    n = len(A)
    m = len(A[0])
    for i in range(n):
        mn = min(mn, A[i][0])
        mx = max(mx, A[i][m - 1])
    ans = -1
    desired = (m * n) // 2 + 1
    while mn <= mx:
        x = (mn + mx) // 2
        cnt = 0
        for i in A:
            cnt += count(i, x)
        if cnt < desired:
            mn = x + 1
        else:
            ans = x
            mx = x - 1
    return ans

print(findMedian(a))
# Given a matrix of integers A of size N x M in which each row is sorted.
# Find and return the overall median of matrix A. NOTE: No extra memory is allowed.
# NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.
