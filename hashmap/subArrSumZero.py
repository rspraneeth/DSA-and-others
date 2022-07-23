# a = [1,3,4,6,6,3,1,2,4,6,8,9,5,2,1,2,3,3,4,5,6,8,5,1,1,2,3,4,5]
# a = [1,2,5,6,8,0,4]
a = [5, 1, 3, -5]
# check if all elements in given array are distinct
def checkAllDistinct(arr):
    """if length of hash set equal to length of array means all are distinct elements
    if not there exists repeated elements"""

    return (False, True)[len(set(arr)) == len(arr)]

print(checkAllDistinct(a))

# check if there exist a subarray with sum = 0
def subArrSumZero1(arr):
    """if there exists repetitive elements in prefix array, then there exists a subarray with sum zero. (take e.g.)"""
    pf = [0] * len(arr)  # prefix array
    pf[0] = arr[0]
    for i in range(1, len(arr)):
        pf[i] = pf[i-1] + arr[i]

    return (False, True)[len(set(pf)) != len(arr) or 0 in pf]

def subArrSumZero2(arr):
    """Approach 2"""
    sum = 0
    c = {}
    for i in arr:
        sum += i
        if sum == 0 or i == 0 or sum in c:
            return 1
        else:
            c[sum] = 1
    return 0


print(subArrSumZero1(a))
print(subArrSumZero2(a))
