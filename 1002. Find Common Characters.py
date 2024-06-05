class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        first_count = Counter(words[0]) #Hashmap of first words letter frequencies
        
        for word in words:
            curr_count = Counter(word)
            for char in first_count:
                first_count[char] = min(first_count[char], curr_count[char])
                #Reassign the letter to frequencies of first count to only common ones
                #If letter not in curr count, Counter sets freq to 0 (like defaultdict)

        output = []
        for char in first_count:
            for i in range(first_count[char]):
                output.append(char) #allows for multiple occurrences of letter in output
        return output