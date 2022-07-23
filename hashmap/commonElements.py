A1 = [2, 1, 4, 10]
B1 = [3, 6, 2, 10, 10]

def solve1(A, B):
    """Approach 1 using 2 hashmaps"""
    hmA = {}
    for i in A:
        hmA[i] = hmA.get(i, 0) + 1
    hmB = {}
    for i in B:
        hmB[i] = hmB.get(i, 0) + 1
    c = []
    for i in hmA:
        if i in hmA and i in hmB:
            fq = min(hmA[i], hmB[i])
            for j in range(fq):
                c.append(i)
    return c

def solve2(A, B):
    """Approach 2, using 1 hash map"""
    hmA = {}
    for i in A:
        hmA[i] = hmA.get(i, 0) + 1
    c = []
    for i in B:
        if i in hmA and hmA[i] != 0:
            c.append(i)
            hmA[i] -= 1

    return c

print(solve1(A1, B1))
print(solve2(A1, B1))

# Two integer arrays, A and B. Find all the common elements in both the array.
# A = [1, 2, 2, 1], B = [2, 3, 1, 2] & Output 1: [1, 2, 2]
