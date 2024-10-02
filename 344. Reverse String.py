class Solution:
    def reverseString(self, s: List[str]) -> None:

        n = len(s)
        for i in range(n//2):
            s[i], s[n-1-i] = s[n-1-i],s[i] 
            #Swaps 0..n//2 with n..n//2 +1
            #If odd then middle index remains unchanged

        """
        Do not return anything, modify s in-place instead.
        """
        