class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        #For every char we add to set if new and remove if not
        #This way there are 0 occurrences of even chars from s in the set
        #And only 1 occurrence for every odd number from s in the input

        #All other chars can be paired (even)
        #This includes chars that had an odd frequency in s
        #IE if 'a' appeared 5 times in s; the set will include a (once as its a set)
        #The other 4 occurrences of a can be used in the output palindrome

        #We also add 1 to output if there exists any odd frequency characters
        #This is because that extra char can be placed in the middle alone

        odds = set()

        for char in s:
            if char in odds:
                odds.remove(char)
            else:
                odds.add(char)
        return len(s) - len(odds) + (1 if odds else 0)