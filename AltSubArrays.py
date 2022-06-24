"""You are given an integer array A of length N comprising of 0's & 1's, and an integer B. You have to tell
all the indices of array A that can act as a center of 2 * B + 1 length 0-1 alternating subarray.
A 0-1 alternating array is an array containing only 0's & 1's, and having no adjacent 0's or 1's.
For e.g. arrays [0, 1, 0, 1], [1, 0] and [1] are 0-1 alternating, while [1, 1] and [0, 1, 0, 0, 1] are not."""
# 1 <= N <= 103
# A[i] equals to 0 or 1.
# 0 <= B <= (N - 1) / 2

A1 = [1, 0, 1, 0, 1]
B1 = 1


# Approach 1, here we are trying to check with center index
def solve1(A, B):
    n = len(A)
    if B == 0:  # l=2*B+1=1, which means every element is considered as alt sub array, so every index is center
        return [i for i in range(n)]
    ind = []
    for i in range(B, n - B):  # we need not check first B-1 indices as they can't be center
        j = i  # j is to check elements present on right of index i
        k = i  # k is to check elements present on left of index i
        is_alt = True
        while is_alt and j < i + B and k > i - B:
            if A[j] == A[j + 1]:
                is_alt = False
            elif A[k] == A[k - 1]:
                is_alt = False
            j += 1
            k -= 1
        if is_alt:
            ind.append(i)
    return ind


# Approach 2, here we are checking from 1st index
def solve2(A, B):
    n = len(A)
    ind = []
    l1 = 2 * B + 1
    for i in range(n-l1+1):
        flag = True
        cur = -1
        for j in range(i, i+l1):
            if A[j] == cur:
                flag = False
                break
            cur = A[j]
        if flag:
            ind.append(i+B)
    return ind

print(solve1(A1, B1))
print(solve2(A1, B1))
