class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        
        rowLen = len(rowSum)
        colLen = len(colSum)
        output = [[0] * colLen for _ in range(rowLen)]
        
        for row in range(rowLen):
            output[row][0] = rowSum[row]

        for col in range(colLen-1):
            curr_col_sum = 0
            for r in range(rowLen):#Calculate the sum of the row currently
                curr_col_sum += output[r][col]
            row = 0
            while curr_col_sum > colSum[col]: #We move numbers to the next col until curr_col_sum = colSum of row.
                diff = curr_col_sum - colSum[col]#Total needed to move to next row so current row = colSum of row
                move = min(diff, output[row][col]) #How much from each element we can/need to move to next column
                output[row][col+1] += move
                output[row][col] -= move
                curr_col_sum -= move
                row+=1
        return output