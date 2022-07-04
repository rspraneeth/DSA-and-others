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

