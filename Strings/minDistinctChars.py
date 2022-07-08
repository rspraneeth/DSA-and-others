import math

def solve(A, B):
    """storing the frequency of an alphabet in a list and using the max and min of the list"""
    al = [0] * 26  # frequency of char[a-z] is stored in array w.r.t the dictionary order
    for i in A:
        al[ord(i) - 97] += 1
    mx = max(al)  # max value
    max_ind = al.index(mx)  # max value index
    while B > 0:
        mn = math.inf  # to calculate min value in list other than 0
        for i in al:
            if i != 0:
                mn = min(mn, i)
        min_ind = al.index(mn)
        if mn <= B:
            al[min_ind] = 0
            al[max_ind] += mn
            B = B - mn
        else:  # condition mn > B means we can't change all the chars at index(mn), at least 1 char will remain
            B = 0
    ans = 0
    for i in al:  # calculating distinct elements
        if i != 0:
            ans += 1
    return ans

print(solve('umeaylnlfd', 1))

# You are given a string A of size N consisting of lowercase alphabets. You can change at most B characters
# in the given string to any other lowercase alphabet such that the number of distinct characters in the
# string is minimized. Find the minimum number of distinct characters in the resulting string.
# A = "abcabbccd" B = 3. Output 2.
