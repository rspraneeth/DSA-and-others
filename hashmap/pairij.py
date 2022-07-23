from collections import defaultdict

arr = [1, 2, 3, 4, 5, 3, 2, 6, 7, 8]

# Given N array elements. Check if there exists a pair (i, j) s.t arr[i] + arr[j] = k & i != j
def solve(a, k):
    """using hashmap"""
    ha = defaultdict(int)
    for i in a:
        ha[i] += 1
    for i in ha:
        b = k - i
        if b in ha:
            if b == i and ha[b] < 2:
                return False
            return True
    return False

def solve1(a, k):
    """using hashset"""
    hs = set()
    for i in a:
        b = k - i
        if b in hs:
            return True
        else:
            hs.add(i)
    return False

print(solve(arr, 2))
print(solve1(arr, 2))

# Given N array elements. Check if there exists a pair (i, j) s.t arr[i] - arr[j] = k & i != j
ar = [77, 28, 19, 21, 67, 15, 53, 25, 82, 52, 8, 94, 50, 30, 37, 39, 9, 43, 35, 48, 82, 53, 16, 20, 13, 95, 18, 67, 77,
      12, 93, 0]

def diffPossible(A, k):
    hs = set()
    for a in A:
        if a == 0 and k in hs:
            return 1
        elif a == k and 0 in hs:
            return 1
        elif a + k in hs or a - k in hs:
            return 1
        # for every number there are two possible values to make it equal to B, so we take k, l
        # B = 9, i = 2, k = 7. (2 + 7 is 9)
        # B = 9, i = 2, l = -7 (2 - (-7) is 9)
        hs.add(a)
    return 0

print(diffPossible(ar, 53))
