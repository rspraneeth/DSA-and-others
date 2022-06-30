def solve(A):
    """Given a binary string A. It is allowed to do at most one swap between any 0 and 1. Find and return the length
    of the longest consecutive 1’s that can be achieved."""
    n = len(A)
    count_one = 0  # to count total 1's
    max_len = 0
    for i in A:
        if i == '1':
            count_one += 1
    if count_one == n:
        return n
    for i in range(n):
        if A[i] == '0':  # we are checking left side and right sie 1's when A[i] = 0
            left = 0
            for j in range(i - 1, -1, -1):
                if A[j] == '1':
                    left += 1
                else:
                    break
            right = 0
            for j in range(i + 1, n):
                if A[j] == '1':
                    right += 1
                else:
                    break
            if count_one == left + right:  # this conditions means 000111, 1111000, 1101111 => adding left and right
                max_len = max(max_len, left + right)
            else:
                max_len = max(max_len, left + right + 1)  # it means there exists another 1 other than
                # left and right of A[i], so we swap that 1 with zero, so adding 1
    return max_len

print(solve('11101100011111'))
