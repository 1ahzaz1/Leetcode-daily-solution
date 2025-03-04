class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        # n must be < 3^16, as defined in input constraints
        start = 16
        total = 0
        # keep summing the largest powers of 3 smaller than n
        while start>=0:
            if total + 3**start <= n:
                total += 3**start
            start -=1
        return total == n