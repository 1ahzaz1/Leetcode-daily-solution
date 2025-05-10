class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        zero1 = 0
        zero2 = 0

        for num in nums1:
            if num == 0:
                zero1 += 1
        
        for num in nums2:
            if num == 0:
                zero2 += 1
        smallest1 = sum1 + zero1
        smallest2 = sum2 + zero2
        if smallest1 == smallest2:
            return smallest1
        if smallest1 > smallest2:
            if zero2 > 0:
                return smallest1
            else:
                return -1
        else:
            if zero1 > 0:
                return smallest2
            else:
                return -1