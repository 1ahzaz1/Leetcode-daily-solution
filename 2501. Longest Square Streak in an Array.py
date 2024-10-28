class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:

        mp = {} #Storing every number and how many of its root have been seen
        nums = sorted(nums) #So we can see a numbers roots beforehand if they exist
        output = -1 #Default if no streaks

        for num in nums:
            root = num**(1/2)
            
            if root == int(root) and root in mp: 
                #If the root is an integer and we have seen it
                mp[num] = mp[root]+1
                #new key for each num, and value is the value of its root incremented
                output = max(output, mp[num])
                #Update output to track the biggest streak
            else:
                mp[num] = 1

        return output


        