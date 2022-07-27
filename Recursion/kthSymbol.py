# On the first row, we write a 0. Now in every subsequent row, we look at the previous row and
# replace each occurrence of 0 with 01, and each occurrence of 1 with 10.
# Given row number A and index B, return the Bth indexed symbol in row A. (The values of B are 1-indexed.).
def solve1(A, B):
    """Approach: There are two parts in string (when A>=2). First part is repeating of (A-1)th> step and
    second part is also compliment of (A-1)th step. Length of each row is 2**(A-1). so what we can do
    when B value is <= mid we can search the result in first part of (A-1)th step solve(A-1, B) and
    when B > mid we can search the result in (A-1)th step but compliment of that index to get
    the actual index in 1st part we have to do (B - mid). """
    def solu(n, k):
        if n == 1 and k == 1:  # considering False as 0 and True as 1
            return False
        m = (2 ** (n - 1)) // 2
        if k <= m:
            return solu(n - 1, k)
        else:
            return not solu(n - 1, k - m)

    return (0, 1)[solu(A, B)]

def solve2(A, B):
    """Approach is similar to previous, but here we find (A-1)row and append its compliment to find Ath row."""
    def comp(a):
        s = ''
        for i in str(a):
            if i == '0':
                s += '1'
            else:
                s += '0'
        return s

    def row(a):
        if a == 1:
            return '0'
        s = row(a - 1)
        return s + comp(s)

    return row(A)[B - 1]

print(solve1(4, 3))
print(solve1(4, 3))
