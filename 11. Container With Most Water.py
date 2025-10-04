class Solution:
    def maxArea(self, height: List[int]) -> int:

        maxArea = 0
        left = 0
        right = len(height)-1
        #two pointer begings with start and end of array
        #move the smaller of the two bars inwards
        while left < right:
            Lheight = height[left]
            Rheight = height[right]
            
            length = min(Lheight, Rheight)
            width = right-left

            maxArea = max(maxArea, length*width)

            if Lheight<Rheight:
                left +=1
            else:
                right-=1
        return maxArea

        