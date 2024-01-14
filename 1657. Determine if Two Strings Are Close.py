class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        #We can see each words characters must appear in the other word.
        #The num of occurrences of each character must be the same in both words (THEY DONT HAVE TO MATCH THE SAME CHAR)
        #e.g word1 = "cabbba", word2 = "abbccc":
        #both have a,b,c. and occurrence of letters are 1,2,3 in each word (although they match to diff letters)

        frequency1 = {}
        frequency2 = {}

        #filling each char and its frequency in its respective set
        for i in word1:
            if i not in frequency1:
                frequency1[i]=1
            else:
                frequency1[i] +=1

        for j in word2:
            if j not in frequency1:
                return False           #character in word2 didnt appear in word2
            if j not in frequency2:
                frequency2[j] = 1
            else:
                frequency2[j] +=1

        return sorted(frequency1.values()) == sorted(frequency2.values())  #sorting is O(logn) but always max 26 length

        #Therefore solution is O(n) or O(n+m)for large inputs, as sets have max length 26
        