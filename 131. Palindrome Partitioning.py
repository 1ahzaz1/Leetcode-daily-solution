class Solution:
    def partition(self, s: str) -> List[List[str]]:

        #Backtracking solution
        #Branch out all possible ways of splitting the string
        #Only continue branches where the substring is palindrome
        #If we reach the end of the string, its a valid answer

        output = []
        current = [] #Stores current substring partition

        def dfs(i):
            if i >= len(s):
                output.append(current.copy())
                return
            for j in range(i, len(s)):
                if isPalindrome(s, i ,j): #Checks if current substring partition is palindrome
                    current.append(s[i:j+1])
                    dfs(j+1)
                    current.pop()

        def isPalindrome(input, left, right): #O(n) with constant space. more optimal than 'return input == input[::-1]'
            while left<right:
                if input[left] != input[right]:
                    return False
                left +=1
                right -=1
            return True

        dfs(0) #Start recursive backtracking
        return output