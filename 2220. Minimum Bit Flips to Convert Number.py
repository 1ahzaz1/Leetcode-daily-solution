class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        #Bit representation of every number is unique
        #Simply count number of bits in each that dont match with the other
        #This can be done using XOR

        xorred = start ^ goal
        #Now convert to binary and count how many 1's in the number
        #A 1 would only appear if there was a 1 in start and 0 in goal or vice versa
        return bin(xorred).count('1')
