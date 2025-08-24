class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        i = 0
        j = 0
        numNot = 0
        longest = 0
        
        while j<len(nums):
            if nums[j] != 1:
                numNot +=1
                if numNot > 1:
                    while numNot >1:
                        if nums[i] != 1:
                            numNot -= 1
                        i +=1
            longest = max(longest, j-i)
            j+=1

        return longest