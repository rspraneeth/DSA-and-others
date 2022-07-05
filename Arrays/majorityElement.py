# Given N +ve elements, find majority element -> an element with frequency > N//2 i.e., greater than half
arr = [3, 3, 4, 5, 3, 6, 7, 5, 3, 2, 2, 3, 3, 4, 4, 3, 3, 3]
ar1 = [3, 4, 8, 3, 9, 4, 3, 4, 3]
def majEle(a):
    # Brute force approach would be sorting and finding max, but TC: O(nlogn).
    # using Boyer-Moore Majority Voting Algorithm, we can optimize it to O(n)
    """Here we take 2 variables, element(el) and its frequency(freq). We iterate array and when the el equals a[i],
    we increase freq by 1, when not equal we decrease freq by 1 and whenever freq = 0 means we take the arr[i] as el
    i.e., el = a[i] and freq = 1. check scaler notes when the approach is doubtful"""
    n = len(a)
    el = a[0]
    freq = 1
    for i in range(1, n):
        if freq == 0:
            el = a[i]
            freq = 1
        elif el != a[i]:
            freq -= 1
        else:  # if el == a[i]
            freq += 1
    ln = 0
    for i in a:  # checking length of 'el', double verification.
        if i == el:
            ln += 1

    return (-1, el)[ln > n // 2]

print(majEle(arr))

# Given N +ve elements, find majority element -> an element with frequency > N//3
def majEleNby3(A):
    """Similar to the previous approach"""
    n = len(A)
    if n == 1:
        return A[0]
    e1 = A[0]
    e2 = A[1]
    f1 = 0
    f2 = 0
    for i in A:
        if e1 == i:
            f1 += 1
        elif e2 == i:
            f2 += 1
        else:
            if f1 == 0:
                e1 = i
                f1 = 1
            elif f2 == 0:
                e2 = i
                f2 = 1
            else:
                f1 -= 1
                f2 -= 1
    ln1, ln2 = 0, 0
    for i in A:  # checking length of 'e1 & e2', double verification.
        if i == e1:
            ln1 += 1
        if i == e2:
            ln2 += 1

    if ln1 > n//3:
        return e1
    elif ln2 > n//3:
        return e2

    return -1


print(majEleNby3(ar1))
