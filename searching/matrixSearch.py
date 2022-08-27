a = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
b = 3

def searchMatrix(A, B):
    m = len(A)
    n = len(A[0])
    low = 0
    high = m * n - 1
    while low != high:
        mid = (high + low) // 2
        if A[mid // n][mid % n] < B:
            low = mid + 1
        else:
            high = mid

    if A[high // n][high % n] == B:
        return 1
    else:
        return 0

def searchMatrix1(A, B):
    m = len(A)
    n = len(A[0])
    low = 0
    high = m * n - 1
    ans = -1
    while low <= high:
        mid = (high + low) // 2
        if A[mid // n][mid % n] <= B:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    if A[ans // n][ans % n] == B:
        return 1
    else:
        return 0

def searchMatrix2(A, B):
    m = len(A)
    n = len(A[0])
    low = 0
    high = m * n - 1
    while low < high:
        mid = low + (high - low + 1) // 2
        if A[int(mid / n)][int(mid % n)] <= B:
            low = mid
        else:
            high = mid - 1

    if A[int(low / n)][int(low % n)] == B:
        return 1
    else:
        return 0

print(searchMatrix(a, b))
print(searchMatrix1(a, b))
print(searchMatrix2(a, b))

# Given a matrix of integers A of size N x M and an integer B. Write an efficient algorithm that
# searches for integer B in matrix A. This matrix A has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than or equal to the last integer of the previous row.
# Return 1 if B is present in A, else return 0.
# NOTE: Rows are numbered from top to bottom, and columns are from left to right.
