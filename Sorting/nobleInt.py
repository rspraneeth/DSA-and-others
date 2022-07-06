# Noble Integer (DISTINCT/REPETITIVE ELEMENTS) Given N array elements. Calculate no of noble integers present.
# arr[i] is said to be a noble Integer if (No of elements < arr[i]) == arr[i]
a = [0, 2, 2, 4, 4, 6]

def nobleInt(arr):
    """Whenever repetitive elements are present, the value(No of elements < arr[i]) doesn't change. When
    new element comes the value will be index position. Take example's for faster understanding"""
    arr.sort()  # arranges them in ascending order, so elements < current will always be on left of current
    ans = 0
    val = 0  # No of elements < arr[i]
    if arr[0] == 0:
        ans += 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i+1]:
            val = i
        if arr[i] == val:
            ans += 1
    return ans

print(nobleInt(a))

# To check (No of elements > arr[i]) == arr[i], then we just reverse the array i.e., sort in descending order.
