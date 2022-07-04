# Given a column title as appears in an Excel sheet, return its corresponding column number.
def titleToNumber(A):
    """ord('A') gives 65, i.e., ASCII value. A = ord('A) % 64 = 1. Similarly Z = 90.
    'ABCD' means 4*26^0 + 3*26^1 + 2*26^2 + 1*26^3. (R->L: similar to binary to decimal)."""
    n = len(A)
    res = 0
    for i in range(n):
        v = ord(A[i]) % 64
        res += v * 26 ** (n - 1 - i)
    return res


print(titleToNumber('ABCD'))


# Given two integers A and B, find the greatest possible positive integer M, such that A % M = B % M.
def greatest(A, B):
    if A > B:
        return A - B
    else:
        return B - A


print(greatest(6, 2))


# LCM
def LCM(A, B):
    if A % B == 0 or B % A == 0:
        return max(A, B)
    mx = max(A, B)
    mn = min(A, B)
    for i in range(2, mx + 1):
        mul = i * mn
        if mul % mx == 0:
            return mul


print(LCM(3, 104))

# Eight integers A, B, C, D, E, F, G, and H represent two rectangles in a 2D plane. For the first rectangle,
# its bottom left corner is (A, B), and the top right corner is (C, D), and for the second rectangle, its bottom left
# corner is (E, F), and the top right corner is (G, H). Return 1 if the two rectangles overlap else, return 0.
def solve(A, B, C, D, E, F, G, H):
    return (1, 0)[F >= D or H <= B or E >= C or G <= A]  # condition checks for rectangles side by side or up and down

print(solve(0, 10, 10, 0, 5, 5, 15, 0))
