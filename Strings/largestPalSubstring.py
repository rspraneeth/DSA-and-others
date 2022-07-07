a = 'gasbagscabac'

def getPalLength(s, i, j):
    n = len(s)
    while i >= 0 and j < n and s[i] == s[j]:
        i -= 1
        j += 1
    return j - i - 1

def largestPalSubstr(s):
    ans = 1
    for i in range(len(s)):
        len1 = getPalLength(s, i, i)
        len2 = getPalLength(s, i, i+1)
        ans = max(ans, len1, len2)

    return ans

print(largestPalSubstr(a))
