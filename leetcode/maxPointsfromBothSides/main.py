cardPoints1 = [1, 2, 3, 4, 5, 6, 1]
k1 = 3
def maxScore(cardPoints, k):
    n = len(cardPoints)
    pf = [0] * n
    pf[0] = cardPoints[0]
    for i in range(1, n):
        pf[i] = cardPoints[i] + pf[i-1]

    sf = [0] * n
    sf[n-1] = cardPoints[n-1]
    for i in range(n-2, -1, -1):
        sf[i] = sf[i+1] + cardPoints[i]

    mx = max(pf[k-1], sf[n-k])
    for i in range(k-1):
        mx = max(mx, pf[i]+sf[n-k+1+i])

    return mx

print(maxScore(cardPoints1, k1))
