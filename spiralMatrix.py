# we are generating spiral array after we iterate through the top row we need not go through it again, so we increase
# top row value by 1, similarly we decrease right column by 1, increase left col by 1, decrease bottom row by 1.
# We change these values of top, right, bottom, left so that we don't iterate through same rows/columns
def generateMatrix(A):
    mat = [[0 for i in range(A)] for j in range(A)]
    top = 0
    left = 0
    right = A - 1
    bottom = A - 1
    g = 1
    while g <= A*A:
        for j in range(left, right + 1):  # going from L->R
            x = top
            y = j
            mat[x][y] = g
            g += 1
        top += 1  # after iterating through top row, we change its value to next row
        for i in range(top, bottom + 1):  # going from T->B
            x = i
            y = right
            mat[x][y] = g
            g += 1
        right -= 1  # after iterating through right column, we change its value to previous column
        for j in range(right, left - 1, -1):  # going from R->L
            x = bottom
            y = j
            mat[x][y] = g
            g += 1
        bottom -= 1  # after iterating through bottom row, we change its value to previous row
        for i in range(bottom, top - 1, -1):  # going from B->T
            x = i
            y = left
            mat[x][y] = g
            g += 1
        left += 1  # after iterating through left column, we change its value to next column

    return mat

print(generateMatrix(5))

"""Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order. 
Problem Constraints
1 <= A <= 1000

Input Format
First and only argument is integer A
Output Format
Return a 2-D matrix which consists of the elements in spiral order.

Example Input
Input 1: 1
Input 2: 2

Example Output
Output 1: [ [1] ]
Output 2: [ [1, 2], [4, 3] ]


Example Explanation
Explanation 1: Only 1 is to be arranged.
Explanation 2: 1 --> 2
                      |
                      |
                4<--- 3                 """