class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        #DP APPROACH

        # start from the second row
        for i in range(1, n):
            for j in range(n):
                # edge cases: if at the first or last column, we can't check one of the sides
                left = matrix[i-1][j-1] if j > 0 else float('inf')
                right = matrix[i-1][j+1] if j < n-1 else float('inf')
                up = matrix[i-1][j]

                #update the current cell with min sum of falling path
                matrix[i][j] += min(left, right, up)

        # the answer in the end is the min value in the last row
        return min(matrix[-1])

        #Can be optomised with memoisation
