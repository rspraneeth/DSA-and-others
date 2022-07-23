a = [1, 2, 3, 4, 5, 11]

def solve(A, B):
    """Brute force approach checking every sub array"""
    N = len(A)
    for i in range(N):
        if A[i] == B:
            return [A[i]]
        for j in range(i+1, N):
            if sum(A[i:j]) == B:
                return A[i:j]

    return [-1]

def solve1(A, B):
    """Optimized Using 2 pointer. Changing the window size i,j based on sum, B"""
    i, j = 0, 0
    n = len(A)
    sum = A[0]
    flag = False
    while i < n and j < n:
        if sum == B:
            flag = True
            break
        elif sum < B:
            if j + 1 == n:
                break
            j += 1
            sum += A[j]
        else:
            if i + 1 == n:
                break
            sum -= A[i]
            i += 1
    if not flag:
        return [-1]
    else:
        return A[i:j+1]

print(solve(a, 11))
print(solve(a, 11))

# Given an array of positive integers A and an integer B, find and return first continuous subarray which adds to B.
# If the answer does not exist return an array with a single element "-1".
# First sub-array means the sub-array for which starting index in minimum.
