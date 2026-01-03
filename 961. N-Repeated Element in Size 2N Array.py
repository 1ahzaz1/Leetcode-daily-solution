class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # Given problem description/constraints:
        # The number that we return is the only one that appears > 1 times

        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)