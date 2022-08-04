a = [1, 2, 3, 4, 5]
b = 10

def solve(A, B):
    """Approach is to check for mid(subarray size) length and based on that
    we either decrease or increase subarray size (mid). For each mid we check every subarray of size mid
    and save if it satisfies"""
    n = len(A)
    pf = [0] * n
    pf[0] = A[0]
    for i in range(1, n):
        pf[i] = pf[i - 1] + A[i]

    def check(prf, total, k):
        ln = len(A)
        for j in range(k - 1, ln):
            if j == k - 1 and prf[j] > total:
                return False
            elif prf[j] - prf[j - k] > total:
                return False
        return True

    l = 1
    h = n
    ans = 0
    while l <= h:
        m = (l + h) // 2
        if check(pf, B, m):
            ans = m
            l = m + 1
        else:
            h = m - 1
    return ans

print(solve(a, b))

# Given an array of integers A and an integer B, find and return the maximum value K such that there is no subarray
# in A of size K with the sum of elements greater than B.
