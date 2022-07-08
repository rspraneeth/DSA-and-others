def longestCommonPrefix(A):
    n = len(A)
    if n == 0:
        return 0
    s = A[0]
    for i in range(1, n):
        a = ''
        for j in range(min(len(A[i]), len(s))):
            if s[j] == A[i][j]:
                a += s[j]
        s = a
    if s != '':
        return s
    return 0

print(longestCommonPrefix(["abcd", "abde", "abcf"]))
