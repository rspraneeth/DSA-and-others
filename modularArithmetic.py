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
