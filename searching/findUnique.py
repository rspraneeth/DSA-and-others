a = [3, 3, 1, 1, 8, 8, 10, 10, 19, 6, 6, 2, 2, 4, 4]


def solve(A):
    n = len(A)
    if n == 1:
        return A[0]
    if A[0] != A[1]:
        return A[0]
    elif A[n - 1] != A[n - 2]:
        return A[n - 1]
    l = 1
    h = n - 2
    while l <= h:
        m = (l + h) // 2
        if A[m] != A[m - 1] and A[m] != A[m + 1]:
            return A[m]
        if A[m] == A[m - 1]:  # landing on second occurrence
            m = m - 1
        if m % 2 == 0:  # the index is even means we can discard left side
            l = m + 2  # to not have 2 unique elements in search space
        else:  # if odd, element is present left side so discard right side
            h = m - 1


print(solve(a))

# every element repeats twice, only one element is unique, find it. Repeated elements are adjacent
