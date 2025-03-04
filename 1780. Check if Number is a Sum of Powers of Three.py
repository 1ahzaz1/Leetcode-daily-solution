class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        # If the number has a 2 in its ternary representation, it cant be a sum of powers of 3

        # 91 = 10101 base 3 -> return true
        # 46 = 1201 base 3 -> return false due to the 2

        while n!=0:
            if n%3 == 2:
                return False
            n = n//3
        return True
