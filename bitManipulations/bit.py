# Given an array of integers A, every element appears twice except for one. Find that integer that occurs once.
A1 = [1, 2, 2, 3, 1]
def singleNumber(A):
    ans = 0
    for i in range(len(A)):
        ans = ans ^ A[i]
    return ans

print(singleNumber(A1))

# Given two binary strings, return their sum (also a binary string).
a = "100"
b = "11"
def addBinary(A, B):
    n = max(len(A), len(B))
    A = A.zfill(n)
    B = B.zfill(n)
    final = ''
    c = 0
    for i in range(n - 1, -1, -1):
        s = int(A[i]) + int(B[i]) + c
        d = s % 2
        c = s // 2
        final = str(d) + final
    if c == 1:
        final = '1' + final

    return final

print(addBinary(a, b))

# Write a function that takes an integer and returns the number of 1 bits it has.
C = 11
def numSetBits1(A):
    len = 0
    # approach 1
    for i in range(32):
        if A >> i & 1:
            len += 1
    # approach 2
    # A = bin(A)[2:]  # turns decimal to binary
    # for i in A:
    #     if i == '1':
    #         len += 1
    return len

print(numSetBits1(C))

# Reverse the bits of an 32-bit unsigned integer A.
D = 3
def reverse(A):
    A = bin(int(A))[2:].zfill(32)  # converting A to int, then again to binary of 32
    A = A[::-1]  # reversing
    A = int(A, 2)  # converting binary to decimal
    return A

print(reverse(D))
