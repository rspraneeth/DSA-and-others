a = 'gasbagscabac'

def getPalLength(s, i, j):
    """using two pointer to return length and palindrome from given indices i & j of string s.
    Considering i, j as centers, we move to left of i and right of j. When the values at these indices are equal,
    we check for i-- and j++ and so on....until values at indices i, j are not equal"""
    n = len(s)
    while i >= 0 and j < n and s[i] == s[j]:
        i -= 1
        j += 1
    return j - i - 1, s[i+1:j]

def largestPalSubstr(A):
    """Approach is to take a char and check left and right. for odd len palindrome we use one center,
    for even length palindrome we use 2 centers."""
    ans = 0
    st = ''
    for i in range(len(A)):
        len1, s1 = getPalLength(A, i, i)  # taking the center char then checking left and right(for odd len)
        len2, s2 = getPalLength(A, i, i + 1)   # taking two centers (for even len)
        if len1 > ans:
            ans = len1
            st = s1
        if len2 > ans:
            ans = len2
            st = s2

    return ans, st

print(largestPalSubstr(a))
