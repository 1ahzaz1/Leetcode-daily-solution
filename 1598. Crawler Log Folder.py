class Solution:
    def minOperations(self, logs: List[str]) -> int:

        folders_away = 0
        
        for log in logs:
            if log[0] != '.': #First letter not . therefore must be a move to child
                folders_away +=1
            if log == '../' and folders_away: #If we go back and arent already at parent
                folders_away -=1
        return folders_away
        