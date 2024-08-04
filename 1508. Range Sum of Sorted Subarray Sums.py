class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        
        sum_subarrays = []
        mod = 10**9 + 7

        for start in range(n):
            for end in range(start,n):
                curr_sub = nums[start:end+1]
                curr_sum = sum(curr_sub)
                sum_subarrays.append(curr_sum)

        sum_subarrays = sorted(sum_subarrays)

        return sum(sum_subarrays[left-1:right]) % mod