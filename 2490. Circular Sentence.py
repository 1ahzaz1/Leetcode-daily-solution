class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        
        sentence = sentence.split(' ') #Turn into an array of individual words

        for i in range (1,len(sentence)):
            curr_word = sentence[i]
            prev_word = sentence[i-1]

            if curr_word[0] != prev_word[-1]: #Compare each words first letter to previous' last letter
                return False

        return sentence[-1][-1] == sentence[0][0] #Compare the final word to first word (not done in loop)
        