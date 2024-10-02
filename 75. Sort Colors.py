class Solution:
    def sortColors(self, nums: List[int]) -> None:

        #O(n) SortinG Using Dijkstra's Dutch Naitonal Flag Algorithm

        low=0
        mid=0
        high = len(nums)-1

        while mid<=high:
            current = nums[mid]
            if current==2: #Blue, highest colour
                nums[high], nums[mid] = nums[mid], nums[high]
                high-=1 #Keep high pointer at the last unknown
            elif current==0:#Red, Lowest colour
                nums[low], nums[mid] = nums[mid], nums[low]
                low +=1
                mid +=1
            else: #We keep high on the right of red, low on the left of low, and in between doesnt matter
                mid +=1 #IE no swaps needed for mid, whatevers left will belong there anyway
