class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        #SOLUTION WITHOUT STACK. BETTER RUNTIME
        
        opens = 0 #Stores how many opening brackets need closing ones
        closes = 0 #Stores how many closing brackets need opening ones


        for char in s:
            if char == '(': #open bracket seen
                opens += 1
            else: #Close bracket seen
                if opens: #If there are previous opens to match this close with
                    opens -= 1
                else:
                    closes += 1 #Closing bracket seen with no open before to pair with
        return opens + closes 
