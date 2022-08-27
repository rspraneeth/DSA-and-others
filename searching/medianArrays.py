from math import inf

a = [1, 4, 5]
b = [2, 3]

def findMedianSortedArrays(A, B):
    if len(A) > len(B):
        A, B = B, A
    n1 = len(A)
    n2 = len(B)
    n = n1 + n2
    l = 0
    h = n1
    while l <= h:
        cut1 = (l + h) // 2
        cut2 = n // 2 - cut1
        l1 = -inf if cut1 == 0 else A[cut1 - 1]
        l2 = -inf if cut2 == 0 else B[cut2 - 1]
        r1 = inf if cut1 == n1 else A[cut1]
        r2 = inf if cut2 == n2 else B[cut2]
        if l1 > r2:
            h = cut1 - 1
        elif l2 > r1:
            l = cut1 + 1
        else:
            return (max(l1, l2) + min(r1, r2)) / 2 if n % 2 == 0 else min(r1, r2)

print(findMedianSortedArrays(a, b))

# https://www.youtube.com/watch?v=yD7wV8SyPrc

# There are two sorted arrays A and B of sizes N and M respectively. Find the median of the two sorted arrays
# ( The median of the array formed by merging both the arrays ). The overall run time complexity should be O(log(m+n)).
# IF the number of elements in the merged array is even, then the median is the average of
# (n/2)th and (n/2+1)th element. For example, if the array is [1 2 3 4], the median is (2 + 3) / 2.0 = 2.5.
