import math

A1 = [1, 6, 4, 2, 6, 9]
B1 = [2, 5, 7, 3, 2, 7]
# ans 7
# """choose 3 trees (let's say, indices p, q, and r), such that Ap < Aq < Ar, where p < q < r. The cost of these trees
# is Bp + Bq + Br. You are to choose 3 trees such that their total cost is minimum. Return that cost.
# If it is not possible to choose 3 such trees return -1."""

def solve(A, B):
    """we solve this by taking q first and then checking left of q(p) and then right of q(r)"""
    n = len(A)
    minpqr = math.inf
    for q in range(1, n-1):
        minpq = math.inf
        for p in range(0, q):  # left of q
            if A[p] < A[q]:
                minpq = min(minpq, B[q]+B[p])
        for r in range(q+1, n):  # right of q
            if A[r] > A[q] and minpq != math.inf:
                minpqr = min(minpqr, minpq + B[r])
    if minpqr == math.inf:  # means no triplet is found
        return -1
    else:
        return minpqr

print(solve(A1, B1))
