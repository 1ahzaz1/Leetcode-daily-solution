class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        #Simple solution, making seperate arrays for nums smaller and larger in the order they appear
        
        smaller = []
        larger = []
        same = 0

        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num > pivot:
                larger.append(num)
            else:
                same += 1
        
        return smaller + (same * [pivot]) + larger