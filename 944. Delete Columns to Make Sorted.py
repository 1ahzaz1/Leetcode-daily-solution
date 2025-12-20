class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        columns = len(strs[0])
        removed = 0
        for col in range(columns):
            for j in range(len(strs)-1):
                if strs[j][col] > strs[j+1][col]:
                    removed += 1
                    break
        return removed