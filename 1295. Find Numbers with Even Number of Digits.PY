class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        output = 0
        for num in nums:
            digits = 0
            while num > 0:
                num = num//10
                digits += 1
            if digits%2==0:
                output+=1
        return output
        