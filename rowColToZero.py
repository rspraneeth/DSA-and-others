mat = [[1, 2, 0, 4], [0, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
def solve(A):
    n = len(A)
    m = len(A[0])
    B = [[A[i][j] for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if A[i][j] == 0:
                for y in range(m):
                    x = i
                    B[x][y] = 0
                for x in range(n):
                    y = j
                    B[x][y] = 0
    return B

print(solve(mat))
# row and columns to zero for any A[i][j] = 0
