# Given an array of elements. Sort them in increasing order of their no of factors
# If 2 elements have the same no of factors element with lesser value should come first
from functools import cmp_to_key

A = [9, 3, 4, 8, 16, 37, 6, 13, 15]

def sortOnFactors(arr):
    def factorsOf(x):
        """returns factors of a number"""
        if x == 0:
            return 0
        elif x == 1:
            return 1
        count = 2
        for i in range(2, x):
            if x % i == 0:
                count += 1
        return count

    def comp(a, b):
        """on returning -1, this function arranges as a, b in the array,
        on returning 1, this function arranges as b, a in the array"""
        f1 = factorsOf(a)
        f2 = factorsOf(b)
        if f1 < f2:
            return -1
        elif f1 == f2 and a < b:
            return -1
        else:
            return 1

    return sorted(arr, key=cmp_to_key(comp))

print(sortOnFactors(A))
