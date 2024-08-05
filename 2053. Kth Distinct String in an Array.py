class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        count = Counter(arr) #Map each string to its occurrences
        times = 0 #Track how many times a string has 1 occurrence

        for char in arr:
            if count[char]==1:
                times+=1
                if times == k:
                    return char
        return ''