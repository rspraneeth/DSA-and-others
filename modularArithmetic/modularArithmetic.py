# Implement a power function(No in built functions). Given a, n, p Calculate (a**n)%p
def power(a, n, p):
    """for very much larger values there can be overflow, to overcome this, we use modulus as it brings value
    in the range(p)"""
    ans = 1
    for i in range(n):
        # ans = (ans * a) % p  # overflow might occur in (ans * a)
        ans = ((ans % p) * (a % p)) % p
    return ans % p

print(power(2, 560, 5))

# Given a number in arr[] format calculate number % p. (number(322) = [3,2,2]).
def numModp(arr, p):
    n = len(arr)
    ans = 0
    for i in range(n):
        ans = ans + ((arr[i] % p) * power(10, n-1-i, p)) % p
        ans = ans % p  # we keep on bringing within the range(p)
    return ans % p
    # n can go up to 10^5, TC: O(n^2), i.e., 10^10, TLE. So this solution fails.

def numModulusP(arr, p):
    """optimized code O(n), using carry forward approach from R->l. refer scaler notes when not clear."""
    n = len(arr)
    ans = 0
    exp = 1
    for i in range(n-1, -1, -1):
        ans = ans + (arr[i] * exp) % p
        exp = (exp * 10) % p
        ans = ans % p

    return ans

print(numModp([2, 2], 3))
