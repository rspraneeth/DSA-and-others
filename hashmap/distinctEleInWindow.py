from collections import defaultdict

A = [2, 4, 3, 8, 3, 9, 4, 9, 4, 10]

# distinct elements in window of size k
def solve(a, k):
    """Using hashset, TC: O(n^2)"""
    for i in range(len(a) - k + 1):
        print(len(set(a[i:i + 4])))

def solve1(a, k):
    """Using sliding window in a hashmap, TC: O(n)"""
    count = []
    hm = defaultdict(int)
    for i in range(k):  # hash map for first k elements
        hm[a[i]] += 1
    count.append(len(hm))
    for i in range(1, len(a) - k + 1):  # using sliding window technique
        hm[a[i - 1]] -= 1  # decreasing i-1 element frequency
        if hm[a[i - 1]] == 0:  # if freq becomes zero then we remove the element
            hm.pop(a[i - 1])
        hm[a[i + k - 1]] += 1  # adding/increasing the next element into window, freq increases
        count.append(len(hm))

    return count

solve(A, 4)
print(solve1(A, 4))
