class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        num_to_occurrences = {} #dictionary mapping each num to its occurrence

        for i in arr:
            if i not in num_to_occurrences:
                num_to_occurrences[i] = 1
            else:
                num_to_occurrences[i] +=1
        
        unique_set = set() #set of each numbers occurrences only. not num itself

        for j in num_to_occurrences.values():
            if j not in unique_set:
                unique_set.add(j)
            else:
                return False #As this number (occurrences) already appeared for a diff num
        return True