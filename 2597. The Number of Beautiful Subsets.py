class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n = len(nums)
        output =0

        def dfs(i, counter): #Backtracking
            nonlocal output
            if i ==n:
                if counter:
                    output +=1
                return
            if nums[i]+k not in counter and nums[i]-k not in counter:
                counter[nums[i]] += 1
                dfs(i+1, counter)
                counter[nums[i]] -=1
                if not counter[nums[i]]:
                    del counter[nums[i]]
            dfs(i+1, counter)
        
        dfs(0,Counter())
        return output