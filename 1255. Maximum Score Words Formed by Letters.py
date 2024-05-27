class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
     
        letter_count = Counter(letters) #Store letter as hashmap instead of list (Counter already imported from collections)
        
        #helper function called later:
        def word_possible(word, letter_count):
            word_count = Counter(word)
            for char in word_count:
                if word_count[char] > letter_count[char]:
                    return False
            return True


        #helper function called later:
        def get_score(word):
            output = 0
            for char in word:    
                output += score[ord(char) - ord('a')] #Could do -97 instead of 'a', we are just converting to ASCII
            return output
        #Backtracking solution (4th day in a row).

        def dfs(i): #Branch each combination of selecting words
            if i == len(words): #On last word
                return 0
            #At every step we can either include the word or skip it

            output = dfs(i+1) #Skip route

            #Include route if possible:
            if word_possible(words[i], letter_count):
                #Create the word by decrementing letter count appropriately:
                for char in words[i]:
                    letter_count[char] -=1
                output = max(output, get_score(words[i]) + dfs(i+1)) #Now we move on to next after decremnting from letters since this is included
                for char in words[i]:
                    letter_count[char] +=1
                #Above we reversed the decrementing AFTER the recursive call, for proper use in other routes

            return output
        return dfs(0)
