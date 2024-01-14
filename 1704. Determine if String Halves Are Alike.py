class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a','e','i','o','u','A','E','I','O','U'} #Storing all vowels in set for O(1) access time

        #Splitting input string into the two halves
        half = len(s)//2
        h1 = s[:half]
        h2 = s[half:]

        counter = 0 #Should be 0 in the end

        #Iterating over each array. O(n) complexity solution. one half adds to counter and other half removes.
        for j in range(half):
            if h1[j] in vowels:
                counter+=1
            if h2[j] in vowels:
                counter-=1
        return not counter #True only when counter = 0