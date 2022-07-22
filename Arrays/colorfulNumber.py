def colorful(A):
    """Approach: 1. digits in given number shouldn't repeat,
                 2. Shouldn't contain 1 or 0 as a digit,
                 3. product of 2 consecutive digits shouldn't be present in given number"""
    if A in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:  # if the given number is single digit, it is cful
        return 1
    a = []
    while A != 0:
        v = A % 10
        if v == 1 or v == 0 or v in a:  # checking for conditions 1 & 2
            return 0
        a.append(v)
        A = A // 10
    for i in range(len(a) - 1):
        if a[i] * a[i + 1] in a:  # checking for condition 3
            return 0
    return 1

print(colorful(2345))

# Given a number A, find if it is COLORFUL number or not. If number A is a COLORFUL number return 1 else, return 0.
# What is a COLORFUL Number: A number can be broken into different contiguous sub-subsequence parts.
# Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
# And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different.
