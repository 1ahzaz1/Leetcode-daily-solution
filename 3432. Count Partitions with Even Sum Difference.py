class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        output = 0
        left = nums[0]
        right = sum(nums)-left

        for i in range(1, len(nums)):
            if (right-left)% 2 == 0:
                output += 1
            left += nums[i]
            right -= nums[i]
        return output



        