a = [7, 1, 3, 4, 1, 7]

def solve(A):
    hA = {}
    for i in range(len(A)):  # saving indices in hash map
        if A[i] in hA:
            hA[A[i]].append(i)
        else:
            hA[A[i]] = [i]
    mn = len(A)
    for i in hA:
        if len(hA[i]) > 1:
            mn = min(mn, hA[i][1] - hA[i][0])  # diff b/w first 2 indices are enough for min distance

    return (-1, mn)[mn != len(A)]

print(solve(a))

#  Array A consisting of N elements. We call a pair of distinct indices in that array a special if elements at
#  those indices in the array are equal. Find a special pair such that the distance between that pair is minimum.
#  Distance between two indices is defined as |i-j|. If there is no special pair in the array, then return -1
