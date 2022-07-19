def generate(numRows):
    a = []
    for i in range(numRows):
        b = [1]  # taking every list with first element as 1
        for j in range(i-1):  # adding current and next element of previous list and appending to b
            s = a[i-1][j] + a[i-1][j+1]
            b.append(s)
        if i != 0:  # edge case when numRows = 1, we need not insert last 1
            b.append(1)
        a.append(b)

    return a

print(generate(5))

# 118. Pascal's Triangle
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers of previous list

# Example 1:
# Input: numRows = 5, Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
