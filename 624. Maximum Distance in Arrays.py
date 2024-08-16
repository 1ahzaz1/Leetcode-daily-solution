class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        
        smallest= arrays[0][0]
        biggest = arrays[0][-1]
        
        output = 0 

        for i in range(1, len(arrays)):
            
            output = max(output,max(arrays[i][-1] - smallest, biggest - arrays[i][0]))

            smallest = min(smallest, arrays[i][0])
            biggest = max(biggest, arrays[i][-1])

        return output