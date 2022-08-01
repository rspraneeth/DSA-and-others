from functools import cache
def uniquePaths(m, n):
    def path(i, j):
        """Using recursion, TC: Exponential"""
        if i == m-1 and j == n-1:
            return 1
        elif i >= m or j >= n:
            return 0
        else:
            return path(i+1, j) + path(i, j+1)
    return path(0, 0)

def uniquePaths1(m, n):
    """Using cache decorator for memoization"""
    @cache
    def path(i, j):
        if i == m-1 and j == n-1:
            return 1
        elif i >= m or j >= n:
            return 0
        else:
            return path(i + 1, j) + path(i, j + 1)

    return path(0, 0)

def uniquePaths2(m, n):
    """Math observation: Combinations. nCr times"""
    n = m + n - 2
    r = m - 1
    res = 1
    for i in range(1, r + 1):  # to calculate nCr
        res = res * (n + i - r) / i
    return int(res)

print(uniquePaths(3, 7))
print(uniquePaths1(23, 12))

# Leet code: 62. Unique Paths
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move
# either down or right at any point in time. Given the two integers m and n,
# return the number of possible unique paths that the robot can take to reach the bottom-right corner.
