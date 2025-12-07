class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        diff = high-low+1
        #diff is the inclusive range of numbers we are checking
        #An even diff means same amount of even and odd numbers
        #Otherwise, we have an additional even or odd, depending on start/end
        if diff%2==1 and low%2==1:
            return diff//2 + 1
        else:
            return diff//2
    