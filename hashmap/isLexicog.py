a = ["no", "none", "mine"]
b = "qwertyuiopasdfghjklzxcvbnm"
def lexicog(A, B):
    hb = {}
    for i in range(len(B)):
        hb[B[i]] = i
    for i in range(1, len(A)):
        w1 = A[i-1]
        w2 = A[i]
        i = 0
        flag = False
        while i < len(w1) and i < len(w2):
            if hb[w1[i]] < hb[w2[i]]:
                flag = True
                break
            elif hb[w1[i]] > hb[w2[i]]:
                return 0
            else:
                i += 1
        if not flag and len(w1) > len(w2):
            return 0

    return 1

print(lexicog(a, b))
# Surprisingly, in an alien language, they also use English lowercase letters, but possibly in a different order.
# The order of the alphabet is some permutation of lowercase letters.
# Given an array of words A of size N written in the alien language, and the order of the alphabet denoted
# by string B of size 26, return 1 if and only if the given words are sorted lexicographically in this \
# alien language else, return 0.
