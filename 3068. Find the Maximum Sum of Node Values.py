class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:

        #SIMPLE TRICK FOUND; EDGES NOT NEEDED
        #We can change any nodes but must be even number of total changes
        #This is true because n-1 edges for n nodes (all connected)
        #Any 2 even nodes dont have to be directly linked to change
        #This is because the nodes connecting them along the line will be 'xored' twice
        #Applying xor after xor will revert the intermediary nodes to their original
    
        #Arrays storing how much we make or gain by doing xor k on each num
        total_sum = sum(nums)
        gains = []
        losses = []

        for num in nums:
            value = num^k
            if value>=num:
                gains.append(value-num)
            else:
                losses.append(abs(value-num))
        gains.sort()
        losses.sort()
        if len(gains)%2==0: #Even number of changes made, all profitable
            return total_sum + sum(gains)
        
        #IN THE CASE THERE ARE NOT EVEN NUMBER OF PROFITABLE XOR CHANGES:

        if len(losses)>0:
            return max(total_sum+sum(gains) - gains[0], total_sum+sum(gains)-losses[0])
        else:
            return total_sum+sum(gains) - gains[0]
        
        #THEN WE RETURN THE MAX OF EITHER REMOVING LEAST PROFITABLE OR ADDING SMALLEST LOSS
        #SINCE WE NEED EVEN NUMBER OF NODES TO CHANGE FOR TRANSORMATIONS TO BE POSSIBLE