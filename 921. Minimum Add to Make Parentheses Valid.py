class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []

        for char in s:
            if char == ')' and stack and stack[-1] == '(': #valid pair of brackets found
                stack.pop()
            else: #We have seen an opening bracket that may later be popped. or we have an invalid closing bracket
                stack.append(char)

        return len(stack) #stack will have all the leftovers that were never validly paired