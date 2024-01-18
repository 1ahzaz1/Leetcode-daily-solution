class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {} #using memoisation / Dynamic Programming
        return self.fibMem(n+1,memo)  #there are fibonacci(n) ways.


    def fibMem(self,n, memo):
        if n in memo:
            return memo[n]
        if n <= 1:
            memo[n] = n
        else:
            memo[n] = self.fibMem(n-1,memo)+self.fibMem(n-2,memo)
        return memo[n]