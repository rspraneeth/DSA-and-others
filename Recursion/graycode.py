def grayCode1(A):
    """Approach: Using recursion. For single bit, sb =  [0 ,1],
    for 2 bits there are 4 numbers which are divided into 2 parts. 1st part: Add 0 before every sb[](single bit)
    2nd part: add 1 before reverse of every sb[](single bit). Convert each binary value to decimal."""
    def grayC(a):
        if a == 1:
            return ['0', '1']
        part = grayC(a - 1)
        return ['0' + str(el) for el in part] + ['1' + str(el) for el in part[::-1]]

    gray = grayC(A)
    return [int(bits, 2) for bits in gray]

def grayCode2(A):
    """Approach: for A number of bits, there exists 2**A numbers. Formula: (i >> 1) ^ i gives decimal value.
    right shift and xor."""
    ans = []
    for i in range(2 ** A):
        ans.append((i >> 1) ^ i)
    return ans

print(grayCode1(4))
print(grayCode2(4))

# The gray code is a binary numeral system where two successive values differ in only one bit.
# Given a non-negative integer A representing the total number of bits in the code, print the sequence of gray code.
# A gray code sequence must begin with 0.
# for A = 2 the gray code sequence is:
#     00 - 0
#     01 - 1
#     11 - 3
#     10 - 2
# So, return [0,1,3,2].
