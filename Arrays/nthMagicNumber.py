# nth magic number = sum of powers of 5 (power of 5 with respect to 1's bit position in binary format for 'n')
# eg: n=10 , binary(10) = 1010 = 5^(4) + 5^(2) = 625 + 25 = 650, but here it starts from 5^1 instead of 5^0.
def solve(A):
    pwr = 1
    ans = 0
    while A > 0:
        if A & 1 == 1:  # checking if RSB is 1, when 0 we need not do anything
            ans += 5 ** pwr
        A = A >> 1  # right shifting binary number, so that when RSB=1, we add 5^pow
        pwr += 1
    return ans

print(solve(10))
