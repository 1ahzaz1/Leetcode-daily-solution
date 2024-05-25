class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        #Backtracking solution:

        #There are 2^n subsets
        #We start from index 0
        #At each point we branch out into a new possible subset that can be made
        #This is done by having 2 options at each index;
        #The subset INCLUDES nums[i] or it does NOT INCLUDE nums[i]
        #At each index we have *2 possible routes, until final index where we have 2^len(nums) routes

        output = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                output.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)

            subset.pop()
            dfs(i+1)

        dfs(0)
        return output
        
