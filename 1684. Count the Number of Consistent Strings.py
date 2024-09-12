class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        #Hashmap for allowed chars (O(1) searching, the value in key-val pair is irrelevant)
        mp_allowed = Counter(allowed)

        #First assume ever word is valid
        output =  len(words)

        for word in words:
            for char in word:
                #If a word contains invalid char, reflect in output and move to next word
                if char not in mp_allowed:
                    output -= 1
                    break
                    
        return output
        