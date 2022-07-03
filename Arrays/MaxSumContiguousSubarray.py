A1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
def maxSubArray(self, A):
    n = len(A)
    mx = A[0]
    sm = 0
    for j in range(n):
        sm += A[j]
        mx = max(mx, sm)
        if sm < 0:
            sm = 0
    return mx
print(maxSubArray(A1))

# using Kadane's Algorithm
