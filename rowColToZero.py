mat = [[1, 2, 0, 4], [0, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 16]]
# def solve1(A):
#     n = len(A)
#     m = len(A[0])
#     B = [[A[i][j] for j in range(m)] for i in range(n)]
#     for i in range(n):
#         for j in range(m):
#             if A[i][j] == 0:
#                 for y in range(m):
#                     x = i
#                     B[x][y] = 0
#                 for x in range(n):
#                     y = j
#                     B[x][y] = 0
#     return B  # O(n**3) and O(n), not good!

def solve2(A):
    """We traverse the matrix and use 1st row and 1st col as flag array to mark the rows and cols which has 0 in it.
    Using 1st row and col we mark the rest of the array 0’s. At the end we mark 1st row or col 0’s if there is any zero
    in them"""
    n = len(A)
    m = len(A[0])
    isColz = False
    isRowz = False
    for i in range(n):
        for j in range(m):
            if i == 0 and A[i][j] == 0:  # checking if first row has any zeros
                isRowz = True
            elif j == 0 and A[i][j] == 0:  # checking if first column has any zeros
                isColz = True
            elif A[i][j] == 0:  # for any other element we use first row and first column to mark them
                A[0][j] = 0
                A[i][0] = 0
    for i in range(1, n):
        for j in range(1, m):
            if A[0][j] == 0 or A[i][0] == 0:
                A[i][j] = 0
    if isColz:
        for i in range(n):
            A[i][0] = 0
    if isRowz:
        for j in range(m):
            A[0][j] = 0
    return A

print(solve2(mat))
# row and columns to zero for any A[i][j] = 0
