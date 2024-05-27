class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        wordDict = set(wordDict) #for O(1) lookup
        def backtrack(i):
            if i == len(s):
                output.append(' '.join(curr))
                return
            for j in range(i, len(s)):
                word = s[i:j+1]
                if word in wordDict:
                    curr.append(word)
                    backtrack(j+1)
                    curr.pop()#revert for use in other recursive calls
        curr = []
        output = []
        backtrack(0)
        return output