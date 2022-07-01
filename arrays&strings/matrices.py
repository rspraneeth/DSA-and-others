# n = int(input("Enter no of rows: "))
# m = int(input("Enter no of columns: "))
# A = [[0]*m]*n
# A = []
# for i in range(n):  # creating array method 1
#     a = []
#     for j in range(m):
#         a.append(int(input(" ")))
#     A.append(a)
# print(A)
# A = [[int(input(" ")) for j in range(m)] for i in range(n)]  # creating array method 2
import math

mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

# print matrix
def PrintMatrix(A):
    n = len(A)
    m = len(A[0])
    for i in range(n):
        for j in range(m):
            print(A[i][j], end=' ')
        print()

# Given mat[n][m] print row wise sum and max row sum
def RowWiseSum(A):
    n = len(A)
    m = len(A[0])
    mx = -math.inf
    print(mx)
    for i in range(n):
        sum = 0
        for j in range(m):
            sum += A[i][j]
        mx = max(mx, sum)
        print(f"Sum of elements in  row {i + 1} is {sum}")
    print(f"Max row sum is {mx}")

# Given mat[n][m] print column wise sum and max column sum
def ColWiseSum(A):
    n = len(A)
    m = len(A[0])
    mx = -math.inf
    for j in range(m):
        sum = 0
        for i in range(n):
            sum += A[i][j]
        mx = max(mx, sum)
        print(f"Sum of elements in  column {j + 1} is {sum}")
    print(f"Max column sum is {mx}")

# Given a mat[n][n] Print diagonals
def SqMatDiagonals(A):
    n = len(A)
    i = 0
    while i < n:  # L->R diagonal
        print(A[i][i])
        i += 1

    i = 0
    j = n - 1
    while i < n and j >= 0:  # R->L diagonal
        print(A[i][j])
        i += 1
        j -= 1

# Given mat[n][m] Print all diagonals going R->L
def AllDiagonalsRtoL(A):
    PrintMatrix(A)
    n = len(A)
    m = len(A[0])
    for j in range(m):  # Diagonals starting from 0th row
        x = 0
        y = j
        while x < n and y >= 0:
            print(A[x][y], end=' ')
            x += 1
            y -= 1
        print()

    for i in range(1, n):  # Diagonals starting from M-1 col. range(1, n), since i=0 is already covered in previous loop
        x = i
        y = m - 1
        while x < n and y >= 0:
            print(A[x][y], end=' ')
            x += 1
            y -= 1
        print()

# transpose of a matrix for size n
def transpose(A):
    n = len(A)
    for i in range(1, n):
        for j in range(i):
            temp = A[i][j]
            A[i][j] = A[j][i]
            A[j][i] = temp
    PrintMatrix(A)
    # return A

# rotate the matrix by 90 deg clockwise direction holding TR(top right), size n
def rotate90(A):
    transpose(A)
    n = len(A)
    for i in range(n):
        A[i].reverse()
    PrintMatrix(A)

rotate90(mat)
