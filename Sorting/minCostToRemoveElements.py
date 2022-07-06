a = [2, 3, 4, 6, 8, 54, 2, 1, 2, 43, 6]

def minCost(arr):
    arr.sort(reverse=True)
    ans = 0
    for i in range(len(arr)):
        ans += arr[i]*(i+1)
    return ans

print(minCost(a))

# arr [a, b, c, d]              Cost
# Remove a from [a b c d]      a+b+c+d
# Remove b from [b c d]          b+c+d
# Remove c from [c d]              c+d
# Remove d from [d]                  d
# Total cost                 a+2b+3c+4d
