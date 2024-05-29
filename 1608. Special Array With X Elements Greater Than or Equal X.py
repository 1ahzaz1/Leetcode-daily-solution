class Solution:
    def specialArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        curr = 0

        for i in range(max(nums),-1,-1):
            curr += count[i]
            if curr==i:
                return i
    
        return -1