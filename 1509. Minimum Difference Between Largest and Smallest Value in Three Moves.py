class Solution:
    def minDifference(self, nums: List[int]) -> int:

        if len(nums)<=4: #In this case all numbers can be made equal
            return 0
        nums = sorted(nums)
        #There are only 4 cases (we can assume changing = removing)
        case1 = nums[-4] - nums[0]
        case2 = nums[-3] - nums[1]
        case3 = nums[-2] - nums[2]
        case4 = nums[-1] - nums[3]
        return min(case1,case2,case3,case4)