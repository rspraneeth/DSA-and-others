class Solution:
    def __init__(self, A):
        self.A = A

    def sqrt(self):
        l = 0
        h = 10**5
        ans = 0
        while l <= h:
            m = (l+h)//2
            if m*m > self.A:
                h = m-1
            else:
                ans = m
                l = m+1
        return ans

s = Solution(38)
print(s.sqrt())
