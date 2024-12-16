class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:


        for j in range(k): #perform operation k times
            idx = 0
            smallest = nums[0]
            for i in range(len(nums)): #find smallest number and its index
                if nums[i] < smallest:
                    smallest = nums[i]
                    idx = i
            nums[idx] = nums[idx]*multiplier #perform operation
        return nums
        