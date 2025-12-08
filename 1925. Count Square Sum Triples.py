class Solution:
    def countTriples(self, n: int) -> int:
        #'brute force' solution
        ans = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c2 = a*a + b*b
                c = int(math.isqrt(c2))  # integer sqrt
                if c <= n and c*c == c2:
                    ans += 1
        return ans
