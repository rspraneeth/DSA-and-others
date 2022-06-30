A1 = [5, 6, 3, 8, -1, 7, 8, 9, 5, 3]
def solve1(A):
    n = len(A)
    mx = 0
    mxi = -1
    mxj = -1
    for i in range(n):
        if A[i] > 0:
            sm = 1
            for j in range(i + 1, n):
                if A[j] > 0:
                    sm += 1
                else:
                    break
            if sm > mx:
                mxi = i
                if j == n - 1 and A[j] > 0:
                    mxj = j + 1
                else:
                    mxj = j
                mx = sm
    return A[mxi:mxj]

# def solve2(A):  # unsolved yet for O(n)
#     i, j, start, end = 0, 0, 0, -1
#     n = len(A)
#     while i < n and j < n:
#         if A[j] >= 0:
#             j += 1
#         else:
#             if j-i > end-start+1:
#                 start = i
#                 end = j-1
#             i = j+1
#             j += 1
#     return A[start:end+1]

print(solve2(A1))
