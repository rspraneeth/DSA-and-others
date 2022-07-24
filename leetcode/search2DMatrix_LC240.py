matrix1 = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target1 = 5


def searchMatrix1(matrix, target):
    """Approach 1: Using in keyword in every list."""
    for i in matrix:
        if target in i:
            return True
    return False  # O(m*n)


def searchMatrix2(matrix, target):
    """Approach 2:
       1. Since the rows are sorted, for any element its right side elements will be always greater than element.
       2. Since the columns are sorted, for any element its upper/above elements will be lesser than element.
       Using 1 & 2 we can say, if target=current, target found. else if current>target, move current up.
       else if current<target, move current right. Start current from bottom left."""
    m = len(matrix)
    n = len((matrix[0]))
    i = m - 1
    j = 0
    while i >= 0 and j < n:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            i -= 1
        else:
            j += 1
    return False  # O(m+n)


def searchMatrix3(matrix, target):
    """Approach 3: Using binary search in each list"""
    m = len(matrix)
    n = len((matrix[0]))
    for i in range(m):
        if matrix[i][0] <= target <= matrix[i][-1]:
            l = 0
            h = n
            while l < h:
                mid = (l + h) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    h = mid
                else:
                    l = mid + 1
    return False  # O(mlogn)


print(searchMatrix1(matrix1, target1))
print(searchMatrix2(matrix1, target1))
print(searchMatrix3(matrix1, target1))

# leet code 240. Search a 2D Matrix II
# Write an efficient algorithm that searches for a value target in an m x n integer matrix.
# This matrix has the following properties:
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
