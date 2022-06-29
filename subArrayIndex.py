k = 3
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(a)
for i in range(n-k+1):  # n-k+1 sub arrays
    print(i, i+k-1)

# return max sum of a sub array of length k, shouldn't use prefix sum, shouldn't modify array, T: O(n), S: O(1)
ans = sum(a[:k])
sum = ans
for i in range(1, n-k+1):
    sum = sum - a[i-1] + a[i+k-1]
    ans = max(ans, sum)
print(ans)
