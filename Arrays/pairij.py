from collections import defaultdict
A = [1, 2, 3, 4, 5, 3, 2, 6, 7, 8]

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

print(solve(A, 2))
print(solve1(A, 2))

# Given N array elements. Check if there exists a pair (i, j) s.t arr[i] + arr[j] = k & i != j
