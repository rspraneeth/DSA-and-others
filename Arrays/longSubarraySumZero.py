from collections import defaultdict
a = [13, -5, 11, -2, -10, 5, 14, -14, 10, -28, 28, 7, 18, -22, 4, -26, 20, 25, 22, 18, -25, 7, 27, 20, 6, -1, -22, -28]

def lszero(A):
    """Approach: Whenever an element is repeating in prefix sum array, it means there exists
    a sub array sum zero. We take the indices of the prefix sum array values in a hash table
    as a list i.e., hashmap<pf[i] value, [indices of pf[i] value]>. When inserting a value
    into hashmap, we find the distance between first and last of list, and we keep the max
    distance value. Also, we save the indices whenever we get a max.
    For edge case prefix sum value '0', we take -1 in list initially. Because if zero
    is present in pf[], that means sum from first element until the index value 0 is 0"""
    N = len(A)
    pf = [0] * N
    pf[0] = A[0]
    for i in range(N):
        pf[i] = pf[i - 1] + A[i]
    seen_table = defaultdict(list)  # saying that values will be of list format in the dictionary
    seen_table[0] = [-1]  # to handle edge case
    longest = -1  # largest sub array length
    indices = None
    for i in range(N):
        s = pf[i]
        seen_table[s].append(i)  # adding the index to dict values
        gap = seen_table[s][-1] - seen_table[s][0]  # finding the gap between first and last index
        if gap > longest:
            longest = gap
            indices = (seen_table[s][0] + 1, seen_table[s][-1] + 1)  # finding indices to return A[i:j]
    if indices:
        return A[indices[0]:indices[1]]
    else:
        return []


print(lszero(a))

# Given an array A of N integers. Find the largest continuous sequence in an array which sums to zero.
