N = 1


def generateMatrix(A):
    mat = [[0] * A] * A
    top = 0
    left = 0
    right = A - 1
    bottom = A - 1
    g = 1
    while g <= A ** 2:
        for j in range(left, right + 1):
            x = top
            y = j
            mat[x][y] = g
            g += 1
        top += 1
        for i in range(top, bottom + 1):
            x = i
            y = right
            mat[x][y] = g
            g += 1
        right -= 1
        for j in range(right, left - 1, -1):
            x = bottom
            y = j
            mat[x][y] = g
            g += 1
        bottom -= 1
        for i in range(bottom, top + 1, -1):
            x = i
            y = left
            mat[x][y] = g
            g += 1
        left += 1

    return mat

print(generateMatrix(3))
