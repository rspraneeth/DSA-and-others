A = [1, 2, 8, 7, 8, 7, 2, 1]

def candy1(ratings):
    """Approach 1: We take 2 arrays lft & ryt. We traverse from L->R and also from R->L and store the candies
    in lft and ryt respectively. We take the max candies present at a position from lft[i] & ryt[i] so that it
    justifies both left and right elements ratings. [TC: O(n), SC: O(n)]"""
    n = len(ratings)
    lft = [1] * n
    ryt = [1] * n
    ans = 0
    for i in range(1, n):  # L->R
        if ratings[i] > ratings[i - 1]:
            lft[i] = lft[i - 1] + 1
    for i in range(n - 2, -1, -1):  # R->L
        if ratings[i] > ratings[i + 1]:
            ryt[i] = ryt[i + 1] + 1
    for i in range(n):  # taking max candies a position can have and adding all candies to get total candies
        ans += max(lft[i], ryt[i])

    return ans

def candy2(ratings):
    """Approach 2: We take a single array res. We traverse from L->R and also from R->L. On L->R we store the candies
    in res. On R->L we store the candies in res based on an extra condition candies at current position should be
    higher than previous position". Sum of elements in res array gives total candies required. [TC: O(n), SC: O(n)]"""
    n = len(ratings)
    res = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            res[i] = res[i-1] + 1
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1] and res[i] <= res[i+1]:
            res[i] = res[i+1] + 1
    return sum(res)

print(candy1(A))
print(candy2(A))
