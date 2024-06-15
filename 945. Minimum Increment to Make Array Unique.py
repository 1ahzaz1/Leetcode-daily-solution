class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:

        #First simple solution.
        #O(nlogn) sorting then O(n) iterating
        
        #Counting sort possible too 
        # higher complexity and is O(n + maxNumSize)
        nums = sorted(nums)
        added = 0

        p1 = 0
        p2 = 1

        while p2<len(nums):
            if nums[p1]==nums[p2]:
                nums[p2] = nums[p2]+1
                added +=1
            elif nums[p1]>nums[p2]:
                diff = (nums[p1]-nums[p2]) + 1 #Sometimes we may need to add >2
                nums[p2] = nums[p2] + diff
                added +=diff
            p1+=1
            p2+=1
        print(nums)
        return added