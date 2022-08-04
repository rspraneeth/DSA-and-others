a = [3, 4, 5, 6, 7, 0, 1, 2, 3]
b = 4

def search1(A, B):
    """Approach: There are 2 sorted arrays now. We find k. Every element in 2nd array is smaller than A[0]
    if the array is rotated. We use this observation and find k and search based on k."""
    def findK(ar):
        """Finding k, how many indexes is the array rotated. Last k elements are rotated to front."""
        l = 0
        h = len(ar) - 1
        K = 0
        while l <= h:
            m = (l + h) // 2
            if ar[m] < ar[m - 1]:
                return m
            elif ar[m] < ar[0]:
                h = m - 1
            else:
                l = m + 1
        return K

    def bin(l, h, arr):
        while l <= h:
            m = (l + h) // 2
            if arr[m] == B:
                return m
            if arr[m] > B:
                h = m - 1
            else:
                l = m + 1
        return -1

    n = len(A)
    k = findK(A)

    if k == 0:
        return bin(0, n - 1, A)
    if B >= A[0]:
        return bin(0, k - 1, A)
    else:
        return bin(k, n - 1, A)

def search2(A, B):
    n = len(A)
    l = 0
    h = n - 1
    while l <= h:
        m = (l + h) // 2
        if A[m] == B:
            return m
        if A[m] < A[0]:  # checking if mid is in 2nd sorted array
            if A[m] < B <= A[h]:
                l = m + 1
            else:
                h = m - 1
        else:
            if A[l] <= B < A[m]:
                h = m - 1
            else:
                l = m + 1
    return -1

def search3(A, B):
    n = len(A)
    l = 0
    h = n - 1
    while l <= h:
        m = (l + h) // 2
        if A[m] == B:
            return m
        if A[l] < A[m]:
            if A[l] <= B < A[m]:
                h = m - 1
            else:
                l = m + 1
        else:
            if A[m] < B <= A[h]:
                l = m + 1
            else:
                h = m - 1
    return -1

print(search1(a, b))
print(search2(a, b))
print(search3(a, b))

# Given a sorted array of integers A of size N and an integer B. Array A is rotated at some pivot unknown
# to you beforehand. (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ).
# You are given a target value B to search. If found in the array, return its index otherwise, return -1.
# You may assume no duplicate exists in the array.
