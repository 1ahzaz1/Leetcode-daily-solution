class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        #Split and place in hashmap for O(1) lookup
        one = Counter(s1.split())
        two = Counter(s2.split())

        output = []
        #For each word in each sentence, ensure it isn't in the other sentence
        #And only appears once in the current sentence

        for c in one:
            if c not in two and one[c]==1:
                output.append(c)
        for c in two:
            if c not in one and two[c] == 1:
                output.append(c)
                
        return output
