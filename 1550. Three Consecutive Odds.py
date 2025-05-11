class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        cons = 0

        for num in arr:
            if num%2==1:
                cons += 1
                if cons == 3:
                    return True
            else:
                cons = 0
        return cons==3