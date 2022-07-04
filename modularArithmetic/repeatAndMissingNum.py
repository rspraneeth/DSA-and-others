# You are given a read only array of n integers from 1 to n. Each integer appears exactly once except A
# which appears twice and B which is missing. Return A and B.
arr = [1, 2, 3, 4, 5, 6, 8, 3]
def repeatedNumber(A):
    n = len(A)
    sum_act = 0  # actual sum (1+2+3+.....+n)
    for i in range(1, n + 1):
        sum_act += i
    sum_giv = 0  # given sum is sum of elements in array
    for i in range(n):
        sum_giv += A[i]
    d = sum_act - sum_giv  # actualSum = givenSum - a + b, b-a = actualSum-givenSum = d
    # similar to sum of elements, we calculate sum of squares of elements
    sum_act_sq = 0
    for i in range(1, n + 1):
        sum_act_sq += i ** 2
    sum_giv_sq = 0
    for i in range(n):
        sum_giv_sq += A[i] ** 2
    d_sq = sum_act_sq - sum_giv_sq  # actualSumSq = givenSumSq - a^2 + b^2, b^2-a^2 = actualSumSq-givenSumSq = d_sq
    s = d_sq // d  # d_sq = (b-a)(b+a) -> b+a = d_sq/b-a = d_sq/d = s
    b = (d + s) // 2  # s+d = b+a+b-a = 2b -> b = (s+d)/2
    a = b - d

    return a, b

print(repeatedNumber(arr))
