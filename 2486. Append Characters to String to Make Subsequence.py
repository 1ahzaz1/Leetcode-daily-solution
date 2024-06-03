class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        tpointer = 0

        #We look for the longest prefix in t that in a subsequence of s
        for char in s:
            if tpointer < len(t) and char == t[tpointer]:
                tpointer += 1
        
        # The characters left in t that were not matched in s need to be appended
        return len(t) - tpointer
